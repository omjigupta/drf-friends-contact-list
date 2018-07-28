from django.test import TestCase
from ..models import Friend


class FriendTest(TestCase):
    """ Test module for Friend model """

    def setUp(self):
        Friend.objects.create(
            name='Om Ji', age=24, phone_number='9696114453', email='omjigupta@live.com', address='kanpur')
        Friend.objects.create(
            name='Suvesh', age=23, phone_number='8015097750', email='suvesh@live.com', address='kanpur')

    def test_friend_phone_number(self):
        friend_om = Friend.objects.get(name='Om Ji')
        friend_suvesh = Friend.objects.get(name='Suvesh')
        self.assertEqual(
            friend_om.get_phone_number(), "Om Ji contact number is 9696114453.")
        self.assertEqual(
            friend_suvesh.get_phone_number(), "Suvesh contact number is 8015097750.")
