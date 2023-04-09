# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 01:48:09 2023

@author: Derya
"""

import pytesseract
import cv2
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
    ret, frame = cap.read()  # cap.isOpened() kullanarak kameranın açılıp açılmadığını kontrol et

    if not ret:
        print("The camera couldn't open!")
        break

    imgH, imgW, _ = frame.shape

    x1, y1, w1, h1 = 0, 0, imgH, imgW

    text = pytesseract.image_to_string(Image.fromarray(frame))

    print(text)

    cv2.putText(frame, text, (x1 + int(w1/50), y1 + int(h1/50)), font, 1.5, (0, 0, 0), 2)
    cv2.imshow("Image", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
