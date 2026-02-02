SEEN_MATCH_IDS = set()
SESSION_COOKIES = None

def is_new(match_id):
    if match_id in SEEN_MATCH_IDS:
        return False
    SEEN_MATCH_IDS.add(match_id)
    return True


def set_cookies(cookies):
    global SESSION_COOKIES
    SESSION_COOKIES = cookies

def get_cookies():
    return SESSION_COOKIES
