# 🎓 LGS Hazırlık Test Programı

Modern ve interaktif LGS sınav hazırlık uygulaması. Progressive Web App (PWA) desteği ile offline çalışır.

## ✨ Özellikler

### 📝 Test Türleri
- **Mini Test**: 10 soruluk hızlı testler
- **Kombo Rekor**: Ardışık doğru cevap rekoru
- **LGS Test**: 135 dakikalık tam sınav simülasyonu

### 📊 İstatistik ve Analiz
- Detaylı performans analizi
- Test geçmişi takibi
- Grafik gösterimleri (Recharts)
- Kombo rekoru takibi

### 📱 PWA Özellikleri
- Offline çalışma (Service Worker)
- Ana ekrana yüklenebilir
- Native app deneyimi
- Cross-platform uyumluluk

### 👥 Kullanıcı Sistemi
- Çoklu kullanıcı desteği
- Kişisel ilerleme takibi
- Veri yedekleme/geri yükleme

## 🚀 Hızlı Başlangıç

### Online Demo
🌐 **[Canlı Demo](https://KULLANICI_ADI.github.io/lgs-test-app/LGS_Test.html)**

### Mobil Kullanım
1. Yukarıdaki linke gidin
2. Tarayıcı menüsünden "Ana ekrana ekle" seçin
3. Uygulama gibi kullanın!

## 🛠️ Geliştirme

### Gereksinimler
- Modern web tarayıcı (Chrome, Firefox, Safari, Edge)
- Python 3.x (veri işleme scriptleri için)
- Live Server (geliştirme için)

### Kurulum
```bash
git clone https://github.com/KULLANICI_ADI/lgs-test-app.git
cd lgs-test-app
```

### Geliştirme Modunda Çalıştırma
```bash
# VS Code ile açın ve Live Server extension kullanın
# Veya Python ile basit server:
python -m http.server 8000
```

### Yeni Sorular Ekleme
```bash
# 1. Excel dosyalarını güncelleyin
# 2. Embedded data'yı yeniden oluşturun:
python convert_excel_to_js.py

# 3. Standalone versiyon oluşturun:
python create_standalone.py
```

## 📁 Dosya Yapısı

```
├── 📄 LGS_Test.html              # Ana geliştirme dosyası
├── 📄 LGS_Test_Standalone.html   # Dağıtım için optimize edilmiş
├── 📄 manifest.json              # PWA manifest
├── 📄 service-worker.js          # Offline destek
├── 📁 DinKültürü/               # Soru resimleri
├── 📁 FenBilimleri/             # Soru resimleri
├── 📁 Matematik/                # Soru resimleri
├── 📄 *.xlsx                    # Excel soru veritabanları
└── 📄 *.py                      # Yardımcı scriptler
```

## 🎯 Teknolojiler

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Framework**: React (CDN)
- **Styling**: Tailwind CSS
- **Charts**: Recharts
- **PWA**: Service Worker, Web App Manifest
- **Data**: LocalStorage, Excel (SheetJS)
- **Build**: Python scripts

## 📈 Roadmap

Gelecek özellikler için [`yapılacaklar.txt`](yapılacaklar.txt) dosyasına bakın.

## 🤝 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/yeni-özellik`)
3. Commit yapın (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'i push edin (`git push origin feature/yeni-özellik`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında dağıtılmaktadır.

## 👨‍💻 Geliştirici

Bu proje Claude Sonnet 4 AI asistanı ile birlikte geliştirilmiştir.

---

⭐ Beğendiyseniz star verin!