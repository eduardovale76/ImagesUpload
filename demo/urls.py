from django.urls import path
from .views import index, uploadView

urlpatterns = [
    path('', index, name='index'),
    path('upload_image', uploadView, name='upload_image'),
]
