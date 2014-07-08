#!/usr/bin/env python

import nose

import sys
import os

from cqlengine.management import sync_table
# more stuff here i promise
# makes the test runner work from top level
sys.path.append(os.getcwd())

from models.connection import connect


connect()

from models.users import User, Photo, Video

sync_table(User)
sync_table(Photo)
sync_table(Video)

nose.run()
