# Demo App View
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import ImageAttachment, Message
from .serializers import ImageAttachmentSerializer, MessageSerializer, UserSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """
    Provides List, Detail, Retrieve, Create, Update, Delete for Model
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ImageAttachmentViewSet(viewsets.ModelViewSet):
    """
    Provides List, Detail, Retrieve, Create, Update, Delete for Model
    """
    queryset = ImageAttachment.objects.all()
    serializer_class = ImageAttachmentSerializer
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

