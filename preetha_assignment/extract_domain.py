import re
def extract_domain(url):
    try:
        domain=re.search('.*\://(?:www.)?([^\/]+)',url)
        print(domain.group(1))
    except:
        print("please enter the valid URL")
url=input("Enter the URL: ")
extract_domain(url)
