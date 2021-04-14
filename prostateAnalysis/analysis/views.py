from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 

import tensorflow as tf
import numpy as np
image = tf.keras.preprocessing.image
model = tf.keras.models.load_model('ProstateModel.h5')

def index(request):
    pagetitle = "Home"
    context = {
        "title": pagetitle
    }
    return render(request, "analysis/index.html", context)


def prediction(request):
    pagetitle = "Prediction Page"
    return render(request, "analysis/prediction.html", {"title": pagetitle})
    
@csrf_exempt 
def predict(request):
    imageFile = request.FILES['image'].file
    f = open('image.dat','wb')
    f.write(imageFile.read())
    f.close()

    img = image.load_img("image.dat",target_size=(256,256))
    img = image.img_to_array(img,dtype='float32')
    img = img.reshape(((1,256,256,3)))
    img = img/255.0 
    prediction = model.predict(img)
    print(prediction)
    #classes= ["negative","positive"] 
 
    return HttpResponse('{"result": %d}' % prediction[0][0],content_type="application/json")

