import urllib.request
from bs4 import BeautifulSoup
import re
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
    url = input('Enter a website with http/https: ')
    anchor_output_file = input('Enter the file name for anchor tags (e.g., anchor_output.txt): ')
    email_output_file = input('Enter the file name for email addresses (e.g., email_output.txt): ')

    try:
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')

        # Retrieve all anchor tags and save them to the anchor_output_file
        with open(anchor_output_file, 'w') as anchor_file:
            tags = soup('a')
            for tag in tags:
                href = tag.get('href', None)
                if href:
                    anchor_file.write(href + '\n')

        # Extract and save email addresses to the email_output_file using regular expressions
        with open(email_output_file, 'w') as email_file:
            email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}'
            email_addresses = re.findall(email_pattern, str(soup))
            for email in email_addresses:
                email_file.write("Email: " + email + '\n')

        print(f"Data saved to {anchor_output_file} and {email_output_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")
