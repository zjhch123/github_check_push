from bs4 import BeautifulSoup
import requests
from datetime import datetime
from tkinter import *
import os

username = 'zjhch123'

notice = {
  'error': 'osascript -e \'display notification "无法获取到你今天是否已提交代码,记得提交哟~" with title "注意提交代码!"\'',
  'not': 'osascript -e \'display notification "你今天还没有在github上提交代码,记得去提交哟~" with title "注意提交代码!"\'',
  'ok': 'osascript -e \'display notification "你今天已经提交过代码了~记得每天坚持哟~" with title "很棒棒!"\'',
}
def req():
  global username
  headers = {
    'Host': 'github.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Cookie': 'tz=Asia/Shanghai'
  }
  try:
    r = requests.get('https://github.com/' + username, timeout = 5, headers = headers)  
  except BaseException as e:
    print(e)
  return r

errorTimes = 0
r = req()
while r.status_code != 200 and errorTimes < 10:
    r = req()
    errorTimes += 1
try:
  doms = BeautifulSoup(r.text, 'lxml').find_all(attrs = {'data-date': datetime.strftime(datetime.now(), '%Y-%m-%d')})
  if len(doms) == 0:
    print('too early to check!')
  else:
    count = int(doms[0]['data-count'])
    if count == 0:
      os.system(notice['not'])
    else:
      os.system(notice['ok'])
except BaseException as e:
  print(e)
  os.system(notice['error'])



