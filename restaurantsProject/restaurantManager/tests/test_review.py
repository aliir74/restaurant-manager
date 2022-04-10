import random
from rest_framework.test import APITestCase
from restaurantManager.models import Restaurant, Review, User
from django.utils import timezone


class ReviewTests(APITestCase):
    def setUp(self) -> None:
        self.username = 'ali'
        self.password = 'ali123'
        self.user = User.objects.create(username=self.username, password=self.password)
        self.restaurant = Restaurant.objects.create(business_id='aslkdja', name='aslkjdas', stars=random.random() * 100,
                                                    review_cnt=random.randint(1, 100))

    def test_add_review(self):
        star = random.randint(0, 10)/2
        old_stars = self.restaurant.stars
        old_review_cnt = self.restaurant.review_cnt
        Review.objects.create(stars=star, restaurant=self.restaurant, text='allkjasd', user=self.user,
                              publish_date=timezone.now())
        new_review_cnt = old_review_cnt + 1
        new_star = (old_stars*old_review_cnt + star)/new_review_cnt

        self.restaurant.refresh_from_db()
        self.user.refresh_from_db()

        self.assertEqual(self.restaurant.stars, new_star)
        self.assertEqual(self.restaurant.review_cnt, new_review_cnt)
        self.assertEqual(self.user.stars_cnt, 1)
        self.assertEqual(self.user.average_stars, star)
