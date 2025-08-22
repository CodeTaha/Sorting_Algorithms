# Sıralama Algoritmaları Görselleştirici

Bu proje, çeşitli sıralama algoritmalarını interaktif ve görsel bir şekilde gösteren bir CustomTkinter uygulamasıdır.

## Özellikler

- **8 Farklı Sıralama Algoritması:**
  - Bubble Sort (Kabarcık Sıralama)
  - Selection Sort (Seçim Sıralama)
  - Insertion Sort (Ekleme Sıralama)
  - Quick Sort (Hızlı Sıralama)
  - Merge Sort (Birleştirme Sıralama)
  - Heap Sort (Yığın Sıralama)
  - Shell Sort (Kabuk Sıralama)
  - Radix Sort (Taban Sıralama)

- **İnteraktif Kontroller:**
  - Algoritma seçimi
  - Liste boyutu ayarlama (10, 25, 50, 100, 200 eleman)
  - Sıralama hızı kontrolü (0.01s - 0.5s arası)
  - Gerçek zamanlı görselleştirme

- **Görsel Özellikler:**
  - Çubuk grafik görünümü
  - Renk kodlaması (karşılaştırma, yer değiştirme)
  - Animasyonlu sıralama süreci
  - Değer etiketleri (küçük listeler için)

## Kurulum

1. Python 3.7 veya üzeri sürümünün yüklü olduğundan emin olun
2. Gerekli paketleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

## Kullanım

Uygulamayı başlatmak için:
```bash
python sorting_visualizer.py
```

### Kontroller

- **Algoritma Seçimi:** Dropdown menüden istediğiniz sıralama algoritmasını seçin
- **Liste Boyutu:** 10 ile 200 arasında eleman sayısı seçin
- **Hız Ayarı:** Sıralama animasyonunun hızını ayarlayın
- **Yeni Liste Oluştur:** Rastgele yeni bir liste oluşturun
- **Sıralamayı Başlat:** Seçilen algoritma ile sıralamayı başlatın
- **Durdur:** Çalışan sıralama işlemini durdurun

### Görsel Gösterim

- **Mavi çubuklar:** Normal elemanlar
- **Kırmızı çubuklar:** Karşılaştırılan elemanlar
- **Turkuaz çubuklar:** Yer değiştirilen elemanlar

## Algoritma Açıklamaları

### Bubble Sort
En basit sıralama algoritması. Komşu elemanları karşılaştırarak sıralar.

### Selection Sort
En küçük elemanı bulup başa taşıyarak sıralar.

### Insertion Sort
Elemanları tek tek alıp uygun pozisyona yerleştirir.

### Quick Sort
Pivot eleman seçerek listeyi böler ve recursive olarak sıralar.

### Merge Sort
Listeyi ikiye böler, sıralar ve birleştirir.

### Heap Sort
Heap veri yapısını kullanarak sıralar.

### Shell Sort
Insertion sort'un geliştirilmiş versiyonu, gap kullanır.

### Radix Sort
Sayıları basamaklarına göre sıralar.

## Sistem Gereksinimleri

- Python 3.7+
- Windows/macOS/Linux
- CustomTkinter 5.2.0+

## Lisans

Bu proje eğitim amaçlı geliştirilmiştir.

## Katkıda Bulunma

1. Projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request oluşturun

## İletişim

Sorularınız için issue açabilir veya projeyi geliştirmeye katkıda bulunabilirsiniz.
