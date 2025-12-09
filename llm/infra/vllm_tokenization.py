from transformers import AutoTokenizer, AutoModel,Qwen3ForCausalLM
import torch

def generate_embedding(text, model_path):
    """
    生成与vLLM API一致的embedding
    关键发现：vLLM使用last_token池化策略
    """
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModel.from_pretrained(model_path, torch_dtype=torch.float16,device="cpu")  # 使用FP16
    model.eval()
    batch = tokenizer(
        [text],
        return_tensors="pt",
        padding=True,
        truncation=True,
        add_special_tokens=True
    )
    
    input_ids = batch["input_ids"]
    print(input_ids)
    attention_mask = batch["attention_mask"]
    with torch.no_grad():
        outputs = model(**batch, output_hidden_states=True)
        token_embeddings = outputs.last_hidden_state  # [batch, seq_len, hidden_dim]
    seq_lengths = attention_mask.sum(dim=1)
    last_token_indices = seq_lengths - 1
    sentence_embeddings = token_embeddings[torch.arange(token_embeddings.size(0)), last_token_indices]
    sentence_embeddings = sentence_embeddings / sentence_embeddings.norm(dim=1, keepdim=True)
    return sentence_embeddings[0]

# 使用示例
if __name__ == "__main__":
    # model_path = "/home/lz/repo/baselearn/llm/models/Qwen3-Embedding-0.6B"
    model_path = "/home/lz/repo/baselearn/llm/models/Qwen3-0.6B-GPTQ-Int4"
    text = "I am Justin, what about you?"
    embedding = generate_embedding(text, model_path)
    print("Generated embedding (first 10 values):")
    print(embedding[:10].tolist())
    print("embedding_shape",embedding.shape)
    
    # 与API结果对比
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
    
    api_tensor = torch.tensor(api_result)
    similarity = torch.cosine_similarity(embedding[:10], api_tensor, dim=0)
    print(f"\nSimilarity with API: {similarity.item():.6f}")
    
    print(f"\nAPI result:  {api_result}")
    print(f"Code result: {embedding[:10].tolist()}")