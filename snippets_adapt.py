# 데이터 바꿔 끼우기: 예제(캘리포니아·Fashion 등)를 다른 데이터(Salary2024·MNIST 등)로 바꿔 푸는 법 + loss 확인 모음

PANDAS_SIDE = """<table>
<tr><th>하려는 것</th><th>캘리포니아 (예제)</th><th>Salary2024 (바꾼 것)</th></tr>
<tr><td>불러오기</td><td><code>df = fetch_california_housing(as_frame=True).frame</code></td><td><code>df = pd.read_csv('/content/Salary2024.csv')</code></td></tr>
<tr><td>~별 개수</td><td><code>df['HouseAge'].value_counts()</code></td><td><code>df['job_title'].value_counts()</code></td></tr>
<tr><td>종류 수</td><td><code>df['HouseAge'].nunique()</code></td><td><code>df['job_title'].nunique()</code></td></tr>
<tr><td>~별 최소·최대·평균</td><td><code>df.groupby('HouseAge')['MedHouseVal'].agg(['min','max','mean'])</code></td><td><code>df.groupby('job_title')['salary_in_usd'].agg(['min','max','mean'])</code></td></tr>
<tr><td>조건으로 거르기</td><td><code>df[df['MedInc'] >= 8]</code></td><td><code>df[df['work_year'] == 2024]</code></td></tr>
<tr><td>높은 순 상위 10</td><td><code>df.sort_values('MedHouseVal', ascending=False).head(10)</code></td><td><code>df.sort_values('salary_in_usd', ascending=False).head(10)</code></td></tr>
<tr><td>두 기준 표(피벗)</td><td><code>df.pivot_table(index='HouseAge', values='MedHouseVal')</code></td><td><code>df.pivot_table(index='work_year', columns='experience_level', values='salary_in_usd')</code></td></tr>
</table>"""


