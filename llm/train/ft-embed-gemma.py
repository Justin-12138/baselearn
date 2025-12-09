from datasets import Dataset

# 加载 Arrow 数据集
train_dataset = Dataset.from_file("/home/lz/repo/baselearn/llm/train/ft_gemma_embed/data-00000-of-00001.arrow")
print("原始数据：")
print(train_dataset[0])

# 新增一列 'anchor_text' 和 'positive_text'，不改原始结构
def extract_texts(example):
    anchor_text = (example["anchor"].get("question") or "") + " " + (example["anchor"].get("answer") or "")
    positive_text = example["positive"].get("chunk") or ""
    return {
        "anchor_text": anchor_text.strip(),
        "positive_text": positive_text.strip()
    }

train_dataset_pairs = train_dataset.map(extract_texts)
print("抽取后的数据：")
print(train_dataset_pairs[0])

print("字段名：", train_dataset_pairs.column_names)
