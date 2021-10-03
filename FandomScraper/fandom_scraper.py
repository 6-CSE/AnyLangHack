import bs4
from urllib.request import Request,urlopen as uReq, HTTPError 
from bs4 import BeautifulSoup as soup_
import re

# TODO The main URL you want to scrape , change it to your requirements
URL = 'https://callofduty.fandom.com/wiki/Category:Transcripts'

def make_soup(url):
    req=Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    uClient = uReq(req)
    page_html = uClient.read()
    uClient.close()
    soup = soup_(page_html, "lxml") 
    return soup

def scrape_text(links):
    link = links.get('href')
    # TODO Keyword to search , Change 
    if("Transcript" not in link):
        return
    # TODO The base url to be searched again , change it accordingly. Make it empty if not needed
    base_url = "https://callofduty.fandom.com"
    main_url = base_url + link
    try:
        sub_soup = make_soup(main_url)
        for para in sub_soup.findAll('p'):
            print(para.get_text())
    except HTTPError: 
        pass
    t_list = get_next_links(main_url)
    for t in t_list:
        scrape_text(t)

def get_next_links(url):
    soup = make_soup(url)
    # TODO The class of the div , para etc which will be searched for links , change it
    allLinks = soup.findAll("a" , class_='category-page__member-link')
    return allLinks

for links in get_next_links(URL):
    scrape_text(links)