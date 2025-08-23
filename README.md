# Sıralama Algoritmaları Görselleştirici

Bu proje, çeşitli sıralama algoritmalarını interaktif ve görsel bir şekilde gösteren bir CustomTkinter uygulamasıdır.

## 🚀 Özellikler

### 📊 **8 Farklı Sıralama Algoritması:**
  - **Bubble Sort** (Kabarcık Sıralama)
  - **Selection Sort** (Seçim Sıralama)
  - **Insertion Sort** (Ekleme Sıralama)
  - **Quick Sort** (Hızlı Sıralama)
  - **Merge Sort** (Birleştirme Sıralama)
  - **Heap Sort** (Yığın Sıralama)
  - **Shell Sort** (Kabuk Sıralama)
  - **Radix Sort** (Taban Sıralama)

### 🎮 **İnteraktif Kontroller:**
  - **Algoritma seçimi** - Dropdown menü ile
  - **Liste boyutu ayarlama** (10, 25, 50, 100, 200 eleman)
  - **Sıralama hızı kontrolü** (0.01s - 0.5s arası)
  - **Seed sistemi** - Random veya özel seed değeri
  - **Gerçek zamanlı görselleştirme**

### ⏱️ **Kronometre Sistemi:**
  - **Dakika:Saniye.Milisaniye** formatında ölçüm
  - **Duraklat/Devam et** özelliği
  - **Sıralama tamamlandığında** final süre gösterimi
  - **Otomatik sıfırlama** sadece manuel işlemlerde

### 🎯 **Gelişmiş Kontrol Sistemi:**
  - **Duraklat (Pause)** - Sıralamayı ortada durdur
  - **Devam Et (Resume)** - Kaldığı yerden devam et
  - **Sıfırla (Reset)** - Orijinal diziye geri dön
  - **Yeni Liste Oluştur** - Rastgele yeni veri seti

### 🎨 **Görsel Özellikler:**
  - **Çubuk grafik görünümü** - Animasyonlu sıralama
  - **Renk kodlaması:**
    - 🔵 **Mavi** - Normal elemanlar
    - 🔴 **Kırmızı** - Karşılaştırılan elemanlar
    - 🟢 **Turkuaz** - Yer değiştirilen elemanlar
  - **Değer etiketleri** (50 elemana kadar)
  - **Flicker-free animasyon** - Göz yormayan görselleştirme

### 📚 **Eğitim Özellikleri:**
  - **ℹ️ Bilgi Butonu** - Her algoritma için detaylı açıklama
  - **Modal pencere** - Algoritma çalışma prensibi
  - **Karmaşıklık analizi** - Zaman ve uzay karmaşıklığı
  - **Avantaj/Dezavantaj** listesi
  - **Nasıl çalışır** adım adım açıklama

### 🖥️ **UI/UX İyileştirmeleri:**
  - **Tam ekran başlatma** - Maksimum görselleştirme alanı
  - **İki satırlı kontrol paneli** - Tüm butonlar görünür
  - **Responsive tasarım** - Farklı ekran boyutlarına uyum
  - **Dark tema** - Göz dostu arayüz
  - **Yeniden boyutlandırma engeli** - Tutarlı deneyim

## 🛠️ Kurulum

1. **Python 3.7+** sürümünün yüklü olduğundan emin olun
2. **Gerekli paketleri** yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Kullanım

### **Uygulamayı Başlatma:**
```bash
python sorting_visualizer.py
```

### **Temel Kontroller:**

#### **Üst Kontrol Satırı:**
- **Algoritma:** Dropdown menüden sıralama algoritması seçin
- **ℹ️ Bilgi:** Seçilen algoritma hakkında detaylı bilgi alın
- **Liste Boyutu:** 10-200 arası eleman sayısı
- **Hız:** 0.01s - 0.5s arası animasyon hızı
- **Seed:** Random veya özel seed değeri

#### **Alt Kontrol Satırı:**
- **Yeni Liste Oluştur:** Rastgele yeni veri seti
- **Sıralamayı Başlat:** Seçilen algoritma ile başlat
- **Durdur:** Çalışan sıralamayı duraklat
- **Devam Et:** Duraklatılan sıralamayı devam ettir
- **Sıfırla:** Orijinal diziye geri dön

### **Gelişmiş Özellikler:**

#### **Seed Sistemi:**
- **Random:** Sistem zamanına göre rastgele
- **Custom:** Belirli bir sayı ile tutarlı sonuçlar
- **Takım çalışması** için aynı veri setini kullanın

#### **Kronometre:**
- **Otomatik başlatma** sıralama ile
- **Duraklat/Devam et** sıralama ile senkronize
- **Final süre** sıralama tamamlandığında
- **Manuel sıfırlama** gerekli

#### **Bilgi Modalı:**
- **ℹ️ Buton** ile açılır
- **Scrollable içerik** ile tüm bilgiler
- **Detaylı açıklamalar** her algoritma için
- **Karmaşıklık analizi** ve performans bilgileri

## 📊 Algoritma Detayları

### **Bubble Sort**
- **Açıklama:** En basit sıralama algoritması
- **Çalışma:** Komşu elemanları karşılaştır ve yer değiştir
- **Karmaşıklık:** O(n²) - En kötü durum
- **Avantaj:** Basit, ekstra bellek gerektirmez
- **Dezavantaj:** Büyük listeler için çok yavaş

