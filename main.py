import requests
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def send_ngl_message():
    RED = '\033[31m'
    GREEN = '\033[32m'
    RESET = '\033[0m'

    ngl_username = input("ngl username: ")
    message = input("message: ")
    count = int(input("count: "))

    success_count = 0
    not_send_count = 0

    while success_count < count:
        headers = {
            'Host': 'ngl.link',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://ngl.link',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': f'https://ngl.link/{ngl_username}',
            'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = {
            'username': f'{ngl_username}',
            'question': f'{message}',
            'deviceId': '0',
            'gameSlug': '',
            'referrer': '',
        }

        response = requests.post('https://ngl.link/api/submit', headers=headers, data=data)

        if response.status_code == 200:
            not_send_count = 0
            success_count += 1
            print(GREEN + "[+]" + RESET + f"{success_count} sent")
        else:
            not_send_count += 1
            print(RED + "[-]" + RESET + " not sent")

        if not_send_count == 10:
            print(RED + "[!]" + RESET + " wait 5 seconds")
            time.sleep(5)
            not_send_count = 0
        
        clear_screen()

send_ngl()
