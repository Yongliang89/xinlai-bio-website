# -*- coding: utf-8 -*-
import fitz
import os

pdf_path = r'C:\Users\Administrator\xwechat_files\wxid_5nte6kyvyy5322_2045\temp\RWTemp\2026-04\fbb48d99aa8f0b585271fb06744c1286\202506-均相发光法 生命科学探索的卓越工具(1).pdf'
output_dir = r'C:\Users\Administrator\.qclaw\workspace\company-website\images'

doc = fitz.open(pdf_path)

for page_num in range(len(doc)):
    page = doc[page_num]
    image_list = page.get_images(full=True)
    
    print(f'Page {page_num + 1}: Found {len(image_list)} images')
    
    for img_idx, img in enumerate(image_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image['image']
        image_ext = base_image['ext']
        
        image_filename = f'luminescence-page{page_num+1}-img{img_idx+1}.{image_ext}'
        image_path = os.path.join(output_dir, image_filename)
        
        with open(image_path, 'wb') as f:
            f.write(image_bytes)
        
        print(f'  Saved: {image_filename} ({len(image_bytes)} bytes)')

doc.close()
print('\nDone!')