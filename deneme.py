import cv2
import numpy as np

import imgback

img = cv2.imread(r'C:\work_work\elektrik.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite(r'C:\work_work\elektrik2.jpeg', img)
cv2.imshow("Gri Resim 1", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


img_color = cv2.imread(r'C:\work_work\elektrik.jpeg', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
cv2.imwrite(r'C:\work_work\elektrik3.jpeg', img_gray)
cv2.imshow("Gri Resim 2", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

threshold = 127
height,width = img_gray.shape
img_bw = np.zeros((height,width), dtype=np.uint8)
for y in range(height):
    for x in range(width):
        if img_gray[y][x] >= threshold:
            img_bw[y][x] = 255
        else:
            img_bw[y][x] = 0

cv2.imwrite(r'C:\work_work\elektrik5.jpeg', img_bw)
cv2.imshow("Siyah Beyaz Resim", img_bw)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_rgb = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
cv2.imwrite(r'C:\work_work\elektrik4.jpeg', img_rgb)
cv2.imshow("RGB Resim", img_rgb)
cv2.waitKey(0)
print("bitti")
cv2.destroyAllWindows()
