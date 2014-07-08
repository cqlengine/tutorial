
from cqlengine import *
from uuid import uuid1


class User(Model):
    user_id = UUID(primary_key=True, default=uuid1)
    name = Text()

class Content(Model):
    # we're using a clustering key

    user_id = UUID(primary_key=True)

    # now rows inside partition are ordered by the timestamp inside the photo_id
    content_id = TimeUUID(primary_key=True, default=uuid1, clustering_order="DESC")
    name = Text()
    url = Text()
    content_type = Text(polymorphic_key=True, index=True)

class Photo(Content):
    __polymorphic_key__ = 'photo'
    exif = Text()

class Video(Content):
    __polymorphic_key__ = 'video'
    duration = Integer()

