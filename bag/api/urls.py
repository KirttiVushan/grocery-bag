from rest_framework.fields import IPAddressField
from django.urls import path, include
from bag.api import views
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('bag', views.Groceries_view, basename='shopping')

urlpatterns = [
    
    path('',include(router.urls)),
]