import cv2
from matplotlib import pyplot as plt


def paint_bbox(file, im):
    f=open(file)
    lines=f.readlines()

    for line in lines:
        bbox=line.split(' ')[1:]
        bbox=[int(float(bbox[0])),int(float(bbox[1])),int(float(bbox[2])),int(float(bbox[3]))]
        print(bbox)

        cv2.circle(im, (bbox[0], bbox[1]), 10, (255,0,0))
        cv2.circle(im, (bbox[0]+int(bbox[2]/2), bbox[1]+int(bbox[3]/2)), 10, (255,255,0))

        cv2.rectangle(im,(bbox[0], bbox[1]), (bbox[2]+bbox[0], bbox[3]+bbox[1]), color=(255,0,0))
        plt.imshow(im)
        plt.show()

if __name__ == '__main__':
    label='obj-data/train/100_0001_0001.txt'
    img=cv2.imread('obj-data/train/100_0001_0001.JPG')
    paint_bbox(label, img)