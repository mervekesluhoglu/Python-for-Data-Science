"""
Biomedical Data Analysis with Pandas
-----------------------------------
İçerik: Hasta verileri üzerinde DataFrame operasyonları, 
       filtreleme, veri temizleme ve toplu işlem (Apply/Map).
"""

import pandas as pd
import numpy as np

# 1. Sentetik Hasta Veri Seti Oluşturma (EDA Hazırlık)
patient_dict = {
    "patient_id": ["P1", "P2", "P3", "P4", "P5", "P6"],
    "age": [15, 16, 17, 33, np.nan, 66],  # Missing value (NaN) yönetimi için
    "salary_level": [100.0, 150.0, 240.0, 350.0, 110.0, 220.0],
    "city": ["Izmir", "Ankara", "Konya", "Ankara", "Ankara", "Antalya"]
}

df = pd.DataFrame(patient_dict)

# 2. Keşifsel Veri Analizi (EDA) Fonksiyonları
print("--- Veri Özeti ---")
print(df.info())
print("\n--- İstatistiksel Analiz ---")
print(df.describe())

# 3. İleri Seviye Filtreleme (Boolean Indexing)
# Ankara'da yaşayan ve yaşı 22'den büyük olan hastalar
filtered_patients = df.loc[(df["city"] == "Ankara") & (df["age"] > 22)]
print("\nFiltrelenmiş Hastalar (Ankara & Yaş > 22):")
print(filtered_patients)

# 4. Özellik Mühendisliği (Feature Engineering)
# Yaş ortalamasına göre gruplandırma (List Comprehension)
age_mean = df["age"].mean()
df["age_group"] = ["Senior" if x > age_mean else "Junior" for x in df["age"]]

# 5. Apply Fonksiyonu ile Dinamik Hesaplama
def risk_score_calc(row):
    """Basit bir sağlık risk skoru simülasyonu"""
    if row["age"] > 50:
        return "High Risk"
    elif row["city"] == "Ankara":
        return "Medium Risk"
    else:
        return "Low Risk"

df["health_risk"] = df.apply(risk_score_calc, axis=1)

print("\n--- Güncellenmiş DataFrame ---")
print(df.head(6))

# 6. Veri Birleştirme (Stacking & Concatenation)
df_extra = pd.DataFrame({"patient_id": ["P7"], "age": [40], "city": ["Istanbul"]})
df_combined = pd.concat([df, df_extra], axis=0, ignore_index=True)
