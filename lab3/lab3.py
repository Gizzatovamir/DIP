import numpy as np
import cv2
import argparse
path = '../123.png'


def image_read(path):
    img = cv2.imread(path, 0)
    return img.copy()


def clastr(img,K):
    Z = img.reshape((-1, 3))
    Z = np.float32(Z)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    return res2

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default=path, action='store', help='path to the aimge')
    parser.add_argument('-k', default=1, action='store',type=int, help='k for k_means')
    args = parser.parse_args()
    try:
        img = cv2.imread(args.path)
        result = clastr(img,args.k)
        cv2.imshow('res2',result)
        cv2.imwrite('result.bmp', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception:
        print("something went wrong")