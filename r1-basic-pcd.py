'''
    Program : Review Pengolahan Citra Digital
    About   : Refreshing PCD, manipulasi os library
    Tanggal : 09 April 2025
'''

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

# Alamat direktori simpan gambar
directory_store = r"D:\Kuliah\SEMESTER 6\computer-vision\refreshing-image-processing\result"

# Input image
path_img = r"D:\Kuliah\SEMESTER 6\computer-vision\refreshing-image-processing\images\bangun-3d.png"

img = cv.imread(path_img, cv.IMREAD_COLOR) # Baca gambar berwarna
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # Konversi ke grayscale
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB) # Konversi ke RGB

# Showing images
plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title("BGR Image")

plt.subplot(1, 3, 2)
plt.imshow(img_gray, cmap='gray')
plt.title("Grayscale Image")

plt.subplot(1, 3, 3)
plt.imshow(img_rgb)
plt.title("RGB Image")
plt.show()

# Simpan gambar pakai library os
os.chdir(directory_store) # Pindah ke direktori simpan gambar

print(
    f'''
      STATUS OPERASI SIMPAN GAMBAR
      -------------------------------------
      Before save image:
      {os.listdir(directory_store)}
      '''
    )

