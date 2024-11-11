from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import FoodViewset

router = DefaultRouter()
router.register('',FoodViewset, basename='food')
app_name = 'Food_app'

urlpatterns = [
    path('',include(router.urls))
]
