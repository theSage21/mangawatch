import requests
from bs4 import BeautifulSoup
from telegram import Bot
import json


def get_json():
    with open("watch.json", "r") as fl:
        d = json.loads(fl.read())
    return d


def set_json(d):
    with open("watch.json", "w") as fl:
        fl.write(json.dumps(d, indent=2))


def notify(title, link, token, uid):
    bot = Bot(token=token)
    bot.send_message(chat_id=uid, text=f"New title: {title}\n\n{link}")


def run():
    watch = get_json()
    root = "https://www.mangapanda.com"
    r = requests.get(root)
    soup = BeautifulSoup(r.text, "lxml")
    notified = set(watch["notified"])
    for link in soup.findAll("a", {"class": "chaptersrec"}):
        title = link.text.lower().strip()
        title_match = any([title.startswith(t) for t in watch["titles"]])
        if title_match:
            if title not in notified:
                notify(title, root + link.get("href"), watch["tg_token"], watch["uid"])
            notified.add(title)
    watch["notified"] = list(sorted(notified))
    watch["titles"] = list(sorted(watch["titles"]))
    set_json(watch)
