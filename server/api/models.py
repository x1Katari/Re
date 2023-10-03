from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Title(models.Model):
    rus_name = models.CharField(max_length=128, null=False)
    en_name = models.CharField(max_length=128, blank=True)
    alt_name = models.CharField(max_length=128, blank=True)
    description = models.TextField(blank=True)
    count_view = models.IntegerField(default=0, blank=True, null=False)
    count_like = models.IntegerField(default=0, blank=True, null=False)
    tags = models.ManyToManyField(Tag, related_name='titles')

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.rus_name


class Volume(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE,
                              related_name="volumes", null=False)
    name = models.CharField(max_length=128, blank=True)
    number = models.IntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=11)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f'{self.title}. Том: {self.number}'


class Chapter(models.Model):
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE,
                               related_name="chapters", null=False, default=1)
    number = models.FloatField(null=False)
    content = models.TextField(null=False)

    class Meta:
        ordering = ["number"]

    def __str__(self):
        return f'{self.volume}. Глава: {self.number}'
