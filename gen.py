import httpx
import requests
import random
import string
import time
from requests.models import HTTPBasicAuth
import json
import aiohttp
def get_captcha():
    captchakey = "973bdf9325894e3eb403201135a27329"
    json2 = {
        "clientKey": captchakey,
        "task":
        {
            "type": "HCaptchaTaskProxyless",
            "websiteURL": "https://discord.com/register",
            "websiteKey": "f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"
        }
    }
    r = requests.post("https://api.capmonster.cloud/createTask",
                      json=json2)  # creates task
    taskid = r.json()["taskId"]
    print(f"created task {taskid}")
    while True:
        time.sleep(5)
        json1 = {
            "clientKey": captchakey,
            "taskId": taskid
        }
        try:
            # gets the task result
            r1 = requests.post(
                "https://api.capmonster.cloud/getTaskResult", json=json1)
            part_one = r1.json()["solution"]
            captcha_key = part_one["gRecaptchaResponse"]
            print(captcha_key)
            return captcha_key
        except:
            print("not ready")
    
def finger():
    return str(requests.get("https://discord.com/api/v9/experiments").json()["fingerprint"])

def return_proxy():
    with open("proxies.txt") as f:
        a = f.read().splitlines()
        return random.choice(a)


def gen():
    proxies = return_proxy()
    proxy={"all://": f'http://{proxies}'}
    fingerprint = finger()
    cookies = {
    '__dcfduid': 'c21b20c068e511eca9a5138eebde931e',
    '__sdcfduid': 'c21b20c168e511eca9a5138eebde931ea0b4d448eda8e54f4b82506bb4f2255da9bdef91407b7ca4a800e39a33bc797c',
    }

    headers = {
    'authority': 'discord.com',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRhLURLIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkyLjAuNDUxNS4xMDcgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjkyLjAuNDUxNS4xMDciLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vd3d3LnlvdXR1YmUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cueW91dHViZS5jb20iLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTEwNjAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
    'x-fingerprint': fingerprint,
    'accept-language': 'da',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'origin': 'https://discord.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://discord.com/register',
    'cookie': '__dcfduid=68f23691ee9d14c8046ce0e1b62db35c; locale=da; OptanonConsent=isIABGlobal=false&datestamp=Sat+Jul+24+2021+02%3A27%3A37+GMT%2B0200+(Centraleurop%C3%A6isk+sommertid)&version=6.17.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0'
    }
    captcha = get_captcha()

    json = {"fingerprint":f"{fingerprint}","email":"kbdvdxdzaidrj421@gmail.com","username":"Mowervi","password":"alexisveryhotlol","invite":"ZjeWaJWe","consent":"true","date_of_birth":"2000-01-01","captcha_key":f"{captcha}"}

    response = httpx.post('https://discord.com/api/v9/auth/register', headers=headers, cookies=cookies, json=json,proxies=proxy)
    print(response.text)
gen()