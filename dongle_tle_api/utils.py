import io
import re
import string
from random import choice, randint


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
    if not any(char.islower() for char in pw):
        return False
    if not any(char.isupper() for char in pw):
        return False
    if not any(char.isdigit() for char in pw):
        return False
    return True


def get_key_obj(val, obj):
    for member in obj:
        if member.value == val:
            return member.name
    return None
