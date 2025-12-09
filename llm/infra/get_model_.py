# import torch
# from transformers import ModernBertModel,AutoModel

# # 加载模型
# mmbert = "/home/lz/repo/baselearn/llm/models/mmBERT-base"
# model = ModernBertModel.from_pretrained(mmbert)
# # mmbert = "/home/lz/repo/baselearn/llm/models/qwen2.5-0.5b-ins"
# # model = AutoModel.from_pretrained(mmbert)


# def get_param_stats(model):
#     total_params = 0
#     print(f"{'Module':50} {'Params':>15} {'Size (MB)':>15}")
#     print("-" * 85)
#     for name, param in model.named_parameters():
#         num_params = param.numel()
#         size_mb = num_params * param.element_size() / 1024**2
#         total_params += num_params
#         print(f"{name:50} {num_params:15,} {size_mb:15.2f}")
#     total_size_mb = total_params * 4 / 1024**2  # fp32
#     print("-" * 85)
#     print(f"{'Total':50} {total_params:15,} {total_size_mb:15.2f}")

# get_param_stats(model)


import torch
from transformers import AutoModel, AutoTokenizer
import gc
import os
from typing import Dict, Tuple

def get_model_memory_stats(model, detailed=True, group_by_layer=False):
    """
    改进的模型内存分析工具，更适合LLM
    
    Args:
        model: 要分析的模型
        detailed: 是否显示详细的参数信息
        group_by_layer: 是否按层分组显示
    """
    
    def get_param_dtype_size(param):
        """获取参数的实际数据类型字节数"""
        dtype_sizes = {
            torch.float32: 4,
            torch.float16: 2,
            torch.bfloat16: 2,
            torch.int8: 1,
            torch.int32: 4,
            torch.int64: 8,
            torch.bool: 1,
        }
        return dtype_sizes.get(param.dtype, 4)  # 默认4字节
    
    # 收集统计信息
    param_stats = []
    total_params = 0
    total_size_bytes = 0
    dtype_counts = {}
    
    for name, param in model.named_parameters():
        num_params = param.numel()
        dtype = param.dtype
        element_size = get_param_dtype_size(param)
        size_bytes = num_params * element_size
        size_mb = size_bytes / 1024**2
        
        param_stats.append({
            'name': name,
            'params': num_params,
            'dtype': dtype,
            'size_mb': size_mb,
            'size_bytes': size_bytes
        })
        
        total_params += num_params
        total_size_bytes += size_bytes
        dtype_counts[dtype] = dtype_counts.get(dtype, 0) + num_params
    
    # 显示结果
    print("=" * 100)
    print(f"模型内存占用分析")
    print("=" * 100)
    
    # 按数据类型统计
    print("\n数据类型分布:")
    print(f"{'类型':15} {'参数数量':>15} {'占用(MB)':>15} {'百分比':>10}")
    print("-" * 70)
    for dtype, count in sorted(dtype_counts.items(), key=lambda x: x[1], reverse=True):
        size_mb = count * get_param_dtype_size(torch.zeros(1, dtype=dtype).squeeze()) / 1024**2
        percentage = count / total_params * 100
        print(f"{str(dtype):15} {count:15,} {size_mb:15.2f} {percentage:9.1f}%")
    
    if group_by_layer:
        # 按层分组统计
        print("\n按层分组统计:")
        layer_stats = {}
        for stat in param_stats:
            layer_name = stat['name'].split('.')[0]  # 取第一级名称
            if layer_name not in layer_stats:
                layer_stats[layer_name] = {'params': 0, 'size_mb': 0}
            layer_stats[layer_name]['params'] += stat['params']
            layer_stats[layer_name]['size_mb'] += stat['size_mb']
        
        print(f"{'层名':30} {'参数数量':>15} {'占用(MB)':>15}")
        print("-" * 65)
        for layer_name, stats in sorted(layer_stats.items(), key=lambda x: x[1]['params'], reverse=True):
            print(f"{layer_name:30} {stats['params']:15,} {stats['size_mb']:15.2f}")
    
    if detailed:
        print(f"\n详细参数信息:")
        print(f"{'参数名':60} {'数量':>12} {'类型':>12} {'大小(MB)':>12}")
        print("-" * 100)
        
        # 按大小排序显示
        for stat in sorted(param_stats, key=lambda x: x['params'], reverse=True):
            print(f"{stat['name']:60} {stat['params']:12,} {str(stat['dtype']):>12} {stat['size_mb']:12.2f}")
    
    print("\n" + "=" * 100)
    print(f"总参数量: {total_params:,}")
    print(f"总占用内存: {total_size_bytes / 1024**2:.2f} MB ({total_size_bytes / 1024**3:.2f} GB)")
    print("=" * 100)
    
    return {
        'total_params': total_params,
        'total_size_mb': total_size_bytes / 1024**2,
        'dtype_distribution': dtype_counts,
        'param_details': param_stats
    }

