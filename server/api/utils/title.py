from django.db import transaction

from ..models import Title


@transaction.atomic
def register_like(title_id):
    title = Title.objects.get(id=title_id)
    title.count_like += 1
    title.save()


@transaction.atomic
def register_view(title_id):
    title = Title.objects.get(id=title_id)
    title.count_view += 1
    title.save()
