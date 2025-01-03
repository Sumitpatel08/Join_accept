from os import environ

API_ID = int(environ.get("API_ID", "20071888"))
API_HASH = environ.get("API_HASH", "1c4cb9d94b23282abd9ae2a87a521b53")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002372863759"))
ADMINS = int(environ.get("ADMINS", "7645440087"))
DB_URI = environ.get("DB_URI", "mongodb+srv://sunitverma080:p1vjMKP150rfkjoE@cluster0.2zd3t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")
