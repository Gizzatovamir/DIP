import cv2
import numpy as np
import argparse
path = '../test.png'

def rotate(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result

def scale(image,k):
    height, width = image.shape[:2]
    result = cv2.resize(image, (int(width/k), int(k * height)), interpolation=cv2.INTER_CUBIC)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default=path, action='store', help='path to the aimge')
    parser.add_argument('-angle', default=45, action='store', type=int, help='angle to rotate')
    parser.add_argument('-k', default=0.5, action='store', type=float, help='k to scale')
    args = parser.parse_args()
    image = cv2.imread(args.path, 2)
    if args.k <= 1 and args.k > 0:
        cv2.imshow('lab1', image)
        rotated_img = rotate(image, args.angle)
        cv2.imshow('rotated', rotated_img)
        scaled_image = scale(rotated_img,args.k)
        cv2.imshow('scaled', scaled_image)
        cv2.imwrite('result.bmp', scaled_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print('k is out of range')