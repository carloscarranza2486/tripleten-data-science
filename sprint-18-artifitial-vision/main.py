import os
import gzip
import struct
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense


# Carpeta donde está este archivo .py (y los .gz)
DATA_DIR = os.path.dirname(os.path.abspath(__file__))


def read_idx(filename):
    with gzip.open(filename, "rb") as f:
        zero, data_type, dims = struct.unpack(">HBB", f.read(4))
        shape = tuple(struct.unpack(">I", f.read(4))[0] for d in range(dims))
        return np.frombuffer(f.read(), dtype=np.uint8).reshape(shape)


# Ejercicio 1
def load_data(path):
    X = read_idx(os.path.join(path, "train-images-idx3-ubyte.gz"))
    y = read_idx(os.path.join(path, "train-labels-idx1-ubyte.gz"))

    X = X.astype("float32") / 255

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=123, stratify=y
    )

    return (X_train, y_train), (X_test, y_test)


# Ejercicio 2
def create_model(input_shape, num_classes):
    model = Sequential()
    model.add(Flatten(input_shape=input_shape))
    model.add(Dense(64, activation="relu"))
    model.add(Dense(32, activation="relu"))
    model.add(Dense(16, activation="relu"))
    model.add(Dense(num_classes, activation="softmax"))

    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.001),
        loss="sparse_categorical_crossentropy",
        metrics=["acc"],
    )
    return model


if __name__ == "__main__":
    # Prueba ejercicio 1
    (X_train, y_train), (X_test, y_test) = load_data(DATA_DIR)
    print("Train:", X_train.shape, y_train.shape)
    print("Test:", X_test.shape, y_test.shape)

    # Prueba ejercicio 2
    create_model((28, 28), 10).summary()

    # Primera imagen (al final, porque plt.show() pausa el script)
    plt.imshow(X_train[0], cmap="gray")
    plt.title(f"Label: {y_train[0]}")
    plt.show()
