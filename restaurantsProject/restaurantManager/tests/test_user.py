import random
from rest_framework.test import APITestCase
from restaurantManager.models import User


class UserTests(APITestCase):
    def setUp(self) -> None:
        self.username = 'ali'
        self.password = 'ali123'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_add_stars(self):
        star = random.randint(0, 10)/2
        self.user.add_stars(star)

        self.user.refresh_from_db()

        self.assertEqual(self.user.stars, star)
        self.assertEqual(self.user.review_cnt, 1)
