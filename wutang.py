from bs4 import BeautifulSoup
import requests 

def wutangName(name): 
	url = 'http://www.mess.be/inickgenwuname.php' 
	data = {'realname': name} 

	req = requests.post(url, data) 
	soup = BeautifulSoup(req.text, "html5lib") 

	wutangName = soup.find_all('font', attrs= {'size': '2'})[0].contents[0].replace('\n', '').strip() 
	return wutangName
