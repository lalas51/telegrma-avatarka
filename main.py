from telethon import TelegramClient, sync
from .config import *
client = TelegramClient(Банан, api_id, api_hash)
client.start()
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from datetime import datetime
from .utils import *
