from datetime import datetime
from django.utils.timezone import make_aware

from django.test import TestCase

from django.urls import reverse
from rest_framework import status

from .models import BaseEvent

from apps.utils.utest import TestMixin
from apps.group.models import Club


class BaseEventTestCase(TestCase, TestMixin):
    def setUp(self) -> None:
        self.user_setup()
        self.club = Club.objects.create(
            name="TestClubForEvents")
        self.club.admins.set([self.u2.student])
        self.event = BaseEvent.objects.create(
            title="TestEvent", group=self.club.slug, date=make_aware(datetime.now()),
            description="Test Desc", location="Amphi A")
        self.assertEqual(len(BaseEvent.objects.all()), 1)

    def test_event_detail_view(self):
        url = reverse('event:detail', args=[self.event.slug])
        # Une personne non connectée ne doit pas pouvoir voir l'event et doit être redirigée vers la page de login
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_302_FOUND)

        self.client.login(username=self.u1, password="pass")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_participate_function(self):
        """Check that a user can registrate for an event."""
        url = reverse('event:add-participant', args=[self.event.slug])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_302_FOUND)
        self.assertEqual(self.event.get_number_participants, 0)

        self.client.login(username=self.u2, password="pass")
        # You get redirected at the end of the function
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_302_FOUND)
        self.assertEqual(self.event.get_number_participants, 1)
        # Check that you only get counted once
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_302_FOUND)
        self.assertEqual(self.event.get_number_participants, 1)

        url = reverse('event:remove-participant', args=[self.event.slug])
        resp = self.client.get(url)
        # You get redirected at the end of the function
        self.assertEqual(resp.status_code, status.HTTP_302_FOUND)
        self.assertEqual(self.event.get_number_participants, 0)

    def test_event_update_view(self):
        url = reverse("event:edit", args=[self.event.slug])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_302_FOUND)

        self.client.login(username=self.u2, password="pass")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