def compare_disk_vs_memory(model_path, model=None):
    """比较磁盘占用和内存占用"""
    print("\n磁盘 vs 内存占用对比:")
    print("-" * 50)
    
    # 磁盘占用
    if os.path.exists(model_path):
        disk_size = sum(os.path.getsize(os.path.join(dirpath, filename))
                       for dirpath, dirnames, filenames in os.walk(model_path)
                       for filename in filenames) / 1024**3
        print(f"磁盘占用: {disk_size:.2f} GB")
    
    # 内存占用
    if model is not None:
        stats = get_model_memory_stats(model, detailed=False)
        memory_size = stats['total_size_mb'] / 1024
        print(f"内存占用: {memory_size:.2f} GB")
        
        if 'disk_size' in locals():
            ratio = disk_size / memory_size if memory_size > 0 else 0
            print(f"磁盘/内存比率: {ratio:.2f}")

def analyze_large_model(model_path, load_in_8bit=False, load_in_4bit=False):
    """分析大型模型的内存占用"""
    print(f"分析模型: {model_path}")
    print(f"量化设置: 8bit={load_in_8bit}, 4bit={load_in_4bit}")
    
    try:
        # 清理GPU内存
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        gc.collect()
        
        # 加载配置
        from transformers import BitsAndBytesConfig
        
        quantization_config = None
        if load_in_4bit:
            quantization_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_compute_dtype=torch.float16
            )
        elif load_in_8bit:
            quantization_config = BitsAndBytesConfig(load_in_8bit=True)
        
        # 加载模型
        model = AutoModel.from_pretrained(
            model_path,
            quantization_config=quantization_config,
            torch_dtype=torch.float16 if not (load_in_8bit or load_in_4bit) else None,
            device_map="auto" if torch.cuda.is_available() else None
        )
        
        # 分析内存占用
        stats = get_model_memory_stats(model, detailed=True, group_by_layer=True)
        
        # 比较磁盘占用
        compare_disk_vs_memory(model_path, model)
        
        # GPU内存使用情况
        if torch.cuda.is_available():
            print(f"\nGPU内存使用:")
            for i in range(torch.cuda.device_count()):
                allocated = torch.cuda.memory_allocated(i) / 1024**3
                cached = torch.cuda.memory_reserved(i) / 1024**3
                print(f"GPU {i}: 已分配 {allocated:.2f} GB, 已缓存 {cached:.2f} GB")
        
        return model, stats
        
    except Exception as e:
        print(f"加载模型时出错: {e}")
        print("尝试使用量化或更小的模型")
        return None, None

# 使用示例
if __name__ == "__main__":
    # 分析BERT模型
    print("分析BERT模型:")
    mmbert_path = "/home/lz/repo/baselearn/llm/models/mmBERT-base"
    try:
        bert_model = AutoModel.from_pretrained(mmbert_path)
        get_model_memory_stats(bert_model, detailed=False, group_by_layer=True)
        compare_disk_vs_memory(mmbert_path, bert_model)
    except Exception as e:
        print(f"BERT模型加载失败: {e}")
    
    print("\n" + "="*100 + "\n")
    
    # 分析LLM模型（如Qwen）
    print("分析LLM模型:")
    qwen_path = "/home/lz/repo/baselearn/llm/models/qwen2.5-0.5b-ins"
    
    # 尝试不同的加载方式
    print("\n1. 标准加载 (float16):")
    model, stats = analyze_large_model(qwen_path)
    
    if model is None:
        print("\n2. 尝试8bit量化:")
        model, stats = analyze_large_model(qwen_path, load_in_8bit=True)
    
    if model is None:
        print("\n3. 尝试4bit量化:")
        model, stats = analyze_large_model(qwen_path, load_in_4bit=True)