"""from PIL import Image
img = Image.open("cordi.png")
w, h = img.size
color = (0, 255, 33, 255)
str2 = []
índice = []
for w2 in range(0, w):
    for h2 in range(0, h):
        if img.getpixel((w2, h2)) == color:
            índice += [w2, h2]
            if len(índice) >= 4:
                str2 += [índice]
                índice = []

for i in str2:
    print(f"Crop_Image(file, {i}),")"""
import threading
def main():
    import time
    print("ok")
    time.sleep(100)

threading.Thread(target=main)

print("ok2")
