#__author:"zfp"
#data:2019/6/22

import glob
import os
import cv2
from PIL import Image
import numpy as np


def get_img_path_list(img_dir, format='png'):
    return glob.glob(os.path.join(img_dir, '*.%s' % format))


def get_img_size(img_path):
    Image.MAX_IMAGE_PIXELS = 933120000
    img = Image.open(img_path)
    return img.size


def summery_imgs_size():
    img_dir = '/data/zfp/data/rssrai2019_object_detection/train/images'
    img_path_list = get_img_path_list(img_dir)
    print(len(img_path_list))
    img_sizes = []
    for img_path in img_path_list:
        img_sizes.append(get_img_size(img_path))
    img_sizes = np.array(img_sizes)
    print(img_sizes.max(axis=0))
    print(img_sizes.min(axis=0))

summery_imgs_size()