import vk_api
from bs4 import BeautifulSoup
import requests
import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
from typing import Final
import time
import string
import art


jokes = []
quotesnobr = []
quotes = []
quotesxx = []
bashorg2 = []



for i in range(1, 60): 
    url = 'https://www.anekdot.ru/author-best/years/?years=anekdot&page=' + str(i)
    print('Парс страницы с анекдотами: ' + url)
    r = requests.get(url)
    r.text
    soup = BeautifulSoup(r.text, 'html.parser')
    
    
    
    url2 = 'http://bashorg.org/pit/page/' + str(i)
    print(url2)
    r2 = requests.get(url2)
    soap = BeautifulSoup(r2.text, 'html.parser')
    Quotes = soap.find_all('div', class_='quote')
    for quotes in Quotes:
        bashorg2.append(quotes.text)
        

    Anegdots = soup.find_all('div', class_='text')


    
    for anegdots in Anegdots:
        jokes.append(anegdots.text)
        


session = vk_api.VkApi(token='')
sesion_api = session.get_api()
#working = True


rand = 0



while working:
    rand = random.randint(0, 8)
    if rand <= 4:
       sesion_api.wall.post(message='Анекдот: ' + jokes[random.randint(1, len(jokes))], owner_id="-217908862", from_group=0)
    else:
       sesion_api.wall.post(message='Цитата для мамантов: ' + bashorg2[random.randint(1, len(bashorg2))], owner_id="-217908862", from_group=0)
    
    time.sleep(4)

