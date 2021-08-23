import cv2
import apriltag
from tag_dict import *
from traffic_signs import *
from linalg import *


def detect(img):
	gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	options = apriltag.DetectorOptions(families='tag36h11')
	detector = apriltag.Detector(options)
	results = detector.detect(gray_img)

	max_area = 0
	sign = None
	id = 0

	if results != []:
		for r in results:
			# extract the bounding box (x, y)-coordinates for the AprilTag
			# and convert each of the (x, y)-coordinate pairs to integers
			(ptA, ptB, ptC, ptD) = r.corners
			ptB = (int(ptB[0]), int(ptB[1]))
			ptC = (int(ptC[0]), int(ptC[1]))
			ptD = (int(ptD[0]), int(ptD[1]))
			ptA = (int(ptA[0]), int(ptA[1]))
			# draw the bounding box of the AprilTag detection
			cv2.line(img, ptA, ptB, (0, 255, 0), 2)
			cv2.line(img, ptB, ptC, (0, 255, 0), 2)
			cv2.line(img, ptC, ptD, (0, 255, 0), 2)
			cv2.line(img, ptD, ptA, (0, 255, 0), 2)
			# draw the center (x, y)-coordinates of the AprilTag
			(cX, cY) = (int(r.center[0]), int(r.center[1]))
			cv2.circle(img, (cX, cY), 5, (0, 0, 255), -1)
			# draw the tag id on the image
			tagID = str(r.tag_id)
			cv2.putText(img, tagID, (ptA[0], ptA[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
			#print("[INFO] tag ID: {}".format(tagID))
			sig = tag_dict[int(tagID)][1]
			#print("[INFO] sign: {}".format(sign.name))
			corners = [ptB, ptC, ptD, ptA]
			a = line_length(corners[3][0], corners[3][1], corners[0][0], corners[0][1])
			b = line_length(corners[0][0], corners[0][1], corners[1][0], corners[1][1])
			c = line_length(corners[1][0], corners[1][1], corners[2][0], corners[2][1])
			d = line_length(corners[2][0], corners[2][1], corners[3][0], corners[3][1])
			e = line_length(corners[2][0], corners[2][1], corners[0][0], corners[0][1])
			sign_area = triangle_area(a, e, d) + triangle_area(e, b, c)
			if sign_area > max_area:
				max_area = sign_area
				sign = sig
				id = tagID
		return sign, max_area, id
	else:
		return '', 0, ''
