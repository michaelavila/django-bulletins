import context_processors
import models

from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import RequestFactory


class GlobalBulletinManagerTests(TestCase):

    def test_creates_necessay_bulletins(self):
        user = User.objects.create_user(username='testuser')

        bulletin = models.GlobalBulletin.objects.create_bulletin(message='', creator=user)

        self.assertEquals(models.GlobalBulletin.objects.all()[0], bulletin)
        self.assertEquals(1, models.GlobalBulletin.objects.count())
        self.assertEquals(1, models.Bulletin.objects.count())


class BulletinsContextProcessorTests(TestCase):

    def test_bulletins_direct(self):
        user = User.objects.create_user(username='testuser')
        bulletin = models.GlobalBulletin.objects.create_bulletin(message='', creator=user)
        request = RequestFactory().get('/')

        context = context_processors.bulletins(request)

        self.assertEqual([bulletin], list(context['bulletins']['global']))
