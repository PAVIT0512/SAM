import os
import cv2
import random
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Activation

# DIRECTORY= r"./boxlabeldataset"
# DIRECTORY= r"./box_label_dataset"
DIRECTORY= r"./boxlabel"
CATAGORIES= ['label','nolabel']

data=[]

for categories in CATAGORIES:
    folder=os.path.join(DIRECTORY,categories)
    print(folder)
    label=CATAGORIES.index(categories)


    for img in os.listdir(folder):
        img=os.path.join(folder,img)
        img_arr=cv2.imread(img)
        img_arr=cv2.resize(img_arr,(100,100))

        data.append([img_arr,label])

random.shuffle(data)
x=[]
y=[]
for features,label in data:
    x.append(features)
    y.append(label)

X=np.array(x)
Y=np.array(y)
X=X/255

model=Sequential()
model.add( Conv2D(64,(3,3),input_shape=X.shape[1:],activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add( Conv2D(32,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add( Conv2D(32,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(2,activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

model.fit(X,Y,epochs=15,validation_split=0.1)
model.summary()
model.save("model3.keras")

# boxlabeldataset => model.keras
# box_label_dataset => model2.keras
# boxlabel => model3.keras