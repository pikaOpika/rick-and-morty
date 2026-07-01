import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rick_and_morty_api.settings')

app = Celery('rick_and_morty_api')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()

 