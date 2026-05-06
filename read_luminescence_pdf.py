# -*- coding: utf-8 -*-
from pypdf import PdfReader

pdf_path = r'C:\Users\Administrator\xwechat_files\wxid_5nte6kyvyy5322_2045\temp\RWTemp\2026-04\fbb48d99aa8f0b585271fb06744c1286\202506-均相发光法 生命科学探索的卓越工具(1).pdf'

reader = PdfReader(pdf_path)
print(f'Total pages: {len(reader.pages)}')

with open(r'C:\Users\Administrator\.qclaw\workspace\company-website\luminescence-content.txt', 'w', encoding='utf-8') as out:
    for i, page in enumerate(reader.pages):
        out.write(f'\n=== Page {i+1} ===\n')
        text = page.extract_text()
        if text:
            out.write(text)
        out.write('\n')

print('Done! Content saved to luminescence-content.txt')