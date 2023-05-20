#!/usr/bin/env python3
"""
Example code on how to change info wifi the modem:
python3 info.py
"""
from argparse import ArgumentParser
from dongle_tle_api.client import Client


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--url', type=str)
    parser.add_argument('--username', type=str)
    parser.add_argument('--password', type=str)
    args = parser.parse_args()

    client = Client(args.url, args.username, args.password)
    client.change_ssid(ssid="NewSSID")
