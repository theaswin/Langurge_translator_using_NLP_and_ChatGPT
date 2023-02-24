import pytesseract
from pytesseract import Output
import cv2
import re

path = input("enter path")

img = cv2.imread(path)
# cv2.imshow('name',img)
# cv2.waitKey()
# cv2.destroyAllWindows()


datas = pytesseract.image_to_string(img)
pattern = '[a-zA-Z]+'
word = re.findall(pattern,datas)

# converting into array
out = " ".join(word)