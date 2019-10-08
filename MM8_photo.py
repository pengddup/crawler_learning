#地址是同事提供，只爬取封面图片
#地址：http://www.mm8mm88.com/xiuren/list-1.html

from bs4 import BeautifulSoup
import requests
import os
import time

os.mkdir(r'D:\fuli3')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"}
print('福利正在传送~')

_url = 'http://www.mm8mm88.com/xiuren/list-{page}.html'
urls = [_url.format(page=page) for page in range(1, 109)]



for i in urls:
    req = requests.get(url=i, headers=headers)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'html.parser')
    targets_url = bf.find('div', class_='wb_listbox').find_all('div', class_='wb_ppic')
    # print(targets_url)

    for i in targets_url:

        tag_a = i.find('img')

        photo = tag_a['src']

        name =tag_a['alt']+'.jpg'



        path = r'D:\fuli3'

        file_name = path + '\\' + name

        try:
            req1 =requests.get(photo,headers=headers)

            f =open(file_name,'wb')

            f.write(req1.content)

            f.close()

        except:
            print('有问题')

print('福利已经发送到你的D盘fuli文件夹了')

print('3秒后自动关闭')

time.sleep(3)