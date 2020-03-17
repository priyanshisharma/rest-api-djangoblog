from django.urls import path
from . import views

urlpatterns = [
   path('post/', views.list),
   path('post/<int:pk>', views.post_detail),
   path('post/new', views.create),
   path('post/<int:pk>/remove/', views.delete),
   path('post/<int:pk>/edit/', views.update),
   path('login', views.login)
]