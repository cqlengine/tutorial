#!/usr/bin/env python

import nose

import sys
import os

# more stuff here i promise
# makes the test runner work from top level
sys.path.append(os.getcwd())

from models.connection import connect
connect()

nose.run()
