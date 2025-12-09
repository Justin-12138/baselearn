import time
import numpy as np
import mymath   # 你写好的 C 扩展

# 生成数据
N = 10_000_000
data = [i * 0.1 for i in range(N)]
np_data = np.array(data, dtype=np.float64)

# -------------------------------
# Python 原生循环
# -------------------------------
t1 = time.time()
sum1 = sum([x * x for x in data])
t2 = time.time()
print(f"Python 循环: {sum1:.2f}, 用时 {t2 - t1:.3f} 秒")

# -------------------------------
# NumPy 矢量化
# -------------------------------
t1 = time.time()
sum2 = np.sum(np_data * np_data)
t2 = time.time()
print(f"NumPy 矢量化: {sum2:.2f}, 用时 {t2 - t1:.3f} 秒")

# -------------------------------
# C 扩展 + OpenMP
# -------------------------------
t1 = time.time()
sum3 = mymath.parallel_sum(data)
t2 = time.time()
print(f"C 扩展 (OpenMP): {sum3:.2f}, 用时 {t2 - t1:.3f} 秒")
