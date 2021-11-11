# import module
import requests 
import bs4 

print("\n                                                      \n _____ _          _____                               \n|_   _| |_ ___   |  _  |___ ___ _ _ _ ___ ___ ___ ___ \n  | | |   | -_|  |     |   |_ -| | | | -_|  _| -_|  _|\n  |_| |_|_|___|  |__|__|_|_|___|_____|___|_| |___|_|  \n                                                      \n")
query = input("Enter the query: ")

url = "https://google.com/search?q=" + query

request_result = requests.get( url )
  
soup = bs4.BeautifulSoup( request_result.text, "html.parser" )
  
temp = soup.find( "div" , class_='BNeawe' ).text 
    
print( temp ) 