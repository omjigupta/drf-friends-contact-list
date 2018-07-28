from django.test import TestCase
from ..models import Friend


class FriendTest(TestCase):
    """ Test module for Friend model """

    def setUp(self):
        Friend.objects.create(
            name='Om Ji', age=24, phone_number='9696404453', email='omjigupta@live.com', address='kanpur')
        Friend.objects.create(
            name='Suvesh', age=23, phone_number='805097750', email='suvesh@live.com', address='kanpur')

    def test_friend_phone_number(self):
        friend_om = Friend.objects.get(name='Om Ji')
        friend_suvesh = Friend.objects.get(name='Suvesh')
        self.assertEqual(
            friend_om.get_phone_number(), "Om Ji conatct number is 9696404453.")
        self.assertEqual(
            friend_suvesh.get_phone_number(), "Suvesh conatct number is 805097750.")