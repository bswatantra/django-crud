
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='posts'),
    path('create', views.create, name='posts.create'),
    path('store', views.store, name='posts.store'),
    path('show/<int:id>/', views.show, name='posts.show'),
    path('edit/<int:id>/', views.edit, name='posts.edit'),
    path('update/<int:id>/', views.update, name='posts.update'),
    path('destroy/<int:id>/', views.destroy, name='posts.destroy'),
]
