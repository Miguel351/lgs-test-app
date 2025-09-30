#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Standalone LGS Test HTML dosyası oluşturur
"""
import json
from pathlib import Path

def create_standalone_version():
    # Ana HTML dosyasını oku
    html_file = Path("LGS_Test.html")
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Embedded data dosyasını oku
    js_file = Path("embedded_excel_data.js")
    with open(js_file, 'r', encoding='utf-8') as f:
        js_content = f.read()
    
    # External script tag'ini embedded data ile değiştir
    external_script = '<script src="embedded_excel_data.js"></script>'
    inline_script = f'<script>\n{js_content}\n    </script>'
    
    standalone_content = html_content.replace(external_script, inline_script)
    
    # Standalone versiyonu kaydet
    standalone_file = Path("LGS_Test_Standalone.html")
    with open(standalone_file, 'w', encoding='utf-8') as f:
        f.write(standalone_content)
    
    print(f"✅ Standalone versiyon oluşturuldu: {standalone_file}")
    print("📱 Bu dosyayı herhangi bir bilgisayara kopyalayıp çift tıklayarak açabilirsiniz!")
    print("🚀 İnternet bağlantısı olmasa bile çalışır (CDN dışında)")

if __name__ == "__main__":
    create_standalone_version()