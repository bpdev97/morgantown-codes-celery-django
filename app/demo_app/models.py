# Demo App Models
from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    """
    A message from one user to another
    """
    subject = models.CharField(max_length=50, blank=True, default='')
    body = models.CharField(max_length=2000, blank=True, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    to_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    active = models.BooleanField(default=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        ordering = ('created_date', )
        db_table = 'message'
        verbose_name = 'User Message'
        verbose_name_plural = 'User Messages'


class ImageAttachment(models.Model):
    """
    S3 URL For Image attached to a Message
    """
    s3_url = models.URLField(blank=False)
    message = models.ForeignKey(Message, models.DO_NOTHING, related_name='image_attachment', null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images_owned')
    active = models.BooleanField(default=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'image_attachment'
        verbose_name = 'Image'
        verbose_name_plural = 'Image Attachments'

