#importing Section
import webbrowser

#Coding Section


print('Greetings')
print('Please enter the name of the Website which you would like to open')

website = input("Caution:\n1.Please enter the name which you enter in a Address/Search Bar\n2.The website will open in your Default browser\n")


website = 'https://www.' + website

print("Opening:", website)

webbrowser.open(website)
