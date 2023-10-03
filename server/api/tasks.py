from .utils.title import register_like, register_view
from server.celery import app as celery


@celery.task()
def register_like_task(title_id):
    register_like(title_id)


@celery.task()
def register_view_task(title_id):
    register_view(title_id)
