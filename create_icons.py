from PIL import Image, ImageDraw, ImageFont
import os

def create_lgs_icon():
    """LGS Test için özel icon oluştur"""
    
    # Icon boyutları
    sizes = [72, 96, 128, 144, 152, 192, 384, 512]
    
    for size in sizes:
        # Yeni image oluştur
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Gradient background
        for i in range(size):
            # Blue to purple gradient
            r = int(59 + (123 - 59) * (i / size))  # 59 -> 123
            g = int(130 + (104 - 130) * (i / size))  # 130 -> 104  
            b = int(246 + (238 - 246) * (i / size))  # 246 -> 238
            draw.line([(0, i), (size, i)], fill=(r, g, b, 255))
        
        # Kenar yuvarlatma
        mask = Image.new('L', (size, size), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.rounded_rectangle([0, 0, size, size], radius=size//8, fill=255)
        
        # Mask uygula
        img.putalpha(mask)
        
        # Graduation cap icon çiz
        center_x, center_y = size // 2, size // 2
        icon_size = size // 3
        
        # Cap base (rectangle)
        cap_top = center_y - icon_size // 3
        cap_bottom = center_y + icon_size // 6
        cap_left = center_x - icon_size // 2
        cap_right = center_x + icon_size // 2
        
        draw.rectangle([cap_left, cap_top, cap_right, cap_bottom], 
                      fill='white', outline='white', width=2)
        
        # Cap top (diamond shape)
        diamond_points = [
            (center_x, cap_top - icon_size // 4),  # top
            (cap_right + icon_size // 4, cap_top),  # right
            (center_x, cap_top + icon_size // 6),   # bottom
            (cap_left - icon_size // 4, cap_top)    # left
        ]
        draw.polygon(diamond_points, fill='white', outline='white')
        
        # Tassel
        tassel_x = cap_right + icon_size // 6
        tassel_y = cap_top + icon_size // 4
        draw.line([tassel_x, tassel_y, tassel_x, tassel_y + icon_size // 3], 
                 fill='white', width=max(1, size // 64))
        draw.ellipse([tassel_x - 2, tassel_y + icon_size // 3 - 2, 
                     tassel_x + 2, tassel_y + icon_size // 3 + 2], 
                    fill='white')
        
        # LGS text (sadece büyük iconlarda)
        if size >= 192:
            try:
                # Font yükle (sistem fontunu kullan)
                font_size = max(size // 12, 8)
                font = ImageFont.load_default()  # Basit font kullan
                
                text = "LGS"
                text_width = draw.textlength(text, font=font)
                text_x = center_x - text_width // 2
                text_y = center_y + icon_size // 2
                
                # Text shadow
                draw.text((text_x + 1, text_y + 1), text, fill=(0, 0, 0, 128), font=font)
                # Main text
                draw.text((text_x, text_y), text, fill='white', font=font)
                
            except Exception as e:
                print(f"Font yükleme hatası (normal): {e}")
        
        # Icon'u kaydet
        filename = f'icon-{size}x{size}.png'
        img.save(filename, 'PNG', optimize=True)
        print(f'✅ {filename} oluşturuldu')

if __name__ == '__main__':
    create_lgs_icon()
    print('\n🎉 Tüm PWA iconları başarıyla oluşturuldu!')
    print('\nKullanım:')
    print('1. python create_icons.py')
    print('2. Oluşan icon dosyalarını LGS Test klasörüne taşıyın')
    print('3. Web sunucunuz ile test edin')