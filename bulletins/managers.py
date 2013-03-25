import models

from django.db.models import Manager


class GlobalBulletinManager(Manager):

    def create_bulletin(self, creator, message):
        bulletin = models.Bulletin.objects.create(
            creator=creator,
            message=message
        )
        return self.create(bulletin=bulletin)
