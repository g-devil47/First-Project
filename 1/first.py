import webbrowser
def open_website(url):
    webbrowser.open(url)
https = "https://www."
website = input("What website would you like to visit?\n")
website_url = https + website
open_website(website_url)
