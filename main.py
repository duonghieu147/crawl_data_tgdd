import string

from bs4 import BeautifulSoup
from selectorlib import Extractor
from PIL import Image, ImageDraw, ImageFont
from time import sleep
import requests
import json
import txt

#Phan Tich lay data cua san pham
def Sort_data(r):
    soup = BeautifulSoup(r.content, "html.parser")
    title = soup.find('div', class_='rowtop').find('h1').text
    area_price = soup.find('div', class_='area_price').find('strong').text
    hisprice = soup.find('span', class_='hisprice').text
    img = soup.find('div', class_='icon-position').find('img').attrs['src']
    cpu = soup.find('li', class_='p224582 g92_94_93').find('div').text
    ram = soup.find('li', class_='p224582 g146_149_155').find('div').text
    disk = soup.find('li', class_='p224582 g184').find('div').text
    man_hinh = soup.find('li', class_='p224582 g187_189').find('div').text
    card_mh = soup.find('li', class_='p224582 g193_191').find('div').text
    cong_kn = soup.find('li', class_='p224582 g200').find('div').text
    os = soup.find('li', class_='p224582 g8599').find('div').text
    thiet_ke = soup.find('li', class_='p224582 g7903_11082').find('div').text
    kich_thuoc = soup.find('li', class_='p224582 g254_255').find('div').text
    time_of_issue = soup.find('li', class_='p224582 g22711').find('div').text
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
        "Gia Goc": hisprice,
        "Thong So KT": Thong_so_kt,
        "Link Anh": img
    })
    # print(title)
    # print(area_price)
    # print(hisprice)
    # print(cpu)
    # print(ram)
    # print(disk)
    # print(man_hinh)
    # print(card_mh)
    # print(cong_kn)
    # print(os)
    # print(thiet_ke)
    # print(kich_thuoc)
    # print(time_of_issue)
    print(Thong_Tin_SP)








def getlinksp(base_url,url):#https://www.thegioididong.com,https://www.thegioididong.com/laptop
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
    with open('urls.txt', 'w') as outfile:
        for link in links:
            data = base_url + link
            print("Downloading %s" % data)
            r = requests.get(data)
            #print(r)
            Sort_data(r)
            if data:
                # txt.dump(data, outfile)
                outfile.write(data)
                outfile.write("\n")
                # sleep(5)
                print('-------------------------------------------------------------------')


#getlinksp('https://www.thegioididong.com','https://www.thegioididong.com/laptop')

r = requests.get("https://www.thegioididong.com/laptop/hp-348-g7-i3-9pg83pa")
# print(r)
Sort_data(r)









