from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np

def load_model_and_tokenizer(model_path, dtype=None):
    """加载模型和分词器"""
    print(f"Loading model from: {model_path}")
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    
    # 尝试不同的数据类型
    if dtype:
        model = AutoModel.from_pretrained(model_path, torch_dtype=dtype)
        print(f"Model loaded with dtype: {dtype}")
    else:
        model = AutoModel.from_pretrained(model_path)
        print(f"Model loaded with default dtype: {next(model.parameters()).dtype}")
    
    model.eval()
    return tokenizer, model

def tokenize_text(tokenizer, text):
    """分词并返回详细信息"""
    print(f"\n=== Tokenization Debug ===")
    print(f"Input text: {text}")
    
    # 分词
    batch = tokenizer(
        [text],
        return_tensors="pt",
        padding=True,
        truncation=True,
        add_special_tokens=True
    )
    
    input_ids = batch["input_ids"]
    attention_mask = batch["attention_mask"]
    
    # 打印分词结果
    tokens = tokenizer.convert_ids_to_tokens(input_ids[0])
    print(f"Tokens: {tokens}")
    print(f"Token IDs: {input_ids[0].tolist()}")
    print(f"Attention mask: {attention_mask[0].tolist()}")
    print(f"Input shape: {input_ids.shape}")
    
    return batch, input_ids, attention_mask

def get_embeddings(model, batch):
    """获取模型输出"""
    print(f"\n=== Model Forward Pass ===")
    
    with torch.no_grad():
        outputs = model(**batch, output_hidden_states=True)
        token_embeddings = outputs.last_hidden_state  # [batch, seq_len, hidden_dim]
    
    print(f"Token embeddings shape: {token_embeddings.shape}")
    print(f"Token embeddings dtype: {token_embeddings.dtype}")
    
    return token_embeddings

def apply_pooling_strategies(token_embeddings, attention_mask):
    """尝试不同的池化策略"""
    print(f"\n=== Pooling Strategies ===")
    results = {}
    
    # 策略1: Mean pooling with attention mask
    masked_embeddings = token_embeddings * attention_mask.unsqueeze(-1)
    mean_pooled = masked_embeddings.sum(dim=1) / attention_mask.sum(dim=1, keepdim=True)
    mean_pooled_norm = mean_pooled / mean_pooled.norm(dim=1, keepdim=True)
    results['mean_pooling'] = mean_pooled_norm[0]
    print(f"Mean pooling (masked): {mean_pooled_norm[0][:10]}")
    
    # 策略2: CLS token (第一个token)
    cls_embeddings = token_embeddings[:, 0, :]
    cls_embeddings_norm = cls_embeddings / cls_embeddings.norm(dim=1, keepdim=True)
    results['cls_token'] = cls_embeddings_norm[0]
    print(f"CLS token: {cls_embeddings_norm[0][:10]}")
    
    # 策略3: 最后一个有效token (通常是EOS)
    seq_lengths = attention_mask.sum(dim=1)
    last_token_indices = seq_lengths - 1
    last_embeddings = token_embeddings[torch.arange(token_embeddings.size(0)), last_token_indices]
    last_embeddings_norm = last_embeddings / last_embeddings.norm(dim=1, keepdim=True)
    results['last_token'] = last_embeddings_norm[0]
    print(f"Last token: {last_embeddings_norm[0][:10]}")
    
    # 策略4: Max pooling
    max_pooled = torch.max(token_embeddings * attention_mask.unsqueeze(-1), dim=1)[0]
    max_pooled_norm = max_pooled / max_pooled.norm(dim=1, keepdim=True)
    results['max_pooling'] = max_pooled_norm[0]
    print(f"Max pooling: {max_pooled_norm[0][:10]}")
    
    # 策略5: 简单mean (不考虑mask)
    simple_mean = token_embeddings.mean(dim=1)
    simple_mean_norm = simple_mean / simple_mean.norm(dim=1, keepdim=True)
    results['simple_mean'] = simple_mean_norm[0]
    print(f"Simple mean: {simple_mean_norm[0][:10]}")
    
    return results

def compare_with_api_result(results, api_result):
    """与API结果对比"""
    print(f"\n=== API Comparison ===")
    api_tensor = torch.tensor(api_result[:10])
    print(f"API result: {api_tensor}")
    
    best_match = None
    best_similarity = -1
    
    for strategy, embedding in results.items():
        similarity = torch.cosine_similarity(embedding[:10], api_tensor, dim=0)
        print(f"{strategy} similarity: {similarity.item():.6f}")
        
        if similarity > best_similarity:
            best_similarity = similarity.item()
            best_match = strategy
    
    print(f"\nBest matching strategy: {best_match} (similarity: {best_similarity:.6f})")
    return best_match

def main():
    # 配置
    model_path = "/home/lz/repo/baselearn/llm/models/Qwen3-Embedding-0.6B"
    text = "I am Justin, what about you?"
    
    # API返回的结果 (前10个值)
    api_result = [
        0.09462561458349228,
        -0.05899850279092789,
        -0.005593456793576479,
        -0.038762301206588745,
        0.02650657296180725,
        -0.047882840037345886,
        0.007410439662635326,
        0.01546216756105423,
        -0.06925910711288452,
        0.001531965914182365
    ]
    
    print("=== Embedding Generation Debug Script ===")
    
    # 尝试不同的数据类型
    dtypes_to_try = [None, torch.float16, torch.float32, torch.bfloat16]
    
    for dtype in dtypes_to_try:
        try:
            print(f"\n{'='*50}")
            print(f"Trying dtype: {dtype}")
            print(f"{'='*50}")
            
            # 1. 加载模型
            tokenizer, model = load_model_and_tokenizer(model_path, dtype)
            
            # 2. 分词
            batch, input_ids, attention_mask = tokenize_text(tokenizer, text)
            
            # 3. 获取embeddings
            token_embeddings = get_embeddings(model, batch)
            
            # 4. 尝试不同池化策略
            results = apply_pooling_strategies(token_embeddings, attention_mask)
            
            # 5. 与API结果对比
            best_match = compare_with_api_result(results, api_result)
            
            # 如果找到高相似度匹配，输出详细结果
            if best_match:
                print(f"\n=== Best Match Details ({best_match}) ===")
                best_embedding = results[best_match]
                print(f"Full embedding (first 20 values):")
                print(best_embedding[:20].tolist())
                
                # 计算与API完整结果的相似度（如果有的话）
                api_tensor_full = torch.tensor(api_result)
                similarity_full = torch.cosine_similarity(
                    best_embedding[:len(api_result)], 
                    api_tensor_full, 
                    dim=0
                )
                print(f"Full similarity with API: {similarity_full.item():.6f}")
            
            # 清理内存
            del model, tokenizer
            torch.cuda.empty_cache() if torch.cuda.is_available() else None
            
        except Exception as e:
            print(f"Error with dtype {dtype}: {e}")
            continue

if __name__ == "__main__":
    main()