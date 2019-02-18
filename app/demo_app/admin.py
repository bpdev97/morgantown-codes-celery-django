# demo_app admin.py -
#   This file governs what is displayed and what is actionable on the Django Admin Dashboard

from django.contrib import admin
from .models import Message, ImageAttachment


# Admin for Messages
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'subject', 'to_user', 'active', 'modified_date',  'created_date']
    list_select_related = ('author', 'to_user')
    search_fields = ['author__username', 'subject', 'to_user__username']
    readonly_fields = ('created_date', 'modified_date')
    ordering = ('author', 'subject', 'to_user', 'created_date', 'modified_date', )
    list_per_page = 30


# Admin for Image Attachments
class ImageAttachmentAdmin(admin.ModelAdmin):
    list_display = ['s3_url', 'owner', 'message', 'active', 'modified_date', 'created_date']
    list_select_related = ('owner', 'message')
    search_fields = ['s3_url', 'owner__username']
    readonly_fields = ('created_date', 'modified_date')
    ordering = ('created_date', )
    list_per_page = 30


# Register Model to Admins
admin.site.register(Message, MessageAdmin)
admin.site.register(ImageAttachment, ImageAttachmentAdmin)
