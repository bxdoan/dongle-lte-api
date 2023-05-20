#!/usr/bin/env python3
"""
Example code on how to change info wifi the modem:
python3 change_wifi_info.py
"""
from argparse import ArgumentParser
from dongle_tle_api import Dongle


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--url', type=str)
    parser.add_argument('--username', type=str)
    parser.add_argument('--password', type=str)
    args = parser.parse_args()

    Dongle(args.url, args.username, args.password).change_ssid(ssid="NewSSID")
