# ---------------------------------------------------------
# Veri Yapıları ve Kontrol Akışı (Data Structures)
# İçerik: Listeler, Sözlükler, Koşullu İfadeler ve Döngüler
# ---------------------------------------------------------

# 1. Liste Operasyonları ve Slicing
hafta_liste = ["pazartesi", "sali", "carsamba", "persembe", "cuma", "cumartesi", "pazar"]
print(f"Hafta içi günleri: {hafta_liste[0:5]}")

# 2. Sözlük (Dictionary) Yapısı - Tıbbi Veri Temsili Örneği
hasta_bilgileri = {
    "isim": "Ahmet",
    "nabiz": 72,
    "durum": "Stabil"
}
print(f"Hasta Durumu: {hasta_bilgileri['durum']}")

# 3. For Döngüsü ve NLP Uygulaması (Metin Parçalama)
cumle = "Bugün Python Dersimiz Var."
kelimeler = [k.lower() for k in cumle.split()]
print(f"Küçük harf kelime listesi: {kelimeler}")

# 4. Fonksiyonel Analiz (Çift Sayı Toplamı)
def cift_sayi_toplami(sayi_listesi):
    return sum([i for i in sayi_listesi if i % 2 == 0])

liste = [1, 2, 3, 4, 5, 6]
print(f"Listenin çift sayıları toplamı: {cift_sayi_toplami(liste)}")
