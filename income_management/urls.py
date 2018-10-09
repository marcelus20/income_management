from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()

router.register('description', views.DescriptionView)
router.register('transactions', views.TransactionView)
router.register('Users', views.UsersView)

urlpatterns = [
    path('', include(router.urls))
]