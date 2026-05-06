# -*- coding: utf-8 -*-
from pypdf import PdfReader
import sys

pdf_path = r'C:\Users\Administrator\xwechat_files\wxid_5nte6kyvyy5322_2045\temp\RWTemp\2026-04\fbb48d99aa8f0b585271fb06744c1286\20250605细胞分选与激活磁珠-宣传手册.pdf'

reader = PdfReader(pdf_path)
print(f'Total pages: {len(reader.pages)}')

with open(r'C:\Users\Administrator\.qclaw\workspace\company-website\cell-selection-content.txt', 'w', encoding='utf-8') as out:
    for i, page in enumerate(reader.pages):
        out.write(f'\n=== Page {i+1} ===\n')
        text = page.extract_text()
        if text:
            out.write(text)
        out.write('\n')

print('Done! Content saved to cell-selection-content.txt')