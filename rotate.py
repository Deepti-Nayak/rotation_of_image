import numpy as np
import argparse
import imutils
import cv2
import os



def saveFile(image):
    
	cv2.imwrite(r"C:\Users\ADMIN\Pictures\qq.png",image)
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,
#	help="C:\Users\ADMIN\Pictures\xxx.png")
ap.add_argument("-i","--image", required=True,
	help=r"C:\Users\ADMIN\Pictures\xxx.png")
args = vars(ap.parse_args())
# load the image from disk
image = cv2.imread(args["image"])
# loop over the rotation angles
#for angle in np.arange(0, 360, 15):
#	rotated = imutils.rotate(image, angle)
#	cv2.imshow("Rotated (Problematic)", rotated)
#	cv2.waitKey(0)
# loop over the rotation angles again, this time ensuring
# no part of the image is cut off
for angle in np.arange(0, 720, 5):
	rotated = imutils.rotate_bound(image, angle)
	cv2.imshow("Press s if you want go ahead with this rotated image", rotated)
	k = cv2.waitKey(0)
	if k == ord('s'):
		saveFile(rotated)
		break

