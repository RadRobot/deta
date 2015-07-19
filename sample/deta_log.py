from deta import Logger

conf = {
	'logfile': 'sample.log',
	'tags_on': ['CRIT', 'DEBUG_FEATURE']
}

dbg = Logger.Logger(conf['logfile'], conf['tags_on'])

dbg.log('DEBUG', "this is a debug message")
dbg.log('CRIT', "this is a critical message")
dbg.log('DEBUG_FEATURE', "this is only to be printed when we are debugging a specific feature")
