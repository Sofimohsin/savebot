import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7804527695:AAExHFbz9ovcWpi-rYGN_WEgukHnwzgpkgM")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25416594"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ee4361d79ef87c88bce8e111dbf562c9")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5803180946"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sofimohusin3:sofimohusin3@cluster2.icwy0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster2") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "savebot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
