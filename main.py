import requests, random, threading, string, time
from colorama import Fore
x = 1
def send():
    global x
    try:
        proxy = random.choice(open('proxies.txt', 'r').read().splitlines())
        proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
        name = "".join(random.choices(string.ascii_letters, k=7))
        surname = "".join(random.choices(string.ascii_letters, k=7))
        email = "".join(random.choices(string.ascii_letters + string.digits, k=7)) + "@gmail.com"
        password = "".join(random.choices(string.ascii_letters + string.digits , k=12))
        headers = {
            'authority': 'www.escapadarural.com',
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.escapadarural.com',
            'referer': 'https://www.escapadarural.com',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = f'traveler%5Buser_name%5D={name}&traveler%5Buser_surname%5D={surname}&traveler%5Buser_email%5D={email}&traveler%5Buser_password%5D={password}&traveler%5Buser_type%5D=traveler&traveler%5Bconditions%5D=1&traveler%5Ballow_comms%5D=1&popUpLog=1&undefined'

        response = requests.post('https://www.escapadarural.com/dynamic/popup/login/signUp', headers=headers, proxies=proxies, data=data)
        with open("accounts.txt", "a+") as f:
            f.write(f"{email}:{password}:{name}:{surname}\n")
        print(f"{Fore.LIGHTGREEN_EX}Account Created: {email}:{password}:{name}:{surname}  | {x}{Fore.RESET}")
        x += 1
    except:
        print(Fore.LIGHTRED_EX + "Error Creating the Account" + Fore.RESET)
y = 1
while True:
    if y % 300 == 0:
        print(Fore.LIGHTYELLOW_EX + "Waiting so ur not ratelimited ^^")
        time.sleep(15)
    else:
        threading.Thread(target=send).start()
    y += 1
