import torch
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained(
    "/home/lz/repo/baselearn/llm/models/Huihui-MoE-0.8B-2E",
    torch_dtype="auto",   # 保持权重文件里的精度
    device_map="cpu"
)

groups = {
    "q_proj": 0,
    "k_proj": 0,
    "v_proj": 0,
    "o_proj": 0,
    "mlp": 0,       # 非 MoE 的 MLP
    "norm": 0,
    "embed": 0,
    "lm_head": 0,
    "others": 0,
}
sizes = {k:0 for k in groups}

# 专门统计 MoE
experts = {}
routers = {"params":0, "size":0}

for name, param in model.named_parameters():
    numel = param.numel()
    size_bytes = numel * torch.finfo(param.dtype).bits // 8

    if "q_proj" in name:
        groups["q_proj"] += numel
        sizes["q_proj"] += size_bytes
    elif "k_proj" in name:
        groups["k_proj"] += numel
        sizes["k_proj"] += size_bytes
    elif "v_proj" in name:
        groups["v_proj"] += numel
        sizes["v_proj"] += size_bytes
    elif "o_proj" in name:
        groups["o_proj"] += numel
        sizes["o_proj"] += size_bytes
    elif "experts" in name:  # MoE expert 权重
        # 提取 expert id
        parts = name.split(".")
        exp_idx = None
        for i, p in enumerate(parts):
            if p == "experts" and i+1 < len(parts):
                exp_idx = parts[i+1]
                break
        if exp_idx is None:
            exp_idx = "unknown"

        if exp_idx not in experts:
            experts[exp_idx] = {"params":0, "size":0}

        experts[exp_idx]["params"] += numel
        experts[exp_idx]["size"] += size_bytes
    elif "router" in name:  # router 权重
        routers["params"] += numel
        routers["size"] += size_bytes
    elif any(x in name for x in ["gate_proj", "up_proj", "down_proj", "w1", "w2", "w3"]):
        groups["mlp"] += numel
        sizes["mlp"] += size_bytes
    elif "norm" in name:
        groups["norm"] += numel
        sizes["norm"] += size_bytes
    elif "embed_tokens" in name:
        groups["embed"] += numel
        sizes["embed"] += size_bytes
    elif "lm_head" in name:
        groups["lm_head"] += numel
        sizes["lm_head"] += size_bytes
    else:
        groups["others"] += numel
        sizes["others"] += size_bytes

print("====== 参数分布统计 ======")
for k in groups:
    print(f"{k:<8}: {groups[k]:>12,} params, {sizes[k]/1024/1024:6.2f} MB")

print("\n====== MoE Experts 参数统计 ======")
for exp, info in experts.items():
    print(f"Expert {exp:<3}: {info['params']:>12,} params, {info['size']/1024/1024:6.2f} MB")

print(f"\nRouter   : {routers['params']:,} params, {routers['size']/1024/1024:.2f} MB")

total_params = sum(groups.values()) + sum(e["params"] for e in experts.values()) + routers["params"]
total_size = sum(sizes.values()) + sum(e["size"] for e in experts.values()) + routers["size"]

print("\n====== 总结 ======")
print(f"总参数量: {total_params:,}")
print(f"总存储大小: {total_size/1024/1024:6.2f} MB")

print("\n====== 精度信息 ======")
print("默认 dtype:", torch.get_default_dtype())
print("模型权重 dtype:", next(model.parameters()).dtype)
