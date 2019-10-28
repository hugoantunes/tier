import redis

from app.settings import REDIS_HOST, REDIS_PORT, REDIS_DB


class redisDB:

    def __init__(self):
        self.db = redis.StrictRedis(
            host=REDIS_HOST, port=REDIS_PORT, socket_connect_timeout=20, db=REDIS_DB
        )


db = redisDB().db
