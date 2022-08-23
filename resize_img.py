import os
import cv2
WORKDIR='yolov7/dataset/valid/images/'
SIZE=((416,416))

dir = os.listdir(WORKDIR)

for name_img in dir:
    img=cv2.imread(WORKDIR+name_img)
    img_resize=cv2.resize(img, SIZE)
    cv2.imwrite(WORKDIR+name_img, img_resize)