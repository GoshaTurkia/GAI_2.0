import cv2
import numpy as np


# Функция для вывода изображения на экран
def viewImage(image, window_name='window name'):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Считываем и визуализируем изображения
cone = cv2.imread('2.png')
road = cv2.imread('1.png')
viewImage(cone, 'cone')
viewImage(road, 'road')

# Переводим их в оттенки серого
gray_cone = cv2.cvtColor(cone, cv2.COLOR_BGR2GRAY)
gray_road = cv2.cvtColor(road, cv2.COLOR_BGR2GRAY)
viewImage(gray_road)

# Бинаризуем изображение конуса
ret, threshold_cone = cv2.threshold(gray_cone, 150, 255, cv2.THRESH_BINARY)
viewImage(threshold_cone)

# Бинаризуем изображение дороги
road_edges = cv2.Canny(gray_road, 125, 200)
viewImage(road_edges)

# Ищем конус на первоначальной картинке
cone_hsv = cv2.cvtColor(cone, cv2.COLOR_BGR2HSV)
lower_or = np.array([8, 100, 100])
upper_or = np.array([17, 255, 255])
mask = cv2.inRange(cone_hsv, lower_or, upper_or)
res = cv2.bitwise_and(cone_hsv, cone_hsv, mask=mask)
viewImage(mask)
#viewImage(res)

# Контуры
contours, h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(cone, contours, 2, (255, 0, 0), 5)
viewImage(cone)

contours, h = cv2.findContours(road_edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
# контуры с индексами 14, 16 - внутренние края полосы
cv2.drawContours(road, contours, -1, (255, 0, 0), 5)
viewImage(road)
