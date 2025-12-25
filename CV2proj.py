import cv2
import numpy as np
def imshow(img):# img - cv2.imread('путь к файлу')
    if img is None:
        print('error')
    else:
        cv2.imshow('image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

blue_img = np.zeros((300, 300, 3), dtype=np.uint8)
blue_img[:, :] = (255, 255, 0)
imshow(blue_img)