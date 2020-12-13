import glob2 as glob
import numpy as np
import cv2
import json
from matplotlib import pyplot as plt
import os

label_list = np.array([[0, 0, 0], [0, 0, 255], [0, 255, 0], [
                      255, 0, 0], [255, 255, 0], [255, 0, 255], [0, 255, 255]])
label_keys = np.array(["_background_", "PCB",
                       "condenser", "copper", "other metals", "plastic", "wire"])


def generate_paths(dir_original, dir_segmented):
    paths_original = glob.glob(dir_original + "/*")
    paths_segmented = glob.glob(dir_segmented + "/*")

    return paths_original, paths_segmented


def color_to_label(img, num):
    label = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)		# imgと同サイズの配列を作成
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # print(i, j)
            for k in range(num):
                if np.all(img[i][j] == label_list[k]) == True:
                    label[i][j] = k
    return label


def one_hot(img, num):
    identity = np.identity(num, dtype=np.uint8)
    # print(img, identity)
    one_hot = identity[img]

    return one_hot


def image_generator(file_paths, init_size=None, normalization=True, gray=False, json=False):
    for file_path in file_paths:
        file_name_sp = file_path.split("/")
        file_name = file_name_sp[len(file_name_sp) - 1].split(".JPG")[0]
        if is_there_data(file_name):
            if gray:
                image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            else:
                image = cv2.imread(file_path)
            if init_size is not None and init_size != image.size:
                image = cv2.resize(image, init_size)
            if normalization:
                image = image / 255.0
            if json:
                image = file_name

            yield image

def is_there_data(file_name):
    return os.path.exists("data/json/" + file_name + ".json") & os.path.exists("data/image/" + file_name + ".JPG")


def extract_images(paths_original, paths_segmented, init_size):
    images_original, images_segmented = np.empty(None), np.empty(None)

    print("Loading original images", end="", flush=True)

    num = 0
    for image in image_generator(paths_original, init_size):
        num += 1
        images_original = np.append(images_original, image)

        if num % 1 == 0:
            print(".", end="", flush=True)
    # print(num)

    images_original = np.delete(images_original, [0])

    print(" Completed", flush=True)
    print("Loading segmented images", end="", flush=True)

    sum = 0
    for file_name in image_generator(paths_original, init_size, json=True):
        raw_json = open("data/json/" + file_name + ".json")
        print(file_name)
        image = cv2.imread("data/image/" + file_name + ".JPG")
        data = json.load(raw_json)
        for shape in data["shapes"]:
            label = shape["label"]
            print(label)
            idx = np.where(label_keys == label)
            color = label_list[idx]
            contour = np.array(shape["points"], np.int32)
            contour = np.reshape(contour, (len(shape["points"]), 1, 2))
            scolor = (int(color[0][0]), int(color[0][1]), int(color[0][2]))
            image = cv2.drawContours(image, [contour], -1, scolor, -1)
        image[image != 255] = 0
        image = cv2.resize(image, (224, 224))
        cv2.imwrite("data/segmented/" + file_name + ".JPG", image)
        image = color_to_label(image, 7)
        image = one_hot(image, 7)
        sum += 1
        images_segmented = np.append(images_segmented, image)

        if sum % 1 == 0:
            print(".", end="", flush=True)
    print(" Completed")

    images_segmented = np.delete(images_segmented, [0])

    images_original = np.asarray(images_original, dtype=np.float16)
    images_segmented = np.asarray(images_segmented, dtype=np.uint8)

    images_original = np.reshape(
        images_original, (num, init_size[0], init_size[1], 3))
    images_segmented = np.reshape(
        images_segmented, (sum, init_size[0], init_size[1], 7))

    print(images_original.size)
    print(images_segmented.size)

    return images_original, images_segmented


def import_data(dir_original, dir_segmented, init_size=None):
    paths_original, paths_segmented = generate_paths(
        dir_original, dir_segmented)

    images_original, images_segmented = extract_images(
        paths_original, paths_segmented, init_size)

    return images_original, images_segmented
