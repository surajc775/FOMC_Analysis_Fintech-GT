from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import urllib.request
import re
import os
import requests
from bs4 import BeautifulSoup

# automatic chromedriver installation
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

from util import folder_check

historical_docs = 'https://www.federalreserve.gov/monetarypolicy/fomc_historical_year.htm'  # Historical documents site

driver = webdriver.Chrome()  #define which browser you are going to be using, I will use Chrome
driver.get(historical_docs)  #navigate to the proper url

#dictionary holding word to year mappings
beige = {}

#method that will take in the url for a specific year, and then scrape documents from the months in that year
def getLinksForYear(year, dir):
	url = driver.find_element_by_link_text(str(year)).get_attribute('href')
	#go to url for that year
	driver.get(url)


	#some years do not have a pdf for its beige books, so must get the url of html page instead
	if year < 2009 and year > 2002:
		b = driver.find_elements_by_partial_link_text('Beige Book')
		beige_books = [i.get_attribute('href') for i in b]
		
		for u in beige_books:
			res = requests.get(u)
			html_page = res.content

			soup = BeautifulSoup(html_page, 'html.parser')
		
		
			text = soup.find_all(text=True)

			for t in text:
				beige[t] = year


	#find all the links by looking for urls that have keyword 'pdf' in them
	d = driver.find_elements_by_partial_link_text('PDF')
	docuList = [i.get_attribute('href') for i in d]
	
	#for each pdf link found, use requests library to download it into your working directory
	for link in docuList:
		temp = link
		ind = temp.rfind('/')
		foldername = os.path.join(data_dir, str(year))
		folder_check(foldername)
		filename = os.path.join(foldername, link[ind+1::])
		download_file(link, filename)
		
#method to download pdf file using its url
def download_file(download_url, filename):
	print(filename)
	file = str(filename)
	response = urllib.request.urlopen(download_url)    
	file = open(filename, 'wb+')
	file.write(response.read())
	file.close()

if __name__ == '__main__':
	#take user input for which years they want to scrape from
	val = input("Enter how many years you want to go back from 2013, with a minimum of 1 and a maximum of 27:\t") 
	years = int(val)

	data_dir = os.path.join("data", "pdfs")  # Directory for all documents
	folder_check(data_dir)

	for y in range((2014 - years), 2014)[::-1]:
		getLinksForYear(y, data_dir)
		driver.back()
