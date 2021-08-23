import cv2


# Функция для вывода изображения на экран
def viewImage(image, window_name='window name'):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Считываем и визуализируем изображения
cone = cv2.imread('2.png')
road = cv2.imread('1.png')
viewImage(road, 'road')
viewImage(cone, 'cone')

# Размеры изображения (высота, ширина, количество каналов)
print(cone.shape)

# Смотрим значение пикселя
print(cone[100, 24])

# Переключение между цветовыми пространствами
cone_hsv = cv2.cvtColor(cone, cv2.COLOR_BGR2HSV)
#viewImage(cone_hsv)

# Смена размера картинки
cone_res = cv2.resize(cone, (400, 400))
#viewImage(cone_res)

# Кадрирование (обрезка) изображения
cone_crop = cone[100:213, 32:89]
#viewImage(cone_crop)


# Поворот изображения
def rotate(image, degrees):
    h, w = image.shape[0], image.shape[1]
    center = (int(w / 2), int(h / 2))
    rotation_matrix = cv2.getRotationMatrix2D(center, degrees, 0.6)
    rotated = cv2.warpAffine(image, rotation_matrix, (w, h))
    return rotated


rot_cone = rotate(cone, 90)
#viewImage(rot_cone)

# Диагональная линия на изображении; окружность радиуса 50
cv2.line(cone, (0, 0), (cone.shape[1]-1, cone.shape[0]-1), (0, 0, 0))
h, w = cone.shape[0], cone.shape[1]
center = (int(w / 2), int(h / 2))
cv2.circle(cone, center, 30, (0, 255, 255), 10)
#viewImage(cone)

