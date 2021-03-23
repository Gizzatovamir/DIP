import numpy as np
import cv2
import argparse

path = '111.png'


def image_read(path):
    img = cv2.imread(path, 0)
    blur_img = cv2.medianBlur(img, 5)
    gray_img = cv2.cvtColor(blur_img, cv2.COLOR_GRAY2BGR)
    return img.copy(),gray_img


def draw_circles(image, circles):
    circles = np.int64(circles)
    for i in circles[0, :]:
        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)
    return image

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default='111.png',action='store',help='path to the aimge')
    parser.add_argument('-dist',default=10,action='store',type=int ,help='min dist for circles')
    parser.add_argument('-min', default=10,action='store',type=int,
                        help='min radius')
    parser.add_argument('-max', default=1000,action='store',type=int,
                        help='max radius')
    args = parser.parse_args()
    img,gray_img = image_read(args.path)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, args.dist, param1=50, param2=30, minRadius=args.min, maxRadius=args.max)
    try:
        draw_circles(img,circles)
        cv2.imshow('detected circles', img)
        cv2.imwrite('result.bmp', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except TypeError:
        print("there are no circles found on this image")
    cv2.waitKey(0)
    cv2.destroyAllWindows()