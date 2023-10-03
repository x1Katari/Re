from django.db import transaction

from ..models import Chapter


@transaction.atomic
def register_like(chapter_id):
    chapter = Chapter.objects.get(id=chapter_id)
    chapter.count_like += 1
    chapter.save()


@transaction.atomic
def register_view(chapter_id):
    chapter = Chapter.objects.get(id=chapter_id)
    chapter.count_view += 1
    chapter.save()
