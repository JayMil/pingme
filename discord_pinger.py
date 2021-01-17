#!/usr/bin/python
import requests
import os
import logging

logging.basicConfig(filename="/var/log/pingme/pingme.log",
                    format='%(asctime)s %(levelname)s: %(message)s',
                    level=logging.DEBUG)




def sendPing(msg):
    urls = getHookUrl()
    for url in urls:
        sendMessage(url, msg)


def sendMessage(url, msg):
    logging.info(f"Sending ping '{msg}'")
    headers = {"content-type": "application/json"}
    content = {"content": msg}
    resp = requests.post(url, headers=headers, json=content) 
    if resp.ok:
        print("Success")
        logging.info(resp.text)
    else:
        print("Fail")


def getHookUrl():
    dpDir = os.path.dirname(__file__)
    urls = list()
    with open(os.path.join(dpDir, "hookurl.txt")) as f:
        for line in f.readlines():
            urls.append(line[:-1])
    return urls


if __name__ == "__main__":
    sendPing("hello");

