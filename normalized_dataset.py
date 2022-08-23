#class x_center y_center width height

from genericpath import exists
import os
import cv2
from matplotlib import pyplot as plt

WORKDIR='yolov7/dataset/test/labels/'
SIZE=(416,416)

dir = os.listdir(WORKDIR)

for file in dir:
    if file == 'normalized':
        continue
    f = open(WORKDIR+file)
    lines = f.readlines()
    im=cv2.imread('yolov7/dataset/test/images/'+file.split('.')[0]+'.JPG')
    h,w=(cv2.imread('obj-data/val/'+file.split('.')[0]+'.JPG')).shape[:2]
    new_lines=[]

    for line in lines:
        bbox=line.split(' ')[1:]
        bbox=[float(bbox[0]),float(bbox[1]),float(bbox[2]),float(bbox[3])]
        
        new_x=(float(bbox[0])*SIZE[0])/w
        new_y=(float(bbox[1])*SIZE[1])/h
        new_width=(float(bbox[2])*SIZE[0])/w
        new_height=(float(bbox[3])*SIZE[1])/h 

        center=new_x+new_width/2

        new_x=(new_x+new_width/2)/SIZE[0]
        new_y=(new_y+new_height/2)/SIZE[1]
        new_width=new_width/SIZE[0]
        new_height=new_height/SIZE[1]

        new_lines.append('0 ' + str(new_x) + ' ' + str(new_y) + ' ' + str(new_width) + ' ' + str(new_height))

    f = open(WORKDIR+'normalized/'+file, 'w+')

    for line in new_lines:
        f.write(line)
        f.write('\n')
    f.close()
