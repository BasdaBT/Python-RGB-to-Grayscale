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

# 1. Görseli doğrudan gri olarak oku
img = cv2.imread(r'C:\work_work\elektrik.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite(r'C:\work_work\elektrik2.jpeg', img)  # Yeni gri görseli kaydet
cv2.imshow("Gri Resim 1", img)                    # Ekranda göster
cv2.waitKey(0)                                    # Klavyeden bir tuş girişini bekler  
cv2.destroyAllWindows()                           # OpenCV ile açılmış tüm pencereli kapatır

# 2. Görseli renkli olarak oku
img_color = cv2.imread(r'C:\work_work\elektrik.jpeg', cv2.IMREAD_COLOR)

# Renkli görseli griye dönüştür
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
cv2.imwrite(r'C:\work_work\elektrik3.jpeg', img_gray)
cv2.imshow("Gri Resim 2", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. BGR formatındaki görseli RGB’ye çevir
img_rgb = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
cv2.imwrite(r'C:\work_work\elektrik4.jpeg', img_rgb)
cv2.imshow("RGB Resim", img_rgb)
cv2.waitKey(0)
print("bitti")  # Konsola bilgi verir
cv2.destroyAllWindows()
