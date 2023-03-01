import cv2
import os
from PIL import Image
import numpy as np

image_directory='datasets/'

no_tumor_images= os.listdir(image_directory + 'no/')
yes_tumor_images= os.listdir(image_directory + 'yes/')
#creating 2 lists
dataset=[]
label=[]
# print(no_tumor_images)



# #to check if the given image is jpeg or not 
for i,image_name in enumerate(no_tumor_images):
    if(image_name.split('.')[1]=='jpg'):
        #to read each image
        image=cv2.imread(image_directory + '/no' + image_name)
        #converting the BGR image to RGB image
        image=Image.fromarray(image,'RGB')
        
        #resizing the image
        image=image.resize((64,64))
        #adding image to the list in the numpy array format
        dataset.append(np.array(image))
        #appending the label list 0 implying no brain tumour
        label.append(0) 

#repetition of the above process for yes_tumour_images
for i,image_name in enumerate(yes_tumor_images):
    if(image_name.split('.')[1]=='jpg'):
        image=cv2.imread(image_directory + '/yes' + image_name)
        image=Image.fromarray(image,'RGB')
        image=image.resize((64,64))
        dataset.append(np.array(image))
        label.append(1)  
        
print(dataset)
print(label)