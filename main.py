import requests
import time, os
import random
from keep_alive import keep_alive

os.system("cls" if os.name == "nt" else "clear")

channel_id = 1091314051201646642 
command = "kd"
delay = 900
emojis = ["1️⃣", "2️⃣", "3️⃣"]

def karuta_solver(tk):
    session = requests.Session()
  
    print("[!] Claiming Karuta Drop with token: %s\n\n" % tk)
    headers = {"Authorization": tk,"Content-Type": "application/json"}
    data = {"content": command,"tts": False}
    r2 = session.post("https://discord.com/api/v9/channels/%s/messages" % (channel_id), headers=headers, json=data)
    if r2.status_code in (200, 201, 204):
        print("[!] Fired Command: %s" % command)
    else:
        print("Failed to fire command: %s" % command, r2.text)
        return
    time.sleep(3)
    r4 = session.get("https://discord.com/api/v9/channels/%s/messages?limit=1" % channel_id, headers=headers)
    time.sleep(1)
    if r4.status_code in (200, 201, 204):
        id = r4.json()[0]["id"]
        print("[!] Fetched Karuta's message ID:", id)
    else:
        print("Failed to fetch Karuta's message ID", r4.text)
        return
    emoji = random.choice(emojis)
    r2 = session.put(f"https://discord.com/api/v9/channels/{channel_id}/messages/{id}/reactions/{emoji}/%40me?location=Message&burst=false", headers=headers)
    if r2.status_code in (200, 201, 204):
        print("[!] Reacted to Karuta's message with emoji: %s" % emoji)
    else:
        print("Failed to react to Karuta's message with emoji: %s" % emoji, r2.text)
        return

keep_alive()
f = open("tokens.txt", "r").readlines()
for x in range(6999999999):
    for tk in f:
        karuta_solver(tk.strip())
    time.sleep(delay)
