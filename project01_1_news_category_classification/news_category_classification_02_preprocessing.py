import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
import pickle

# ------------------------------------------------------------
# pip install konlpy가 안깔리는 경우 오라클 홈페이지에서 java se 등을 깐다
# 이 사이트를 참고할 것.https://webnautes.tistory.com/1394
# path에 자바가 있는지 확인해볼 것. 없다면 JAVA_HOME 추가하는것 따라해볼 것.
# 파이참 터미널에서  > java -version 을 쳐서 버전 확인해볼 것
#-------------------------------------------------------------
# 설정에서 tweepy가 안보이면 터미널에서 pip list로 확인해보고 버전을
# 4.3에서  > pip install tweepy==3.10.0 해서 다운해주면 설정에서도 잡힌다.
#-------------------------------------------------------------


pd.set_option('display.unicode.east_asian_width', True)

df = pd.read_csv('./crawling/naver_news.csv')

print(df.head())
print(df.info())

# 컬럼을 X와 Y로 나눔 --------------
X = df['title']
Y = df['category']
# Y에는 지금 politics,, 이런 식으로 문자열로 들어있는데 이걸 숫자로 바꾸자


# labelencoder(문자를 숫자로), onehotencoder(숫자를 0,1로)
encoder = LabelEncoder()
labeled_Y = encoder.fit_transform(Y)
label = encoder.classes_
print(labeled_Y[0])
print(label)
with open('./models/encoder.pickle', 'wb') as f:
    pickle.dump(encoder, f)
onehot_Y = to_categorical(labeled_Y)
print(onehot_Y)

# Y가 데이터프레임의 카테고리. 지금 정치, 경제, 사회, 문화 이런거 들어있어
# fit_transform으로 걔네들한테 012345 숫자를 붙여주는 것임
# Y를 라벨인코딩 해준 다음에 원핫인코딩 해준거야
# 어떤게 0이고 어떤게 1인지는 encoder가 기억
# fit_transform이 어떻게 됐는지를 보려면 classes_하면 돼. 그걸 label로 받자
# categorical을 통해서 1을 [0,1,0,0] 이런 식으로 바꿔줌.
exit()

# 형태소 분리

okt = Okt()
okt_morphs_X = okt.morphs(X[0], norm=True)                #숫자 1 등으로 바꾸면 다음 타이틀로-
# # stem=True를 주면 어간만 뽑혀나옴. 안적으면 어미도 다 나옴.norm은 정규화(normalizing).디폴트는 False
print(X[0])
print(okt_morphs_X)

# okt_pos_X = okt.pos(X[0])                               # 명사 동사 등 품사 나오는데 한글은 정확하지 않음.
## print(X[0])
## print(okt_pos_X)

# open korean tokenizer 형태소로 나눠주는 것


for i in range(len(X)):
    X[i] = okt.morphs(X[i])
print(X)
# X를 형태소로 나눔

stopwords = pd.read_csv('./crawling/stopwords.csv',
                        index_col=0)

for j in range(len(X)):
    words = []
    for i in range(len(X[j])):
        if len(X[j][i]) > 1:
            if X[j][i] not in list(stopwords['stopword']):
                words.append(X[j][i])
    X[j] = ' '.join(words)
print(X)

# X에 들어있는 문장만큼 포문을 돌리겠다
# 한글자짜리 빼고, 불용어 빼고 나머지들만 들어있는 리스트를 만든 것
# 문자열들을 띄어쓰기해서 붙이게끔 ' '.join

# 이제 tokenizer를 만들어서 다 숫자로 바꿔보겠습니다.

token = Tokenizer()
token.fit_on_texts(X)
tokened_X = token.texts_to_sequences(X)
print(tokened_X[:5])

with open('./models/news_token.pickle', 'wb') as f:
    pickle.dump(token, f)

# 형태소에다가 숫자만 라벨링해놓은 상태임
# token이 단어사전을 갖고있으니 저장하겠습니다. 피클담글게요


wordsize = len(token.word_index) + 1
print(wordsize)
print(token.index_word)

# 모델 만들 때 필요하므로 만들어놓아야함
# 단어의 갯수는 944개. 생각보다 적어(중복이 많다) 갯수 기억해놓자.
# 1부터 시작하는데 0을 써야돼. 그러니 +1
# index_word는 토큰에 있는 숫자와 단어를 딕셔너리 형태로 뽑아줘

# input_dim을 맞춰줘야하지 max값이 아닌 애들은 0으로 채우자

max = 0
for i in range(len(tokened_X)):
    if max < len(tokened_X[i]):
        max = len(tokened_X[i])
print(max)


# padding(0으로 채워서 길이맞추기, pad_sequences)

X_pad = pad_sequences(tokened_X, max)
print(X_pad[:10])

X_train, X_test, Y_train, Y_test = train_test_split(
    X_pad, onehot_Y, test_size=0.1)
print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)

xy = X_train, X_test, Y_train, Y_test
np.save('./crawling/news_data_max_{}_wordsize_{}'.format(max, wordsize),xy)

