# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw
import os

# 处理所有磁珠图片，去除底部文字
images_dir = r'C:\Users\Administrator\.qclaw\workspace\company-website\images'

# 获取所有magnetic开头的图片
magnetic_images = [f for f in os.listdir(images_dir) if f.startswith('magnetic-')]

print(f"Found {len(magnetic_images)} magnetic images")

for img_name in magnetic_images:
    img_path = os.path.join(images_dir, img_name)
    
    try:
        # 打开图片
        img = Image.open(img_path)
        width, height = img.size
        
        # 创建绘图对象
        draw = ImageDraw.Draw(img)
        
        # 在图片底部画一个白色矩形覆盖文字区域
        # 文字区域大约在图片底部 15-20% 的位置
        text_area_height = int(height * 0.15)  # 覆盖底部15%的区域
        
        # 画白色矩形覆盖文字
        draw.rectangle(
            [(0, height - text_area_height), (width, height)],
            fill=(255, 255, 255)  # 白色
        )
        
        # 保存处理后的图片
        img.save(img_path, quality=95)
        print(f"Processed: {img_name} ({width}x{height})")
    except Exception as e:
        print(f"Error processing {img_name}: {e}")

print("Done! Text removed from images.")
