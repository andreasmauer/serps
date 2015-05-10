import csv
import urllib
import time
import serps_crawler
import serps_report
# as always with portable python, I have to define paths depending on environment
# in this file when i shoot the crawler and the report for example

class Controller:

	def __init__(self):

		self.keywordlist = 'kws2.csv'
		self.where = 'kws_fashionette4.csv'

		self.one_by_one()


	def one_by_one(self):

		with open(self.keywordlist, 'rb') as csvfile:

			csvfiletoread = csv.reader(csvfile, delimiter = ',')
			for row in csvfiletoread:

				# if the line is empty, it jumps to the next
				if row == '':
					continue

				# clean the free spaces from the txt & convert to nice-for-urls
				keyword = row[0].rstrip('\r\n')
				keywordquoted = urllib.quote(keyword)

				# website
				website = row[1]


				# google url
				googleurl = row[2]
				
				# for each keyword I create a Serp object and get the rankings for a website
				completeUrl = googleurl + keywordquoted

				try:
					aSerp = serps_crawler.Serp(completeUrl)

					if aSerp.http_response_code is not 200:
						ranking = 'error'
						landingPage = 'error'
						break

					else:
						ranking = aSerp.returnRanking(website)
						landingPage = aSerp.returnLandingPage(website)


				except:
					pass

				print keyword + ' ' + str(ranking) + ' ' + str(landingPage)	

				# I pass the line to the report 
				try: 


					aReport = serps_report.ToCsv([keyword, ranking, landingPage, time.strftime("%d/%m/%Y")], self.where)

				except:
					print 'error: couldnt write on the csv file'




a = Controller()
