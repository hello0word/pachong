import sqlite3
import json
from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
import requests
global url 
global db 
global proxy
global test_sign
test_sign = False

def get_config():
    with open("config.json",encoding='utf-8') as f:
        setting = json.load(f)
        global url ,db ,proxy
        url = setting["url"]
        proxy = setting["proxy"]
        db = setting["datebase"]

def process():
    get_config()
    complate_url = 'http://' + url + '/story/'
    
    #配置使用本地代理,只供测试时使用
    global test_sign,proxy

    headers = {
    'Host':"www.google.com",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"
    }

    try:
        if test_sign:
            html = requests.get(complate_url,proxies = {"http":"127.0.0.1:18888"})
        else:
            html = requests.get(complate_url,headers)
    except Exception as e:
        print(e)
    finally:
        pass
    
    bsObj = BeautifulSoup(html.read())

    print(bsObj.h1)
    #conn = sqlite3.connect("test.db")
    #cursor = conn.cursor()

    #cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")


def test():
    pass


def main():
    process()
    #test()

if __name__ == '__main__':
    main()