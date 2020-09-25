import string
from bs4 import BeautifulSoup
from selectorlib import Extractor
from PIL import Image, ImageDraw, ImageFont
from time import sleep
import requests
import json
import txt
import pandas as pd
import numpy as np

#Phan Tich lay data cua san pham them item
def Sort_data(r,item):
    soup = BeautifulSoup(r.content, "html.parser")
    title = soup.find('div', class_='rowtop')
    area_price = soup.find('div', class_='area_price')
    #hisprice = soup.find('span', class_='hisprice')
    img = soup.find('div', class_='icon-position')
    try:
        title = title.find('h1').text
        area_price=area_price.find('strong').text
        img = img.find('img').attrs['src']
        #hisprice=hisprice.text
    except:
        print("San Pham Khong Dong form")
        title=''
        area_price=''
        img=''
        #hisprice=''
    #hisprice = soup.find('span', class_='hisprice').text
    #Nếu item là latop
    if item == 1:
        index_child = soup.find('ul', class_='parameter')
        cpu = index_child.findChildren('li')[0].text
        ram = index_child.findChildren('li')[1].text
        disk = index_child.findChildren('li')[2].text
        man_hinh = index_child.findChildren('li')[3].text
        card_mh = index_child.findChildren('li')[4].text
        cong_kn = index_child.findChildren('li')[5].text
        os = index_child.findChildren('li')[6].text
        thiet_ke = index_child.findChildren('li')[7].text
        kich_thuoc = index_child.findChildren('li')[8].text
        time_of_issue = index_child.findChildren('li')[9].text
        Thong_so_kt = []
        Thong_Tin_SP = []
        Thong_so_kt.append({
            "CPU": cpu,
            "RAM": ram,
            "DISK": disk,
            "Man Hinh": man_hinh,
            "Card Man Hinh": card_mh,
            "Cong ket Noi": cong_kn,
            "HDH": os,
            "Thiet Ke": thiet_ke,
            "kich Thuoc": kich_thuoc,
            "Thoi Gian Ra Mat": time_of_issue
        })
        Thong_Tin_SP.append({
            "Ten San Pham": title,
            "Gia Sale": area_price,
            # "Gia Goc": hisprice,
            "Thong So KT": Thong_so_kt,
            "Link Anh": img
        })
        print(Thong_Tin_SP)
        df = pd.DataFrame(data=Thong_Tin_SP)
        df.to_csv("c:\\Users\\hieudv\\PycharmProjects\\crawl_data_tgdd\\latop.csv", header=True, index=False)
    #Nếu item la dien thoai
    elif item == 2:
        index_child = soup.find('ul', class_='parameter')
        index_0 = index_child.findChildren('li')[0].text
        index_1 = index_child.findChildren('li')[1].text
        index_2 = index_child.findChildren('li')[2].text
        index_3 = index_child.findChildren('li')[3].text
        index_4 = index_child.findChildren('li')[4].text
        index_5 = index_child.findChildren('li')[5].text
        index_6 = index_child.findChildren('li')[6].text
        index_7 = index_child.findChildren('li')[7].text
        index_8 = index_child.findChildren('li')[8].text
        #index_9 = index_child.findChildren('li')[9].text
        Thong_so_kt = []
        Thong_Tin_SP = []
        Thong_so_kt.append({
            index_0,
            index_1,
            index_2,
            index_3,
            index_4,
            index_5,
            index_6,
            index_7,
            index_8,
            #index_9
        })
        Thong_Tin_SP.append({
            "Ten San Pham": title,
            "Gia Sale": area_price,
            # "Gia Goc": hisprice,
            "Thong So KT": Thong_so_kt,
            "Link Anh": img
        })
        print(Thong_Tin_SP)
    else:
        return 0;
    return Thong_Tin_SP







def getlinksp(base_url,url,item): #https://www.thegioididong.com,https://www.thegioididong.com/laptop
    #req HTTP toi trang web
    response = requests.get(url)
    #resp chuan hoa html
    soup = BeautifulSoup(response.content, "html.parser")
    # print(soup)
    titles = soup.findAll('li', class_='item')
    # print(titles)
    links = [link.find('a').attrs['href'] for link in titles]
    # print(links)
    # lay link tung san pham luu vao file urls.txt
    count=0
    with open('urls.txt', 'w') as outfile:
        for link in links:
            data = base_url + link
            print("Downloading %s" % data)
            r = requests.get(data)
            Sort_data(r, item)
            #print(r)
            count= count + 1
            if data:
                # txt.dump(data, outfile)
                outfile.write(data)
                outfile.write("\n")
                # sleep(5)
                print(count)

#get data laptop
laptop=getlinksp('https://www.thegioididong.com','https://www.thegioididong.com/laptop',1)
#Get Data dien thoai di dong
dt=getlinksp('https://www.thegioididong.com','https://www.thegioididong.com/dtdd#i:3',2)#1=28 ,2,3
splist = Sort_data(r, item)
df = pd.DataFrame(data=splist)
df.to_csv("c:\\Users\\hieudv\\PycharmProjects\\crawl_data_tgdd\\dienthoai.csv", header=True, index=False)

#Test tren 1 link san pham
# r = requests.get("https://www.thegioididong.com/laptop/hp-348-g7-i3-1a0z1pa")
# # print(r)
# Sort_data(r)









