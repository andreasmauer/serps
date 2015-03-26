import os
import csv



class ToCsv:

	def __init__ (self, data_to_write, where):

		self.data_to_write = data_to_write
		self.where = where

		# shoot the function to write 
		self.write_rankings()

	
	def write_rankings(self):
		
		for element in self.data_to_write:
	
			with open(self.where, 'ab') as f:
				mycsv = csv.writer(f, delimiter=',', lineterminator='\n')
				mycsv.writerow(element)







