from celery import Celery

from ctt.config import settings

celery_app = Celery(
    "ctt", broker=settings.redis_url, backend=settings.redis_url,
    include=["ctt.workers.tasks"],
)
