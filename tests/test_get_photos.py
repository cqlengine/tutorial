from unittest import TestCase
from models.users import User, Photo


class GetPhotosTest(TestCase):
    def test_get_photos(self):
        user = User.create(name="Jon Haddad")
        photo = Photo.create(user_id=user.user_id,
                             name="Profile Photo",
                             url="https://pbs.twimg.com/profile_images/378800000375781556/2c9dedfd19613c88248d621cbe604857_400x400.jpeg")

        photos = Photo.objects(user_id=user.user_id)

        assert len(photos) == 1



