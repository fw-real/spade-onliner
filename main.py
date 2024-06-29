# this code is crafted with hands by nostorian | dc: @fw.nos

import os
import json
import time
import websocket
import threading
import requests
import os
import signal
from colorama import Fore
import ctypes



def warn_print(text):
    print(f"[{Fore.LIGHTBLACK_EX}{time.strftime('%H:%M:%S')}{Fore.RESET}] - {Fore.LIGHTBLACK_EX}{text}{Fore.RESET} - [{Fore.LIGHTYELLOW_EX}WARN{Fore.RESET}]")
    return

def error_print(text):
    print(f"[{Fore.LIGHTBLACK_EX}{time.strftime('%H:%M:%S')}{Fore.RESET}] - {Fore.LIGHTBLACK_EX}{text}{Fore.RESET} - [{Fore.LIGHTRED_EX}ERROR{Fore.RESET}]")
    return

def success_print(text):
    print(f"[{Fore.LIGHTBLACK_EX}{time.strftime('%H:%M:%S')}{Fore.RESET}] - {Fore.LIGHTBLACK_EX}{text}{Fore.RESET} - [{Fore.LIGHTGREEN_EX}SUCCESS{Fore.RESET}]")
    return

def info_print(text):
    print(f"[{Fore.LIGHTBLACK_EX}{time.strftime('%H:%M:%S')}{Fore.RESET}] - {Fore.LIGHTBLACK_EX}{text}{Fore.RESET} - [{Fore.LIGHTBLUE_EX}INFO{Fore.RESET}]")
    return

print_lock = threading.Lock()
stop_threads = False
given_token_count = 0
working_token_count = 0
tokens = []
working_tokens = []
lock = threading.Lock()

def token_validator_thread(token):
    global working_token_count
    try:
        r = requests.get("https://discord.com/api/v9/users/@me", headers={"authorization": token})
        with lock:
            if r.status_code == 200:
                working_tokens.append(token)
                working_token_count += 1
    except:
        pass

with open("tokens.txt", "r") as f:
    for line in f:
        tokens.append(line.strip())
given_token_count += len(tokens)

given_token_count = len(tokens)
for token in tokens:
    t = threading.Thread(target=token_validator_thread, args=(token,))
    t.start()

for thread in threading.enumerate():
    if thread != threading.current_thread():
        thread.join()


ctypes.windll.kernel32.SetConsoleTitleW(f"Spade Onliner - {given_token_count} Given, {working_token_count} Working")

def main():
    os.system("cls")
    banner = """
┏┓  ┓•      
┃┃┏┓┃┓┏┓┏┓┏┓
┗┛┛┗┗┗┛┗┗ ┛     
"""
    print(f"{Fore.RED}{banner}{Fore.RESET}")
    print(f"{Fore.LIGHTMAGENTA_EX}discord: {Fore.LIGHTCYAN_EX}fw.nos{Fore.RESET}\n\n")
    print(f"1. {Fore.LIGHTGREEN_EX} Online Tokens{Fore.RESET}")
    print(f"2. {Fore.LIGHTGREEN_EX} VC Spammer{Fore.RESET}")
    print(f"3. {Fore.LIGHTGREEN_EX} Exit Tool{Fore.RESET}\n")
    global choice
    choice = input(f"{Fore.LIGHTYELLOW_EX}Choice: {Fore.RESET}")
    if choice == "3":
        print("\n")
        warn_print("Exiting...")
        time.sleep(2)
        os._exit(0)
    try:
        global thread_amt
        thread_amt = int(input(f"{Fore.LIGHTYELLOW_EX}Threads: {Fore.RESET}"))
    except:
        print(f"{Fore.RED}Invalid data type.{Fore.RESET}")
        time.sleep(2)
        main()
    if choice == "1":
        status_choice = input(f"{Fore.LIGHTYELLOW_EX}Online/Idle/DND (o/i/d): {Fore.RESET}")
        if status_choice not in ["o", "i", "d"]:
            print(f"{Fore.RED}Invalid choice.{Fore.RESET}")
            time.sleep(2)
            main()
        else:
            global real_status
            real_status = "online" if status_choice == "o" else "idle" if status_choice == "i" else "dnd"
        print("\n")
        info_print("Starting threads...")
        time.sleep(5)
        os.system("cls")
        warn_print("Press CTRL+C to stop.")
        print("\n")
    elif choice == "2":
        global guild_id
        global channel_id
        try:
            guild_id = int(input(f"{Fore.LIGHTYELLOW_EX}Guild ID: {Fore.RESET}"))
            channel_id = int(input(f"{Fore.LIGHTYELLOW_EX}Channel ID: {Fore.RESET}"))
        except:
            print(f"{Fore.RED}Invalid data type.{Fore.RESET}")
            time.sleep(2)
            main()
        if guild_id == "" or channel_id == "":
            print(f"{Fore.RED}Invalid choice.{Fore.RESET}")
            time.sleep(2)
            main()
        print("\n")
        info_print("Starting threads...")
        time.sleep(5)
        os.system("cls")
        warn_print("Press CTRL+C to stop.")
        print("\n")
    else:
        print(f"{Fore.RED}Invalid choice.{Fore.RESET}")
        os._exit(0)


