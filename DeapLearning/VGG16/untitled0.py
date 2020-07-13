import pandas as pd
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.layers import Dense,Flatten
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from glob import glob
IMAGE_SIZE=[244,244]

train_path="train"
test_path="test"

vgg=VGG16(input_shape=IMAGE_SIZE+[3],weights='imagenet',include_top=False)

for layers in vgg.layers:
    layers.trainable=False
    
folders=glob('/user/K DataScience/*')


train_datagentrater=ImageDataGenerator(rescale=1./255,
                                       shear_range=0.2,
                                       zoom_range=0.2,
                                       horizontal_flip=True)


test_datagentrater=ImageDataGenerator(rescale=1./255)