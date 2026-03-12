import numpy as np

# 1. Array Oluşturma ve Reshape (1D -> 2D)
dizi = np.arange(1, 16)
matris = dizi.reshape(3, 5)
print(f"3x5 Boyutlu Matris:\n{matris}")

# 2. İstatistiksel Hesaplamalar
print(f"Matris Toplamı: {np.sum(matris)}")
print(f"Sütun Bazlı Ortalamalar: {matris.mean(axis=0)}")

# 3. Stacking (Matris Birleştirme)
dizi1 = np.array([[1, 2], [3, 4]])
dizi2 = np.array([[-1, -2], [-3, -4]])
print("Dikey Birleştirme (Vertical Stack):")
print(np.vstack((dizi1, dizi2)))
