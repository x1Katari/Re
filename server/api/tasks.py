from .utils.chapter import register_like, register_view
from server.celery import app as celery


@celery.task()
def register_like_task(chapter_id):
    register_like(chapter_id)


@celery.task()
def register_view_task(chapter_id):
    register_view(chapter_id)
