from data_config import API_ID, API_HASH, CHANNEL_ID
from pyrogram import Client

api_id = API_ID
api_hash = API_HASH
channel_id = int(CHANNEL_ID)

app = Client("Bender_pc", api_id, api_hash)
