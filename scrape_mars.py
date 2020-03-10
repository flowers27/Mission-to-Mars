from bs4 import BeautifulSoup 
from splinter import Browser
import os
import pandas as pd
import time
from selenium import webdriver
import requests

def init_browser():
    executable_path = {'executable_path':'C:\Drivers\Webdriver\chromedriver_win32\chromedriver'}
    return Browser('chrome', **executable_path, headless = False)


def scrape():
    browser = init_browser()
    mars_data = {}
    words = {}
    url = ('https://mars.nasa.gov/news/')
    response = requests.get(url)
    soup =BeautifulSoup(response.text, 'lxml')
    words = {}
    titles = soup.find_all('div', class_ ="content_title")    
    news = soup.find('div', class_ = 'content_title').text
    news_paragraph = soup.find('div', class_ ='rollover_description_inner').get_text()
    words['news_title'] = news
    words['news_paragraph'] = news_paragraph

    # mars_data['news_date'] = news_date
    
    url = ('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    images = soup.find_all('a', class_='fancybox')
    pic_src = []
    for image in images:
        pic = image['data-fancybox-href']
    pic_src.append(pic)
    featured_image_url = 'https://www.jpl.nasa.gov' + pic
    mars_data['featured_image_url'] = featured_image_url

    url = ('https://twitter.com/marswxreport?lang=en')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    contents = soup.find_all('div', class_='content')
    climate = []
    for content in contents:
        mars_weather = content.find('div', class_='js-tweet-text-container').text
    climate.append(mars_weather)

    mars_url = 'https://space-facts.com/mars/'
    table_mars = pd.read_html(mars_url)
    table_mars[0]

    space = table_mars[0]
    space.columns = ['Facts', 'Value']
    space.set_index(['Facts'])
    facts_html = space.to_html()
    facts_html = facts_html.replace('\n', '')

    url = ('https://astrogeology.usgs.gov//search/map/Mars/Viking/valles_marineris_enhanced')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    valles_marineris_img = soup.find_all('div', class_='wide-image-wrapper')
    for img in valles_marineris_img:
        pic = img.find('li')
    valles_image = pic.find('a')['href']
    valles_marineris_title = soup.find('h2', class_='title').text
    valles_hemisphere = {"Title": valles_marineris_title, 'url': valles_image}

    url = ('https://astrogeology.usgs.gov//search/map/Mars/Viking/cerberus_enhanced')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    cerberus_image = soup.find_all('div', class_='wide-image-wrapper')
    for image in cerberus_image:
        pic = image.find('li')
    photo = pic.find('a')['href']
    cerberus_title = soup.find('h2', class_='title').text
    cerberus_hemisphere = {"Title": cerberus_title, 'url': photo}

    url = ('https://astrogeology.usgs.gov//search/map/Mars/Viking/schiaparelli_enhanced')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    schiaparelli_image = soup.find_all('div', class_='wide-image-wrapper')
    for image in schiaparelli_image:
        pic = image.find('li')
    photo = pic.find('a')['href']
    schiaparelli_title = soup.find('h2', class_='title').text
    schiaparelli_hemisphere = {'Title': schiaparelli_title, 'url': photo}

    url = ('https://astrogeology.usgs.gov//search/map/Mars/Viking/syrtis_major_enhanced')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    major_image = soup.find_all('div', class_='wide-image-wrapper')
    for image in major_image:
        pic = image.find('li')
    photo = pic.find('a')['href']
    syrtris_title = soup.find('h2', class_='title').text
    syrtris_hemisphere = {'Title': syrtris_title, 'url': photo}
    
    return mars_data





    
