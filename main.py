import json
import os
import random
import logging
import requests
from keep_alive import keep_alive
import threading
import websocket
from rich.console import Console
import time
import delorean
from datetime import datetime, timedelta, timezone

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s -> %(message)s",
    datefmt="%H:%M:%S",
)

class Discord(object):

    def __init__(self):
        self.tokens = []
        self.songStart = 0
        self.songEnd = 0
        self.songFinish = 0
        self.isNext = False

        with open("data/spotify_songs.json", encoding="utf8") as f:
            self.songs = json.loads(f.read())
        with open("data/config.json") as f:
            self.config = json.loads(f.read())
        with open("data/custom_status.txt", encoding="utf-8") as f:
            self.status = [i.strip() for i in f]
        with open("data/user_bios.txt", encoding="utf-8") as f:
            self.bios = [i.strip() for i in f]

        # Update here to use environment variable
        tokens_env = os.getenv("DISCORD_TOKENS")
        if tokens_env:
            self.tokens = tokens_env.split(":")
        else:
            logging.error("DISCORD_TOKENS environment variable not set.")
            return

        self.ack = json.dumps({"op": 1, "d": None})

        self.activities = {}
        self.spotifyActivities = {}
        self.vcs = []

    # Rest of the code remains unchanged
    # ...

if __name__ == "__main__":
    keep_alive()
    discord = Discord()
    tkc = 0
    for token in discord.tokens:
        tkc += 1
        print(tkc)
        threading.Thread(target=discord.connect, args=(token,)).start()
    logging.info("All tokens are online!")
    time.sleep(1000)
    os.system("kill 1")
