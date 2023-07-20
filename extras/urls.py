from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'extras', views.ExtraViewSet, basename='extras')

urlpatterns = [
    path('', include(router.urls))
]