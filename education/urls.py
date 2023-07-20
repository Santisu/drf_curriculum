from django.urls import include, path

from rest_framework.routers import DefaultRouter

from education import views

router = DefaultRouter()
router.register(r'education', views.EducationViewSet, basename='education')

urlpatterns = [
    path('', include(router.urls))
]