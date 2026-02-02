import random

def load_proxies(path="config/proxies.txt"):
    with open(path, "r", encoding="utf-8") as f:
        proxies = [line.strip() for line in f if line.strip()]
    return proxies

def pick_proxy(proxies):
    return random.choice(proxies) if proxies else None
