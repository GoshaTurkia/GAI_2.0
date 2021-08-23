import cv2


def warning(warning_text: str):
    warning_img = cv2.imread('img.jpeg')
    warning_img = cv2.resize(warning_img, (500, 100))
    cv2.putText(warning_img, warning_text, (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (37, 37, 247), 2)
    cv2.imshow('Warning Window', warning_img)
    cv2.waitKey(1)
