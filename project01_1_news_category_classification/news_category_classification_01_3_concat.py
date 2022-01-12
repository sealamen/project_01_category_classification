import pandas as pd
import glob


# 만약 누가 실수를 했다. 이런 식으로 바꿔줄 수 있어

# df_IT = pd.read_csv(
#     './crawling/team_crawling/news_IT_1-50.csv',
#     index_col=0)
# # df_IT.columns = ['Title', 'category']
# df_IT.rename(columns={'Title':'title'}, inplace=True)
# print(df_IT.columns)
# df_IT.to_csv('./crawling/team_crawling/news_IT_1-50.csv')

data_paths = glob.glob('./crawling/team_crawling/*')
print(data_paths)

# 파일 경로들 리스트로 쭉 만들어놓고 concat해주면 되겠다. > glob함수
# print하면 경로들이 리스트로 쭉 나와

df = pd.DataFrame()
for data_path in data_paths:
    df_temp = pd.read_csv(data_path, index_col=0)
    df = pd.concat([df, df_temp])
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)
print(df.head())
print(df.tail())
print(df['category'].value_counts())
print(df.info())
# df.to_csv('./crawling/naver_news.csv', index=False)

# 그냥 읽어오면 unnamed = 0라는게 있어. 이거 없애려면 index_col = 0 주면됨
# 애초에 저장할때 index=False를 주면 index_col = 0 안줘도 되겠지.

