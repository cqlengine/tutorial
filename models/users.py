
from cqlengine import *
from uuid import uuid1


class User(Model):
    user_id = UUID(primary_key=True, default=uuid1)
    name = Text()

class Photo(Model):
    # we're using a clustering key
    user_id = UUID(primary_key=True)

    # now rows inside partition are ordered by the timestamp inside the photo_id
    photo_id = TimeUUID(primary_key=True, default=uuid1, clustering_order="DESC")
    name = Text()
    url = Text()

