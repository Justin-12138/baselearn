import torch

# GPU 架构表
ARCH_MAP = {
    (6, 0): "Pascal (P100)",
    (6, 1): "Pascal (GTX 10xx)",
    (7, 0): "Volta (V100)",
    (7, 5): "Turing (RTX 20, T4)",
    (8, 0): "Ampere (A100)",
    (8, 6): "Ampere (RTX 30)",
    (8, 9): "Ada Lovelace (RTX 40)",
    (9, 0): "Hopper (H100)",
    (10, 0): "Blackwell (B100)"
}

# 数据精度 → 字节数
PRECISION_BYTES = {
    "FP64": 8,
    "FP32": 4,
    "TF32": 4,   # TF32 存储上与 FP32 相同
    "FP16": 2,
    "BF16": 2,
    "FP8": 1,
    "INT8": 1
}

def get_precision_support(major, minor):
    sm = (major, minor)
    support = {"FP32": True, "FP64": True, "FP16": False, "BF16": False,
               "TF32": False, "INT8": False, "FP8": False, "TensorCore": False}

    if sm >= (7, 0):  # Volta+
        support["TensorCore"] = True
        support["FP16"] = True
    if sm >= (7, 5):  # Turing+
        support["INT8"] = True
    if sm >= (8, 0):  # Ampere+
        support["BF16"] = True
        support["TF32"] = True
    if sm >= (9, 0):  # Hopper+
        support["FP8"] = True
    return support

def format_size(bytes_per_element, num_elements=1e6):
    """格式化显示 100万个元素占用的显存"""
    total_bytes = bytes_per_element * num_elements
    if total_bytes < 1024**2:
        return f"{total_bytes:.1f} B"
    elif total_bytes < 1024**3:
        return f"{total_bytes/1024**2:.2f} MB"
    else:
        return f"{total_bytes/1024**3:.2f} GB"

def main():
    if not torch.cuda.is_available():
        print("❌ CUDA 不可用")
        return
    
    props = torch.cuda.get_device_properties(0)
    print(props)
    sm = (props.major, props.minor)
    arch = ARCH_MAP.get(sm, f"未知架构 (SM {sm[0]}.{sm[1]})")

    print(f"✅ GPU: {props.name}")
    print(f"SM (Compute Capability): {sm[0]}.{sm[1]}")
    print(f"架构: {arch}")
    print(f"显存: {props.total_memory/1024**3:.2f} GB")
    print("-" * 50)

    support = get_precision_support(props.major, props.minor)
    print("👉 精度支持情况 (以 100万元素为例)：")
    for k, v in support.items():
        if k == "TensorCore":
            print(f"{k:9}: {'✅ 支持' if v else '❌ 不支持'}")
        else:
            if v:
                bytes_per_elem = PRECISION_BYTES[k]
                print(f"{k:9}: ✅ 支持 | 每元素 {bytes_per_elem} B | 100万元素≈ {format_size(bytes_per_elem)}")
            else:
                print(f"{k:9}: ❌ 不支持")

if __name__ == "__main__":
    main()