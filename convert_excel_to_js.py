#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Excel dosyalarını JavaScript veri formatına dönüştürür
"""
import pandas as pd
import json
import os
from pathlib import Path

def excel_to_js_data():
    # Excel dosyaları ve karşılık gelen isimler
    excel_files = {
        "DinKültürü": "DinKulturu.xlsx",
        "Fen Bilimleri": "FenBilimleri.xlsx", 
        "İnkılap Tarihi": "inkilapTarihi.xlsx",
        "Matematik": "Matematik.xlsx",
        "Sosyal Bilgiler": "SosyalBilgiler.xlsx",
        "Türkçe": "Türkçe.xlsx",
        "Yabancı Dil": "YabancıDil.xlsx",
        "LGSTest": "LGSTest.xlsx"
    }
    
    all_data = {}
    
    for subject_name, filename in excel_files.items():
        filepath = Path(filename)
        if filepath.exists():
            try:
                print(f"İşleniyor: {filename}")
                # Excel dosyasını oku
                df = pd.read_excel(filepath)
                
                # NaN değerleri boş string ile değiştir
                df = df.fillna("")
                
                # DataFrame'i dictionary listesine çevir
                data = df.to_dict('records')
                
                # Sütun isimlerini normalize et (Excel'deki gibi)
                normalized_data = []
                for row in data:
                    normalized_row = {}
                    for key, value in row.items():
                        # Boşlukları temizle ve standardize et
                        clean_key = str(key).strip()
                        normalized_row[clean_key] = str(value).strip() if value != "" else ""
                    normalized_data.append(normalized_row)
                
                all_data[subject_name] = normalized_data
                print(f"✓ {filename}: {len(normalized_data)} soru yüklendi")
                
            except Exception as e:
                print(f"❌ Hata - {filename}: {e}")
        else:
            print(f"⚠️  Dosya bulunamadı: {filename}")
    
    # JavaScript formatında dosya oluştur
    js_content = "// Excel verilerinden otomatik oluşturuldu\n"
    js_content += "const EMBEDDED_EXCEL_DATA = " + json.dumps(all_data, ensure_ascii=False, indent=2) + ";\n\n"
    js_content += "// Gömülü verileri kullanabilmek için global olarak erişilebilir yap\n"
    js_content += "window.EMBEDDED_EXCEL_DATA = EMBEDDED_EXCEL_DATA;\n"
    
    # JS dosyasını kaydet
    with open("embedded_excel_data.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    
    print(f"\n✅ JavaScript veri dosyası oluşturuldu: embedded_excel_data.js")
    print(f"📊 Toplam {len(all_data)} ders verisi hazır")
    
    # Özet bilgi
    for subject, data in all_data.items():
        print(f"   - {subject}: {len(data)} soru")

if __name__ == "__main__":
    excel_to_js_data()