from bs4 import BeautifulSoup
import requests
import os
import time

os.mkdir(r'D:\fuli')

if __name__ == '__main__':
    url =['https://www.2717.com/tag/649.html','https://www.2717.com/tag/649_2.html','https://www.2717.com/tag/649_3.html']
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"}
    print('福利正在传送~')

    for i in url:
        req = requests.get(url=i, headers=headers)
        req.encoding = 'GB2312'
        html = req.text
        bf = BeautifulSoup(html, 'html.parser')
        targets_url = bf.find('ul', class_='w110 oh Tag_list').find_all('a', target='_blank')

        for i in targets_url:

            tag_a = i.find('img')

            photo = tag_a['src']

            name =tag_a['alt']+'.jpg'



            path = r'D:\fuli'

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

#手记：学习很无聊，但是可以加点调味料。爬美女，爬帅哥，没有邪念，只为了更好的学技术~