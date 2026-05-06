# -*- coding: utf-8 -*-
try:
    from pdf2image import convert_from_path
    print("pdf2image is available")
except ImportError:
    print("pdf2image not installed")
    
try:
    import pytesseract
    print("pytesseract is available")
except ImportError:
    print("pytesseract not installed")

try:
    import tesseract
    print("tesseract OCR available")
except:
    print("tesseract OCR not available")
