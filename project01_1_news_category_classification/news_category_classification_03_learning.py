# -*- coding: utf-8 -*-
"""news_category_classification_03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yNvDZ1VbGBQuaGwB1jVu9koE1yTvlhsh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *

X_train, X_test, Y_train, Y_test = np.load(
    './crawling/news_data_max_23_wordsize_15601.npy',
    allow_pickle = True)
print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)

model = Sequential()
model.add(Embedding(15601, 300, input_length=23))
model.add(Conv1D(32, kernel_size = 5, padding='same',
                 activation='relu'))
model.add(MaxPool1D(pool_size=1))
model.add(LSTM(128,activation = 'tanh', return_sequences=True))
model.add(Dropout(0.3))
model.add(LSTM(64,activation = 'tanh', return_sequences=True))
model.add(Dropout(0.3))
model.add(LSTM(64,activation = 'tanh'))
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(128, activation = 'relu'))
model.add(Dense(6, activation='softmax'))  # 카테고리가 6개니까 6(다중분류기)
print(model.summary())

# 차원을 엄청 줄여줘야해. 굉장히 큰 공간에 데이터가 흩어져있으면 데이터가 희소해져서
# 학습이 안돼. 그래서 300차원으로 줄이는거야. 이것도 embedding이 해주는 것임

# 임베딩 레이어를 통해서 아래와 같은 945차원의 선들이 만들어져서 좌표가 생기게 되는것
# 킹과 퀸의 방향과 각도, 맨과 워먼의 방향과 각도가 같을 때 벡터가 갖다(벡터라이징)
# 벡터라이징을 하는 이유는, 계산을 하기 위함. 단어들의 의미를 갖고 연산이 가능해져
# ex) 킹 - man + woman = queen 이런 식으로 가능해짐. 
# ex) man(10,20) woman(20,10) king(15,25) queen (25,15)
# ex) (15,25) - (10,20) + (20,10) = (25,15) 

# 문맥을 파악하기 위해 conv레이어를 쓰는 것. ('말라') 라는 단어는 앞뒤 문맥에 따라
# 달라질 수 있음. conv 1차원이면 한줄로 되어있음(루미큐브느낌?)
# kernelsize를 5줬고, padding='same'을 하려면 앞뒤로 0이 두개씩 붙겠지?
# 설명을 쉽게하려고 저렇게 커널을 0과 1로 구성한것이고, 처음시작은 랜덤값, 학습을
# 통해서 점점 가까워져(커널이 문맥의 특성을 파악하기 최적화되어감)

# LSTM에다가 값을 넣어주면 
# ex) 한 문장이 13개의 형태소로 이루어져있음
# 입력이 13개면, 출력도 13개가 되어야해. 그럼 다음 LSTM에도 13개가 들어가야되잖아.
# return_sequence를 True로 줘야 13개가 들어가. 디폴트값이 0
# 안그러면 다른 LSTM레이어에 1개만 들어가


model.compile(loss='categorical_crossentropy',
              optimizer = 'adam', metrics=['accuracy'])
fit_hist = model.fit(X_train, Y_train, batch_size=100,
                     epochs=8, validation_data=(X_test,Y_test))

model.save('./models/news_category_classification_model_{}.h5'.format(
    fit_hist.history['val_accuracy'][-1]))

plt.plot(fit_hist.history['accuracy'], label='accuracy')
plt.plot(fit_hist.history['val_accuracy'], label='val accuracy')
plt.legend()
plt.show()