import context_processors
import models

from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import RequestFactory
from django.utils import timezone


class BulletinHasBeenReadTests(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='testuser')
        self.bulletin = models.Bulletin.objects.create(message='', creator=user)

    def test_has_not_been_read(self):
        has_been_read = self.bulletin.has_been_read()

        self.assertFalse(has_been_read)

    def test_has_been_read(self):
        self.bulletin.read_at = timezone.now()

        has_been_read = self.bulletin.has_been_read()

        self.assertTrue(has_been_read)


class BulletinReadTests(TestCase):

    def test_mark_read(self):
        user = User.objects.create_user(username='testuser')
        self.bulletin = models.Bulletin.objects.create(message='', creator=user)

        self.assertFalse(self.bulletin.has_been_read())
        self.bulletin.mark_read()
        self.assertTrue(self.bulletin.has_been_read())


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
