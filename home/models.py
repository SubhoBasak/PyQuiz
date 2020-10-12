from django.db import models
from django.contrib.auth.models import User


class Score(models.Model):
    user = models.ForeignKey(verbose_name='User', to=User, on_delete=models.CASCADE)
    score = models.IntegerField(verbose_name='Score', default=0)
    date_time = models.DateTimeField(verbose_name='Date time', auto_now_add=True)

    @property
    def full_name(self):
        return self.user.first_name+' '+self.user.last_name

    def __str__(self):
        return self.user.username
