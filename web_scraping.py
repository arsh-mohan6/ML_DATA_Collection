# Collecting data from the website automatically from the coding
import requests
from bs4 import BeautifulSoup
import pandas as pd
# Get the content from the website
url  = "https://quotes.toscrape.com/"
response = requests.get(url)
html = response.text

#  We take the messy text code of the webpage and break it into a structure that Python Can understood
soup = BeautifulSoup(html,'html.parser')

# Take the data that you want
quotes = [quote.text for quote in
          soup.find_all("span",class_="text")]
authors = [author.text for author in
           soup.find_all("small",class_="author")]
# Store in the Data Frame
df = pd.DataFrame({
    "Quote":quotes,
    "Author":authors
})
#Save in Csv File
df.to_csv("web_scraped_data.csv",index = False)
print("web Scraping Done!.......")
print(df)
