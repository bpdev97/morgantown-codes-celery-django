# Demo App Serializers
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Message, Image


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    image_attachment = serializers.HyperlinkedRelatedField(view_name='image-detail', many=True, read_only=True)

    class Meta:
        model = Message
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        read_only_fields = ('owner',)
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    images_owned = serializers.HyperlinkedRelatedField(view_name='image-detail', many=True, read_only=True)
    messages = serializers.HyperlinkedRelatedField(view_name='message-detail', many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'messages', 'images_owned')
