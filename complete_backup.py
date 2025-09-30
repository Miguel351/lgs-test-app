import subprocess
import sys
import os
from datetime import datetime

def create_complete_archive():
    """Hem proje hem chat özetini içeren komple arşiv"""
    
    print("🚀 LGS Test Projesi - Komple Arşivleme Başlıyor...")
    print("=" * 50)
    
    try:
        # 1. Proje arşivini oluştur
        print("\n1️⃣ Proje dosyaları arşivleniyor...")
        
        # archive_project.py dosyasını import et ve çalıştır
        if os.path.exists("archive_project.py"):
            from archive_project import create_project_archive
            project_archive = create_project_archive()
        else:
            print("❌ archive_project.py dosyası bulunamadı!")
            return
        
        # 2. Chat özetini oluştur
        print("\n2️⃣ Chat geçmişi özeti oluşturuluyor...")
        
        # chat_summary.py dosyasını import et ve çalıştır
        if os.path.exists("chat_summary.py"):
            from chat_summary import create_chat_summary
            chat_summary = create_chat_summary()
        else:
            print("❌ chat_summary.py dosyası bulunamadı!")
            return
        
        # 3. Komple arşiv bilgilerini göster
        print("\n3️⃣ Komple arşiv raporu oluşturuluyor...")
        
        # Dosya boyutlarını hesapla
        project_size = 0
        if os.path.exists(project_archive):
            project_size = os.path.getsize(project_archive) / (1024 * 1024)
        
        chat_size = 0
        if os.path.exists(chat_summary):
            chat_size = os.path.getsize(chat_summary) / 1024
        
        # Komple arşiv raporu oluştur
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = f"LGS_Test_Complete_Backup_Report_{timestamp}.txt"
        
        report_content = f"""
LGS Test Projesi - Komple Yedekleme Raporu
==========================================

Yedekleme Tarihi: {datetime.now().strftime("%d.%m.%Y %H:%M:%S")}
Oluşturan: complete_backup.py

OLUŞTURULAN DOSYALAR:
--------------------
📦 Proje Arşivi: {project_archive}
   └── Boyut: {project_size:.1f} MB
   └── İçerik: Tüm kod, Excel, resim, PWA dosyaları

📋 Chat Özeti: {chat_summary}
   └── Boyut: {chat_size:.1f} KB
   └── İçerik: Geliştirme süreci ve teknik detaylar

PROJE ÖZETİ:
-----------
🎯 Proje Adı: LGS Hazırlık Test Programı
🔧 Teknoloji: HTML5 + React + PWA
📱 Platform: Web (Desktop + Mobile)
👥 Kullanıcı: Çoklu kullanıcı sistemi

ÖNEMLİ ÖZELLIKLER:
-----------------
✅ 3 Test Türü (Mini, Kombo, LGS)
✅ PWA Desteği (Offline çalışma)
✅ Geri sayım sayacı (135 dakika LGS)
✅ İstatistik ve ilerleme takibi
✅ Veri yedekleme sistemi
✅ Mobil uyumlu responsive tasarım

KURULUM TALİMATLARI:
-------------------
1. Proje arşivini ({project_archive}) açın
2. LGS_Test_Standalone.html + resim klasörlerini web sunucusuna yükleyin
3. PWA olarak cihaza yüklenebilir
4. Offline çalışma desteği mevcuttur

GELIŞTIRME NOTLARI:
------------------
- Kod değişiklikleri için LGS_Test.html kullanın
- Yeni sorular için convert_excel_to_js.py çalıştırın
- Standalone versiyon için create_standalone.py kullanın
- PWA güncelleme için create_icons.py çalıştırın

Bu yedekleme Claude Sonnet 4 AI asistanı ile oluşturulmuştur.
Tüm geliştirme süreci chat geçmişinde detaylandırılmıştır.

GÜVENLİK ÖNERİLERİ:
------------------
🔒 Bu dosyaları güvenli konumda saklayın:
   - Cloud storage (Google Drive, Dropbox)
   - External hard drive
   - Network attached storage (NAS)

🔄 Düzenli yedekleme programı oluşturun:
   - Haftalık otomatik yedekleme
   - Önemli güncellemeler sonrası manuel yedekleme
   - 3-2-1 kuralı: 3 kopya, 2 farklı medya, 1 uzak lokasyon

Son Güncelleme: {datetime.now().strftime("%d.%m.%Y %H:%M")}
        """
        
        # Raporu kaydet
        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(report_content)
        
        print("\n" + "=" * 50)
        print("✅ KOMPLE ARŞİVLEME TAMAMLANDI!")
        print("=" * 50)
        
        print(f"\n📦 OLUŞTURULAN DOSYALAR:")
        print(f"   ├── 📁 {project_archive} ({project_size:.1f} MB)")
        print(f"   ├── 📄 {chat_summary} ({chat_size:.1f} KB)")
        print(f"   └── 📋 {report_filename}")
        
        print(f"\n💾 TOPLAM ARŞİV BOYUTU: {project_size + (chat_size/1024):.1f} MB")
        
        print(f"\n🔒 GÜVENLİK ÖNERİSİ:")
        print(f"   Bu dosyaları güvenli konumda yedekleyin:")
        print(f"   • Cloud storage (Google Drive, Dropbox)")
        print(f"   • External hard drive")
        print(f"   • Network storage")
        
        print(f"\n🚀 DAĞITIM İÇİN:")
        print(f"   {project_archive} dosyasını açıp LGS_Test_Standalone.html'i kullanın")
        
        return {
            'project_archive': project_archive,
            'chat_summary': chat_summary,
            'report': report_filename,
            'total_size_mb': project_size + (chat_size/1024)
        }
        
    except ImportError as e:
        print(f"❌ Import Hatası: {e}")
        print("📋 Gerekli dosyaların mevcut olduğundan emin olun:")
        print("   • archive_project.py")
        print("   • chat_summary.py")
        return None
        
    except Exception as e:
        print(f"❌ Beklenmeyen Hata: {e}")
        return None

def quick_backup():
    """Hızlı yedekleme - sadece temel dosyalar"""
    print("⚡ Hızlı yedekleme başlıyor...")
    
    import shutil
    from pathlib import Path
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    quick_dir = Path(f"Quick_Backup_{timestamp}")
    quick_dir.mkdir(exist_ok=True)
    
    # Temel dosyalar
    essential_files = [
        "LGS_Test.html",
        "LGS_Test_Standalone.html",
        "manifest.json", 
        "service-worker.js"
    ]
    
    for file in essential_files:
        if Path(file).exists():
            shutil.copy2(file, quick_dir)
            print(f"✓ {file}")
    
    print(f"⚡ Hızlı yedekleme tamamlandı: {quick_dir}/")
    return str(quick_dir)

if __name__ == "__main__":
    print("🎯 LGS Test Projesi Yedekleme Aracı")
    print("=" * 40)
    print("1. Komple yedekleme (önerilen)")
    print("2. Hızlı yedekleme (sadece temel dosyalar)")
    
    choice = input("\nSeçiminiz (1/2): ").strip()
    
    if choice == "1" or choice == "":
        result = create_complete_archive()
        if result:
            print(f"\n🎉 İşlem başarılı! Toplam {result['total_size_mb']:.1f} MB yedeklendi.")
        else:
            print("\n❌ Yedekleme işlemi başarısız!")
            
    elif choice == "2":
        backup_dir = quick_backup()
        print(f"\n⚡ Hızlı yedekleme tamamlandı: {backup_dir}")
        
    else:
        print("❌ Geçersiz seçim!")