from drf_yasg.openapi import Schema, Parameter, IN_PATH, \
    TYPE_STRING, TYPE_NUMBER, TYPE_ARRAY, TYPE_INTEGER, TYPE_OBJECT, TYPE_BOOLEAN, IN_QUERY, IN_HEADER


class AuthenticationSchema:
    auth_param = Parameter('AUTHORIZATION', IN_HEADER,
                           description="You must fill this header with 'Token <your-token>'",
                           type=TYPE_STRING)


PAGINATION_PROPERTIES = {
    "count": Schema(
        type=TYPE_INTEGER,
        title="Number of Results",
    ),
    "next": Schema(
        type=TYPE_STRING,
        title="Next Page Result URL",
        description="If there isn't next page it'll be null"
    ),
    "previous": Schema(
        type=TYPE_STRING,
        title="Previous Page Result URL",
        description="If there isn't previous page it'll be null"
    ),
}
