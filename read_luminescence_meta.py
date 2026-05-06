# -*- coding: utf-8 -*-
from pypdf import PdfReader

pdf_path = r'C:\Users\Administrator\xwechat_files\wxid_5nte6kyvyy5322_2045\temp\RWTemp\2026-04\fbb48d99aa8f0b585271fb06744c1286\202506-均相发光法 生命科学探索的卓越工具(1).pdf'

reader = PdfReader(pdf_path)

print(f'Total pages: {len(reader.pages)}')
print(f'Metadata: {reader.metadata}')

# Get page info
for i, page in enumerate(reader.pages):
    print(f'\nPage {i+1}:')
    print(f'  Size: {page.mediabox}')
    
# Try to extract any embedded text
print('\n\nAttempting text extraction...')
for i, page in enumerate(reader.pages[:5]):  # First 5 pages
    text = page.extract_text()
    if text and text.strip():
        print(f'\nPage {i+1} text:')
        print(text[:500])