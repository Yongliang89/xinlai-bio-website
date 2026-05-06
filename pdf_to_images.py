# -*- coding: utf-8 -*-
import fitz
import os

pdf_path = r'C:\Users\Administrator\.qclaw\workspace\company-website\luminescence.pdf'
output_dir = r'C:\Users\Administrator\.qclaw\workspace\company-website\pdf_pages'

os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
print(f'Total pages: {len(doc)}')

for page_num in range(len(doc)):
    page = doc[page_num]
    # High resolution render
    mat = fitz.Matrix(3, 3)  # 3x zoom = high quality
    pix = page.get_pixmap(matrix=mat)
    
    output_path = os.path.join(output_dir, f'page_{page_num+1:02d}.png')
    pix.save(output_path)
    print(f'Saved: page_{page_num+1:02d}.png')

doc.close()
print('Done!')
