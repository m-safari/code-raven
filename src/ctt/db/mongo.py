from pymongo import MongoClient

from ctt.config import settings

_db = MongoClient(settings.mongo_url)[settings.mongo_db]
reports = _db["reports"]  # one document per investigation; add "traces", "raw_events" later
