from celery import task
from time import sleep

@task
def count_to_ten():
    for i in range(10):
        print(i + 1)
        sleep(1)
