import redis
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="../../../../.env")

REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_HOST = os.getenv("REDIS_HOST", "redis")

redis_client = redis.Redis(host=REDIS_HOST, port=int(REDIS_PORT), decode_responses=True)
