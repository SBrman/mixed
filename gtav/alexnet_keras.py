import tesnorflow as tf
from tf.keras.models import Sequential
from tf.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tf.keras.layers.normalization import BatchNormalization
import numpy as np

def alexnet2(width, height, lr, output=4):
    model = Sequential()

    # 1st Convolutional Layer
    model.add(Conv2D(filters=96, input_shape=(None, width, height, 1), kernal_size=(11, 11), strides=(4, 4), padding='valid'))
    mode.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(3,3), strides=(2,2), padding=’valid’))

    # 2nd Convolutional Layer
    model.add(Conv2D(filters=256, kernel_size=(5,5)))
    model.add(Activation(‘relu’))
    model.add(MaxPooling2D(pool_size=(3,3), strides=(2,2), padding=’valid’))

    # 3rd Convolutional Layer
    model.add(Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding=’valid’))
    model.add(Activation(‘relu’))

    # 4th Convolutional Layer
    model.add(Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding=’valid’))
    model.add(Activation(‘relu’))

    # 5th Convolutional Layer
    model.add(Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), padding=’valid’))
    model.add(Activation(‘relu’))
    model.add(MaxPooling2D(pool_size=(3,3), strides=(2,2), padding=’valid’))

    # Passing it to a Fully Connected layer
    model.add(Flatten())
    # 1st Fully Connected Layer
    model.add(Dense(4096))
    model.add(Activation(‘relu’))
    # Add Dropout to prevent overfitting
    model.add(Dropout(0.4))

    # 2nd Fully Connected Layer
    model.add(Dense(4096))
    model.add(Activation(‘relu’))
    # Add Dropout
    model.add(Dropout(0.4))

    # Output Layer
    model.add(Dense(output))
    model.add(Activation(‘softmax’))

    # Compile
    model.compile(Loss='categorical_crossentropy', 
                    optimizer='adam', 
                    metrics=['accuracy'])

    return model