from http.client import responses
from os import times_result
import httpx
from requests import Session
import random, string

def GetEmail(cookie):
    proxy = random.choice(open("proxies.txt","r").read().splitlines())
    proxymap = {
        "all": f"http://{proxy}"
    }
    requests = Session()
    headers = {
    'authority': 'tempmail.dev',
    'content-length': '0',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'accept': '*/*',
    'dnt': '1',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://tempmail.dev',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://tempmail.dev/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'PHPSESSID=' + cookie,
}
    response = requests.post('https://tempmail.dev/Email/newEmail', headers=headers, proxies=proxymap)
    return response.json()["Email"]

def GetDiscordEmail(cookie: str):
    proxy = random.choice(open("proxies.txt","r").read().splitlines())
    proxymap = {
        "all": f"http://{proxy}"
    }
    requests = Session()
    headers = {
    'authority': 'tempmail.dev',
    'content-length': '0',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'accept': '*/*',
    'dnt': '1',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://tempmail.dev',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://tempmail.dev/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'PHPSESSID=' + cookie,
}
    response = requests.post('https://tempmail.dev/Email/inbox', headers=headers, proxies=proxymap)
    try:
        return response.text.split("\\r\\n\\r\\n")[2].strip("Verify Email: ")
    except:
        return response.text