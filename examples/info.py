#!/usr/bin/env python3
"""
Example code on how to get info the modem:
python3 info.py
"""
from argparse import ArgumentParser
from dongle_tle_api import Dongle
from dongle_tle_api.enums import FieldsQuery


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--url', type=str)
    parser.add_argument('--username', type=str)
    parser.add_argument('--password', type=str)
    args = parser.parse_args()

    d = Dongle(args.url, args.username, args.password)
    info = d.get_data()
    print(info)
    device_list = d.get_data(fields=FieldsQuery.WifiInfo)
    print(device_list)

