import managers

from django.contrib.auth.models import User
from django.db import models


class Bulletin(models.Model):
    message = models.TextField()
    creator = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)


class GlobalBulletin(models.Model):
    objects = managers.GlobalBulletinManager()
    bulletin = models.ForeignKey(Bulletin)
