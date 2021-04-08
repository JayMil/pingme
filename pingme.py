#!/usr/bin/python

import argparse
import discord_pinger as pinger


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("message", help="Message to send")
    args = parser.parse_args()

    pingme(args.message)


def pingme(msg):
    pinger.send_ping(msg)


if __name__ == "__main__":
    main()
