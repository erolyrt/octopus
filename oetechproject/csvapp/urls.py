from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file_view, name='upload-view'),
    path('viewdata', views.view_d0010, name='viewdata'),
]