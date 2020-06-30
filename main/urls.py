from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lookup', views.lookup, name='lookup'),
    path('wireframe1', views.wireframe1, name='wireframe1'),
    path('wireframe2', views.wireframe2, name='wireframe2'),
    path('svg', views.svg, name='svg'),
    path('aspect', views.aspect, name='aspect'),
    path('render_page/<int:lesson_id>/', views.render_intro, name='render_intro'),
    path('render_page/<int:lesson_id>/<int:page_id>/', views.render_slideshow, name='render_slideshow'),
    # path('render_page/<int:lesson_id>/<int:page_id>/?fs=<int:fs>', views.render_slideshow, name='render_slideshow'),
]
