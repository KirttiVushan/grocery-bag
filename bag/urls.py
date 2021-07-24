from django.contrib import admin
from django.urls import path
from . import views


app_name='bag'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('update/<int:item_pk>', views.update, name='update'),
    path('delete/<int:item_pk>', views.delete_item, name='delete'),
    path('logout/',views.logOut, name="logOut")
]
