import os
import shutil
import zipfile
import json
from datetime import datetime
from pathlib import Path

def create_project_archive():
    """LGS Test projesinin tam arşivini oluşturur"""
    
    # Tarih damgası
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"LGS_Test_Project_Archive_{timestamp}"
    
    # Arşiv klasörü oluştur
    archive_dir = Path(archive_name)
    archive_dir.mkdir(exist_ok=True)
    
    print(f"🗂️ Proje arşivi oluşturuluyor: {archive_name}")
    
    # 1. Tüm proje dosyalarını kopyala
    project_files = [
        "LGS_Test.html",
        "LGS_Test_Standalone.html", 
        "manifest.json",
        "service-worker.js",
        "embedded_excel_data.js",
        "convert_excel_to_js.py",
        "create_standalone.py",
        "create_icons.py",
        "browserconfig.xml"
    ]
    
    code_dir = archive_dir / "01_Project_Files"
    code_dir.mkdir(exist_ok=True)
    
    for file in project_files:
        if Path(file).exists():
            shutil.copy2(file, code_dir)
            print(f"✓ Kopyalandı: {file}")
    
    # 2. Excel dosyalarını kopyala
    excel_dir = archive_dir / "02_Excel_Data"
    excel_dir.mkdir(exist_ok=True)
    
    excel_files = [
        "DinKulturu.xlsx", "FenBilimleri.xlsx", "inkilapTarihi.xlsx",
        "Matematik.xlsx", "SosyalBilgiler.xlsx", "Türkçe.xlsx", 
        "YabancıDil.xlsx", "LGSTest.xlsx"
    ]
    
    for file in excel_files:
        if Path(file).exists():
            shutil.copy2(file, excel_dir)
            print(f"✓ Excel kopyalandı: {file}")
    
    # 3. Resim klasörlerini kopyala
    image_dirs = [
        "DinKültürü", "FenBilimleri", "İnkılapTarihi", "Matematik",
        "SosyalBilgiler", "Türkçe", "YabancıDil", "LGSTest"
    ]
    
    images_dir = archive_dir / "03_Question_Images"
    images_dir.mkdir(exist_ok=True)
    
    for img_dir in image_dirs:
        if Path(img_dir).exists():
            shutil.copytree(img_dir, images_dir / img_dir, dirs_exist_ok=True)
            print(f"✓ Resim klasörü kopyalandı: {img_dir}")
    
    # 4. PWA icon'larını kopyala
    icons_dir = archive_dir / "04_PWA_Icons"
    icons_dir.mkdir(exist_ok=True)
    
    icon_files = [f"icon-{size}x{size}.png" for size in [72, 96, 128, 144, 152, 192, 384, 512]]
    
    for icon in icon_files:
        if Path(icon).exists():
            shutil.copy2(icon, icons_dir)
            print(f"✓ Icon kopyalandı: {icon}")
    
    # 5. Proje dokümantasyonu oluştur
    docs_dir = archive_dir / "05_Documentation"
    docs_dir.mkdir(exist_ok=True)
    
    # README dosyası
    readme_content = f"""# LGS Test Projesi Arşivi
    
## Proje Bilgileri
- **Oluşturulma Tarihi**: {datetime.now().strftime("%d.%m.%Y %H:%M")}
- **Proje Adı**: LGS Hazırlık Test Programı
- **Versiyon**: 1.0
- **Teknolojiler**: HTML5, React, PWA, JavaScript

## Dosya Yapısı

### 01_Project_Files/
- `LGS_Test.html` - Ana geliştirme dosyası
- `LGS_Test_Standalone.html` - Dağıtım için hazır standalone versiyon
- `manifest.json` - PWA manifest dosyası
- `service-worker.js` - Offline çalışma için service worker
- `embedded_excel_data.js` - Excel verilerinin JavaScript formatı

### 02_Excel_Data/
- Tüm ders Excel dosyaları (DinKulturu.xlsx, Matematik.xlsx, vb.)
- Her ders için soru veritabanı

### 03_Question_Images/
- Ders klasörleri altında soru görüntüleri
- s01.jpg, s02.jpg formatında numaralandırılmış

### 04_PWA_Icons/
- Progressive Web App için çeşitli boyutlarda icon'lar
- Android ve iOS desteği için optimize edilmiş

### 05_Documentation/
- Bu README dosyası
- Geliştirme notları ve talimatlar

## Özellikler

### Test Türleri:
1. **Mini Test** - 10 soruluk hızlı test
2. **Kombo Rekor** - Sürekli doğru cevap rekoru
3. **LGS Test** - 135 dakikalık tam sınav simülasyonu

### PWA Özellikleri:
- Offline çalışma
- Ana ekrana yükleme
- Native app görünümü
- Otomatik güncelleme

### Kullanıcı Özellikleri:
- Çoklu kullanıcı desteği
- İstatistik takibi
- Test geçmişi
- Veri yedekleme/geri yükleme

## Kurulum ve Kullanım

### Geliştirme Ortamında:
1. VS Code ile LGS_Test.html'i açın
2. Live Server extension ile çalıştırın
3. http://127.0.0.1:5500/LGS_Test.html adresine gidin

### Dağıtım için:
1. LGS_Test_Standalone.html + resim klasörlerini web sunucusuna yükleyin
2. PWA olarak yüklenebilir ve offline çalışır

### Yeni Sorular Eklemek:
1. İlgili Excel dosyasına soruları ekleyin
2. Resim dosyalarını uygun klasöre ekleyin
3. `python convert_excel_to_js.py` çalıştırın
4. `python create_standalone.py` ile standalone güncelleyin

## Geliştirici Notları
- React componentleri Babel ile transpile ediliyor
- Tailwind CSS kullanılıyor
- Recharts ile grafik gösterimleri
- LocalStorage ile veri saklama
- Service Worker ile offline destek

Bu proje Claude Sonnet 4 AI asistanı ile birlikte geliştirilmiştir.
"""
    
    with open(docs_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    # Geliştirme notları
    dev_notes = {
        "development_timeline": {
            "phase_1": "Temel test sistemi ve UI",
            "phase_2": "Çoklu kullanıcı desteği",
            "phase_3": "İstatistik ve veri yönetimi", 
            "phase_4": "PWA dönüşümü ve mobile optimizasyon",
            "phase_5": "Timer sistemi ve advanced features"
        },
        "technical_decisions": {
            "frontend": "React with Babel (no build process)",
            "styling": "Tailwind CSS (CDN)",
            "data_storage": "LocalStorage + JSON backup system",
            "offline": "Service Worker + Cache API",
            "mobile": "PWA with manifest.json"
        },
        "future_enhancements": [
            "Backend database integration",
            "Real-time multiplayer tests",
            "AI-powered question analysis", 
            "Advanced statistics and analytics",
            "Teacher dashboard for monitoring"
        ]
    }
    
    with open(docs_dir / "development_notes.json", "w", encoding="utf-8") as f:
        json.dump(dev_notes, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Dokümantasyon oluşturuldu")
    
    # 6. ZIP arşivi oluştur
    zip_filename = f"{archive_name}.zip"
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(archive_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arc_name = os.path.relpath(file_path, archive_dir.parent)
                zipf.write(file_path, arc_name)
                
    print(f"\n🎉 Arşiv başarıyla oluşturuldu!")
    print(f"📦 ZIP Dosyası: {zip_filename}")
    print(f"📁 Klasör: {archive_name}/")
    
    # Arşiv klasörünü sil (ZIP yeterli)
    shutil.rmtree(archive_dir)
    
    # Dosya boyutunu göster
    size_mb = os.path.getsize(zip_filename) / (1024 * 1024)
    print(f"💾 Dosya Boyutu: {size_mb:.1f} MB")
    
    return zip_filename

if __name__ == "__main__":
    archive_file = create_project_archive()
    print(f"\n✅ Proje arşivleme tamamlandı: {archive_file}")