from django.test import TestCase
from ..models import Friend


class FriendTest(TestCase):
    """ Test module for Friend model """

    def setUp(self):
        Friend.objects.create(
            name='Om Ji', age=24, email='omji@live.com', address='kanpur')
        Friend.objects.create(
            name='Suvesh', age=23, email='suvesh@live.com', address='kanpur')

    def test_friend_email(self):
        friend_om = Friend.objects.get(name='Om Ji')
        friend_suvesh = Friend.objects.get(name='Suvesh')
        self.assertEqual(
            friend_om.get_email(), "Om Ji email address is omji@live.com .")
        self.assertEqual(
            friend_suvesh.get_email(), "Suvesh email address is suvesh1@live.com .")
