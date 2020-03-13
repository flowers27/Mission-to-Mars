from bs4 import BeautifulSoup 
from splinter import Browser
import os
import pandas as pd
from time import sleep
from selenium import webdriver
import requests

def init_browser():
    executable_path = {'executable_path':'C:\Drivers\Webdriver\chromedriver_win32\chromedriver'}
    return Browser('chrome', **executable_path, headless = False)


def scrape():
    browser = init_browser()
    mars_data = {}
    words = {}
    nasa_url = ('https://mars.nasa.gov/news/')
    response = requests.get(nasa_url)
    soup =BeautifulSoup(response.text, 'lxml')
    while not browser.is_element_not_present_by_tag("div", wait_time=5):pass
    words = {}
    titles = soup.find_all('div', class_ ="content_title")    
    news = soup.find('div', class_ = 'content_title').text
    news_paragraph = soup.find('div', class_ ='rollover_description_inner').get_text()
    words['news_title'] = news
    words['news_paragraph'] = news_paragraph

    # mars_data['news_date'] = news_date
    
    jpl_url = ('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
    browser.visit(jpl_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    main_url = "https://www.jpl.nasa.gov" 
    featured_image_url = soup.find("article")["style"].replace("background_image: url(","").replace(");", "")[1:1]

    featured_image_url = main_url + featured_image_url
    
    tweet_url = ('https://twitter.com/marswxreport?lang=en')
    response = requests.get(tweet_url)
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

    base_hemisphere_url = "https://astrogeology.usgs.gov"
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    main_url = soup.find_all('div', class_='item')
    hemisphere_image_urls = []
    titles = []


    for photo in main_url:
        title = photo.find('h3').text
        url = photo.find('a')['href']
        space_hemisphere_url = base_hemisphere_url + url
    
    browser.visit(space_hemisphere_url)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    hemispheres_images = soup.find('div', class_='downloads')
    hemisphere_image_url = hemispheres_images.find('a')['href']
         
    img_data = dict({'title': title, 'img_url':hemisphere_image_url})
    hemisphere_image_urls.append(img_data)
    
    mars_data["hemisphere_image_urls"] = hemisphere_image_urls
    
    return mars_data





    
