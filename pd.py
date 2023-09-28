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
# < iloc와 loc 실습 >

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

# loc 조건으로 나이가 30이상인 선수의 'name'과 'value'를 가져오시오.
print(df.loc[df['age']>=30, ['name', 'value']])

# < Dataframe 정렬하기와 컬럼바꾸기 >

# 인덱스로 정렬하기 df.sort_index()
print(df.head())
print(df.sort_index().head())

# 내림차순으로 정리하기 (ascending = false)
print(df.sort_index(ascending=False)[:5])

# sort_value로 정렬하기 df.sort_value(컬럼이름)
# 나이 많은 선수 10명 보여주기
print(df.sort_values("age", ascending=False).head())

# 인덱스를 컬럼 이름으로 바꾸기 df.set_index('컬럼이름')
# number로 인덱스 바꿔보기
print(df.set_index('number').head())

# 컬럼 이름 바꾸고 저장하기 : 'team'을 'club'으로 바꾸기 위해 cheat sheet에서 검색
print(df.rename(columns= {'team':'club'}, inplace=True)) # inplace=True -> 변경된 값이 저장된다.

# 데이터 전처리(Pre-processing)
# value 값에서 불필요한 문자는 없애고 데이터 타입을 숫자형으로 바꾸기
# 어떻게? 검색해서 예) 판다스 특수문자 제거
df['value'] = df['value'].str.replace('€', '')
df['value'] = df['value'].str.replace('m', '').astype('float')
print(df['value'].head())
print(df.head())
print(df.info())

# 컬럼 생성
# 시장가치는 단위가 백만유로인데... 13을 곱해 한화로 억원으로 만들어준다.
df['시장가치(억)'] = df['value']*13
print(df.head())

# 컬럼 삭제 df.drop(columns=['컬럼이름'])
df.drop(columns=['value'], inplace=True)
print(df.head())

# < Dataframe 통계분석과 groupby() >

# 숫자형 데이터에 대한 통계
print(df.describe())

# df[컬럼이름].mean()
# 나이평균 구하기
print(df['age'].mean())

# 몸값 합계 구하기
print(df['시장가치(억)'].sum())

# 선수들이 속한 가장 많은 나라는? 최빈값 mode()
print(df['nation'].mode())

# 국적이 Brazil인 선수들은?
print(df[df['nation']=='Brazil'])

# < groupby() >
# 데이터를 그룹으로 묶어 분석
df.groupby('nation')
g = df.groupby('nation')
print(g.size())
print(g.count())

# 수치형 데이터 총량 알아보기
print(g.sum())

# 나라별 시장가치 총합
print(g['시장가치(억)'].sum())

# 선수들의 몸값의 합이 큰 클럽별로 정렬해서 보여주기
print(c = df.groupby("club"))
# c.sum()
print(df['시장가치(억)'].sum().sort_values(ascending=False))

# 빠진 값 채우기와 지우기 fillna(), dropna()