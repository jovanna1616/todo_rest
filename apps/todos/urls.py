from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todos import views

# Create a router and register our viewsets with it.
router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]