from splinter import Browser, driver
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime as dt
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    mars_dict = {}

    url = "https://redplanetscience.com/"
    browser.visit(url)
    html  = browser.html
    soup = BeautifulSoup(html, "html.parser")
    news_title = soup.find("div", class_ = "content_title").text
    news_p = soup.find("div", class_ = "article_teaser_body").text

    url2 = ("https://spaceimages-mars.com/")
    browser.visit(url2)
    html2 = browser.html
    soup2 = BeautifulSoup(html2, "html.parser")
    header = soup2.find('div', class_ = "header")
    browser.links.find_by_partial_text('FULL IMAGE').click()
    html2 = browser.html
    soup2 = BeautifulSoup(html2, 'html.parser')
    image = soup2.find('img', class_= 'headerimage fade-in').get('src')
    featured_image_url = ("https://spaceimages-mars.com/"+image)

    url3 = "https://galaxyfacts-mars.com/"
    mars_facts = pd.read_html(url3)
    mars_facts_df = mars_facts[0]
    mars_facts_df = mars_facts_df.rename(columns={0: " ", 1: "Mars" , 2: "Earth"})
    mars_html = mars_facts_df.to_html()
    mars_html = mars_html.replace("\n", "")

    url4 = "https://marshemispheres.com/"
    browser.visit(url4)
    html4 = browser.html
    soup4 = BeautifulSoup(html4, "html.parser")
    hemispheres = soup.find_all("div", class_="item")
    hemispheres_info = []
    url4 = "https://marshemispheres.com/"

    
    for x in hemispheres:
        titles = x.find("h3").text
        images = x.find("a", class_="itemLink product-item")["href"]
        browser.visit(url4 + images)
        html4 = browser.html
        soup4 = BeautifulSoup(html4, "html.parser")
        images_url = url4 + soup4.find('img', class__= 'wide-image')['src']
        hemispheres_info.append({"title" : titles, "images_url": images_url})
    
    
    mars_dict = {
    "news_title" : news_title,
    "news_paragraph" : news_p,
    "featured_image_url" : featured_image_url,
    "mars_facts" : mars_html,
    "hemisphere_images" : hemispheres_info
    }

    
    browser.quit()
    return mars_dict
        

        


