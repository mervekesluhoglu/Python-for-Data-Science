"""
Biomedical Data Visualization with Matplotlib
--------------------------------------------
İçerik: Iris ve Meme Kanseri veri setleri üzerinde karşılaştırmalı 
       görselleştirme, Histogram, Scatter Plot ve Subplots kullanımı.
"""

import pandas as pd
import matplotlib.pyplot as plt

def iris_visualization_demo(df):
    """Iris veri seti üzerinde temel grafik türlerini gösterir."""
    plt.figure(figsize=(10, 5))
    
    # Çizgi Grafiği (Line Plot)
    plt.plot(df["Id"], df["SepalLengthCm"], label="Sepal Length", alpha=0.7)
    plt.plot(df["Id"], df["PetalLengthCm"], label="Petal Length", color='red', alpha=0.7)
    plt.title("İris Parametrelerinin Dağılımı")
    plt.xlabel("Örnek ID")
    plt.ylabel("Uzunluk (cm)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

def cancer_diagnosis_analysis(data):
    """Malignant (M) ve Benign (B) tümör verilerini karşılaştırmalı görselleştirir."""
    # Veri Ayırma
    m = data[data["diagnosis"] == "M"].reset_index(drop=True)
    b = data[data["diagnosis"] == "B"].reset_index(drop=True)

    # 2x3 Subplot Yapısı
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle("Meme Kanseri Veri Analizi: Malignant (M) vs Benign (B)", fontsize=16)

    # --- Üst Satır: Malignant (M) ---
    axes[0, 0].scatter(m.radius_mean, m.texture_mean, color='darkred', alpha=0.5)
    axes[0, 0].set_title("M: Radius vs Texture")
    
    axes[0, 1].hist(m.radius_mean, bins=15, color='red', edgecolor='black')
    axes[0, 1].set_title("M: Radius Histogram")
    
    axes[0, 2].plot(m.radius_mean, color='red')
    axes[0, 2].set_title("M: Radius Line Plot")

    # --- Alt Satır: Benign (B) ---
    axes[1, 0].scatter(b.radius_mean, b.texture_mean, color='darkblue', alpha=0.5)
    axes[1, 0].set_title("B: Radius vs Texture")
    
    axes[1, 1].hist(b.radius_mean, bins=15, color='blue', edgecolor='black')
    axes[1, 1].set_title("B: Radius Histogram")
    
    axes[1, 2].plot(b.radius_mean, color='blue')
    axes[1, 2].set_title("B: Radius Line Plot")

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

# Not: Veri setlerinin yüklü olduğu varsayılmıştır.
# data = pd.read_csv("breast-cancer-data.csv")
# cancer_diagnosis_analysis(data)
