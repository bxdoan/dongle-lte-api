import re
import requests

from dongle_lte_api.config import get_logger

logger = get_logger(__name__)


def validate_ssid(ssid : str):
    if not isinstance(ssid, str):
        return False
    elif len(ssid) > 32:
        return False
    elif len(ssid) < 5:
        return False
    elif " " in ssid:
        return False
    return True


def validate_password(pw :str):
    if not re.match(r'^[^\s]{8,63}$', pw):
        return False
    elif len(pw) > 32:
        return False
    elif len(pw) < 8:
        return False
    if not any(char.isdigit() for char in pw):
        return False
    return True


def get_key_obj(val, obj):
    for member in obj:
        if member.value == val:
            return member.name
    return None


def ip():
    ip = requests.get('https://checkip.amazonaws.com').text.strip()

    return ip
