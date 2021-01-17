import requests
import os



def sendPing(msg):
    # make secret
    urls = getHookUrl()

    print(f"Sending ping '{msg}'")


def sendMessage(url, msg):
    headers = {"content-type": "application/json"}
    content = {"content": msg}
    resp = requests.post(url, headers=headers, json=content) 
    if resp.ok:
        print("Success")
        print(resp.text)
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

