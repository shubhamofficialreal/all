import json
import os


def get_user_list(config, key):
    with open("{}/Razerbot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    API_ID = 27899654  # integer value, dont use ""
    API_HASH = "644a291c69677a2fd785c43455b1df08"
    TOKEN = "5921690368:AAHri6jwz184gY8KPcKu_KDAepEJSRNyPEI"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    BOT_USERNAME = "MeTimeXUnlimitedMe_Bot"
    BOT_NAME = "𝘔𝘦𝘛𝘪𝘮𝘦𝘟𝘜𝘯𝘭𝘪𝘮𝘪𝘵𝘦𝘥𝘔𝘌🌸🧿"
    BOT_ID = "5921690368"
    OWNER_ID = 5327883761  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "@blazeshubham"
    START_IMG = "https://graph.org/file/b357032c74b0929f53a6f.jpg"
    ALIVE_IMG = "https://graph.org/file/b357032c74b0929f53a6f.jpg"
    UPDATE_CHANNEL = "blazerocks" # Your own channel for updates, do not add the @
    SUPPORT_CHAT = "blazekidschat"  # Your own group for support, do not add the @
    JOIN_LOGGER = (-1001852420702)  # A new channel ID To log who started the bot. Starting with "-100", Put inside braces
    EVENT_LOGS = (-1001852420702)  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    MONGO_DB_URI = "mongodb+srv://blazeshubham:shubham@cluster0.vftwypv.mongodb.net/?retryWrites=true&w=majority" 
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:yaaNKkIoojIPNbLciJqL@containers-us-west-106.railway.app:6086/railway"  # needed for any database module
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "HgDfUWJdRME3aIxMITgwYAB6aIePpp90fP6nBlVcNXmdwQJv1nphYVEFAauzyXmM"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    TEMP_DOWNLOAD_DIRECTORY = "./"
    
    # OPTIONAL
    DRAGONS = []  ##List of integer ids separated by "," for users which have sudo access to the bot.
    DEV_USERS = [] ##List of integer ids separated by ","  for developers who will have the same perms as the owner
    DEMONS = [] ##List of integer ids separated by ","  for users which are allowed to gban, but can also be banned.
    TIGERS = [] ##List of integer ids separated by ","  for users which WONT be banned/kicked by the bot.
    WOLVES = []
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (8)  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    OPENWEATHERMAP_ID = "63518f5e5a9daea21b22b7a2cc00694d"
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = "WM0ABTSEZI7CMNSW"  # Get your API key from https://www.alphavantage.co/support/#api-key
    IBM_WATSON_CRED_URL = ""
    IBM_WATSON_CRED_PASSWORD = ""
    TIME_API_KEY = "61173EY5C54Y"  # Get your API key from https://timezonedb.com/api
    AI_API_KEY = ""  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    ALLOW_CHATS = True
    SPAMMERS = None

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
