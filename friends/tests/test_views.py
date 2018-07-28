import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Puppy
from ..serializers import FriendSerializer


# initialize the APIClient app
client = Client()

class CreateNewFriendTest(TestCase):
    """ Test module for inserting a new Friend contact """

    def setUp(self):
        self.valid_payload = {
            name='Om Ji', age=24, phone_number='9696404453', email='omjigupta@live.com', address='kanpur'
        }

        self.invalid_payload = {
            name='Suvesh1', age=27, phone_number='805097750', email='suvesh@live.com', address='up'
        }

    def test_create_valid_friend(self):
        response = client.post(
            reverse('get_post_friends'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_friend(self):
        response = client.post(
            reverse('get_post_friends'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
