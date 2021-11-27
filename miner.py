import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

print("""\
               __                               
              /  |                              
 _____  ____  $$/  _______    ______    ______  
/     \/    \ /  |/       \  /      \  /      \ 
$$$$$$ $$$$  |$$ |$$$$$$$  |/$$$$$$  |/$$$$$$  |
$$ | $$ | $$ |$$ |$$ |  $$ |$$    $$ |$$ |  $$/ 
$$ | $$ | $$ |$$ |$$ |  $$ |$$$$$$$$/ $$ |      
$$ | $$ | $$ |$$ |$$ |  $$ |$$       |$$ |      
$$/  $$/  $$/ $$/ $$/   $$/  $$$$$$$/ $$/       
------------------------------------------                                               
------------------------------------------""")

ctx = ssl.create_default_context() #ignore ssl certification error with this 3 lines
ctx.check_hostname = False
ctx.verify_mode= ssl.CERT_NONE

while True:
 url = input('enter website with http/https : ')
 html=urllib.request.urlopen(url, context=ctx).read()
 soup = BeautifulSoup(html, 'html.parser')

#Retrive all anhcor tags

 tags = soup('a')
 for tag in tags:
    print(tag.get('href', None))


