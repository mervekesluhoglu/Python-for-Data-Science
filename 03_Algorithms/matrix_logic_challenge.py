import numpy as np

# ---------------------------------------------------------
# Proje: Matris Mantık ve Filtreleme Algoritması
# Amaç: İki matrisin elemanlarını çapraz şekilde işleme sokmak 
#       ve belirli eşik değerlerine (threshold) göre filtrelemek.
# ---------------------------------------------------------

def run_matrix_logic():
    # 1. Veri Hazırlığı
    A = np.random.rand(3, 5)  # 3x5 rastgele matris
    B = np.arange(15).reshape(3, 5)
    C = A + B
    
    # D ve E matrisleri üzerinden F matrisini hesaplama
    D = np.linspace(10, 50, 15).reshape(3, 5)
    E = np.arange(10, 160, 10).reshape(3, 5)
    F = D + E

    # 2. Yeniden Şekillendirme (Flattening)
    C_flat = C.reshape(-1, 1)
    F_flat = F.reshape(-1, 1)
    
    # F matrisini ters çevirme (Çapraz eşleşme için)
    F_reversed = F_flat[::-1]

    # 3. Koşullu Filtreleme Algoritması
    # C'nin ilk elemanı ile F'nin son elemanını (ters haliyle ilk) toplayarak ilerleme
    G1 = []  # 1'den büyük olanlar
    G2 = []  # 1'den küçük veya eşit olanlar

    for i in range(len(C_flat)):
        toplam_deger = C_flat[i, 0] + F_reversed[i, 0]
        
        if toplam_deger > 1:
            G1.append(toplam_deger)
        else:
            G2.append(toplam_deger)

    # 4. Sonuçları Raporlama
    print(f"İşlem yapılan toplam eleman sayısı: {len(C_flat)}")
    print(f"G1 Listesi (Toplam > 1) eleman sayısı: {len(G1)}")
    print(f"G2 Listesi (Toplam <= 1) eleman sayısı: {len(G2)}")
    
    return G1, G2

if __name__ == "__main__":
    g1, g2 = run_matrix_logic()
