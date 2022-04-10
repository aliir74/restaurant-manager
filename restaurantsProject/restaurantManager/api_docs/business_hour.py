from drf_yasg.openapi import Schema, Parameter, IN_PATH, \
    TYPE_STRING, TYPE_NUMBER, TYPE_ARRAY, TYPE_INTEGER, TYPE_OBJECT, TYPE_BOOLEAN


class BusinessHourModelSchema:
    schema = Schema(
        type=TYPE_OBJECT,
        properties={
            'day': Schema(
                type=TYPE_STRING,
                title="Week Day",
                description="Choices: Mon, Tue, Wed, Thu, Fri, Sat, Sun",
            ),
            'open_time': Schema(
                type=TYPE_STRING,
                title='Restaurant Open Time',
                description='Time Format is %H:%M:%S'
            ),
            'close_time': Schema(
                type=TYPE_STRING,
                title='Restaurant Open Time',
                description='Time Format is %H:%M:%S'
            ),
        },
        example={
            "day": "Mon",
            "open_time": "11:00:00",
            "close_time": "23:00:00"
        }
    )
