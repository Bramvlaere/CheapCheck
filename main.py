#MAKE SURE PYTHON IS 3.8.8


#get a product from the user
#search the 3 websites for those products
#get the correct data from those websites
#compare the products price with eachother 
# give back the cheapest together with the link to buy it 


import requests 
from bs4 import BeautifulSoup

#setting headers to avoid website security for webscrapers
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    

g_searchterm=input("Enter the item you would like the price from below please \n")
user_search='https://www.fairwaymarket.com/sm/delivery/rsid/183/results?q='+g_searchterm  #Create a variable witht the url

def getsearchpage(l_searchterm):
    url=user_search
    req = requests.get(url, headers) #go to the website and create an object req 
    soup = BeautifulSoup(req.content, 'html.parser') # create a beautifulsoup object that gets the content
    print(soup.prettify())#print the content

getsearchpage(user_search)