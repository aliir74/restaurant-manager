import json
import random
from django.urls import reverse
from rest_framework.test import APITestCase
from django.conf import settings
from restaurantManager.models import Restaurant, Review, User
from django.utils import timezone


class RestaurantTests(APITestCase):
    def setUp(self) -> None:
        self.username = 'ali'
        self.password = 'ali123'
        self.user = User.objects.create(username=self.username, password=self.password)
        self.restaurant = Restaurant.objects.create(business_id='aslkdja', name='aslkjdas', stars=random.random()*100,
                                                    review_cnt=random.randint(1, 100))
        self.restaurant_with_many_reviews = Restaurant.objects.create(business_id='aslksdja', name='aslkjdas')
        Review.objects.create(review_id='alkjdasd', restaurant=self.restaurant_with_many_reviews, text='asldkj',
                              stars=3, user=self.user, publish_date=timezone.now())
        Review.objects.create(review_id='l1kjl1k2', restaurant=self.restaurant_with_many_reviews, text='asldasdasdkj',
                              stars=1, user=self.user, publish_date=timezone.now())

    def test_limited_review_result(self):
        with self.settings(LIMITED_RESULT_NUMBER=1):
            response = self.client.get(reverse('restaurant-detail',
                                               kwargs={'business_id': self.restaurant_with_many_reviews.business_id}))
            js_response = json.loads(response.content)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(js_response['reviews']), settings.LIMITED_RESULT_NUMBER)

    def test_add_stars(self):
        random_float = random.randint(0, 10)/2
        old_stars = self.restaurant.stars
        old_review_cnt = self.restaurant.review_cnt
        self.restaurant.add_stars(random_float)
        new_review_cnt = old_review_cnt + 1
        new_star = (old_stars*old_review_cnt + random_float)/new_review_cnt

        self.restaurant.refresh_from_db()

        self.assertEqual(self.restaurant.stars, new_star)
        self.assertEqual(self.restaurant.review_cnt, new_review_cnt)
