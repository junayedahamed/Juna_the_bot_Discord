from tkinter import Image

import requests
import pytesseract
from PIL import Image
import io
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\AC\AppData\Local\Tesseract-OCR\tesseract'


def imgtotxt(file):
    if file=='':
        return "No file attached"
    result=requests.get(file)
    img=Image.open(io.BytesIO(result.content))
    istr = str(pytesseract.image_to_string(img))
    if istr == "":
        return  "it's a blank document"
    else:
        return istr