"""最小二乘线性回归演示：y = a*x + b

运行：python3.12 lr_demo.py
依赖：pip install numpy
"""
import numpy as np

def fit(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    a, b = np.polyfit(x, y, 1)
    return float(a), float(b)

if __name__ == "__main__":
    x = np.array([1, 2, 3, 4, 5], dtype=float)
    y = np.array([2.1, 3.9, 6.1, 7.8, 10.2])
    a, b = fit(x, y)
    print(f"y = {a:.3f} * x + {b:.3f}")
