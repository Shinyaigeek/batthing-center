from tensorflow.keras.layers import Input, Conv2D, MaxPool2D, Conv2DTranspose, Flatten, Conv2DTranspose, Cropping2D, Activation
from tensorflow.keras.models import Model


def fcn(fcn_classes):
    input = Input(shape=(224, 224, 3))
    middle_layer = Conv2D(32, (3, 3))(input)
    middle_layer = MaxPool2D((2, 2))(middle_layer)
    middle_layer = Conv2D(64, (3, 3))(middle_layer)
    middle_layer = Conv2D(64, (3, 3))(middle_layer)
    middle_layer = Conv2D(64, (3, 3))(middle_layer)
    middle_layer = Conv2D(64, (3, 3))(middle_layer)
    middle_layer = Conv2D(64, (3, 3))(middle_layer)
    middle_layer = MaxPool2D((2, 2))(middle_layer)
    middle_layer = Conv2D(64, (3, 3))(middle_layer)
    middle_layer = Conv2D(64, (3, 3))(middle_layer)
    middle_layer = Conv2D(128, (3, 3))(middle_layer)
    middle_layer = Conv2D(128, (3, 3))(middle_layer)
    middle_layer = Conv2D(128, (3, 3))(middle_layer)
    middle_layer = MaxPool2D((2, 2))(middle_layer)
    middle_layer = Conv2D(128, (3, 3))(middle_layer)
    middle_layer = Conv2D(128, (3, 3))(middle_layer)
    middle_layer = Conv2D(128, (3, 3))(middle_layer)
    middle_layer = Conv2D(128, (3, 3))(middle_layer)
    middle_layer = Conv2D(128, (3, 3))(middle_layer)
    middle_layer = Conv2D(128, (3, 3))(middle_layer)
    middle_layer = Conv2D(128, (3, 3))(middle_layer)
    middle_layer = Conv2D(128, (3, 3))(middle_layer)

    output = Conv2D(fcn_classes, (4, 4), activation="softmax")(middle_layer)

    output = Conv2DTranspose(fcn_classes, (232, 232),
                             padding='valid')(output)
    output = Cropping2D(((4, 4), (4, 4)))(output)

    output = Activation("softmax")(output)

    return Model(inputs=input, outputs=output)
