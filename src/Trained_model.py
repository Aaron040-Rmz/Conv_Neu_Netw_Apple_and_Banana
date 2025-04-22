import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator    #type: ignore
from tensorflow.keras.models import Sequential    #type: ignore
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense    #type: ignore
from tensorflow.keras.optimizers import Adam    #type: ignore

def train_model():
    data_dir = "dataset"
    model_save_path = "Trained_model/model.h5"

    img_size = (100, 100)
    batch_size = 16

    datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

    train_gen = datagen.flow_from_directory(
        data_dir,
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='training'
    )

    val_gen = datagen.flow_from_directory(
        data_dir,
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='validation'
    )

    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(64, activation='relu'),
        Dense(2, activation='softmax')  # 2 clases
    ])

    model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

    model.fit(train_gen, validation_data=val_gen, epochs=75)

    model.save(model_save_path)
    print(f"Modelo guardado en {model_save_path}")

