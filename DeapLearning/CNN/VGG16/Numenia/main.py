import pandas as pd
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.layers import Dense,Flatten
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from glob import glob
from keras.layers import Flatten,Dense
from keras.models import Model
IMAGE_SIZE=[244,244]

folders=glob("/Users/ART/K DataScience/DeapLearning/CNN/VGG16/Numenia/test/*")

vgg=VGG16(input_shape=IMAGE_SIZE+[3],weights='imagenet',include_top=False)

for layers in vgg.layers:
    layers.trainable=False
    
x=Flatten()(vgg.output)
prediction=Dense(len(folders),activation="softmax")(x)

model=Model(input=vgg.input,output=prediction)
model.summary()
model.compile(optimizer="adam",
              loss="categorical_crossentropy",
              metrics=["accuracy"]
              )

train_datagentrater=ImageDataGenerator(rescale=1./255,
                                       shear_range=0.2,
                                       zoom_range=0.2,
                                       horizontal_flip=True)


test_datagentrater=ImageDataGenerator(rescale=1./255)


train_set=train_datagentrater.flow_from_directory('/Users/ART/K DataScience/DeapLearning/CNN/VGG16/Numenia/train',
                                                  target_size=(244,244),
                                                  batch_size=32,
                                                  class_mode='categorical')

test_set=test_datagentrater.flow_from_directory('/Users/ART/K DataScience/DeapLearning/CNN/VGG16/Numenia/test',
                                                target_size=(2444,244),
                                                batch_size=32,
                                                class_mode='categorical'
                                                )


r=model.fit_generator(train_set,
                      validation_data=test_set,
                      epochs=5,
                      steps_per_epoch=len(train_set),
                      validation_steps=len(test_set),
                      verbose=1)
