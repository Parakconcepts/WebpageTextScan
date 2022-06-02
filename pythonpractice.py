import urllib.request
import re

xtest = urllib.request.urlopen('https://bimboilori.com/meetbi.html')

web_content = xtest.read().decode("utf-8")
    
key_word = ['God','Bimbo','kingdom','director', 'Director']
 
#s_webcontent = re.findall(r'God', web_content)
 
for words in key_word:
	print('Looking for "%s" in bimbo ilori profile page'  % words )
	
	if re.search(words, web_content):
		print('"%s" is found in the profile page' % words)
	else:
		print('"%s" is not found' % words)
