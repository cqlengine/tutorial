from cqlengine import management
from cqlengine.connection import setup

def connect():
    setup("127.0.0.1", "tutorial")
    management.create_keyspace("tutorial", replication_factor=1)
