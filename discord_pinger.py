#!/usr/bin/python
import requests
import os
import logging

logging.basicConfig(filename="/var/log/pingme/pingme.log",
                    format='%(asctime)s %(levelname)s: %(message)s',
                    level=logging.DEBUG)


def send_ping(msg):
    urls = __get_hook_urls()
    for url in urls:
        __send_message(url, msg)


def __send_message(url, msg):
    logging.info(f"Sending ping '{msg}'")
    headers = {"content-type": "application/json"}
    content = {"content": msg}
    resp = requests.post(url, headers=headers, json=content) 
    if resp.ok:
        logging.info(resp.text)
    else:
        logging.error(f"Failed to send message: {resp.text}")


def __get_hook_urls():
    """ Parse hookurls.txt and return list of urls """
    exe_dir = os.path.dirname(__file__)
    hookurls_path = os.path.join(exe_dir, "hookurls.txt")

    if not os.path.exists(hookurls_path):
        raise FileNotFoundError(f"hookurls.txt not found at '{hookurls_path}'")

    urls = list()
    with open(hookurls_path) as f:
        for line in f.readlines():
            urls.append(line[:-1])
    return urls


if __name__ == "__main__":
    send_ping("hello")

