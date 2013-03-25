import managers

from django.contrib.auth.models import User
from django.db import models


class Bulletin(models.Model):
    message = models.TextField()
    creator = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)


class GlobalBulletin(models.Model):
    bulletin = models.ForeignKey(Bulletin)

    objects = managers.GlobalBulletinManager()


class DirectBulletin(models.Model):
    bulletin = models.ForeignKey(Bulletin)
    recipient = models.ForeignKey(User)

    objects = managers.DirectBulletinManager()
