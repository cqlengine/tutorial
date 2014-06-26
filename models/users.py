
from cqlengine import *
from uuid import uuid1


class User(Model):
    user_id = UUID(primary_key=True, default=uuid1)
    name = Text()

class Photo(Model):
    # we're using a clustering key
    user_id = UUID(primary_key=True)
    photo_id = UUID(primary_key=True, default=uuid1)
    name = Text()
    url = Text()

