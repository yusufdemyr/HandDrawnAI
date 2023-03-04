
import os
import cv2
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.models import load_model
from PIL import Image


# Görüntü dosyalarının bulunduğu klasörün yolu
data_path = "screenshots"

# Verilerin yüklenmesi ve önişlenmesi
import os
import numpy as np
from PIL import Image

def load_data(data_path):
    data = []
    labels = []
    for file in os.listdir(data_path):
        if file.endswith(".png"):
            img_path = os.path.join(data_path, file)
            img = cv2.imread(img_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            data.append(img)
            if "-" in file:
                label = int(file.split("-")[0])
            else:
                label = int(file.split(".")[0])
            labels.append(label)
    return np.array(data,dtype=np.float32), np.array(labels,dtype=np.float32)



def create_model():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation="relu"))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(64, (3, 3), activation="relu"))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(128, (3, 3), activation="relu"))
    model.add(MaxPooling2D((2, 2)))
    model.add(Flatten())
    model.add(Dense(128, activation="relu"))
    model.add(Dense(10, activation="softmax"))
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    return model

data, labels = load_data(data_path)

data = np.reshape(data, (data.shape[0], data.shape[1], data.shape[2], 1))

model = create_model()





model.fit(data, labels, epochs=10, validation_split=0.2)

# Assuming `model` is your trained Keras model
model.save('model.h5')  # save the model as HDF5 file

# Load the saved model
model = load_model('model.h5')

# Load test image
test_img = cv2.imread('test-screenshot.png')

# Convert test image to grayscale
test_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

# Resize test image to the input shape of the model
test_img = cv2.resize(test_img, (640, 480))

# Add an extra dimension to match the input shape of the model
test_img = np.expand_dims(test_img, axis=0)
test_img = np.expand_dims(test_img, axis=-1)

prediction = model.predict(test_img)
predicted_label = np.argmax(prediction)

print("Predicted label: ", predicted_label)