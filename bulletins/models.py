import managers

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Bulletin(models.Model):
    message = models.TextField()
    creator = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True)

    def has_been_read(self):
        return self.read_at != None

    def mark_read(self):
        self.read_at = timezone.now()
        self.save()


class GlobalBulletin(models.Model):
    bulletin = models.ForeignKey(Bulletin)

    objects = managers.GlobalBulletinManager()


class DirectBulletin(models.Model):
    bulletin = models.ForeignKey(Bulletin)
    recipient = models.ForeignKey(User)

    objects = managers.DirectBulletinManager()
