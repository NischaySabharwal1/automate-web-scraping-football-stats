import requests
import pandas as pd
from bs4 import BeautifulSoup
def get_data(url:str, table_name:str)->pd.DataFrame:
    data = requests.get(url)
    df = pd.read_html(data.text, match = table_name)[0]
    try: 
        df.columns.droplevel(level=0)
    except ValueError:
        return df, data.text
    else:
        df.columns = df.columns.droplevel(level=0)
        return df, data.text

        
def scrape_hyperlinks(data:str, find_this:str)->list:
    burl = "https://fbref.com"
    soup = BeautifulSoup(data, features = 'lxml')
    links = soup.find_all("a")
    links = [l.get("href") for l in links]
    links = [l for l in links if l and find_this in l]
    links = [f"{burl}{l}" for l in links]
    return links