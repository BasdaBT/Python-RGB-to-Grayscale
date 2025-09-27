# Python-RGB-to-Grayscale
# OpenCV ile Görüntü İşleme Tutorial 🚀  

Bu proje, **OpenCV** kütüphanesini kullanarak bir resmi farklı formatlarda okuma, gri tonlamaya dönüştürme ve renk kanallarını değiştirme üzerine hazırlanmış basit bir örnektir.  

## 🛠️ Gereksinimler

Bu kodu çalıştırabilmek için aşağıdaki kütüphaneyi kurmanız gerekir:

```bash
-pip install opencv-python
 ```
 
## PYTHON KODU
 
```python
import cv2
import numpy as np

#1.Görseli doğrudan gri olarak oku
img = cv2.imread(r'C:\work_work\elektrik.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite(r'C:\work_work\elektrik2.jpeg', img) #Yeni gri görseli kaydet.
cv2.imshow("Gri Resim 1", img)                   #Ekranda göster.
cv2.waitKey(0)                                   #Klavyeden bir tuş gririşini bekle.
cv2.destroyAllWindows()                          #OpenCV ile açılmış tüm pencereleri kapat.

#2.Görseli renkli olrak oku
img_color = cv2.imread(r'C:\work_work\elektrik.jpeg', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY) #Renkli görseli griye dönüştür.
cv2.imwrite(r'C:\work_work\elektrik3.jpeg', img_gray)
cv2.imshow("Gri Resim 2", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#3.Gri resmi siyah beyaz yap
threshold = 127                                   #Eşik değeri belirt.
height,width = img_gray.shape                     #Görselin yükseklik ve genişlik değerlerini al.
img_bw = np.zeros((height,width), dtype=np.uint8) #Tüm pikselleri siyah olan bir görsel oluştur.
for y in range(height):                           #Eğer piksel eşik değerden yüksekse beyaz değilse siyah yap.
    for x in range(width):
        if img_gray[y][x] >= threshold:
            img_bw[y][x] = 255
        else:
            img_bw[y][x] = 0

cv2.imwrite(r'C:\work_work\elektrik5.jpeg', img_bw)
cv2.imshow("Siyah Beyaz Resim", img_bw)
cv2.waitKey(0)
cv2.destroyAllWindows()

#4.BGR formatındaki görseli RGB'ye çevir.
img_rgb = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
cv2.imwrite(r'C:\work_work\elektrik4.jpeg', img_rgb)
cv2.imshow("RGB Resim", img_rgb)
cv2.waitKey(0)
print("bitti")
cv2.destroyAllWindows()

```
## RESİMLER SIRASIYLA
![Kullanılan Görsel Örneği]("C:\work_work\elektrik.jpeg")
![Doğrudan Gri Okunmuş Görsel Örneği]("C:\work_work\elektrik2.jpeg")
![Griye Çevirilmiş Görsel Örneği]("C:\work_work\elektrik3.jpeg")
![Siyah-Beyaza Çevrilmiş Görsel Örneği]("C:\work_work\elektrik5.jpeg")
![BGR Formatındaki Resmin RGB'ye Çevirilmiş Örneği]("C:\work_work\elektrik4.jpeg")
