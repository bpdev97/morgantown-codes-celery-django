# Demo App View
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from demo_app.tasks import count_to_ten, scrape_image

from .models import Image, Message
from .serializers import ImageSerializer, MessageSerializer, UserSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """
    Provides List, Detail, Retrieve, Create, Update, Delete for Model
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ImageAttachmentViewSet(viewsets.ModelViewSet):
    """
    Provides List, Detail, Retrieve, Create, Update, Delete for Model
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    User ViewSet automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )


class CountToTen(APIView):
    """
    Dispatches a given number of count to ten task(s) on a remote server via celery.
    """
    def get(self, request, number_of_tasks):
        for _ in range(number_of_tasks):
            count_to_ten.delay()
        return Response(f'{number_of_tasks} tasks coming right up!', status=status.HTTP_200_OK)


class ScrapeImage(APIView):
    """
    Dispatches a task for a given image url.
    """
    def get(self, request):
        image_url = request.GET.get('image_url')
        scrape_image.delay(user=request.user.pk, image_url=image_url)
        return Response(f'Dispatched a task to grab the image at {image_url}.')
