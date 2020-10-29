from tensorflow.keras import datasets

def get_data_from_mnist():
    (train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()
    return (train_images / 255.0, train_labels), (test_images / 255.0 , test_labels)
    
