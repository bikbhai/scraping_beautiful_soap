import requests
from bs4 import BeautifulSoup 
import re
print("hello")

WEBSITE_URL='http://auc.autoworldjapan.com/m?name=catalog&mnf_id=1&mdl_id=2'
STATIC_URL='http://auc.autoworldjapan.com/'

#---Request html page---
def get_url(website_url):
	r = requests.get(website_url)
	return r

def get_all_container_tables(soup):
	return soup.find_all("a",href=re.compile("m?name=catalog&mnf_id=1&mdl_id=2&rec="))

#---Main function---
def main():
	html_page=get_url(WEBSITE_URL)
	print(html_page.status_code)
	soup = BeautifulSoup(html_page.content, 'html.parser') 
	table_list=get_all_container_tables(soup)
	for a_tag in table_list:
		try:
			new_url=STATIC_URL+a_tag["href"]
			html_page=get_url(new_url)
			print(html_page.status_code)
		except:
			pass

#---Main function called---
if __name__=="__main__":
	main()