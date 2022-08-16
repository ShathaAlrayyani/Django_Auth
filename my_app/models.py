from django.db import models
from django.contrib.auth import get_user_model


class MyApp(models.Model):
    ruler = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    number_of_people = models.IntegerField(null=True, blank=True)
    area = models.IntegerField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'MyApp'
