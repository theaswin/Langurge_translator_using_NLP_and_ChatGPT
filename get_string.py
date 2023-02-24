import pytesseract
from pytesseract import Output
import cv2
import re

path = '/home/user/Desktop/Langurge_translator/This world is so beautiful.png'

img = cv2.imread(path)
# cv2.imshow('name',img)
# cv2.waitKey()
# cv2.destroyAllWindows()

datas = pytesseract.image_to_string(img)
pattern = '[a-zA-Z]+'
word = re.findall(pattern,datas)

out = " ".join(word)

print("Please RUN the 'translator.py' file")