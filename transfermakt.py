import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

# url1 = "https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop"
# url2 = "https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop?page=1"

# 7개 정보를 담을 빈 리스트 만들기
# number, name, position, age, nation, team, value
number = []
name = []
position = []
age = []
nation = []
team = []
value = []

for i in range(1, 3):
    url = f"https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop?page={i}"

    r = requests.get(url, headers=headers)
    # print(r.status_code) # 200이 나오면 정상

    soup = BeautifulSoup(r.content, 'html.parser') # r.content 대신 r.text도 가능
    # print(soup)

    # 선수들의 정보가 담긴 태그와 클래스 찾기
    player_info = soup.find_all('tr', class_=['odd', 'even'])

    # 첫번째 요소 확인하기
    # print(player_info[0])

    # 전체 갯수 확인하기
    # print(len(player_info)) # 25개

    # player_info에서 'td'태그만 모두 찾기
    for info in player_info:
        player = info.find_all("td")
        # print(player[0])

    # 해당 정보를 찾아서 각 리스트에 .append로 추가하기
        number.append(player[0].text)
        name.append(player[3].text)
        position.append(player[4].text)
        age.append(player[5].text)
        nation.append(player[6].img['alt'])
        team.append(player[7].img['alt'])
        value.append(player[8].text.strip()) # xa0 -> 공백제거
    time.sleep(1)

    # print(number + "\n")
    # print(name + "\n")
    # print(position + "\n")
    # print(age + "\n")
    # print(nation + "\n")
    # print(team + "\n")
    # print(str(value) + "\n")

    # pd.dataframe()으로 저장하기
df = pd.DataFrame(
    {
        "number":number,
        "name":name,
        "position":position,
        "age":age,
        "nation":nation,
        "team":team,
        "value":value
    }
)

print(df)

# .csv 파일로 저장하기
df.to_csv('transfermakt.csv', index=False)