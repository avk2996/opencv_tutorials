# Read an image from file (using cv2.imread(filepath))
# Display an image in an OpenCV window (using cv2.imshow('caption','filepath'))
# Write an image to a file (using cv2.imwrite('filepath',image_to_save))

import cv2 #Importing opencv
image = cv2.imread('image1.jpg') #loading images
print(image.shape) #printing image shape
cv2.imshow('image',image) # displaying image
# saving the loaded image into another file name. you will find in the path specified after you run the code.
cv2.imwrite('image1_resave.jpg',image)
cv2.waitKey(0) # waitime for displaying image. 0 means it exits when you click on X mark on pop-up window

