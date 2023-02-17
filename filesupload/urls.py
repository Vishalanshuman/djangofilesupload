from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='single_upload'),
    path('multiple', views.upload_multiple_files, name='multiple_upload'),

]
