import compile_data as cd 
import pandas as pd
from datetime import date

def define_data_source():
    this_year = date.today().year
    c = 5
    try:
        while True:
            print("Please enter the latest season year and the earliest season year in the same order in 20XX format:")
            start_year = int(input()) 
            end_year = int(input())
            if start_year > this_year or end_year > this_year or start_year == end_year:
                print("Input is invalid, end year or start year cannot be greater than current year and both cannot be equal")
                continue
            else: break
    except ValueError:
        return "The format entered is incorrect, please enter only single year value in 20XX"
    else: 
        if start_year<end_year:
            start_year, end_year = end_year, start_year
        while True:
            print("""Please input the number as per the following:
                 FIFA World Cup: 1 
                 Premier League: 9 
                 Serie A: 11 
                 La Liga: 12 
                 Ligue 1: 13 
                 Bundesliga: 20 
                 Champions League: 8 
                 Europa League: 19""")

            league = int(input())
            leag = {1: "FIFA World Cup", 9: "Premier League", 11: "Serie A", 12: "La Liga", 13: "Ligue 1", 20: "Bundesliga", 8: "Champions League", 19: "Europa League"}
            flag = True
            r = 0
            for l in leag.keys():
                if league==l:
                    r = l
                    flag = False
                    r1 = "-".join(leag[r].split(" "))+"-Stats"
                    break
            if flag:
                c-=1
                print(f'League not available for scraping, please enter from the given options, trials remaining {c}')
                if c==0:
                    print("Script Ended, Nothing was extracted")
                    return None
                continue 
            else: break
        years = [i if start_year != end_year else start_year for i in range(start_year, end_year, -1)]
        url = f"https://fbref.com/en/comps/{r}/{start_year}-{start_year+1}/{start_year}-{start_year+1}-{r1}"

        matches = cd.collect_matches_data(url, leag[league], years)
        file_name = f'{leag[league]}-{end_year}-{start_year}_match_stats_dataset'
        matches.to_csv(f'{file_name}.csv')

        return "Data has been saved in the {file_name}.csv file"

define_data_source()