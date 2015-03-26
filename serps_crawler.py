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
		#self.db_object = db_object
		self.htmlcrawler()



	def htmlcrawler (self):

		# I NEED TO LAUNCH THE HTML CRAWLER JUST ONCE PER QUERY. IT IS LAUNCHED ON __INIT__
		#print self.url
			
		# create a random sleep time between 0.5 secs and 1.5
		randomfloat = random.uniform(0.5, 1.5)
		sleep(randomfloat)
			
		request = urllib2.Request(self.url)
		request.add_header("User-Agent", "My Python Crawler")
		opener = urllib2.build_opener()
		response = opener.open(request)
		self.html = response.read()
		self.http_response_code = response.getcode()


		# security
		# print self.http_response_code
		# if self.http_response_code is not 200:
		# 	print 'superalert: google not giving 200 for keyword ' + self.url
		# 	sys.exit()


	def printHtml (self):
		print self.html

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

		if self.find_seo_links() == []:
			self.find_seo_links()

		i = 1
		for link in self.links:

			if website in link:

				ranking = i

				return ranking

				break

			i = i + 1
	
		
	
	def returnLandingPage(self, website):
		
		if self.find_seo_links() == []:
			self.find_seo_links()

		for link in self.links:

			if website in link:

				return link

				break

	def returnLinks(self):

		if self.find_seo_links() == []:
			self.find_seo_links()

		return self.links




class Bluelinks():

	def __init__ (self, keyword_list):
		
		self.keyword_list = keyword_list
		self.websites_with_rankings = []
		self.get_rankings()

	def get_rankings(self):

		with open(self.keyword_list, 'rb') as csvfile:

			csvfiletoread = csv.reader(csvfile, delimiter = ',')
			for row in csvfiletoread:

				# if the line is empty, it jumps to the next
				if row == '':
					continue

				# clean the free spaces from the txt & convert to nice-for-urls
				keyword = row[0].rstrip('\r\n')
				keyword = urllib.quote(keyword)

				# website
				website = row[1]

				# google url
				googleurl = row[2]
				
				# for each keyword I create a Serp object and get the rankings for a website
				completeUrl = googleurl + keyword

				try:
					aSerp = Serp(completeUrl)
					ranking = aSerp.returnRanking(website)
					landingPage = aSerp.returnLandingPage(website)
				except:
					ranking = 'error'
					landingPage = 'error'
					pass





				# now the keyword is again a nice one not for URLs
				keyword = urllib.unquote(keyword)

				website_with_ranking_to_list = [keyword, ranking, landingPage, aSerp.http_response_code]
				self.websites_with_rankings.append(website_with_ranking_to_list)

				# give feedback to user in console
				print keyword + " " + str(ranking) 
			








				








