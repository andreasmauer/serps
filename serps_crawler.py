import urllib2
import urllib
import os
import csv
from time import sleep
import random
import sys


### the class Serp
###    it is about a single Serp (10 results for a query)
###    as input it has the url (http://www.google.de/search?hl=de&q=kontaktlinsen)
###    as instance variable has url, html, http_response_code, links
###	   as functions:
###		 - htmlcrawler, just get the html and send it to the self.html variable
###      - find_seo_links, send the links to self.links
###		 - show, write the links on the console & on a csv - for testing
###		 - shooter, for testing, it shoot all those functions

###	to do:
###		adding SEM links, adding shopping, images
### IMPORTANT:
### I NEED TO LAUNCH THE HTML CRAWLER JUST ONCE PER QUERY. IT IS LAUNCHED ON __INIT__


class Serp:

	def __init__ (self, url):

		self.html = ''
		self.http_response_code = ''
		self.url = url
		self.links = []
		self.htmlcrawler()



	def htmlcrawler (self):


		# I NEED TO LAUNCH THE HTML CRAWLER JUST ONCE PER QUERY. IT IS LAUNCHED ON __INIT__
		#print self.url
			
		# create a random sleep time between 0.5 secs and 1.5
		randomfloat = random.uniform(0, 0.5)
		sleep(randomfloat)
		request = urllib2.Request(self.url)

		request.add_header("User-Agent", "")
		opener = urllib2.build_opener()

		try: 
			response = opener.open(request)
			self.html = response.read()
			self.http_response_code = response.getcode()

		except:
			print 'crawlwer error: htmlcrawler open didnt work'




	def printHtml (self):
		print self.html

	def getHtmlOnFile(self, where):
		with open(where, 'ab') as text_file:
			text_file.write(self.html)


	def find_seo_links (self):


		# splitting the html code in order to get the clean links
		
		links = self.html.split('<li class="g">')

		for link in links[1:]:
			subitem = link.split('<a href="')
			subsubitem = subitem[1].split('&amp')

		
		# cleaning the response, changing weird urls for utf8

			s = subsubitem[0].replace('/url?q=', '')
			s = urllib.unquote(s).decode('utf8')

		# sending the links to the list self.links	
			self.links.append(s)

	def returnRanking (self, website):

		# as long as I have no information then is unknown
		ranking = '>10'

		if self.links == []:
			self.find_seo_links()

		i = 1
		for link in self.links:
			
			if website in link:

				ranking = i

				break

			i = i + 1

		return ranking
	
		
	
	def returnLandingPage(self, website):

		landingPage = '>10'
		
		if self.links == []:
			self.find_seo_links()

		for link in self.links:

			if website in link:

				landingPage = link
				break

		return landingPage

	def returnLinks(self):

		if self.find_seo_links() == []:
			self.find_seo_links()

		return self.links









				








