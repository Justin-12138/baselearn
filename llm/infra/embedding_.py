from transformers import AutoTokenizer, AutoModel,ModernBertForMaskedLM,ModernBertModel
import torch
import torch.nn.functional as F

# 你的模型路径
mmbert = "/home/lz/repo/baselearn/llm/models/mmBERT-base"

tokenizer = AutoTokenizer.from_pretrained(mmbert)
model = ModernBertModel.from_pretrained(mmbert)

print("Embedding shape:", model.embeddings.tok_embeddings.weight.shape)
print("Embedding params:", model.embeddings.tok_embeddings.weight.numel())
print("Embedding size (MB):", 
      model.embeddings.tok_embeddings.weight.element_size() * model.embeddings.tok_embeddings.weight.numel() / 1024**2, "MB")
print("First 5 tokens, first 10 dims:\n", model.embeddings.tok_embeddings.weight[:5, :10])


# 输入文本
texts = ["你好，世界！", "篮球明星"]


# 编码输入
inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
print(f"input:{inputs}")
print(type(inputs))

with torch.no_grad():
    outputs = model(**inputs)

last_hidden_state = outputs.last_hidden_state  # (batch_size, seq_len, hidden_size)
attention_mask = inputs["attention_mask"]      # (batch_size, seq_len)

# Mean Pooling
mask_expanded = attention_mask.unsqueeze(-1).expand(last_hidden_state.size()).float()
sum_embeddings = torch.sum(last_hidden_state * mask_expanded, dim=1)
sum_mask = torch.clamp(mask_expanded.sum(dim=1), min=1e-9)
mean_pooled = sum_embeddings / sum_mask  # (batch_size, hidden_size)

# Last Token Pooling (取每个句子中最后一个非 padding token 的向量)
# 首先得到每个句子的有效长度 idx
# attention_mask 为 1 的地方是有效 token。可以用它找到最后一个 1 的索引。
lengths = attention_mask.sum(dim=1)  # 每句有效 token 数量, shape (batch_size,)
# 注意：sum 返回的是 long 类型，需要转换
last_token_indices = lengths - 1  # 索引从 0 开始
# 用 gather 方法取出对应的 vector
batch_size, seq_len, hidden_size = last_hidden_state.size()
# 为 gather 构造索引
# last_token_indices 形状 (batch_size,), 需要扩展成 (batch_size, hidden_size)
idx = last_token_indices.unsqueeze(-1).unsqueeze(-1).expand(-1, 1, hidden_size)  # (batch_size, 1, hidden_size)
last_token_embeddings = last_hidden_state.gather(dim=1, index=idx).squeeze(1)  # (batch_size, hidden_size)

# 准备计算相似度
# 余弦相似度
def cosine_sim(a: torch.Tensor, b: torch.Tensor):
    a_norm = F.normalize(a, p=2, dim=1)
    b_norm = F.normalize(b, p=2, dim=1)
    # 计算 a 和 b 每一对的相似度，这里 batch=2，两句之间
    # 用 dot product 后取对角线
    sim = (a_norm * b_norm).sum(dim=1)
    return sim

# 因为 batch 是 2，所以下面取句子 0 和句子 1 的 sim
mean_sim = cosine_sim(mean_pooled, mean_pooled.flip(dims=[0]))[0]  # 或者直接对两个向量比
last_token_sim = cosine_sim(last_token_embeddings, last_token_embeddings.flip(dims=[0]))[0]

print("Mean Pooled embeddings：", mean_pooled.shape)
print("Last Token embeddings：", last_token_embeddings.shape)
print("Cosine similarity (mean pooled)：", mean_sim.item())
print("Cosine similarity (last token pooled)：", last_token_sim.item())
