from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:pk>', views.post, name='post'),
    path('add/', views.add_blog_post, name='add-blog-post'),
    path('login/', views.login,name='login')
]