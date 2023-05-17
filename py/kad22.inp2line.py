import requests
import subprocess
import datetime
import time
time.sleep(120)
now = datetime.datetime.now()
DATE = now.strftime('%m月%d日')

cmd = "hostname -I | cut -d\' \' -f1"
IP = subprocess.check_output(cmd, shell=True).decode("utf-8").strip()

url = "https://notify-api.line.me/api/notify"
token="FvbAeQypLxcEfwJM4T02Q6JqOqI8mtMXuGuMHesEa3D"
headers = {"Authorization":"Bearer " + token }

message = "本日" + DATE + "ラズパイのIPアドレスは " + IP + " です"
payload = {"message" : message}
r  = requests.post(url, headers = headers, params=payload)