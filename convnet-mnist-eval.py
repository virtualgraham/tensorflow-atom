from keras import layers
from keras import models
from keras.models import load_model

model = load_model('convnet-minst.h5')

from keras.datasets import mnist
from keras.utils import to_categorical

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

test_images = test_images.reshape((10000, 28, 28, 1))
test_images = test_images.astype('float32') / 255
test_labels = to_categorical(test_labels)

test_loss, test_acc = model.evaluate(test_images, test_labels)

print(test_acc)