import torch
import time
import matplotlib.pyplot as plt
import numpy as np
from transformers import AutoModelForCausalLM, AutoTokenizer

# 加载模型
model_path = "/home/lz/repo/baselearn/llm/models/qwen2.5-0.5b-ins"
model = AutoModelForCausalLM.from_pretrained(
    model_path, 
    torch_dtype=torch.float32, 
    device_map="cpu"
)
tok = AutoTokenizer.from_pretrained(model_path)

print("=" * 80)
print("KV Cache 性能对比基准测试")
print("=" * 80)

# 测试文本
prompt = "Hello world, I am"
inputs = tok(prompt, return_tensors="pt")

# 测试不同的生成步数
test_steps = [20,40, 60,80,100]
results = {
    'steps': [],
    'no_cache_time': [],
    'cache_time': [],
    'speedup': [],
    'memory_mb': []
}

for generation_steps in test_steps:
    print(f"\n{'='*80}")
    print(f"测试 {generation_steps} 个 token 的生成")
    print(f"{'='*80}")
    
    # ========================================================================
    # 方案 1: 不使用 KV Cache
    # ========================================================================
    print("🔴 测试不使用 KV Cache...")
    generated_ids = inputs['input_ids'].clone()
    
    start_time = time.time()
    for step in range(generation_steps):
        outputs = model(generated_ids, use_cache=False)
        next_token_logits = outputs.logits[:, -1, :]
        next_token = torch.argmax(next_token_logits, dim=-1, keepdim=True)
        generated_ids = torch.cat([generated_ids, next_token], dim=1)
    
    no_cache_time = time.time() - start_time
    print(f"   ⏱️  耗时: {no_cache_time:.3f} 秒")
    
    # ========================================================================
    # 方案 2: 使用 KV Cache
    # ========================================================================
    print("🟢 测试使用 KV Cache...")
    generated_ids = inputs['input_ids'].clone()
    past_key_values = None
    
    start_time = time.time()
    for step in range(generation_steps):
        if step == 0:
            current_input = generated_ids
        else:
            current_input = generated_ids[:, -1:]
        
        outputs = model(
            current_input, 
            past_key_values=past_key_values,
            use_cache=True
        )
        past_key_values = outputs.past_key_values
        
        next_token_logits = outputs.logits[:, -1, :]
        next_token = torch.argmax(next_token_logits, dim=-1, keepdim=True)
        generated_ids = torch.cat([generated_ids, next_token], dim=1)
    
    cache_time = time.time() - start_time
    print(f"   ⏱️  耗时: {cache_time:.3f} 秒")
    
    # 计算 KV Cache 内存占用
    total_bytes = 0
    for k, v in zip(past_key_values.key_cache, past_key_values.value_cache):
        if k is not None and v is not None:
            total_bytes += k.numel() * k.element_size()
            total_bytes += v.numel() * v.element_size()
    
    memory_mb = total_bytes / 1024 / 1024
    speedup = no_cache_time / cache_time
    
    print(f"   🚀 加速比: {speedup:.2f}x")
    print(f"   💾 内存: {memory_mb:.2f} MB")
    
    # 保存结果
    results['steps'].append(generation_steps)
    results['no_cache_time'].append(no_cache_time)
    results['cache_time'].append(cache_time)
    results['speedup'].append(speedup)
    results['memory_mb'].append(memory_mb)

# ============================================================================
# 绘制对比图表
# ============================================================================
print("\n" + "=" * 80)
print("📊 生成可视化图表...")
print("=" * 80)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('KV Cache', fontsize=16, fontweight='bold')


plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 图1: 绝对时间对比
ax1 = axes[0, 0]
x = np.arange(len(results['steps']))
width = 0.35
bars1 = ax1.bar(x - width/2, results['no_cache_time'], width, 
                label='Without Cache', color='#ff6b6b', alpha=0.8)
bars2 = ax1.bar(x + width/2, results['cache_time'], width, 
                label='With Cache', color='#51cf66', alpha=0.8)

