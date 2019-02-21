from django.db.models.signals import post_save

from .models import Message, Image
from .tasks import send_email


def send_message(sender, instance, **kwargs):
    """
    Sends a message to its corresponding recipient.

    :param sender: The model that we are attaching this signal to.
    :param instance: The instance of the model that invoked this signal.
    :param kwargs: Extra key value data passed into the signal.
    """
    # Get data from the instance object.
    subject = instance.subject
    message = instance.body
    to_email = instance.to_user.email
    from_email = instance.author.email

    # Find and add to the body any image links
    images = Image.objects.filter(message=instance)
    urls = ""
    for img in images:
        print(img.url)
        urls = urls + f'  {img.url}  '
    print("Sending email out to customer.")
    send_email.delay(subject, message + urls, from_email=from_email, to_email=to_email)


# Attach the send_message signal to the Message Model.
# We are using a post_save signal, the send_message handler will be invoked after the instance has been saved.
post_save.connect(send_message, sender=Message)
