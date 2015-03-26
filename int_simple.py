import model

#http://www.google.de/search?hl=de&q=


class simpleInt:


	def __init__(self):
	# set the values of the variables from user input
		self.googletld = raw_input('insert the google tld (de, es, fr, co.uk): ')
		
		keyword   = raw_input('insert the keyword: ')
		#clean the keywords
		self.keyword = urllib.quote(keyword)
		

		self.language  = raw_input('insert the language: ')
		self.serp_url  = 'http://www.google.' + self.googletld + '/search?hl=' + self.language + '&q=' + self.keyword
		self.links = []
		self.Serp = ''
		self.print_links()


	def print_links(self):
		self.Serp = model.Serp(self.serp_url)
		self.links = self.Serp.returnLinks()

		i = 1
		for link in self.links:
			print i 
			print link
			i = i + 1

		print self.links
		#self.Serp.printHtml()

execute = simpleInt()
