import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Friend
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


class GetAllFriendsTest(TestCase):
    """ Test module for GET all friends API """

    def setUp(self):
        Friend.objects.create(
            name='Om Ji', age=24, phone_number='9696404453', email='omjigupta@live.com', address='kanpur')
        Friend.objects.create(
            name='Om Ji1', age=25, phone_number='9696404454', email='omjigupta1@live.com', address='kanpur2')
        Friend.objects.create(
            name='Om Ji1', age=26, phone_number='9696404455', email='omjigupta2@live.com', address='kanpur3')


    def test_get_all_friends(self):
        # get API response
        response = client.get(reverse('get_post_friends'))
        # get data from db
        friends = Friend.objects.all()
        serializer = FriendSerializer(friends, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleFriendTest(TestCase):
    """ Test module for GET single Friend API """

    def setUp(self):
        self.omji = Friend.objects.create(
            name='Om Ji', age=24, phone_number='9696404453', email='omjigupta@live.com', address='kanpur')
        self.omji1 = Friend.objects.create(
            name='Om Ji1', age=25, phone_number='9696404454', email='omjigupta1@live.com', address='kanpur2')
        self.omji2 = Friend.objects.create(
            name='Om Ji1', age=26, phone_number='9696404455', email='omjigupta2@live.com', address='kanpur3')



    def test_get_valid_single_friend(self):
        response = client.get(
            reverse('get_delete_update_friend', kwargs={'pk': self.rambo.pk}))
        friend = Friend.objects.get(pk=self.rambo.pk)
        serializer = FriendSerializer(friend)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_friend(self):
        response = client.get(
            reverse('get_delete_update_friend', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
