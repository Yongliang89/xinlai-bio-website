# -*- coding: utf-8 -*-
import os
import sys

# Try PyMuPDF first
try:
    import fitz
    USE_FITZ = True
except ImportError:
    USE_FITZ = False
    print("PyMuPDF not available, trying alternative method...")

pdf_path = r'C:\Users\Administrator\xwechat_files\wxid_5nte6kyvyy5322_2045\temp\RWTemp\2026-04\fbb48d99aa8f0b585271fb06744c1286\聚乙烯亚胺（PEI）转染试剂.pdf'
output_dir = r'C:\Users\Administrator\.qclaw\workspace\company-website\images'

if USE_FITZ:
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
            
            # Save image
            image_filename = f'pei-page{page_num+1}-img{img_idx+1}.{image_ext}'
            image_path = os.path.join(output_dir, image_filename)
            
            with open(image_path, 'wb') as f:
                f.write(image_bytes)
            
            print(f'  Saved: {image_filename} ({len(image_bytes)} bytes)')
    
    doc.close()
    print('Done!')
else:
    # Alternative: use pdfimages command if available
    import subprocess
    try:
        result = subprocess.run(['pdfimages', '-list', pdf_path], capture_output=True, text=True)
        print("pdfimages output:")
        print(result.stdout)
        
        # Extract images
        subprocess.run(['pdfimages', '-j', pdf_path, os.path.join(output_dir, 'pei')], check=True)
        print("Images extracted using pdfimages")
    except Exception as e:
        print(f"pdfimages not available: {e}")
        print("Please install PyMuPDF: pip install PyMuPDF")
