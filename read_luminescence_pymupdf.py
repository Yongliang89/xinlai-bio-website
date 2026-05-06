# -*- coding: utf-8 -*-
import fitz

pdf_path = r'C:\Users\Administrator\xwechat_files\wxid_5nte6kyvyy5322_2045\temp\RWTemp\2026-04\fbb48d99aa8f0b585271fb06744c1286\202506-均相发光法 生命科学探索的卓越工具(1).pdf'

doc = fitz.open(pdf_path)
print(f'Total pages: {len(doc)}')

with open(r'C:\Users\Administrator\.qclaw\workspace\company-website\luminescence-content.txt', 'w', encoding='utf-8') as out:
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        
        out.write(f'\n=== Page {page_num+1} ===\n')
        if text:
            out.write(text)
        out.write('\n')

doc.close()
print('Done! Content saved to luminescence-content.txt')