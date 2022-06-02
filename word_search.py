import urllib.request
import re

key_word = []
resource = input("Enter the Website url to search for: ")
entry_word = input("Enter the word to search on website: ")
key_word.append(entry_word)

xtest = urllib.request.urlopen(resource)

web_content = xtest.read().decode("utf-8")
    
 
#s_webcontent = re.findall(r'God', web_content)
 
for words in key_word:
	print('Looking for "%s" on "%s" '  % (words, resource))
	
	if re.search(words, web_content):
		print('"%s" is found on "%s" '  % (words, resource))
	else:
		print('"%s" is not found on "%s" '  % (words, resource))
