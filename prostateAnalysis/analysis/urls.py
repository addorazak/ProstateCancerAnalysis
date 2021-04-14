from django.urls import path, include
from . import views

urlpatterns = [
    path('prediction', views.prediction, name="prediction"),
    path('/api/predict', views.predict, name="predict")
]

