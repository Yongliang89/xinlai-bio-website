# -*- coding: utf-8 -*-
import fitz
import pytesseract
from PIL import Image
import io
import os

pdf_path = r'C:\Users\Administrator\xwechat_files\wxid_5nte6kyvyy5322_2045\temp\RWTemp\2026-04\fbb48d99aa8f0b585271fb06744c1286\202506-均相发光法 生命科学探索的卓越工具(1).pdf'
output_dir = r'C:\Users\Administrator\.qclaw\workspace\company-website\images'

doc = fitz.open(pdf_path)

output_text = []

for page_num in range(len(doc)):
    page = doc[page_num]
    
    # Convert page to image
    mat = fitz.Matrix(2, 2)  # 2x zoom for better OCR
    pix = page.get_pixmap(matrix=mat)
    img_data = pix.tobytes("png")
    
    img = Image.open(io.BytesIO(img_data))
    
    # OCR
    text = pytesseract.image_to_string(img, lang='chi_sim+eng')
    
    output_text.append(f'\n=== Page {page_num+1} ===\n{text}\n')
    
    print(f'OCR Page {page_num+1} done')

doc.close()

with open(r'C:\Users\Administrator\.qclaw\workspace\company-website\luminescence-content.txt', 'w', encoding='utf-8') as f:
    f.write(''.join(output_text))

print('\nDone! Content saved to luminescence-content.txt')