import pandas as pd

# 저장된 엑셀 파일을 불러와서 분석하기
pd.read_excel('transfermakt_utf8.xlsx')

# 데이터프레임을 df에 저장하기
df = pd.read_excel('./transfermakt_utf8.xlsx')

# (50, 7) 50은 행의 갯수, 7은 열의 갯수
print(df.shape)

(rows, columns) = df.shape
print(rows) # 50
print(columns) # 7

print(df.info)

# 제일 상위 데이터 몇 가지만
print(df.head)

# 제일 하위 데이터 몇 가지만
print(df.tail)

# df[:] 인덱싱
print(df[0:5]) # df.head()
print(df[10:16])

# 컬럼 이름 선택하기 df['컬럼 이름']
# 'name'만 가져와서 처음 5개만 보여주기
print(df['name'].head())

# 여러 개 컬럼 이름 선택하기 - df[]안에 리스트로 삽입
# 'number', 'name', 'nation' 정보를 보여주기
print(df[['number', 'name', 'nation']].head())

#-------------------------------------------------------
# iloc와 loc 실습

# df[0:2]와 같다. 즉, 마지막 숫자 포함X
print(df.iloc[0:2])

# loc는 인덱스 숫자(문자)를 기준으로 한다. 즉, 마지막 숫자(문자)도 포함
print(df.loc[0:2])

# 쉼표를 기준으로 행과 열 표시 df.loc[행이름, 열이름]
# 첫 번째 행의 이름이 'name'인 값
print(df.loc[0, 'name'])

# 행은 처음부터 5까지, 열은 'name', 'team', 'value'인 값
print(df.loc[0:5, ['name', 'team', 'value']])

# 조건 인덱싱
print(df['age']<=20)

# 조건 색인
print(df[df['age']<=20]) # 나이가 20 이하인 선수

# 소속팀이 토트넘인 선수
print(df[df['team']== 'Real Madrid'])