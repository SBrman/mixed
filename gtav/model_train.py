import numpy as np
import time
from alexnet_keras_new import alexnet_model
import tensorflow as tf
from tensorflow.keras.callbacks import TensorBoard
import os

os.chdir(r'H:\python\gtav')

WIDTH = 128
HEIGHT = 72
LR = 1e-3
EPOCHS = 8
MODEL_NAME = f'gtav_car_{LR}_AlexNet2_{EPOCHS}_epochs.model'

model = alexnet_model(WIDTH, HEIGHT, outputs=4)
tensorboard = TensorBoard(log_dir=f'./logs/{MODEL_NAME}')

data = np.load(r'H:/python/gtav/balanced_training_data/balanced_data_for_training.npy', allow_pickle=True)

train = data[:-5000]
test = data[-5000:]

train_x = np.array([frame[0] for frame in train]).reshape(-1, WIDTH, HEIGHT, 1)

train_y = np.array([frame[1] for frame in train])

test_x = np.array([frame[0] for frame in test]).reshape(-1, WIDTH, HEIGHT, 1)
test_y = np.array([frame[1] for frame in test])


model.fit(train_x, train_y, batch_size=64, epochs=EPOCHS, validation_data=(test_x, test_y), callbacks=[tensorboard])

# tensorboard --logdir='logs/'

model.save(MODEL_NAME)
