import redis

try:
    # ⚠️ 必须顶格写！前面不能有空格或 Tab
    redis_client = redis.Redis(
        host='localhost',
        port=6379,
        db=0,
        decode_responses=True,
        socket_connect_timeout=2
    )
    redis_client.ping()
except Exception:
    # 连不上或没装 Redis，直接赋值为 None，绝不阻断启动
    redis_client = None
