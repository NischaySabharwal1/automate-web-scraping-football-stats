import extract_data as ed

import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
def collect_matches_data(url : str , league: str , years: list)-> pd.DataFrame:
    burl = "https://fbref.com"
    all_matches = []
    for year in years:
        data = requests.get(url)
        soup = BeautifulSoup(data.text, features= 'lxml')
        stds_table = soup.select('table.stats_table')[0]
        links = stds_table.find_all('a')
        links = [l.get('href') for l in links]
        links = [l for l in links if '/squads' in l]
        team_urls = [f"{burl}{l}" for l in links]
        
        prevseason_url = soup.select("a.prev")[0].get("href")
        url = f"{burl}{prevseason_url}"
        for team in team_urls:
            team_name = team.split('/')[-1].replace('-Stats',"").replace('-', " ")
        
            matches, d = ed.get_data(team, "Scores & Fixtures")
            link = ed.scrape_hyperlinks(d, 'all_comps/shooting/')[0]
            shooting, d = ed.get_data(link, 'Shooting')
        
            try:
                team_data = matches.merge(shooting[['Date','Sh','SoT','Dist','FK','PK','PKatt']], on = 'Date')
            except ValueError: 
                continue
        
            team_data = team_data[team_data['Comp']==league]
            team_data['year'] = year
            team_data['team'] = team_name
            all_matches.append(team_data)
            time.sleep(2)
    match_df = pd.concat(all_matches)
    match_df.columns = [column.lower() for column in match_df]
    return match_df