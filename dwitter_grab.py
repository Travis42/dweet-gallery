import subprocess
import time

offset = 0

f = open("dwitter.json", "a")

while True:
    subprocess.call(['curl', 'GET', f'https://www.dwitter.net/api/dweets/?limit=100&offset={offset}', '>>', 'dweets.json'], stdout=f)
    offset += 100
    time.sleep(1) 