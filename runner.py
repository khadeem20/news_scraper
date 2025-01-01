from webscrapers import Sel_Scraper
import sys
import requests
from bs4 import BeautifulSoup



def runner():
    if len(sys.argv) > 1:
        #take the arguement passed to the script
        url = sys.argv[1]
        scraper= Sel_Scraper(url)
        scraper.dynamic_search_url()
        scraper.create_doc()
        scraper.finito()
    else:
        print("NO URL ENTERED!!")

     



if __name__ == "__main__":
    runner()  
    
  
    