def onliner(status, token, pid):
    try:
        ua = "Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"
        r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers={"authorization": token, "User-Agent": ua, "Content-Type": "application/json"}, json={"status": status})
        ws = websocket.WebSocket()
        ws.connect("wss://gateway.discord.gg/?v=9&encoding=json", header={"Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.5", "Cache-Control": "no-cache", "Connection": "Upgrade", "Host": "gateway.discord.gg", "Origin": "https://discord.com", "Pragma": "no-cache", "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits", "Sec-WebSocket-Version": "13", "Upgrade": "websocket", "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"})
        hello = json.loads(ws.recv())
        auth = {
    "op": 2,
    "d": {
        "token": token,
        "properties": {
        "os": "Windows",
        "browser": "Discord Android",
        "device": "Discord Android",
        "referrer": "",
        "referring_domain": ""
        },
        "presence": {
            "game": {
                "name": "Spade Onliner",
                "type": 0,
                "details": "discord: nostorian"
            },
        "status": "unknown",
        "since": 0,
        "activities": [],
        "afk": False
        }
    }
    }
        ws.send(json.dumps(auth))
        res1 = json.loads(ws.recv())
        with print_lock:
            success_print(f"Logged in as {res1['d']['user']['username']}")
        while True:
            hb_data = {
                "op": 1,
                "d": {
                    "token": token
                }
            }
            ws.send(json.dumps(hb_data))
            time.sleep(hello["d"]["heartbeat_interval"] / 1000)
    except Exception as err:
        with print_lock:
            error_print(f"Invalid token: [{token[:10]}...{token[-10:]}]")
            with open("logs.txt", "a") as f:
                f.write(f"[{token[:10]}...{token[-10:]}] Encountered: {err}\n")
                f.close()

def vc_spammer(token, gid, vcid , pid):
    ua = "Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"
    r = requests.get(f"https://discord.com/api/v9/guilds/{gid}/channels", headers={"authorization": token, "User-Agent": ua, "Content-Type": "application/json"})
    r1 = requests.get(f"https://discord.com/api/v9/channels/{vcid}", headers={"authorization": token, "User-Agent": ua, "Content-Type": "application/json"})
    if r.status_code != 200:
        with print_lock:
            error_print(f"[{token[:10]}...{token[-10:]}] - Invalid guild ID: {gid}")
    elif r1.status_code != 200:
        with print_lock:
            error_print(f"[{token[:10]}...{token[-10:]}] - Invalid channel ID: {vcid}")
    else:
        try:
            ws = websocket.WebSocket()
            ws.connect("wss://gateway.discord.gg/?v=9&encoding=json", header={"Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.5", "Cache-Control": "no-cache", "Connection": "Upgrade", "Host": "gateway.discord.gg", "Origin": "https://discord.com", "Pragma": "no-cache", "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits", "Sec-WebSocket-Version": "13", "Upgrade": "websocket", "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"})
            hello = json.loads(ws.recv())
            auth = {
                "op": 2,
                "d": { 
                    "token": token,
                    "properties": {
                    "os": "Windows",
                    "browser": "Discord Android",
                    "device": "Discord Android",
                    "referrer": "",
                    "referring_domain": ""
                },
                "presence": {
                    "game": {
                        "name": "Spade Onliner",
                        "type": 0,
                        "details": "discord: nostorian"
                    },
                    "status": "unknown",
                    "since": 0,
                    "activities": [],
                "afk": False
                    }
                }
            }
            ws.send(json.dumps(auth))
            res1 = json.loads(ws.recv())
            vc_json = {
                "op": 4,
                "d": {
                    "guild_id": gid,
                    "channel_id": vcid, 
                    "self_mute": False,
                    "self_deaf": False
                }
            
            }
            ws.send(json.dumps(vc_json))
            while True:
                res2 = json.loads(ws.recv())
                if res2["t"] == "VOICE_STATE_UPDATE" and res2["d"]["user_id"] == res1["d"]["user"]["id"]:
                    auth_vc = res2["d"]["channel_id"]
                    break
            with print_lock:
                success_print(f"{res1['d']['user']['username']} joined VC ({auth_vc})")
            while True:
                hb_data = {
                    "op": 1,
                    "d": {
                        "token": token
                    }
                }
                ws.send(json.dumps(hb_data))
                time.sleep(hello["d"]["heartbeat_interval"] / 1000)
        except Exception as err:
            with print_lock:
                error_print(f"Join Failed - {token[:10]}...{token[-10:]}")
                with open("logs.txt", "a") as f:
                    f.write(f"[{token[:10]}...{token[-10:]}] Encountered: {err}\n")
                    f.close()

def run(token, pid):
    try:
        if choice == "1":
            onliner(real_status, token, pid)
        elif choice == "2":
            vc_spammer(token, guild_id, channel_id, pid)
    except KeyboardInterrupt:
        pass

def signal_handler(sig, frame):
    print("\n")
    info_print("Stopping threads...")
    time.sleep(2)
    warn_print("Exiting...")
    time.sleep(3)
    os._exit(0)

if __name__ == '__main__':
    main()
    signal.signal(signal.SIGINT, signal_handler)
    
    pids = []

    for idx, token in enumerate(working_tokens):
        pid = os.getpid() + idx + 1
        pids.append(pid)
        num2_threads = thread_amt
        for i in range(num2_threads):
            thread = threading.Thread(target=run, args=(token, pid,))
        thread.daemon = True
        thread.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        stop_threads = True
