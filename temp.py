import re
import requests
import time
import os,sys

def get():
    url="http://192.paul1212.sinaapp.com/qxjiesuo.php"

    r=requests.get(url)
    pattern=re.compile('[0-9a-zA-Z]{1,}\|7200')

    match=pattern.search(r.text)
    if match:
        with open('/home/php/index.htm','w') as f:
            f.write(match.group())
        print(match.group())

def autopush():
    os.system('git add .')
    os.system('git commit -m "add log"')
    os.system('git push origin master')
    
while True:
    
    # start=time.time()
    get()
    autopush()
    time.sleep(60)