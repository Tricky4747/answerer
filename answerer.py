# import module
import requests 
import bs4 
import webbrowser

print("\n                                                      \n _____ _          _____                               \n|_   _| |_ ___   |  _  |___ ___ _ _ _ ___ ___ ___ ___ \n  | | |   | -_|  |     |   |_ -| | | | -_|  _| -_|  _|\n  |_| |_|_|___|  |__|__|_|_|___|_____|___|_| |___|_|  \n                                                      \n")
query = input("What do you wanna search: ")

url = "https://google.com/search?q=" + query

request_result = requests.get( url )
  
soup = bs4.BeautifulSoup( request_result.text, "html.parser" )
  
temp = soup.find( "div" , class_='BNeawe' ).text 
    
print( temp )

def webopen(url):
    webbrowser.register(
        "chrome",
        None,
        webbrowser.BackgroundBrowser(
            "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        ),
    )
    webbrowser.get("chrome").open(url)

res=input("Do you want to open the result in google? (y for yes, n for no): ")

if res == "y":
	webopen(url)
if res == "n":
	exit();
