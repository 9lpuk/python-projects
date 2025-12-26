import cv2
import numpy as np
def imshow(img):             # img - cv2.imread('путь к файлу')
    if img is None:
        print('error')
    else:
        cv2.imshow('image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
#image =  cv2.imread('/home/yarik/Рабочий стол/Python/Git/img.jpeg')
