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
img =  cv2.imread('/home/yarik/Рабочий стол/Python/Git/img.jpeg')
window_name = 'window1'
#кадрирование
cropped = img[0:150, 0:330]
print("Размеры (высота, ширина, каналы):", img.shape)
print("Высота:", img.shape[0])
print("Ширина:", img.shape[1])
print("Количество каналов:", img.shape[2] if len(img.shape) == 3 else 1)
imshow(cropped, "после кадрирования")
