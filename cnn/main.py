from datas.get_datas import get_data_from_mnist
from models.cnn import cnn

(train_images, train_labels), (test_images, test_labels) = get_data_from_mnist()
model = cnn()

model.summary()

model.compile(optimizer="adam",
              loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)