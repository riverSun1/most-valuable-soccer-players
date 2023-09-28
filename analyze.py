import pandas as pd

# 저장된 엑셀 파일을 불러와서 분석하기
pd.read_excel('transfermakt_utf8.xlsx')

# 데이터프레임을 df에 저장하기
df = pd.read_excel('./transfermakt_utf8.xlsx')

df['value'] = df['value'].str.replace('€', '')
df['value'] = df['value'].str.replace('m', '').astype('float')

df['시장가치(억)'] = df['value']*13

# 선수들이 속한 가장 많은 나라는? 최빈값 mode()
print(df['nation'].mode())

# 팀별 시장가치(억) 총합
g = df.groupby('team')
print(g['시장가치(억)'].sum().sort_values(ascending=False))

# 나라별 시장가치(억) 총합
g = df.groupby('nation')
print(g['시장가치(억)'].sum().sort_values(ascending=False))