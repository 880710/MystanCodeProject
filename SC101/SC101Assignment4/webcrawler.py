"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
        response = requests.get(url,headers = header)
        html = response.text
        soup = BeautifulSoup(html,'html.parser')

        # ----- Write your code below this line ----- #
        tags = soup.find_all('tbody')
        male_total= 0
        female_total = 0
        for tag in tags:
            texts = tag.text.replace(',', '')
            lines = texts.splitlines()
            for line in lines:
                line = line.split()
                if len(line) == 4:
                    male_num = line[1]
                    male_total += int(male_num)
                    female_num = line[3]
                    female_total += int(female_num)
        print('male number: ',male_total)
        print('female number: ',female_total)


if __name__ == '__main__':
    main()
