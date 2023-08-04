from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "23097696"))
API_HASH = getenv("API_HASH", "0e4f1a26757d253329b3bb46fb03ad36")

TOKEN = getenv("TOKEN")
MONGO_DB_URL = getenv("MONGO_DB_URL", None)

OWNER_ID = int(getenv("OWNER_ID", "1410593160")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/FallenAssociation")

LOGGER_ID = getenv("LOGGER_ID", "-1001596697160")
