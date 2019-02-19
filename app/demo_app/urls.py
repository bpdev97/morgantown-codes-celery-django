# Demo App URLs file

from django.urls import path
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from . import views

# Create a router and register our ViewSets
router = DefaultRouter()
router.register(r'messages', views.MessageViewSet)
router.register(r'images', views.ImageAttachmentViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    path('celery/count_to_ten/<int:number_of_tasks>', views.CountToTen.as_view()),
]
