#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import csv
import html5lib
from urllib.request import urlopen
import os
import requests
import csv

class profile:
    name = ''
    link = ''

# change the following variable for the address that you want to begin with
# maybe your own FB profile

initialUrl = "https://www.facebook.com/IgnacioGomezArboleda"

def scrape(aUrl):
    page = requests.get(aUrl).text
    soup = BeautifulSoup(page, 'lxml')
    similarProfiles = soup.find_all('div', class_="profileFriendsText", limit=4)
    for aProfile in reversed(similarProfiles):
        if aProfile.find_all('a', limit=1)!=[]:
            tag = aProfile.find('a')
            newProfile = profile()
            newProfile.name = aProfile.find('a').string
            newProfile.link = tag.get('href').replace("https" , "http")
            writeProfile(newProfile)
            scrape(newProfile.link)

def writeProfile(theProfile):
    with open('results.csv','a') as csvfile:
        fieldnames = ['name' , 'link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'name': theProfile.name , 'link': theProfile.link})

scrape(initialUrl)
