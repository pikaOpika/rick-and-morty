from characters.models import Character
from characters.scapper import sync_api


from celery import shared_task

@shared_task
def run_sync_with_api() -> int:
    sync_api()


@shared_task
def run_count_of_characters() -> int:
    return Character.objects.count()
