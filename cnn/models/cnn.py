from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.models import Model

def cnn():
    input = Input(shape=(28, 28, 1))
    middle_layer = Conv2D(32, (3, 3), activation="relu")(input)
    middle_layer = MaxPooling2D((2, 2))(middle_layer)
    middle_layer = Conv2D(64, (3, 3), activation="relu")(middle_layer)
    middle_layer = MaxPooling2D((2, 2))(middle_layer)
    middle_layer = Conv2D(64, (3, 3), activation="relu")(middle_layer)

    # dense
    middle_layer = Flatten()(middle_layer)
    middle_layer = Dense(64, activation="relu")(middle_layer)
    output = Dense(10, activation="softmax")(middle_layer)
    
    return Model(inputs=input, outputs=output)

