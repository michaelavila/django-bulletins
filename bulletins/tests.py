import context_processors
import models

from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import RequestFactory


class GlobalBulletinManagerTests(TestCase):

    def test_creates_necessay_bulletins(self):
        user = User.objects.create_user(username='testuser')

        bulletin = models.GlobalBulletin.objects.create_bulletin(
            message='',
            creator=user
        )

        self.assertEquals(models.GlobalBulletin.objects.all()[0], bulletin)
        self.assertEquals(1, models.GlobalBulletin.objects.count())
        self.assertEquals(1, models.Bulletin.objects.count())


class DirectBulletinManagerTests(TestCase):

    def test_creates_necessay_bulletins(self):
        user = User.objects.create_user(username='testuser')
        recipient = User.objects.create_user(username='testuserrecipient')

        bulletin = models.DirectBulletin.objects.create_bulletin(
            message='',
            creator=user,
            recipient=recipient
        )

        self.assertEquals(models.DirectBulletin.objects.all()[0], bulletin)
        self.assertEquals(1, models.DirectBulletin.objects.count())
        self.assertEquals(1, models.Bulletin.objects.count())


class GlobalBulletinsContextProcessorTests(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='testuser')
        self.bulletin = models.GlobalBulletin.objects.create_bulletin(
            message='',
            creator=user
        )
        self.request = RequestFactory().get('/')

    def test_bulletins_global(self):
        context = context_processors.bulletins(self.request)

        self.assertEqual([self.bulletin], list(context['bulletins']['global']))


class DirectBulletinsContextProcessorTests(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='testuser')
        recipient = User.objects.create_user(username='testuserrecipient')
        self.bulletin = models.DirectBulletin.objects.create_bulletin(
            message='',
            creator=user,
            recipient=recipient
        )
        self.request = RequestFactory().get('/')
        self.request.user = recipient

    def test_bulletins_direct(self):
        context = context_processors.bulletins(self.request)

        self.assertEqual([self.bulletin], list(context['bulletins']['direct']))
