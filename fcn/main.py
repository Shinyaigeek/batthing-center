from models.fcn import fcn
from format_data.format import import_data
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import numpy as np
import tensorflow as tf
import tensorflow.keras.backend as K
import pydot_ng as pydot
import glob2 as glob

from tensorflow.keras.utils import plot_model

model = fcn(7)
model.summary()

img_size = (224, 224)
label_list = np.array([[0, 0, 0], [0, 0, 255], [0, 255, 0], [
                      255, 0, 0], [255, 255, 0], [255, 0, 255], [0, 255, 255]])
# images_original, images_segmented = import_data(
#     dir_original="data/image", dir_segmented="data/label", init_size=img_size)

# weight_list = K.cast([K.sum(images_segmented[:, :, :, i]/100000)
#                       for i in range(7)], K.floatx())
# sum = K.sum(weight_list)
# weight_list = sum/(7*weight_list)

# print(weight_list)


# def class_cross_entropy(class_label, y_true, y_pred):
#     return -y_true[:, :, :, class_label] * K.log(y_pred[:, :, :, class_label])*weight_list[class_label]


# def average_cross_entropy(y_true, y_pred):
#     class_count = y_pred.shape[-1]
#     class_cross_entropy_list = [class_cross_entropy(
#         i, y_true, y_pred) for i in range(class_count)]
#     class_cross_entropy_matrix = K.concatenate(
#         class_cross_entropy_list, axis=0)
#     return K.mean(class_cross_entropy_matrix)


# model.compile(loss=average_cross_entropy,
#               optimizer="adam", metrics=["accuracy"])

# model.fit(x=images_original,
#           y=images_segmented,
#           epochs=52
#           )

# model.save_weights("fcn.hdf5")

model.load_weights("fcn.hdf5")

plot_model(model, to_file='model.png')


def max_pooling_without_first(target):
    without_first = target[1:]
    return np.argmax(without_first)


def create_mask(pred_mask):
    pred_mask = pred_mask[0]
    mask = np.zeros((224, 224, 3))
    for i in range(len(pred_mask)):
        for j in range(len(pred_mask[i])):
            el = pred_mask[i][j]
            highest_idx = np.argmax(el)
            # if highest_idx == 0:
            #     if el[0] > 0.22:
            #         a = 0
            #     else:
            #         # print("other")
            #         # print(max_pooling_without_first(el))
            #         # print(el)
            #         a = 9
            #         # mask[i][j] = label_list[max_pooling_without_first(el) + 1]
            # else:
            #     print("other")
            #     print(max_pooling_without_first(el))
            #     print(el)
                # mask[i][j] = label_list[max_pooling_without_first(el) + 1]

            mask[i][j] = label_list[highest_idx]
    return mask


def display(display_list):
    plt.figure(figsize=(15, 15))

    title = ['Input Image', 'True Mask', 'Predicted Mask']

    for i in range(len(display_list)):
        plt.subplot(1, len(display_list), i+1)
        plt.title(title[i])
        plt.imshow(tf.keras.preprocessing.image.array_to_img(display_list[i]))
        plt.axis('off')
    plt.show()


def show_predictions(dataset=None, num=1):
    if dataset:
        for image, mask in dataset.take(num):
            pred_mask = model.predict(image)
            display([image[0], create_mask(pred_mask)])
    else:
        display([sample_image, sample_mask,
                 create_mask(model.predict(sample_image[tf.newaxis, ...]))])

def full_right(left, right):
    for i in range(len(left)):
        print(right[i])
        if not (left[i] == right[i]):
            return False
    return True

def get_presice():
    paths = glob.glob("./data/presice/image/*")
    precice = 0
    recall = 0
    for ab_path in paths:
        file_name_sp = ab_path.split("/")
        file_name = file_name_sp[len(file_name_sp) - 1].split(".JPG")[0]
        image = cv2.imread("./data/presice/image/" + file_name + ".JPG")
        image = cv2.resize(image, (224, 224))
        image = np.asarray(image, dtype=np.float16)
        image = np.expand_dims(image, axis=0)
        segmented = cv2.imread("./data/presice/label/" + file_name + ".JPG")
        segmented = cv2.resize(segmented, (224, 224))
        segmented = np.asarray(segmented, dtype=np.float16)
        segmented = np.expand_dims(segmented, axis=0)

        print(image.shape, segmented.shape)

        p = model.predict(image)
        p = create_mask(p)

        precice_per_file = 0
        recall_per_file = 0

        for label in label_list:
            tp = 0
            fp = 0
            fn = 0
            for i in range(len(p)):
                col = p[i]
                for j in range(len(col)):
                    el = col[j]

                    # print(el)

                    if np.allclose(el, label):
                        if np.allclose(segmented[0][i][j], el):
                            tp += 1
                        else:
                            fp += 1
                    if np.allclose(segmented[0][i][j], label):
                        if not np.allclose(label, el):
                            fn += 1
            print(tp, fp, fn)
            print("------")
            if not(((tp + fp) == 0) | ((tp + fn) == 0)):
                precice_per_file += tp / (tp + fp)
                recall_per_file += tp / (tp + fn)

        precice_per_file /= 7
        recall_per_file /= 7

        precice += precice_per_file
        recall += recall_per_file
    precice /= 3
    recall /= 3

    return 2 * recall * precice / (recall + precice)




image = cv2.imread("./IMG_3062.JPG")

image = cv2.resize(image, (224, 224))
data = np.asarray(image, dtype=np.float16)
image = np.expand_dims(data, axis=0)
print(image.shape)
# image = np.reshape(image, (224, 224, 3))

p = model.predict(image)



print(get_presice())
# for i in range(len(p[0])):
#     for j in range(len(p[0][i])):
#         p[0][i][j][0] -= 0.09
#         p[0][i][j][5] *= 0.6
#         p[0][i][j][1] *= 0.7

# display([data, create_mask(p)])
