from django.test import TestCase
from apps.utils.utest import TestMixin
from django.urls import reverse
from rest_framework import status

from .models import Club, NamedMembershipClub

class TestGroups(TestCase, TestMixin):
    def setUp(self):
        self.user_setup()

    def test_create_club(self):
        Club.objects.create(name='TestClub')
        self.assertEqual(len(Club.objects.all()),1)
    
    def test_club_views(self):
        Club.objects.create(name='TestClub')
        club = Club.objects.all().first()
        url = reverse('group:detail', args=[club.slug])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        url = reverse('group:update', args=[club.slug])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_302_FOUND)

    def test_add_member(self):
        club = Club.objects.create(name='TestClub')
        payload = {
            'function': 'test',
            'year': 2020
        }
        url = reverse('group:add-membership', args=[club.id])
        resp = self.client.post(url, payload)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

        self.client.login(username=self.u2.username, password='pass')
        resp = self.client.post(url, payload)
        self.assertEqual(resp.status_code, status.HTTP_302_FOUND)

        self.assertEqual(NamedMembershipClub.objects.filter(club=club, student=self.u2.student).count(), 1)

