from dynaconf import settings
import redis


class SingletonRedis:
    __shared_instance: redis.Redis = 'redis'

    @staticmethod
    def get_instance(cls):
        if SingletonRedis.__shared_instance == 'redis':
            SingletonRedis()
        return SingletonRedis.__shared_instance

    def __init__(self):
        if SingletonRedis.__shared_instance != 'redis':
            raise Exception('This class is a singleton class.')
        else:
            SingletonRedis.__shared_instance = redis.Redis(
                host="localhost", port=settings.REDIS_PORT, password=settings.REDIS_PASSWORD, db=0)

