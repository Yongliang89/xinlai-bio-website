# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw
import os

# 处理两张对比图片
images_dir = r'C:\Users\Administrator\.qclaw\workspace\company-website\images'

# 图片文件列表
images_to_process = [
    'pei-comparison-import.jpg',
    'pei-comparison-vdo.jpg'
]

for img_name in images_to_process:
    img_path = os.path.join(images_dir, img_name)
    
    if not os.path.exists(img_path):
        print(f"File not found: {img_name}")
        continue
    
    # 打开图片
    img = Image.open(img_path)
    width, height = img.size
    
    # 创建绘图对象
    draw = ImageDraw.Draw(img)
    
    # 在图片底部画一个白色矩形覆盖文字区域
    # 文字区域大约在图片底部 15-20% 的位置
    text_area_height = int(height * 0.18)  # 覆盖底部18%的区域
    
    # 画白色矩形覆盖文字
    draw.rectangle(
        [(0, height - text_area_height), (width, height)],
        fill=(255, 255, 255)  # 白色
    )
    
    # 保存处理后的图片
    img.save(img_path, quality=95)
    print(f"Processed: {img_name} ({width}x{height})")

print("Done! Text removed from images.")
