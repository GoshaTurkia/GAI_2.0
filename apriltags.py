import cv2
import apriltag


# Функция для вывода изображения на экран
def viewImage(image, window_name='window name'):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Считываем изображение и преобразуем его в grayscale
tag = cv2.imread('/home/administrator/PycharmProjects/trial/signs/t9.png')
gray_tag = cv2.cvtColor(tag, cv2.COLOR_BGR2GRAY)
viewImage(gray_tag)

# Определяем семейство apriltags, затем настраиваем детектор и распознаем apriltag на картинке
options = apriltag.DetectorOptions(families='tag36h11')
detector = apriltag.Detector(options)
results = detector.detect(gray_tag)
print("[INFO] {} total AprilTags detected".format(len(results)))
print(results)

for r in results:
    # extract the bounding box (x, y)-coordinates for the AprilTag
    # and convert each of the (x, y)-coordinate pairs to integers
    (ptA, ptB, ptC, ptD) = r.corners
    ptB = (int(ptB[0]), int(ptB[1]))
    ptC = (int(ptC[0]), int(ptC[1]))
    ptD = (int(ptD[0]), int(ptD[1]))
    ptA = (int(ptA[0]), int(ptA[1]))
    # draw the bounding box of the AprilTag detection
    cv2.line(tag, ptA, ptB, (0, 255, 0), 2)
    cv2.line(tag, ptB, ptC, (0, 255, 0), 2)
    cv2.line(tag, ptC, ptD, (0, 255, 0), 2)
    cv2.line(tag, ptD, ptA, (0, 255, 0), 2)
    # draw the center (x, y)-coordinates of the AprilTag
    (cX, cY) = (int(r.center[0]), int(r.center[1]))
    cv2.circle(tag, (cX, cY), 5, (0, 0, 255), -1)
    # draw the tag family on the image
    tagID = str(r.tag_id)
    cv2.putText(tag, tagID, (ptA[0], ptA[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    print("[INFO] tag ID: {}".format(tagID))
viewImage(tag)
