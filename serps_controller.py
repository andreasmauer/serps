import serps_crawler
import serps_report
# as always with portable python, I have to define paths depending on environment
# in this file when i shoot the crawler and the report for example

class Controller:

	def __init__(self):

		self.shoot_crawler_report()

	def shoot_crawler_report(self):

		#crawler = serps_crawler.Bluelinks('kws-celebrity.csv')
		#serps_report.ToCsv(crawler.websites_with_rankings, 'rankings_celebrity.csv')
		crawler = serps_crawler.Bluelinks('R:\\Marketing\\Channels\\SEO\\Ongoing\\Regularly - Weekly reports\\python\\Portable Python 2.7.5.1\\projects\\serps\\kws_newfooter1.csv')
                serps_report.ToCsv(crawler.websites_with_rankings, 'R:\\Marketing\\Channels\\SEO\\Ongoing\\Regularly - Weekly reports\\python\\Portable Python 2.7.5.1\\projects\\serps\\rankings4.csv')


a = Controller()
