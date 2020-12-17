from models.fcn import fcn
from format_data.format import import_data
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import numpy as np
import tensorflow as tf
import tensorflow.keras.backend as K
import pydot_ng as pydot

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
    print(mask)
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


image = cv2.imread("./IMG_3062.JPG")

image = cv2.resize(image, (224, 224))
data = np.asarray(image, dtype=np.float16)
image = np.expand_dims(data, axis=0)
print(image.shape)
# image = np.reshape(image, (224, 224, 3))

p = model.predict(image)

# for i in range(len(p[0])):
#     for j in range(len(p[0][i])):
#         p[0][i][j][0] -= 0.09
#         p[0][i][j][5] *= 0.6
#         p[0][i][j][1] *= 0.7

display([data, create_mask(p)])
