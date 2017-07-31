# -*- coding: utf-8 -*-

"""
This is the file place to setting the application before you try to run it!
"""

class Settings:
	def __init__(self):
		# -> Main setting.
		# Your authentication token.
		self.AUTH_TOKEN = "T7dp3QPaWXg+RNPdpxPY8VJAZBt6vqWtkIKOew/Fn+Q1yZz219iQCh/M80BIfNyiSCwp6T0w9lwCbAsjpUNEi8VnQ0cC/A3M5Ps0gKRFH2wM8WmWPqXgMvb49Z2QSw4j3QVLuxl4RSoGh5Y9WgnkogdB04t89/1O/w1cDnyilFU=" 
		
		# -> Youtube video downloader setting.
		# Integrate with your site url + the path for saving the downloaded videos.
		self.SITE_URL = "http://yoursite.com/DIRECTORY" #your address site to see the saved videos, eg: http://site.com/videos/.
		self.SITE_PATH = "YOUR_PATH" #path/directory to save the videos, eg: /home/user/public_html/videos/.
		
		# -> Welcome Message when you are accepted the invite groups.
		self.WELCOME_MESSAGE = '\
		Hai, terimakasih sudah meng-invite aku. Silahkan gunakan perintah\
		"!bothelp" untuk melihat perintah yang tersedia.'
		
		# -> Auto reply setting.
		# Replacing "simi" words to another words.
		self.REPLACEMENT_CALL = "Mbot Jinak"

		# -> Not Important setting.
		# Have another account? you can set it for your secondary account, it will called you/the others account as a boss.
		self.HERE_IAM_YOUR_BOSS = "0xffa" 