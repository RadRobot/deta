from datetime import datetime as dt

class Logger():

	def __init__(self, logfile, tags_on):
		self.logfile = logfile
		self.tags_on = tags_on

	def log(self, level, message):
		if level in self.tags_on:
			with open(self.logfile, "a+") as f:
				f.write(str(dt.utcnow()) + ' ' + level + ': ' + message + '\n')