ax1.set_xlabel('Number of Generated Tokens', fontsize=11)
ax1.set_ylabel('Time (seconds)', fontsize=11)
ax1.set_title('Absolute Time Comparison', fontsize=12, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(results['steps'])
ax1.legend()
ax1.grid(True, alpha=0.3, linestyle='--')

# 添加数值标签
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}s', ha='center', va='bottom', fontsize=8)

# 图2: 加速比
ax2 = axes[0, 1]
line = ax2.plot(results['steps'], results['speedup'], 
                marker='o', linewidth=2.5, markersize=8, 
                color='#4c6ef5', label='Speedup Ratio')
ax2.fill_between(results['steps'], results['speedup'], alpha=0.3, color='#4c6ef5')
ax2.set_xlabel('Number of Generated Tokens', fontsize=11)
ax2.set_ylabel('Speedup (x)', fontsize=11)
ax2.set_title('KV Cache Acceleration Effect', fontsize=12, fontweight='bold')
ax2.grid(True, alpha=0.3, linestyle='--')
ax2.axhline(y=1, color='red', linestyle='--', alpha=0.5, label='Baseline (1x)')
ax2.legend()

# 添加数值标签
for x, y in zip(results['steps'], results['speedup']):
    ax2.text(x, y, f'{y:.2f}x', ha='center', va='bottom', fontsize=9)

# 图3: 内存占用
ax3 = axes[1, 0]
bars = ax3.bar(results['steps'], results['memory_mb'], 
               color='#ffa94d', alpha=0.8, edgecolor='#fd7e14', linewidth=1.5)
ax3.set_xlabel('Number of Generated Tokens', fontsize=11)
ax3.set_ylabel('Memory Usage (MB)', fontsize=11)
ax3.set_title('KV Cache Memory Overhead', fontsize=12, fontweight='bold')
ax3.grid(True, alpha=0.3, linestyle='--', axis='y')

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.2f}', ha='center', va='bottom', fontsize=9)

# 图4: 效率对比（时间节省百分比）
ax4 = axes[1, 1]
time_saved_pct = [(no - cache) / no * 100 
                  for no, cache in zip(results['no_cache_time'], results['cache_time'])]
bars = ax4.bar(results['steps'], time_saved_pct, 
               color='#20c997', alpha=0.8, edgecolor='#12b886', linewidth=1.5)
ax4.set_xlabel('Number of Generated Tokens', fontsize=11)
ax4.set_ylabel('Time Saved (%)', fontsize=11)
ax4.set_title('Time Saving Percentage', fontsize=12, fontweight='bold')
ax4.grid(True, alpha=0.3, linestyle='--', axis='y')

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.1f}%', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('kv_cache_comparison.png', dpi=300, bbox_inches='tight')
print("✅ 图表已保存为 'kv_cache_comparison.png'")
plt.show()

# ============================================================================
# 打印汇总表格
# ============================================================================
print("\n" + "=" * 80)
print("📊 性能汇总表")
print("=" * 80)
print(f"{'Token数':<10} {'无Cache(s)':<12} {'有Cache(s)':<12} {'加速比':<10} "
      f"{'时间节省':<12} {'内存(MB)':<10}")
print("-" * 80)

for i in range(len(results['steps'])):
    time_saved = (results['no_cache_time'][i] - results['cache_time'][i]) / results['no_cache_time'][i] * 100
    print(f"{results['steps'][i]:<10} "
          f"{results['no_cache_time'][i]:<12.3f} "
          f"{results['cache_time'][i]:<12.3f} "
          f"{results['speedup'][i]:<10.2f} "
          f"{time_saved:<12.1f}% "
          f"{results['memory_mb'][i]:<10.2f}")

print("=" * 80)
print("\n✅ 关键发现:")
print(f"   • 最大加速比: {max(results['speedup']):.2f}x (生成 {results['steps'][results['speedup'].index(max(results['speedup']))]} tokens)")
print(f"   • 平均加速比: {np.mean(results['speedup']):.2f}x")
print(f"   • 最大内存开销: {max(results['memory_mb']):.2f} MB")
print(f"   • 结论: 生成 token 越多，KV Cache 优势越明显")
print("=" * 80)