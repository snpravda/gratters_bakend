import time
import datetime
from gratters_backend.celery import app
from .models import Gratter
from gratters_backend.telethon import *


client = TelegramClient(phone, api_id, api_hash)


@app.task(name='send_messages')
def send_messages():
    client.connect()
    for obj in Gratter.objects.all():
        if obj.date == datetime.date.today():
            message = obj.message
            nickname = obj.person_to
            client.send_message(nickname, message)

# @app.task(name='work')
# def work():
#     print("it works")

