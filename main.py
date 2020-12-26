import time
from datetime import datetime as dt

host_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
host_temp = "hosts"
redirect = "127.0.0.1"
websites = ["www.facebook.com", "facebook.com", "www.instagram.com", "instagram.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < \
            dt(dt.now().year, dt.now().month, dt.now().day, 15):
        print(1)
        with open(host_path, 'r+') as file:
            content = file.read()
            print("Working Hours")
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect + "  " + website + "\n")
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
            print("Fun Hours")
    time.sleep(5)
