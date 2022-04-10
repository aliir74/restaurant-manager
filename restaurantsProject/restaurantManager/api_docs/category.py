from drf_yasg.openapi import Schema, Parameter, IN_PATH, \
    TYPE_STRING, TYPE_NUMBER, TYPE_ARRAY, TYPE_INTEGER, TYPE_OBJECT, TYPE_BOOLEAN


class CategoryModelSchema:
    schema = Schema(
        type=TYPE_OBJECT,
        properties={
            'name': Schema(
                type=TYPE_STRING,
                title="Category Name",
                description="",
            ),
        },
        example={
            "name": "Breweries"
        }
    )
