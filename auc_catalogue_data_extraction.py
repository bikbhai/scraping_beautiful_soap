import requests
from bs4 import BeautifulSoup 
import re
import pandas as pd
print("hello")

WEBSITE_URL='http://auc.autoworldjapan.com/m?name=catalog&mnf_id=1&mdl_id=2&rec=10020605'

#---Request html page---
def get_url(website_url):
	r = requests.get(website_url)
	return r

def get_all_container_tables(soup):
	return soup.find_all("table",class_="tbl_st4")

def extract_data(table_tag,table_no):
	df_list=pd.DataFrame()
	first_col=list()
	second_col=list()
	for td_tag in table_tag.find_all("span",class_="cat_st4"):
		try:
			if td_tag.find_parent("td").find_next_sibling("td").contents[0].name=="img":
				first_col.append(td_tag.get_text().strip().lower())
				second_col.append(td_tag.find_parent("td").find_next_sibling("td").contents[0]["alt"])
				#print(td_tag.get_text().strip().lower(),"--",td_tag.find_parent("td").find_next_sibling("td").contents[0]["alt"])
			else:
				first_col.append(td_tag.get_text().strip().lower())
				second_col.append(td_tag.find_parent("td").find_next_sibling("td").get_text())
				#print(td_tag.get_text().strip().lower(),"--",td_tag.find_parent("td").find_next_sibling("td").get_text())
		except:
			pass

	df_list["first_col"]=first_col
	df_list["second_col"]=second_col
	#df=df.append(df_list,ig)
	return df_list

#---Main function---
def main():
	html_page=get_url(WEBSITE_URL)
	print(html_page.status_code)
	soup = BeautifulSoup(html_page.content, 'html.parser') 
	table_list=get_all_container_tables(soup)
	df=pd.DataFrame()
	for tab_tag in range(len(table_list[0:2])):
		df_list=extract_data(table_list[tab_tag],tab_tag)
		df=df.append(df_list,ignore_index=True)

	print(df)
	'''
	for a_tag in table_list:
		try:
			new_url=STATIC_URL+a_tag["href"]
			html_page=get_url(new_url)
			print(html_page.status_code)
		except:
			pass
	'''
	
#---Main function called---
if __name__=="__main__":
	main()