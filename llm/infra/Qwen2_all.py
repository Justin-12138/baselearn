import os
import time
import psutil
import datetime
import threading
import matplotlib.pyplot as plt
from transformers import Qwen2ForCausalLM, Qwen2Tokenizer,GenerationMixin,DynamicCache

from utils.utils import long_prompts,short_prompts

mem_log = []
time_log = []
sampling = True

def memory_sampler(interval=0.5):
    process = psutil.Process(os.getpid())
    start_time = time.time()
    while sampling:
        mem_mb = process.memory_info().rss / 1024 / 1024
        mem_log.append(mem_mb)
        time_log.append(time.time() - start_time)
        time.sleep(interval)

def print_memory_usage(step):
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / 1024 / 1024  # MB
    print(f"{step} - 内存使用: {mem:.2f} MB")


thread = threading.Thread(target=memory_sampler, daemon=True)
thread.start()

model_path = "/home/lz/repo/baselearn/llm/models/qwen2.5-0.5b-ins"
print_memory_usage("启动脚本")

tokenizer = Qwen2Tokenizer.from_pretrained(model_path,return_attention_mask=True,padding_side='left')
print_memory_usage("加载Tokenizer后")


prompts = []
for i in range(1):
    prompts.append(short_prompts)
# prompts.append("I am Julie")

batch_inputs = tokenizer(prompts, return_tensors="pt", padding=True).input_ids




for i, ids in enumerate(batch_inputs):
    tokens = tokenizer.convert_ids_to_tokens(ids)
    print(f"\n提示词 {i}:")
    for tid, tok in zip(ids.tolist(), tokens):
        print(f"  {tid:<6} -> {tok}")

model = Qwen2ForCausalLM.from_pretrained(model_path)
batch_inputs_embed = model.model.embed_tokens(batch_inputs)


print('*'*50+'batch_embedding'+'*'*50)
print(batch_inputs_embed.shape)
print("inputs_embeds 前20个元素:", batch_inputs_embed.view(-1)[:20])


print('*'*50+'batch_embedding'+'*'*50)

print_memory_usage("模型加载完成")


# cache = DynamicCache()
# outputs = model(**batch_inputs, past_key_values=cache, use_cache=True)

outputs = model.generate(
    batch_inputs,
    max_new_tokens=2,
    output_scores=True,
    return_dict_in_generate=True
)
print_memory_usage("推理完成")

sampling = False
thread.join()

plt.figure(figsize=(10, 6))
plt.plot(time_log, mem_log, label="memory used (MB)")
plt.xlabel("time (s)")
plt.ylabel("memory (MB)")
plt.title("memory with the llm inference (batch processing)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("res.png")


