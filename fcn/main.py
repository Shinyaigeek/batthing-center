from models.fcn import fcn
from format_data.format import import_data
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import numpy as np

model = fcn(7)
model.summary()

# model.compile(loss="categorical_crossentropy", optimizer="adam")

# img_size = (224, 224)

# images_original, images_segmented = import_data(
#     dir_original="data/image", dir_segmented="data/label", init_size=img_size)

# model.fit(x=images_original,
#           y=images_segmented,
#           batch_size=1,
#           epochs=3
#           )

# model.save_weights("fcn.hdf5")

model.load_weights("fcn.hdf5")


def create_mask(pred_mask):
    pred_mask = tf.argmax(pred_mask, axis=-1)
    pred_mask = pred_mask[..., tf.newaxis]
    return pred_mask[0]


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
# image = np.reshape(image, (224, 224, 3))

# p = model.predict(image)

display([data, create_mask(model.predict(image))])
