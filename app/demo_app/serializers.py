# Demo App Serializers
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Message, ImageAttachment


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    image_attachment = serializers.HyperlinkedRelatedField(many=True, read_only=True)
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Message
        fields = '__all__'


class ImageAttachmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageAttachment
        read_only_fields = ('owner',)
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    images_owned = serializers.HyperlinkedRelatedField(many=True, read_only=True)
    messages = serializers.HyperlinkedRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'messages', 'images_owned')
