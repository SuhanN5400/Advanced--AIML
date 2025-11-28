import cv2
import numpy as np
import matplotlib.pyplot as plt
img_color = cv2.imread(r'C:\Users\HP\OneDrive\Desktop\Image Processing Programs\darthvader.jpg')
img = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)  # Convert color image for correct display in matplotlib
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
if img_color is None:
    print("Image not found or path is incorrect")
    exit()
kernel = np.ones((3, 3), np.uint8)
eroded = cv2.erode(img_gray, kernel, iterations=1)
edge_by_erosion = cv2.subtract(img_gray, eroded)
dilated = cv2.dilate(img_gray, kernel, iterations=1)
edge_by_dilation = cv2.subtract(dilated, img_gray)
titles = ['Original Image (Color)', 'Eroded', 'Edge by Erosion', 'Dilated', 'Edge by Dilation']
images = [img, eroded, edge_by_erosion, dilated, edge_by_dilation]
cmaps = [None, 'gray', 'gray', 'gray', 'gray']
plt.figure(figsize=(15, 8))
for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap=cmaps[i])
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
