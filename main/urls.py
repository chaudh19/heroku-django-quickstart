from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lookup', views.lookup, name='lookup'),
    path('wireframe1', views.wireframe1, name='wireframe1'),
    path('wireframe2', views.wireframe2, name='wireframe2'),
]
