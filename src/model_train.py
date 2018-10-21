from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import os 
print('Imported')

app = ClarifaiApp() #('c50b25d56e0645449f8afe316cacfa6d')
model = app.models.get('Crop')

model.model_version = 'a8c163102e0b4420b4a44c0b636eaeb6'

directory = os.path.dirname(os.path.abspath(__file__))
directory = os.path.join(directory, 'rice')
# image = ClImage(os.path.join(directory,'6.jpg'))

image = ClImage(url='https://5.imimg.com/data5/SA/BI/MY-10025503/wgl-paddy-500x500.jpg')
print(model.predict([image]))

# '''
# Train model with images of rice
# '''
# directory = os.path.dirname(os.path.abspath(__file__))
# directory = os.path.join(directory, 'rice')
# imgs = []
# for file in os.listdir(directory):
# 	print('Adding ' + file)
# 	img = C1Image(url=file,concepts=['rice'],not_concepts=['wheat'])
# 	imgs.append(img)

# '''
# Train model with image of wheat
# '''
# directory = os.path.dirname(os.path.abspath(__file__))
# directory = os.path.join(directory, 'wheat')
# for file in os.listdir(directory):
# 	print('Adding ' + file)
# 	img = C1Image(url=file,concepts=['rice'],not_concepts=['wheat'])
# 	imgs.append(img)

# print('Added all images')
# app.inputs.bulk_create_images(imgs)

# print('Creating model')
# model = app.models.create('plants', concepts = ['rice','wheat'])
# with open('model.txt','w') as f:
# 	f.write(model)

# print('Done')