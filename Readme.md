# Scraping football stats

This is a fully automated data scraper for football stats. 
Currently, only the top 5 popular football leagues, FIFA world cup, Champions league and Europa League are supported.
With updates, this might increase to include many more leagues.

To get your required dataset you need to follow the described steps:
1. Download all files into a single directory in your computer.
2. Ensure you have python 3 and above, pandas and beautifulsoup installed or just pip install.
3. Run only get-data.py file, by either using the terminal, command-prompt or your IDE.
4. Provide the following inputs:
    a. Most recent year(if thats what you need), otherwise the latest year from which you wanna start your dataset, eg: 2021
    b. Earliest year from where you want your data: eg: 2019
    Note: Please make sure your years don't exceed present year and both inputs are different
    c. Input the appropriate number associated with the leagues given in the options
    Note: You will only get 5 trials to enter the right input, make sure your input matches one of the options
5. That's all, get a snack and your data will be saved in the same directory in '.csv' format with an appropriate name.

Enjoy your analysis or ML project process with the collected data :)

It is a sweet data collection project for someone like me and would really appreciate your feedback. 
Please leave comments if you use the data set. 
