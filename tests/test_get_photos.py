from unittest import TestCase
from models.users import User, Photo, Video, Content


class GetPhotosTest(TestCase):
    def test_get_photos(self):
        user = User.create(name="Jon Haddad")
        photo = Photo.create(user_id=user.user_id,
                             name="Profile Photo",
                             url="https://pbs.twimg.com/profile_images/378800000375781556/2c9dedfd19613c88248d621cbe604857_400x400.jpeg")

        photos = Photo.objects(user_id=user.user_id)

        assert len(photos) == 1


def test_clustering():
    me = User.create(name="Jon")
    for x in range(10):
        Photo.create(user_id=me.user_id, name=str(x))

    for x in Photo.objects(user_id=me.user_id):
        print x.name

def test_polymorphism():
    me = User.create(name="pete")
    Photo.create(user_id=me.user_id, name="sunset")
    Video.create(user_id=me.user_id, name="kickball")

    for content in Video.objects(user_id=me.user_id):
        print content
