import pytesseract
from PIL import Image
import os
dirpath='/home/anandajith-s/amfoss-tasks-s2/task-02'
for i in os.listdir(dirpath):
    if i.endswith(".png"):
        imgpath=os.path.join(dirpath,i)
        img=Image.open(imgpath)
        text=pytesseract.image_to_string(img)
        print(f"Filename: {i}")
        print(f"{text.strip()}={eval(text)}")
        print()
        