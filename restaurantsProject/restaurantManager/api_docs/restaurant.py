from drf_yasg.openapi import Schema, Parameter, IN_PATH, \
    TYPE_STRING, TYPE_NUMBER, TYPE_ARRAY, TYPE_INTEGER, TYPE_OBJECT, TYPE_BOOLEAN, IN_QUERY
from rest_framework import status
from restaurantManager.api_docs.business_hour import BusinessHourModelSchema
from restaurantManager.api_docs.category import CategoryModelSchema
from restaurantManager.api_docs.review import ReviewModelSchema
from restaurantManager.api_docs import PAGINATION_PROPERTIES


class RestaurantModelSchema:
    schema = Schema(
        type=TYPE_OBJECT,
        properties={
            'business_id': Schema(
                type=TYPE_STRING,
                title="Created Restaurant's Business Id",
                description="You should use this id to perform further actions on this restaurant."
            ),
            'name': Schema(
                type=TYPE_STRING,
                title='Restaurant Name',
                description=''
            ),
            'address': Schema(
                type=TYPE_STRING,
                title="Restaurant Address",
                description=''
            ),
            'city': Schema(
                type=TYPE_STRING,
                title="Restaurant City",
                description=""
            ),
            'state': Schema(
                type=TYPE_STRING,
                title="Restaurant State",
                description=""
            ),
            'postal_code': Schema(
                type=TYPE_STRING,
                title="Restaurant Postal Code",
                description=""
            ),
            'latitude': Schema(
                type=TYPE_STRING,
                title="Restaurant Location Latitude",
                description=""
            ),
            'longitude': Schema(
                type=TYPE_STRING,
                title="Restaurant Location Longitude",
                description=""
            ),
            'stars': Schema(
                type=TYPE_NUMBER,
                title="Restaurant Stars",
                description=""
            ),
            'review_cnt': Schema(
                type=TYPE_INTEGER,
                title="Number of Restaurant Reviews",
                description=""
            ),
            'is_open': Schema(
                type=TYPE_BOOLEAN,
                title="Is Restaurant Open?",
                description=""
            ),
            'attributes': Schema(
                type=TYPE_OBJECT,
                title="Restaurant Attributes",
                description="",
                properties={
                    "attr1": "value1",
                    "attr2": "value2",
                    "attrn": "valuen"
                }
            ),
            'reviews': Schema(
                type=TYPE_ARRAY,
                title="Restaurant Reviews",
                description="Five last reviews on restaurant",
                items=ReviewModelSchema.schema
            ),
            'categories': Schema(
                type=TYPE_ARRAY,
                title="Restaurant Categories",
                items=CategoryModelSchema.schema
            ),
            'business_hours': Schema(
                type=TYPE_ARRAY,
                title="Restaurant Open Hours Per Day",
                items=BusinessHourModelSchema.schema
            )
        },
        example={
            "business_id": "6iYb2HFDywm3zjuRg0shjw",
            "name": "Oskar Blues Taproom",
            "address": "921 Pearl St",
            "city": "Boulder",
            "state": "CO",
            "postal_code": "80302",
            "latitude": 40.0175444,
            "longitude": -105.2833481,
            "stars": 4.0,
            "review_cnt": 86,
            "is_open": True,
            "attributes": {
                "WiFi": "u'free'",
                "HasTV": "True",
                "Caters": "True",
                "Alcohol": "'beer_and_wine'",
                "Ambience": "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': True}",
                "HappyHour": "True",
                "NoiseLevel": "u'average'",
                "BikeParking": "True",
                "DogsAllowed": "False",
                "GoodForMeal": "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}",
                "OutdoorSeating": "True",
                "BusinessParking": "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}",
                "RestaurantsAttire": "'casual'",
                "RestaurantsTakeOut": "True",
                "RestaurantsDelivery": "None",
                "WheelchairAccessible": "True",
                "BusinessAcceptsBitcoin": "False",
                "RestaurantsPriceRange2": "2",
                "RestaurantsReservations": "False",
                "RestaurantsTableService": "True",
                "RestaurantsGoodForGroups": "True",
                "BusinessAcceptsCreditCards": "True"
            },
            "reviews": [
                {
                    "review_id": "bkHUOCicGZ856vpvcWuW7Q",
                    "username": "93z0yh-sUpGZS-cSKu6xxA",
                    "restaurant_name": "Oskar Blues Taproom",
                    "stars": 5.0,
                    "text": "Stopped in on a busy Friday night. Despite the crowd, the service was expedient and warm. \n\nThe beers here speak for themselves, so we sampled some of their taproom only offerings, and the galaxy smash was clean, tropical and sessionable.\n\nThis being said, the real star of this place is the pizza. It's a hand tossed style crust, that's the perfect mix of crispy and doughy. We ordered the special pizza (luau- bacon, pineapple and fresh jalapeño), and it was the perfect mix of fat, sweetness and heat. \n\nIf you're looking for a comfortable spot to grab a beer, and share some food with some friends on pearl, this is the place!",
                    "useful": 1,
                    "funny": 0,
                    "cool": 0,
                    "publish_date": "2018-03-04T00:59:21Z"
                },
                {
                    "review_id": "VKBc48PPwyWIUE1RhBT_8A",
                    "username": "Q_CZIvnsDHjpls-EPzzG7Q",
                    "restaurant_name": "Oskar Blues Taproom",
                    "stars": 2.0,
                    "text": "Went there about 1 PM on a Monday.  It wasn't particularly busy, and we were seated quickly.  Our drink order was taken promptly, one coke and one beer, and we didn't see our server again for 10 minutes.  I believe it was the bartender who finally brought the beer, but didn't get the coke. He then brought our second drink a few minutes later.  When we did see our server, she was  taking an order at another table, and then 5 minutes later brought those people their drinks.  Didn't see her again for another 5 minutes when she finally came back to take our order.  At that point we were more than 20 minutes into this place, and decided it wasn't worth any more waiting so we put a few bucks down and got up and left.  Very poor service.  No idea how the food is since we didn't even get our order in.  Only about the second place I had to walk out of due to extremely poor service.",
                    "useful": 0,
                    "funny": 0,
                    "cool": 0,
                    "publish_date": "2018-08-14T05:22:00Z"
                },
                {
                    "review_id": "JKNv1l7JgayZjG6nK__hXQ",
                    "username": "rqxTSFFj5fZNmabY1fmTlw",
                    "restaurant_name": "Oskar Blues Taproom",
                    "stars": 5.0,
                    "text": "This was the place the be on Friday Night! If you're looking for the best French Onion Soup in Boulder, paired with the best craft beer selection on Pearl Street. Go. Go now!",
                    "useful": 0,
                    "funny": 0,
                    "cool": 0,
                    "publish_date": "2018-03-17T14:22:48Z"
                },
                {
                    "review_id": "WNM_Oyzy6mB6n0Z9lcuZyQ",
                    "username": "vNPxlt5f50q0e2nVAScW3Q",
                    "restaurant_name": "Oskar Blues Taproom",
                    "stars": 4.0,
                    "text": "Went to this place with my family over the weekend after a hike in Boulder and it was really nice. Their patio is perfect for bringing your dog (you cannot have the dog on the patio but you can have them tied up on the other side and still have them very close to you) and also nice and big so there is lots of room on a beautiful, sunny day. Beers on tap were super cheap and they brought out samples when we weren't sure what to order. Wait staff was attentive. Everyone enjoyed their food but there was nothing special about it- typical brewery food.",
                    "useful": 0,
                    "funny": 0,
                    "cool": 0,
                    "publish_date": "2018-04-04T21:16:50Z"
                },
                {
                    "review_id": "jG4gZz5FrHyItJXz1YV9Sw",
                    "username": "eXRC79iX60xwA1UuGRuWNg",
                    "restaurant_name": "Oskar Blues Taproom",
                    "stars": 4.0,
                    "text": "Stopped on a midweek afternoon, and so glad that I did! One of the newer additions to the West End of Pearl Street, and it turns out to be a superb place to get a burger! Have been to the original Oskar Blues also, didn't disappoint. Lot of space to enjoy the restaurant and bar, plenty of indoor booths and tables, plenty of outside seating. Good atmosphere, some really fun items on the walls, and multiple giant screen televisions to stay on top of the latest games. Really appreciated the customer service from my server, Phoebe, who knew the menu, was extremely positive and professional, and could not have been better. Quick service, attention to detail. Loved my burger, cooked exactly as I requested, and the tater tots are so darn good. Liked their multiple in-house beverage options, had a great root beer! I'll definitely return!",
                    "useful": 0,
                    "funny": 0,
                    "cool": 0,
                    "publish_date": "2018-04-28T19:17:04Z"
                }
            ],
            "categories": [
                {
                    "name": "Gastropubs"
                },
                {
                    "name": "Food"
                },
                {
                    "name": "Beer Gardens"
                },
                {
                    "name": "Restaurants"
                },
                {
                    "name": "Bars"
                },
                {
                    "name": "American (Traditional)"
                },
                {
                    "name": "Beer Bar"
                },
                {
                    "name": "Nightlife"
                },
                {
                    "name": "Breweries"
                }
            ],
            "business_hours": [
                {
                    "day": "Mon",
                    "open_time": "11:00:00",
                    "close_time": "23:00:00"
                },
                {
                    "day": "Tue",
                    "open_time": "11:00:00",
                    "close_time": "23:00:00"
                },
                {
                    "day": "Wed",
                    "open_time": "11:00:00",
                    "close_time": "23:00:00"
                },
                {
                    "day": "Thu",
                    "open_time": "11:00:00",
                    "close_time": "23:00:00"
                },
                {
                    "day": "Fri",
                    "open_time": "11:00:00",
                    "close_time": "23:00:00"
                },
                {
                    "day": "Sat",
                    "open_time": "11:00:00",
                    "close_time": "23:00:00"
                },
                {
                    "day": "Sun",
                    "open_time": "11:00:00",
                    "close_time": "23:00:00"
                }
            ]
        }
    )

    business_id_param = Parameter('business_id', IN_PATH, description="Restaurant's Business Id", type=TYPE_STRING)


class GetAllRestaurant:
    RESPONSE_SCHEMA = {
        status.HTTP_200_OK: Schema(
            type=TYPE_OBJECT,
            properties=PAGINATION_PROPERTIES | {
                    "results": Schema(
                        type=TYPE_ARRAY,
                        items=RestaurantModelSchema
                    )
                }
        )
    }
    category_param = Parameter('category', IN_QUERY, description="Search all restaurant with this category if provided",
                               type=TYPE_STRING)

class GetRestaurantDetail:
    RESPONSE_SCHEMA = {
        status.HTTP_200_OK: RestaurantModelSchema
    }
    business_id_param = Parameter('business_id', IN_PATH, description="Get Restaurant Details", type=TYPE_STRING)
