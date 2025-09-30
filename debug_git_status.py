import subprocess
import os
from pathlib import Path

def debug_git_status():
    """Git durumunu detaylı kontrol et"""
    
    print("🔍 Git Durum Analizi")
    print("=" * 40)
    
    # 1. Git kurulu mu?
    try:
        result = subprocess.run(['git', '--version'], 
                              capture_output=True, text=True)
        print(f"✅ Git Versiyonu: {result.stdout.strip()}")
    except FileNotFoundError:
        print("❌ Git kurulu değil!")
        return
    
    # 2. Git repository var mı?
    if not Path('.git').exists():
        print("❌ Bu klasör bir git repository değil!")
        print("💡 Çözüm: git init çalıştırın")
        return
    
    # 3. Git status
    try:
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True)
        if result.stdout.strip():
            print("📝 Commit edilmemiş değişiklikler:")
            print(result.stdout)
        else:
            print("✅ Working tree temiz")
    except Exception as e:
        print(f"❌ Git status hatası: {e}")
    
    # 4. Remote kontrolü
    try:
        result = subprocess.run(['git', 'remote', '-v'], 
                              capture_output=True, text=True)
        if result.stdout.strip():
            print("🔗 Remote repository:")
            print(result.stdout)
        else:
            print("❌ Remote repository tanımlanmamış!")
    except Exception as e:
        print(f"❌ Remote kontrol hatası: {e}")
    
    # 5. Son commit'ler
    try:
        result = subprocess.run(['git', 'log', '--oneline', '-3'], 
                              capture_output=True, text=True)
        if result.stdout.strip():
            print("📜 Son commit'ler:")
            print(result.stdout)
        else:
            print("❌ Henüz commit yapılmamış!")
    except Exception as e:
        print(f"❌ Log kontrol hatası: {e}")
    
    # 6. Dosya sayısı
    files = list(Path('.').glob('*'))
    print(f"📁 Klasörde {len(files)} dosya/klasör var")
    
    # 7. Önemli dosyalar var mı?
    important_files = ['LGS_Test.html', 'manifest.json', 'service-worker.js']
    for file in important_files:
        if Path(file).exists():
            print(f"✅ {file} mevcut")
        else:
            print(f"❌ {file} bulunamadı!")

if __name__ == "__main__":
    debug_git_status()