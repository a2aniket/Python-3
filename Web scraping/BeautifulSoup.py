# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 09:41:13 2020

@author: ART
"""
import requests
from bs4 import BeautifulSoup

url="https://codewithharry.com"

#step 1 :Get the HTML
r=requests.get(url)
html_content=r.content
#step 2: Parse the HTML

soup= BeautifulSoup(html_content,'html.parser')
#print(soup)
#print(soup.prettify())


#step 3: HTML Tree traversal
# commonly used types of objects
#print(title)#1. tag
#print(type(title)) #2. NavigableString
#print(type(soup)) #3. Beautifilsoup
#4. comment

#get the title of the html page
title =soup.title

#get all the the paragraphs form the page
paras=soup.find_all('p')
#print(paras)


#print(soup.find('p'))  #get first element
#print(soup.find('p')['class'])  #get class of first element


#find all elements with class lead
#print(soup.find_all('p',class_="lead"))

#get the text from tags/soup
#print(soup.find("p").get_text())
#print(soup.get_text())


#get all the anchor tags from the page
anchor = soup.find_all('a')
#print(anchor)
# get all link in page
all_link=set() 
for links in anchor:
    if links.get("href") != "#":
        all_link.add("https://codewithharry.com"+links.get('href'))
print(all_link)