from celery import task
from time import sleep
from .models import Image
from django.contrib.auth.models import User

@task
def count_to_ten():
    for i in range(10):
        print(i + 1)
        sleep(1)


@task
def scrape_image(user, image_url):
    print(f'Grabbing the image at: {image_url}')
    sleep(5)
    # Get the user
    user_obj = User.objects.get(pk=user)
    Image.objects.create(owner=user_obj, url=image_url)
    print('Finished grabbing and storing image in the db.')
