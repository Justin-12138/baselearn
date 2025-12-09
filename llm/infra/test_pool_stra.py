import torch
import time
import numpy as np
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple
import pandas as pd

class PoolingBenchmark:
    def __init__(self, model_path: str):
        """初始化基准测试"""
        print("正在加载模型...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModel.from_pretrained(model_path, torch_dtype=torch.float16)
        self.model.eval()
        print("模型加载完成！")
        
        # 移动到GPU（如果可用）
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(self.device)
        print(f"使用设备: {self.device}")
    
    def mean_pooling(self, token_embeddings: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
        """Mean pooling实现"""
        # 应用attention mask
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        masked_embeddings = token_embeddings * input_mask_expanded
        
        # 计算平均值
        sum_embeddings = torch.sum(masked_embeddings, 1)
        sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
        mean_embeddings = sum_embeddings / sum_mask
        
        # L2归一化
        return mean_embeddings / mean_embeddings.norm(dim=1, keepdim=True)
    
    def last_token_pooling(self, token_embeddings: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
        """Last token pooling实现"""
        # 找到每个序列的最后一个有效token位置
        seq_lengths = attention_mask.sum(dim=1) - 1
        batch_size = token_embeddings.shape[0]
        
        # 提取最后一个token的embedding
        last_embeddings = token_embeddings[torch.arange(batch_size), seq_lengths]
        
        # L2归一化
        return last_embeddings / last_embeddings.norm(dim=1, keepdim=True)
    
    def get_embeddings(self, texts: List[str]) -> Tuple[torch.Tensor, torch.Tensor]:
        """获取token embeddings"""
        # 分词
        encoded = self.tokenizer(
            texts,
            padding=True,
            truncation=True,
            max_length=512,
            return_tensors='pt'
        )
        
        input_ids = encoded['input_ids'].to(self.device)
        attention_mask = encoded['attention_mask'].to(self.device)
        
        # 前向传播
        with torch.no_grad():
            outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)
            token_embeddings = outputs.last_hidden_state
        
        return token_embeddings, attention_mask
    
    def speed_benchmark(self, texts: List[str], num_runs: int = 100) -> Dict[str, float]:
        """速度基准测试"""
        print(f"\n{'='*20} 速度测试 {'='*20}")
        print(f"测试文本数量: {len(texts)}")
        print(f"重复次数: {num_runs}")
        
        results = {}
        
        # 预热
        print("预热中...")
        token_embeddings, attention_mask = self.get_embeddings(texts[:5])
        _ = self.mean_pooling(token_embeddings, attention_mask)
        _ = self.last_token_pooling(token_embeddings, attention_mask)
        
        # 获取token embeddings（只计算一次，排除模型推理时间）
        print("获取token embeddings...")
        start_time = time.time()
        token_embeddings, attention_mask = self.get_embeddings(texts)
        model_time = time.time() - start_time
        print(f"模型推理时间: {model_time:.4f}秒")
        
        # 测试Mean Pooling
        print("测试Mean Pooling...")
        times = []
        for _ in range(num_runs):
            torch.cuda.synchronize() if torch.cuda.is_available() else None
            start_time = time.time()
            _ = self.mean_pooling(token_embeddings, attention_mask)
            torch.cuda.synchronize() if torch.cuda.is_available() else None
            times.append(time.time() - start_time)
        
        mean_pooling_time = np.mean(times[10:])  # 排除前10次的预热
        results['mean_pooling'] = mean_pooling_time
        
        # 测试Last Token Pooling
        print("测试Last Token Pooling...")
        times = []
        for _ in range(num_runs):
            torch.cuda.synchronize() if torch.cuda.is_available() else None
            start_time = time.time()
            _ = self.last_token_pooling(token_embeddings, attention_mask)
            torch.cuda.synchronize() if torch.cuda.is_available() else None
            times.append(time.time() - start_time)
        
        last_token_time = np.mean(times[10:])  # 排除前10次的预热
        results['last_token'] = last_token_time
        
        # 输出结果
        print(f"\n速度测试结果:")
        print(f"Mean Pooling:     {mean_pooling_time*1000:.3f} ms")
        print(f"Last Token:       {last_token_time*1000:.3f} ms")
        print(f"速度提升:          {mean_pooling_time/last_token_time:.2f}x")
        
        return results
    
    def semantic_benchmark(self) -> Dict[str, Dict]:
        """语义质量基准测试"""
        print(f"\n{'='*20} 语义测试 {'='*20}")
        
        # 测试数据集
        test_datasets = {
            "相似句对": [
                ("The cat is on the mat", "A cat sits on the mat"),
                ("I love programming", "Programming is my passion"),
                ("The weather is nice", "It's a beautiful day"),
                ("Machine learning is powerful", "ML has great capabilities"),
                ("Hello world", "Hi there, world")
            ],
            "不相似句对": [
                ("The cat is on the mat", "I hate vegetables"),
                ("I love programming", "The ocean is deep"),
                ("The weather is nice", "Mathematics is difficult"),
                ("Machine learning is powerful", "I need to buy groceries"),
                ("Hello world", "Quantum physics is complex")
            ],
            "长短句对比": [
                ("Hi", "Hello there, how are you doing today? I hope everything is going well."),
                ("Yes", "Absolutely, I completely agree with your assessment and think it's correct."),
                ("Good", "That's excellent news and I'm very happy to hear about this development."),
                ("Maybe", "I'm not entirely certain about this, but it might be possible under circumstances."),
                ("Thanks", "Thank you very much for your help, I really appreciate your time and effort.")
            ]
        }
        
        results = {}
        
        for dataset_name, pairs in test_datasets.items():
            print(f"\n测试数据集: {dataset_name}")
            
            # 提取所有句子
            all_sentences = []
            for sent1, sent2 in pairs:
                all_sentences.extend([sent1, sent2])
            
            # 获取embeddings
            token_embeddings, attention_mask = self.get_embeddings(all_sentences)
            
            # 计算不同池化策略的embeddings
            mean_embeddings = self.mean_pooling(token_embeddings, attention_mask)
            last_embeddings = self.last_token_pooling(token_embeddings, attention_mask)
            
            # 计算句子对相似度
            mean_similarities = []
            last_similarities = []
            
            for i in range(0, len(all_sentences), 2):
                # Mean pooling相似度
                mean_sim = torch.cosine_similarity(
                    mean_embeddings[i:i+1], mean_embeddings[i+1:i+2], dim=1
                ).item()
                mean_similarities.append(mean_sim)
                
                # Last token相似度
                last_sim = torch.cosine_similarity(
                    last_embeddings[i:i+1], last_embeddings[i+1:i+2], dim=1
                ).item()
                last_similarities.append(last_sim)
            
            # 统计结果
            results[dataset_name] = {
                'mean_pooling': {
                    'similarities': mean_similarities,
                    'avg': np.mean(mean_similarities),
                    'std': np.std(mean_similarities)
                },
                'last_token': {
                    'similarities': last_similarities,
                    'avg': np.mean(last_similarities),
                    'std': np.std(last_similarities)
                }
            }
            
            # 输出详细结果
            print(f"Mean Pooling - 平均相似度: {np.mean(mean_similarities):.4f} (±{np.std(mean_similarities):.4f})")
            print(f"Last Token   - 平均相似度: {np.mean(last_similarities):.4f} (±{np.std(last_similarities):.4f})")
            
            # 显示具体例子
            for i, (sent1, sent2) in enumerate(pairs):
                print(f"  例子 {i+1}: {mean_similarities[i]:.3f} vs {last_similarities[i]:.3f}")
                print(f"    句子1: {sent1}")
                print(f"    句子2: {sent2}")
        
        return results
    
    def memory_usage_test(self, batch_sizes: List[int]) -> Dict[str, List[float]]:
        """内存使用测试"""
        print(f"\n{'='*20} 内存使用测试 {'='*20}")
        
        results = {'batch_sizes': batch_sizes, 'mean_pooling': [], 'last_token': []}
        test_text = "This is a test sentence for memory usage benchmark."
        
        for batch_size in batch_sizes:
            print(f"测试批次大小: {batch_size}")
            
            # 创建测试批次
            texts = [test_text] * batch_size
            token_embeddings, attention_mask = self.get_embeddings(texts)
            
            # 测试Mean Pooling内存使用
            torch.cuda.empty_cache() if torch.cuda.is_available() else None
            if torch.cuda.is_available():
                torch.cuda.reset_peak_memory_stats()
                _ = self.mean_pooling(token_embeddings, attention_mask)
                mean_memory = torch.cuda.max_memory_allocated() / 1024**2  # MB
            else:
                mean_memory = 0  # CPU内存测试较复杂，这里简化
            
            # 测试Last Token内存使用
            torch.cuda.empty_cache() if torch.cuda.is_available() else None
            if torch.cuda.is_available():
                torch.cuda.reset_peak_memory_stats()
                _ = self.last_token_pooling(token_embeddings, attention_mask)
                last_memory = torch.cuda.max_memory_allocated() / 1024**2  # MB
            else:
                last_memory = 0
            
            results['mean_pooling'].append(mean_memory)
            results['last_token'].append(last_memory)
            
            print(f"  Mean Pooling: {mean_memory:.2f} MB")
            print(f"  Last Token:   {last_memory:.2f} MB")
        
        return results
    
    def comprehensive_report(self, speed_results: Dict, semantic_results: Dict, memory_results: Dict):
        """生成综合报告"""
        print(f"\n{'='*50}")
        print("综合对比报告")
        print(f"{'='*50}")
        
        print("\n🚀 速度对比:")
        mean_time = speed_results['mean_pooling'] * 1000
        last_time = speed_results['last_token'] * 1000
        speedup = speed_results['mean_pooling'] / speed_results['last_token']
        
        print(f"  Mean Pooling: {mean_time:.3f} ms")
        print(f"  Last Token:   {last_time:.3f} ms")
        print(f"  Last Token 比 Mean Pooling 快 {speedup:.2f} 倍")
        
        print("\n🎯 语义质量对比:")
        for dataset, results in semantic_results.items():
            mean_avg = results['mean_pooling']['avg']
            last_avg = results['last_token']['avg']
            print(f"  {dataset}:")
            print(f"    Mean Pooling: {mean_avg:.4f}")
            print(f"    Last Token:   {last_avg:.4f}")
            print(f"    差异: {abs(mean_avg - last_avg):.4f}")
        
        if torch.cuda.is_available():
            print("\n💾 内存使用对比:")
            avg_mean_mem = np.mean(memory_results['mean_pooling'])
            avg_last_mem = np.mean(memory_results['last_token'])
            print(f"  Mean Pooling 平均: {avg_mean_mem:.2f} MB")
            print(f"  Last Token 平均:   {avg_last_mem:.2f} MB")
        
        print("\n📊 推荐使用场景:")
        print("  Mean Pooling:")
        print("    ✅ 需要更丰富的语义信息")
        print("    ✅ 文档相似度计算")
        print("    ✅ 语义搜索任务")
        print("    ✅ 句子聚类")
        
        print("  Last Token:")
        print("    ✅ 推理速度要求高")
        print("    ✅ 大批量处理")
        print("    ✅ 与vLLM兼容")
        print("    ✅ 生成式任务")

def main():
    model_path = "/home/lz/repo/baselearn/llm/models/mmBERT-base"
    
    try:
        # 初始化测试
        benchmark = PoolingBenchmark(model_path)
        
        # 准备测试文本（不同长度）
        test_texts = [
            "Hi",
            "Hello world!",
            "I am Justin, what about you?",
            "The quick brown fox jumps over the lazy dog.",
            "Machine learning is revolutionizing the way we process information.",
            "In the field of natural language processing, embeddings play a crucial role in understanding semantic meaning.",
            "Artificial intelligence has made tremendous progress in recent years, with applications spanning from computer vision to natural language understanding and beyond.",
        ] * 20  # 创建更大的测试集
        
        # 1. 速度基准测试
        speed_results = benchmark.speed_benchmark(test_texts, num_runs=50)
        
        # 2. 语义质量测试
        semantic_results = benchmark.semantic_benchmark()
        
        # 3. 内存使用测试
        memory_results = benchmark.memory_usage_test([1, 10, 50, 100])
        
        # 4. 生成综合报告
        benchmark.comprehensive_report(speed_results, semantic_results, memory_results)
        
    except Exception as e:
        print(f"测试过程中出现错误: {e}")
        print("请确保:")
        print("1. 模型路径正确")
        print("2. 有足够的GPU内存")
        print("3. 已安装必要的依赖包")

if __name__ == "__main__":
    main()