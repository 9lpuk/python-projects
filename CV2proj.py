import cv2
import numpy as np
def imshow(img,window_name):             # img - cv2.imread('путь к файлу')
    if img is None:
        print('error')
    else:
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.imshow(window_name,img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
image =  cv2.imread('/home/yarik/Рабочий стол/Python/Git/img.jpeg')
window_name = 'window1'
imshow(image,window_name)