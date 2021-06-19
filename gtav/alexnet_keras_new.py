from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.regularizers import l2

def alexnet_model(WIDTH, HEIGHT, outputs=4, l2_reg=0.,
    weights=None):
    
    img_shape=(WIDTH, HEIGHT, 1)
    # Initialize model
    model = Sequential()

    # Layer 1
    model.add(Conv2D(96, (11, 11), input_shape=img_shape,
        padding='same', kernel_regularizer=l2(l2_reg)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # Layer 2
    model.add(Conv2D(256, (5, 5), padding='same'))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(3, 3)))

    # Layer 3
    model.add(ZeroPadding2D((1, 1)))
    model.add(Conv2D(512, (3, 3), padding='same'))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # Layer 4
    model.add(ZeroPadding2D((1, 1)))
    model.add(Conv2D(1024, (3, 3), padding='same'))
    model.add(BatchNormalization())
    model.add(Activation('relu'))

    # Layer 5
    model.add(ZeroPadding2D((1, 1)))
    model.add(Conv2D(1024, (3, 3), padding='same'))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # Layer 6
    model.add(Flatten())
    model.add(Dense(3072))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(Dropout(0.5))

    # Layer 7
    model.add(Dense(4096))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(Dropout(0.5))

    # Layer 8
    model.add(Dense(outputs))
    model.add(BatchNormalization())
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy', 
                    optimizer='adam', 
                    metrics=['accuracy'])

    return model