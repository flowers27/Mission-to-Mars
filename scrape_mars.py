from bs4 import BeautifulSoup 
from splinter import Browser
import os
import pandas as pd
import time
from selenium import webdriver

def init_browser():
    executable_path = {'executable_path':'C:\Drivers\Webdriver\chromedriver_win32\chromedriver'}
    return Browser('chrome', **executable_path, headless = False)


def scrape():
    browser = init_browser()
    mars_data = {}

    url = "https://mars.nasa.gov/news/"
    Browser.visit(nasa)
    
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')


    article = soup.find('div', class_='list_text')
    news_para = article.find('div', class_='article_teaser_body').text
    news_title = article.find('div', class_='content_title').text
    news_date = article.find('div', class_='list_date').text

    # mars_data['news_date'] = news_date
    mars_data['news_title'] = news_title
    mars_data['sunnary'] = news_para

    url_mars = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    Browser.visit(url_mars)

    html = Browser.html
    soup = BeautifulSoup(html, 'lxml')
    image = soup.find('img', class_='thumb')['src']
    image_url = 'https://www.jpl.nasa.gov' +pic 
    featured_image_url = image_url

    mars_data['featured_image_url'] = featured_image_url

    url_weather = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url_weather)
    html_weather = browser.html
    soup = BeautifulSoup(html_weather, 'lxml')
    mars_weather = soup.find('p', class_='TweetTextSize--normal js-tweet-text tweet-text').text 
    mars_data['mars_weather'] = mars_weather

    mars_url = 'https://space-facts.com/mars/'
    table_mars = pd.read_html(mars_url)
    table_mars[0]

    space = table_mars[0]
    space.columns = ['Facts', 'Value']
    space.set_index(['Facts'])
    facts_html = space.to_html()
    facts_html = facts_html.replace('\n', '')
    mars_data['tabel_mars'] = facts_html
    mars_data['hemisphere_image+'] = full_hemisphere_dict

    return mars_data

def hemisphere_images():
    image_one = 'https://astrogeology.usgs.gov//search/map/Mars/Viking/valles_marineris_enhanced'
    image_two = 'https://astrogeology.usgs.gov//search/map/Mars/Viking/cerberus_enhanced'
    image_three = 'https://astrogeology.usgs.gov//search/map/Mars/Viking/schiaparelli_enhanced'
    image_four = 'https://astrogeology.usgs.gov//search/map/Mars/Viking/syrtis_major_enhanced'

    full_hemisphere_dict = {'image_one': image_one, 'image_two': image_two, 'image_three':image_three, 'image_four': image_four}
    return full_hemisphere_dict




    
