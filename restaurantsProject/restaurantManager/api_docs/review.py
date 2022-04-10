from drf_yasg.openapi import Schema, Parameter, IN_PATH, \
    TYPE_STRING, TYPE_NUMBER, TYPE_ARRAY, TYPE_INTEGER, TYPE_OBJECT, TYPE_BOOLEAN, IN_QUERY
from rest_framework import status
from restaurantManager.api_docs import PAGINATION_PROPERTIES


class ReviewModelSchema:
    schema = Schema(
        type=TYPE_OBJECT,
        properties={
            'review_id': Schema(
                type=TYPE_STRING,
                title="Review's Id",
                description="You should use this id to perform further actions on this review."
            ),
            'username': Schema(
                type=TYPE_STRING,
                title='Review Creator Username',
                description=''
            ),
            'restaurant_name': Schema(
                type=TYPE_STRING,
                title='Restaurant Name',
                description=''
            ),
            'stars': Schema(
                type=TYPE_NUMBER,
                title="Review Stars",
                description=''
            ),
            'text': Schema(
                type=TYPE_STRING,
                title='Review Text',
                description=''
            ),
            'useful': Schema(
                type=TYPE_NUMBER,
                title='Review Useful Vote',
                description='How many people find this review useful?'
            ),
            'funny': Schema(
                type=TYPE_NUMBER,
                title='Review Funny Vote',
                description='How many people find this review funny?'
            ),
            'cool': Schema(
                type=TYPE_NUMBER,
                title='Review Cool Vote',
                description='How many people find this review cool?'
            ),
            'publish_date': Schema(
                type=TYPE_STRING,
                title='Review Publish Date',
                description='Date format is: "%Y-%m-%d %H:%M:%S"'
            )
        },
        example={
            "review_id": "lWC-xP3rd6obsecCYsGZRg",
            "username": "ak0TdVmGKo4pwqdJSTLwWw",
            "restaurant_name": "Prides Osteria",
            "stars": 4.0,
            "text": "Apparently Prides Osteria had a rough summer as evidenced by the almost empty dining room at 6:30 on a Friday night. However new blood in the kitchen seems to have revitalized the food from other customers recent visits. Waitstaff was warm but unobtrusive. By 8 pm or so when we left the bar was full and the dining room was much more lively than it had been. Perhaps Beverly residents prefer a later seating. \n\nAfter reading the mixed reviews of late I was a little tentative over our choice but luckily there was nothing to worry about in the food department. We started with the fried dough, burrata and prosciutto which were all lovely. Then although they don't offer half portions of pasta we each ordered the entree size and split them. We chose the tagliatelle bolognese and a four cheese filled pasta in a creamy sauce with bacon, asparagus and grana frita. Both were very good. We split a secondi which was the special Berkshire pork secreto, which was described as a pork skirt steak with garlic potato purée and romanesco broccoli (incorrectly described as a romanesco sauce). Some tables received bread before the meal but for some reason we did not. \n\nManagement also seems capable for when the tenants in the apartment above began playing basketball she intervened and also comped the tables a dessert. We ordered the apple dumpling with gelato and it was also quite tasty. Portions are not huge which I particularly like because I prefer to order courses. If you are someone who orders just a meal you may leave hungry depending on you appetite. Dining room was mostly younger crowd while the bar was definitely the over 40 set. Would recommend that the naysayers return to see the improvement although I personally don't know the former glory to be able to compare. Easy access to downtown Salem without the crowds on this month of October.",
            "useful": 3,
            "funny": 1,
            "cool": 1,
            "publish_date": "2014-10-11T03:34:02Z"
        }
    )


class RestaurantReviews:
    RESPONSE_SCHEMA = {
        status.HTTP_200_OK: Schema(
            type=TYPE_OBJECT,
            properties=PAGINATION_PROPERTIES | {
                "results": Schema(
                    type=TYPE_ARRAY,
                    items=ReviewModelSchema.schema
                )
            }
        )
    }
    business_id_param = Parameter('business_id', IN_PATH, description="Get Restaurant Reviews", type=TYPE_STRING)


class GetAllReviews:
    RESPONSE_SCHEMA = {
        status.HTTP_200_OK: Schema(
            type=TYPE_OBJECT,
            properties=PAGINATION_PROPERTIES | {
                "results": Schema(
                    type=TYPE_ARRAY,
                    items=ReviewModelSchema.schema
                )
            }
        )
    }
    keyword_param = Parameter('keyword', IN_QUERY,
                              description="Search all reviews with contain this keyword if provided",
                              type=TYPE_STRING)


class GetMyReviews:
    RESPONSE_SCHEMA = {
        status.HTTP_200_OK: Schema(
            type=TYPE_OBJECT,
            properties=PAGINATION_PROPERTIES | {
                "results": Schema(
                    type=TYPE_ARRAY,
                    items=ReviewModelSchema.schema
                )
            }
        )
    }


class GetReviewDetail:
    RESPONSE_SCHEMA = {
        status.HTTP_200_OK: ReviewModelSchema.schema
    }
    review_id_param = Parameter('review_id', IN_PATH, description="Get Review Details", type=TYPE_STRING)


class AddReview:
    REQUEST_SCHEMA = Schema(
        type=TYPE_OBJECT,
        properties={
            'restaurant_id': Schema(
                type=TYPE_STRING,
                title='Restaurant Business Id',
            ),
            'stars': Schema(
                type=TYPE_NUMBER,
                title="Review Stars",
                description=''
            ),
            'text': Schema(
                type=TYPE_STRING,
                title="Review Text",
                description=""
            )
        },
        example={
            "restaurant_id": "laksjdlakjsdkljsd",
            "stars": 4.0,
            "text": "llkjaslkjlkjalksdjalksdj"
        },
        required=['restaurant_id', 'stars', 'text']
    )

    RESPONSE_SCHEMA = {
        status.HTTP_201_CREATED: Schema(
            type=TYPE_OBJECT,
            properties={
                'review_id': Schema(
                    type=TYPE_STRING,
                    title='Review Id',
                ),
                'stars': Schema(
                    type=TYPE_NUMBER,
                    title="Review Stars",
                    description=''
                ),
                'text': Schema(
                    type=TYPE_STRING,
                    title="Review Text",
                    description=""
                )
            },
            example={
                "review_id": "laksjdlakjsdkljsd",
                "stars": 4.0,
                "text": "llkjaslkjlkjalksdjalksdj"
            },
        )
    }


class DeleteReview:
    REQUEST_SCHEMA = Schema(
        type=TYPE_OBJECT,
        properties={
            'restaurant_id': Schema(
                type=TYPE_STRING,
                title='Restaurant Business Id',
            ),
            'stars': Schema(
                type=TYPE_NUMBER,
                title="Review Stars",
                description=''
            ),
            'text': Schema(
                type=TYPE_STRING,
                title="Review Text",
                description=""
            )
        },
        example={
            "restaurant_id": "laksjdlakjsdkljsd",
            "stars": 4.0,
            "text": "llkjaslkjlkjalksdjalksdj"
        },
        required=['restaurant_id', 'stars', 'text']
    )

    RESPONSE_SCHEMA = {
        status.HTTP_204_NO_CONTENT: "No Content"
    }
    review_id_param = Parameter('review_id', IN_PATH, description="Delete Review", type=TYPE_STRING)
