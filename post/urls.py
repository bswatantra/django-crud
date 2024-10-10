
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='posts'),
    path('create', views.create, name='posts.create'),
    path('store', views.store, name='posts.store'),
    path('edit/<int:post_id>/', views.edit, name='posts.edit'),
    path('update/<int:post_id>/', views.update, name='posts.update'),
    path('destroy/<int:post_id>/', views.destroy, name='posts.destroy'),
]
