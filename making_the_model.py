import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, LeakyReLU, Flatten
from keras.metrics import AUC
from keras import backend as K
from keras.datasets import mnist
import matplotlib.pyplot as plt

(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train, X_test = X_train/255, X_test/255


model = Sequential()


model.add(Flatten(input_shape=(28,28)))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(10,activation='softmax'))



model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy'])

Results = model.fit(X_train,
          y_train,
          epochs=5)

plt.plot(Results.history['accuracy'])

plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train'], loc='upper left')
plt.show()

model.summary()

model.evaluate(X_test,y_test)


model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
 #serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")


%run serverr.py