### **Selection Sort**
- **Açıklama:** En küçük elemanı bul ve başa taşı
- **Çalışma:** Minimum elemanı bul, yer değiştir
- **Karmaşıklık:** O(n²) - Her durumda
- **Avantaj:** Yer değiştirme sayısı az
- **Dezavantaj:** Her durumda O(n²)

### **Insertion Sort**
- **Açıklama:** Elemanları tek tek uygun pozisyona yerleştir
- **Çalışma:** Her elemanı öncekilerle karşılaştır
- **Karmaşıklık:** O(n²) ortalama, O(n) en iyi
- **Avantaj:** Küçük listeler için verimli
- **Dezavantaj:** Büyük listeler için yavaş

### **Quick Sort**
- **Açıklama:** Pivot ile böl ve recursive sırala
- **Çalışma:** Pivot seç, küçükleri sola, büyükleri sağa
- **Karmaşıklık:** O(n log n) ortalama, O(n²) en kötü
- **Avantaj:** Ortalama durumda çok hızlı
- **Dezavantaj:** En kötü durumda O(n²)

### **Merge Sort**
- **Açıklama:** Böl, sırala, birleştir
- **Çalışma:** Listeyi ikiye böl, recursive sırala
- **Karmaşıklık:** O(n log n) - Her durumda
- **Avantaj:** Kararlı performans, büyük veri için uygun
- **Dezavantaj:** Ekstra bellek gerektirir
- **Kararlılık:** ✅ Evet

### **Heap Sort**
- **Açıklama:** Heap veri yapısını kullan
- **Çalışma:** Max heap oluştur, root'u sona taşı
- **Karmaşıklık:** O(n log n) - Her durumda
- **Avantaj:** Her durumda O(n log n)
- **Dezavantaj:** Cache dostu değil

### **Shell Sort**
- **Açıklama:** Insertion Sort'un geliştirilmiş versiyonu
- **Çalışma:** Gap ile grupla, Insertion Sort uygula
- **Karmaşıklık:** O(n^1.5) ortalama
- **Avantaj:** Insertion Sort'tan daha hızlı
- **Dezavantaj:** Gap sequence kritik

### **Radix Sort**
- **Açıklama:** Basamaklarına göre sırala
- **Çalışma:** Her basamak için Counting Sort
- **Karmaşıklık:** O(d(n+k)) - d: basamak sayısı
- **Avantaj:** Sayısal veriler için çok hızlı
- **Dezavantaj:** Sadece sayısal veriler için

## 💻 Sistem Gereksinimleri

- **Python:** 3.7 veya üzeri
- **İşletim Sistemi:** Windows/macOS/Linux
- **Paketler:** CustomTkinter 5.2.0+
- **Ekran:** Minimum 1200x800 çözünürlük (tam ekran önerilir)

## 🔧 Teknik Özellikler

### **Performans Optimizasyonları:**
- **Threading:** UI donmaz, sıralama ayrı thread'de
- **Canvas optimizasyonu:** Sadece değişen elemanlar güncellenir
- **Flicker-free rendering:** Göz yormayan animasyon
- **Memory efficient:** Büyük listeler için optimize

### **UI Framework:**
- **CustomTkinter:** Modern, güzel arayüz
- **Dark tema:** Göz dostu renk paleti
- **Responsive layout:** Farklı ekran boyutlarına uyum
- **Modal windows:** Bilgi gösterimi için

## 📚 Eğitim Kullanımı

### **Sınıf İçi Gösterim:**
- Algoritma karşılaştırması
- Performans analizi
- Görsel öğrenme
- İnteraktif deneyim

### **Bireysel Öğrenme:**
- Algoritma çalışma prensibi
- Karmaşıklık analizi
- Performans karşılaştırması
- Kod optimizasyonu

### **Araştırma ve Test:**
- Seed sistemi ile tutarlı testler
- Farklı veri setleri
- Algoritma performans analizi
- Benchmark karşılaştırması

## 🚀 Gelecek Özellikler

- [ ] **Çoklu algoritma** aynı anda çalıştırma
- [ ] **Grafik analizi** - Performans grafikleri
- [ ] **Veri seti import/export** - CSV, JSON desteği
- [ ] **Algoritma karşılaştırma** - Side-by-side görünüm
- [ ] **Özel algoritma** ekleme desteği
- [ ] **Batch testing** - Çoklu test senaryoları

## 🤝 Katkıda Bulunma

1. **Projeyi fork** edin
2. **Feature branch** oluşturun (`git checkout -b feature/AmazingFeature`)
3. **Değişikliklerinizi commit** edin (`git commit -m 'Add some AmazingFeature'`)
4. **Branch'inizi push** edin (`git push origin feature/AmazingFeature`)
5. **Pull Request** oluşturun

### **Katkı Alanları:**
- 🐛 Bug düzeltmeleri
- ✨ Yeni özellikler
- 📚 Dokümantasyon iyileştirmeleri
- 🎨 UI/UX geliştirmeleri
- 🚀 Performans optimizasyonları

## 📄 Lisans

Bu proje **eğitim amaçlı** geliştirilmiştir. Özgürce kullanabilir, değiştirebilir ve dağıtabilirsiniz.

## 📞 İletişim

- **GitHub Issues:** Proje sayfasında issue açın
- **Pull Requests:** Katkılarınızı bekliyoruz
- **Öneriler:** Yeni özellik önerileri için issue açın

## 🙏 Teşekkürler

Bu proje, sıralama algoritmalarını öğrenmek ve öğretmek isteyen herkes için geliştirilmiştir. Katkıda bulunan herkese teşekkürler!

---

**⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın!**