def register(add):
    def card(title, kw, html, code=""):
        add("study", title, kw + " 데이터 바꾸기 다른 데이터 변형 응용 적용", code=code, html=html)

    card("데이터 바꿔 끼우기 (1) 원칙: 코드에서 데이터에 묶인 곳은 5군데", "데이터 바꿔 끼우기 원칙 다섯 군데 열 이름 입력 크기 출력층 loss",
html="""<p>예제 코드를 다른 데이터에 쓸 때 <b>모델 구조·compile·fit의 틀은 그대로</b>이고, 아래 5군데만 바꾼다. 문제를 받으면 먼저 <code>df.head()</code>, <code>df.info()</code>, <code>X.shape</code>, <code>y[:10]</code>로 데이터 모양을 본다.</p>
<table>
<tr><th>#</th><th>바꿀 곳</th><th>무엇을 보고 바꾸나</th><th>예</th></tr>
<tr><td>①</td><td><b>불러오기</b></td><td>데이터가 어디 있나</td><td><code>keras.datasets.mnist.load_data()</code> ↔ <code>fashion_mnist</code> / <code>pd.read_csv('/content/파일.csv')</code></td></tr>
<tr><td>②</td><td><b>열 이름 (X·y)</b></td><td>무엇으로(X) 무엇을(y) 맞히나</td><td>캘리포니아 y = <code>MedHouseVal</code> ↔ Salary y = <code>salary_in_usd</code></td></tr>
<tr><td>③</td><td><b>전처리</b></td><td>글자 열이 있나, 숫자 크기가 제각각인가</td><td>글자 → <code>pd.get_dummies</code>(원-핫) 또는 <code>.astype('category').cat.codes</code>(번호) / 크기 → <code>StandardScaler</code>, 이미지는 <code>/255.</code></td></tr>
<tr><td>④</td><td><b>입력 크기 · 출력층</b></td><td><code>X.shape[1:]</code>, 맞힐 것이 숫자인가 종류인가</td><td><code>Input(shape=X_train.shape[1:])</code> / 숫자 → <code>Dense(1)</code>, 종류 n개 → <code>Dense(n, activation="softmax")</code>, 예/아니오 → <code>Dense(1, activation="sigmoid")</code></td></tr>
<tr><td>⑤</td><td><b>loss · metrics</b></td><td>④와 짝</td><td>숫자 → <code>"mse"</code>, <code>["mae"]</code> / 종류(정수 라벨) → <code>"sparse_categorical_crossentropy"</code>, <code>["accuracy"]</code> / 예·아니오 → <code>"binary_crossentropy"</code></td></tr>
</table>
<p><b>문제 종류 판단</b>: 맞힐 값(y)이 <b>연속 숫자</b>(집값·연봉) → <b>회귀</b> / <b>정해진 종류</b>(옷 10종, 경력 4단계) → <b>분류</b></p>
<table>
<tr><th></th><th>회귀</th><th>분류 (n종류)</th><th>이진 분류</th></tr>
<tr><td>출력층</td><td>Dense(1) (활성화 없음)</td><td>Dense(n, softmax)</td><td>Dense(1, sigmoid)</td></tr>
<tr><td>loss</td><td>mse</td><td>sparse_categorical_crossentropy (원-핫이면 categorical_)</td><td>binary_crossentropy</td></tr>
<tr><td>metrics</td><td>mae</td><td>accuracy</td><td>accuracy</td></tr>
<tr><td>예측 결과 읽기</td><td>predict 값 그대로</td><td>np.argmax(predict, axis=-1)</td><td>predict > 0.5</td></tr>
</table>""")

    card("데이터 바꿔 끼우기 (2) Pandas: 캘리포니아 ↔ Salary2024", "pandas 캘리포니아 salary2024 열 이름 바꾸기 대응표 groupby value_counts",
html="<p>함수는 그대로, <b>열 이름만</b> 바꾼다. '~별로' 뒤에 오는 열 = groupby 안, '~의 최소·최대·평균'의 대상 = 대괄호 안.</p>" + PANDAS_SIDE +
"""<p><b>문장 → 코드 번역</b></p>
<ul><li>"<u>job_title</u>별 <u>salary_in_usd</u>의 평균" → <code>df.groupby('<u>job_title</u>')['<u>salary_in_usd</u>'].mean()</code></li>
<li>"<u>2024년</u> 데이터만" → <code>df[df['work_year'] == 2024]</code> (같다는 == 두 개, 문자열이면 따옴표 <code>== 'Senior-level'</code>)</li>
<li>"두 조건 모두" → <code>df[(조건1) &amp; (조건2)]</code> (괄호 필수, and 대신 &amp;)</li>
<li>"상위 10개" → <code>.sort_values(ascending=False).head(10)</code>. sort_values는 원본을 안 바꾸므로 이어서 쓰거나 변수에 다시 넣기</li>
<li>열 이름을 모르겠으면 <code>df.columns</code></li></ul>""")

    card("데이터 바꿔 끼우기 (3) 모델: 캘리포니아 회귀 예제 → Salary2024로 연봉 예측", "salary2024 회귀 모델 연봉 예측 get_dummies 원핫 standardscaler 캘리포니아 회귀 변형 dense 1 mse",
code='''import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# ① 불러오기 (캘리포니아 예제: housing = fetch_california_housing())
datafile = '/content/Salary2024.csv'
df = pd.read_csv(datafile)

# ② X·y 정하기 (캘리포니아: X = housing.data, y = housing.target)
y = df['salary_in_usd'].values.reshape(-1, 1) / 1000            # 맞힐 값: 연봉(천 달러 단위로 줄임)
X = df[['experience_level', 'employment_type', 'work_models',
        'work_year', 'company_size']]                             # 쓸 열 (salary·salary_currency는 정답과 같은 정보라 빼기)

# ③ 전처리: 글자 열 → 원-핫(0/1 열들), 캘리포니아는 전부 숫자라 이 단계가 없었음
X = pd.get_dummies(X, columns=['experience_level', 'employment_type', 'work_models', 'company_size'],
                   dtype=float)
print(X.shape, list(X.columns)[:5])

X_train_full, X_test, y_train_full, y_test = train_test_split(X.values, y, random_state=42)
X_train, X_valid, y_train, y_valid = train_test_split(X_train_full, y_train_full, random_state=42)
scaler = StandardScaler()                                         # 캘리포니아 예제와 동일
X_train = scaler.fit_transform(X_train)                          # fit은 훈련 데이터로만
X_valid = scaler.transform(X_valid)
X_test = scaler.transform(X_test)

# ④ 입력 크기·출력층 (구조는 캘리포니아 예제 그대로)
model = keras.models.Sequential([
    keras.layers.Input(shape=X_train.shape[1:]),                  # 열 개수가 바뀌어도 자동
    keras.layers.Dense(30, activation="relu"),
    keras.layers.Dense(1)                                         # 숫자 하나(연봉) → Dense(1), 활성화 없음
])
# ⑤ loss·metrics: 회귀 → mse, mae
model.compile(loss="mse", optimizer=keras.optimizers.Adam(learning_rate=1e-3), metrics=["mae"])
history = model.fit(X_train, y_train, epochs=20, validation_data=(X_valid, y_valid))
mse_test, mae_test = model.evaluate(X_test, y_test)
print("평균 절대 오차(천 달러):", round(mae_test, 1))
print(model.predict(X_test[:3]).round(1), y_test[:3].round(1))   # 예측 vs 실제''',
html="""<ul>
<li>캘리포니아는 <b>열이 전부 숫자</b>라 바로 넣었지만, Salary2024는 <code>experience_level</code> 같은 <b>글자 열</b>이 있어서 신경망에 못 넣음 → <code>pd.get_dummies</code>로 '열마다 0/1'(원-핫)로 바꿈 (3장 원-핫과 같은 이유: 글자에 번호를 매기면 없는 크기 관계가 생김)</li>
<li><b>정답과 같은 정보는 X에서 빼기</b>: salary(현지 통화 연봉), salary_currency는 사실상 답 → 넣으면 '커닝'</li>
<li>연봉은 숫자가 커서(수십만) /1000으로 줄임 → 손실 값이 너무 커지지 않게</li>
<li>StandardScaler는 <b>훈련 데이터로만 fit</b>, 검증·테스트는 transform만</li>
<li>나머지(Input 크기, Dense(1), mse)는 캘리포니아 예제와 같은 틀</li></ul>""")

    card("데이터 바꿔 끼우기 (4) 모델: 같은 Salary2024로 분류 (경력 맞히기)", "salary2024 분류 모델 경력 experience_level 맞히기 cat.codes softmax 4개 sparse_categorical 회귀를 분류로",
code='''import pandas as pd
import numpy as np
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('/content/Salary2024.csv')

# 맞힐 것: experience_level (4종류) → 번호로
y_cat = df['experience_level'].astype('category')
class_names = list(y_cat.cat.categories)                 # ['Entry-level', 'Executive-level', 'Mid-level', 'Senior-level']
y = y_cat.cat.codes.values                               # 0~3 정수 라벨

X = pd.get_dummies(df[['work_year', 'salary_in_usd', 'work_models', 'company_size', 'employment_type']],
                   columns=['work_models', 'company_size', 'employment_type'], dtype=float)
X_train, X_test, y_train, y_test = train_test_split(X.values, y, random_state=42, stratify=y)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = keras.models.Sequential([
    keras.layers.Input(shape=X_train.shape[1:]),
    keras.layers.Dense(30, activation="relu"),
    keras.layers.Dense(len(class_names), activation="softmax")   # 종류 4개 → Dense(4, softmax)
])
model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(X_train, y_train, epochs=10, validation_split=0.1)
print(model.evaluate(X_test, y_test))
pred = np.argmax(model.predict(X_test[:5]), axis=-1)
print([class_names[i] for i in pred], [class_names[i] for i in y_test[:5]])''',
html="""<ul>
<li>같은 데이터라도 <b>무엇을 맞히느냐</b>로 회귀/분류가 갈림: 연봉(숫자) → 회귀, 경력(종류) → 분류</li>
<li>바뀌는 것: 정답을 번호로(<code>.astype('category').cat.codes</code>), 출력층 <code>Dense(종류 수, softmax)</code>, loss <code>sparse_categorical_crossentropy</code>, metrics <code>accuracy</code>, 결과는 <code>argmax</code></li>
<li><code>validation_split=0.1</code>: 검증 세트를 따로 안 만들고 훈련 데이터 끝 10%를 자동으로 씀</li>
<li><code>stratify=y</code>: 나눌 때 종류 비율을 맞춤 (종류마다 개수 차이가 클 때)</li></ul>""")

    card("데이터 바꿔 끼우기 (5) 이미지: Fashion ↔ MNIST, MLP ↔ CNN, 이미지 ↔ 표", "fashion mnist 바꾸기 class_names cnn 채널 newaxis input shape 이미지 표 데이터 바꾸기",
code='''import numpy as np
from tensorflow import keras

# Fashion → MNIST: 불러오기 한 줄과 class_names만
(X_train_full, y_train_full), (X_test, y_test) = keras.datasets.mnist.load_data()   # ← fashion_mnist 에서 바꿈
class_names = [str(i) for i in range(10)]                                          # ← 옷 이름 대신 '0'~'9'
X_train_full, X_test = X_train_full / 255., X_test / 255.
X_train, X_valid = X_train_full[:-5000], X_train_full[-5000:]
y_train, y_valid = y_train_full[:-5000], y_train_full[-5000:]

# MLP → CNN: 채널 축 추가 + Input 모양 + 층
X_train_c, X_valid_c, X_test_c = (a[..., np.newaxis] for a in (X_train, X_valid, X_test))   # (N, 28, 28, 1)
cnn = keras.models.Sequential([
    keras.layers.Input(shape=[28, 28, 1]),              # MLP는 [28, 28]
    keras.layers.Conv2D(32, 3, padding="same", activation="relu"),
    keras.layers.MaxPool2D(2),
    keras.layers.Flatten(),
    keras.layers.Dense(10, activation="softmax")])      # 출력층·loss는 그대로
cnn.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
cnn.fit(X_train_c, y_train, epochs=1, validation_data=(X_valid_c, y_valid))''',
html="""<table>
<tr><th>바꾸기</th><th>고칠 곳</th><th>그대로인 곳</th></tr>
<tr><td>Fashion ↔ MNIST</td><td>load_data 한 줄, class_names</td><td>전처리(/255.), 모델, compile 전부 (둘 다 28×28, 10종류)</td></tr>
<tr><td>MLP → CNN</td><td><code>[..., np.newaxis]</code>로 채널 추가, <code>Input(shape=[28, 28, 1])</code>, 앞부분을 Conv2D·MaxPool2D로</td><td>Flatten 뒤 Dense, 출력층, compile</td></tr>
<tr><td>컬러 사진</td><td>채널 3 (<code>Input(shape=[높이, 너비, 3])</code>)</td><td>나머지</td></tr>
<tr><td>이미지 → 표 데이터</td><td>Flatten 빼기, <code>Input(shape=X_train.shape[1:])</code>, 글자 열 원-핫, StandardScaler</td><td>Dense 층 쌓는 방식</td></tr>
<tr><td>출력 종류 수가 다름</td><td>마지막 <code>Dense(종류 수, softmax)</code></td><td>나머지</td></tr>
</table>""")

    card("loss 확인하는 법 모음 (학습 곡선 · evaluate · 비교 · 작년 형식)", "loss 확인 손실 확인 history val_loss 그래프 학습 곡선 evaluate 비교 최소 epoch log_loss 작년",
code='''import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras

(X_train_full, y_train_full), (X_test, y_test) = keras.datasets.fashion_mnist.load_data()
X_train_full, X_test = X_train_full / 255., X_test / 255.
X_train, X_valid = X_train_full[:-5000], X_train_full[-5000:]
y_train, y_valid = y_train_full[:-5000], y_train_full[-5000:]

def build_model():
    model = keras.models.Sequential([keras.layers.Input(shape=[28, 28]), keras.layers.Flatten(),
        keras.layers.Dense(100, activation="relu"), keras.layers.Dense(10, activation="softmax")])
    return model

model = build_model()
model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
history = model.fit(X_train, y_train, epochs=5, validation_data=(X_valid, y_valid))

# 1) epoch별 loss 값 보기
print(history.history.keys())                    # loss, accuracy, val_loss, val_accuracy
print(history.history["loss"])                   # 훈련 손실 리스트
print(history.history["val_loss"])               # 검증 손실 리스트

# 2) 학습 곡선 그리기
pd.DataFrame(history.history).plot(figsize=(8, 5))
plt.grid(True); plt.xlabel("epoch"); plt.show()

# 3) 검증 손실이 가장 낮았던 epoch
best_epoch = int(np.argmin(history.history["val_loss"])) + 1
print("val_loss 최소 epoch:", best_epoch, min(history.history["val_loss"]))

# 4) 테스트 손실·정확도
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"test loss {test_loss:.4f}, accuracy {test_acc:.4f}")

# 5) 여러 설정(옵티마이저 등) loss 비교: 한 그래프 + 표
results = {}
for name, opt in {"SGD": keras.optimizers.SGD(learning_rate=0.01),
                  "Adam": keras.optimizers.Adam(learning_rate=0.001)}.items():
    m = build_model()
    m.compile(loss="sparse_categorical_crossentropy", optimizer=opt, metrics=["accuracy"])
    h = m.fit(X_train, y_train, epochs=3, validation_data=(X_valid, y_valid), verbose=0)
    plt.plot(h.history["val_loss"], label=name)
    results[name] = m.evaluate(X_test, y_test, verbose=0)
plt.legend(); plt.xlabel("epoch"); plt.ylabel("val_loss"); plt.show()
print(pd.DataFrame(results, index=["test_loss", "test_accuracy"]).T)

# 6) sklearn 방식 (작년 머신러닝 시험처럼 확률로 손실 계산)
from sklearn.metrics import log_loss
print("log loss:", log_loss(y_test, model.predict(X_test, verbose=0)))   # = 교차 엔트로피''',
html="""<table>
<tr><th>보고 싶은 것</th><th>코드</th><th>읽는 법</th></tr>
<tr><td>epoch별 손실</td><td><code>history.history["loss"]</code>, <code>["val_loss"]</code></td><td>loss = 문제집(훈련), val_loss = 모의고사(검증)</td></tr>
<tr><td>학습 곡선</td><td><code>pd.DataFrame(history.history).plot()</code></td><td>둘 다 내려가면 정상. <b>loss는 내려가는데 val_loss가 올라가면 과적합</b></td></tr>
<tr><td>가장 좋았던 epoch</td><td><code>np.argmin(history.history["val_loss"]) + 1</code></td><td>그 epoch 근처에서 멈추는 게 좋음 → EarlyStopping</td></tr>
<tr><td>테스트 손실</td><td><code>model.evaluate(X_test, y_test)</code> → [loss, accuracy]</td><td>마지막에 한 번</td></tr>
<tr><td>설정별 비교</td><td>반복문으로 학습 → val_loss를 한 그래프에, evaluate를 DataFrame 표로</td><td>더 빨리·더 낮게 내려간 쪽이 좋음</td></tr>
<tr><td>확률로 직접 계산</td><td><code>sklearn.metrics.log_loss(y, 예측확률)</code></td><td>= 교차 엔트로피 (evaluate의 loss와 거의 같음)</td></tr>
</table>
<p>작년 시험 형식(GridSearchCV 결과표, 최적 조합 재학습, ROC·AUC, plotROC)은 "빈칸 채우기"와 "튜닝·평가" 분류에 있음: <a href="#q=plotROC">plotROC</a> · <a href="#q=cv_results_">cv_results_</a> · <a href="#q=roc auc">ROC·AUC</a></p>""")
