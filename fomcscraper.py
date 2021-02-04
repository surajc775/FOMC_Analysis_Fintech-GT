from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import urllib.request
import re

#take user input for which years they want to scrape from
val = input("Enter how many years you want to go back from 2013, with a minimum of 1 and a maximum of 27 ") 

years = int(val)

#create a list to hold the years that you want to scrape from
yearsList = [i for i in range((2014 - years), 2014)]

yearsList.reverse()

#define which browser you are going to be using, I will use Chrome

driver = webdriver.Chrome()




#navigate to the proper url
driver.get('https://www.federalreserve.gov/monetarypolicy/fomc_historical_year.htm')


#get web element based on the text of the link, and grab its href attribute (the link to that years fomc documents)
year_urls = [driver.find_element_by_link_text(str(i)).get_attribute('href') for i in yearsList]











#method that will take in the url for a specific year, and then scrape documents from the months in that year
def getLinksForYear(url):
	#go to url for that year
	driver.get(url)

	#find all the links by looking for urls that have keyword 'pdf' in them
	d = driver.find_elements_by_partial_link_text('PDF')
	docuList = [i.get_attribute('href') for i in d]
	
	#for each pdf link found, use requests library to download it into your working directory
	for link in docuList:
		temp = link
		ind = temp.rfind('/')
		filename = link[ind+1::]
		download_file(link, filename)
		
		
#method to download pdf file using its url
def download_file(download_url, filename):
	print(filename)
	file = str(filename)
	response = urllib.request.urlopen(download_url)    
	file = open(filename, 'wb')
	file.write(response.read())
	file.close()
 


for link in year_urls:
	getLinksForYear(link)

