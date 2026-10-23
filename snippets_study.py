# 공부 순서 (장별 해설): 사이트만 보고 처음부터 공부할 수 있게 교수님 노트북 순서대로 풀어 쓴 해설
# register(add, nb) : nb(key, 제목) → 교수님 노트북 페이지의 해당 위치 링크

SECTIONS_STUDY = [("study", "공부 순서 (장별 해설)")]


def _q(word, label=None):
    """사이트 안 검색 링크"""
    return f'<a href="#q={word}">{label or word}</a>'


def _sec(title, body):
    return f"<h3 class=\"pq\">{title}</h3>{body}"


def register(add, nb, after_intro=None):
    def L(key, heading, label=None):
        return f'<a href="{nb(key, heading)}" target="_blank">{label or heading}</a>'

    def card(title, kw, html, code=""):
        add("study", title, kw + " 공부 순서 해설 정리 장별", code=code, html=html)

    # ================================================================== 0
    card("0. 이 사이트로 공부하는 법", "공부 방법 순서 시작 사용법 시간 배분",
html=_sec("순서", """<ol>
<li><b>큰 그림</b> 카드(1번)로 "신경망이 어떻게 배우는가"를 먼저 잡는다</li>
<li><b>2장 → 7장</b> 해설 카드를 순서대로 읽는다. 각 카드는 교수님 노트북 순서 그대로이고, 노트북 위치 링크가 붙어 있다</li>
<li>각 카드 끝의 <b>스스로 점검</b> 질문에 말로 답해 본다. 막히면 "더 보기" 링크로 해당 카드를 연다</li>
<li><b>"교수님 강조"</b> 분류의 질문→답 표에서 <b>답 가리기</b>를 누르고 직접 써 본다</li>
<li><b>"과제 변형 연습"</b>에서 Week3·Week4 문제를 빈 Colab에 직접 쳐 본다</li>
<li><b>"노트북 에러 수정"</b>에서 에러 원인 문장을 자기 말로 바꿔 써 본다</li>
</ol>""") + _sec("분류별 쓰임", """<table>
<tr><th>분류</th><th>언제</th></tr>
<tr><td>공부 순서 (장별 해설)</td><td>처음 공부할 때, 흐름을 잡을 때</td></tr>
<tr><td>개념 + 예제</td><td>용어 하나의 뜻·비유·코드·바꾸면 어떻게 되는지</td></tr>
<tr><td>교수님 강조</td><td>수업에서 질문했던 것, 서술형 대비</td></tr>
<tr><td>과제 변형 연습</td><td>시험과 같은 형식으로 손 풀기</td></tr>
<tr><td>노트북 에러 수정</td><td>"에러를 고치고 원인을 쓰라"는 문제</td></tr>
<tr><td>빈칸 채우기</td><td>시험 노트북 주석 문장 → 넣을 코드 (교수님 변수 이름 그대로)</td></tr>
<tr><td>바꾸면 이렇게 된다</td><td>하나만 바꿨을 때 정확도가 어떻게 변하는지 실제 실험 결과</td></tr>
<tr><td>나머지 (시작·데이터·모델…)</td><td>시험 중 코드 찾기</td></tr>
</table>""") + _sec("시험 중 검색 요령", f"""<ul>
<li>문제 문장의 단어를 그대로 친다: {_q('배치 정규화')}, {_q('조기 종료')}, {_q('groupby')}</li>
<li>에러 메시지 일부를 친다: {_q('incompatible')}, {_q('item assignment')}</li>
<li>띄어쓰기·대소문자는 상관없음, 여러 단어는 모두 들어간 것만 나옴</li>
</ul>"""))

    if after_intro: after_intro(add)

    # ================================================================== 1
    card("1. 큰 그림: 신경망은 어떻게 배우나 (순전파 → 손실 → 역전파 → 옵티마이저)", "큰 그림 학습 과정 순전파 손실 역전파 옵티마이저 경사하강 가중치 편향 활성화 epoch batch",
html=_sec("한 문장", "<p>입력에 가중치를 곱해 답을 내 보고(순전파), 정답과 얼마나 틀렸는지 재고(손실), 각 가중치가 그 틀림에 얼마나 책임이 있는지 미분으로 구한 뒤(역전파), 그만큼 가중치를 조금씩 고친다(옵티마이저). 이걸 데이터 전체에 대해 여러 번 반복(epoch)한다.</p>")
+ _sec("① 뉴런 하나", """<ul>
<li>앞 뉴런들의 출력 a₁…aₙ에 각각 가중치 w를 곱해 모두 더하고 편향 b를 더한다: <b>z = Σ wᵢaᵢ + b</b></li>
<li>z를 활성화 함수에 넣어 이 뉴런의 출력 <b>a = σ(z)</b>를 만든다 (교수님: "결론을 내는 게 활성화 함수")</li>
<li>편향 = 뉴런이 얼마나 쉽게 켜지는지 ("흥분 잘하는 뉴런 / 침착한 뉴런")</li>
<li>활성화가 없으면 층을 아무리 쌓아도 곱하고 더하기만 반복 → 선형 함수 하나와 같아져서 복잡한 걸 못 배움</li>
</ul>""")
+ _sec("② 층과 네트워크", """<ul>
<li>MNIST 예: 입력 784(28×28 픽셀) → 은닉층 → 출력 10(숫자 0~9)</li>
<li>Dense(완전 연결) 층은 앞 층의 모든 뉴런과 연결 → 파라미터 = 입력 수 × 뉴런 수 + 뉴런 수(편향)</li>
<li>행렬로 쓰면 한 층 전체가 <b>a¹ = σ(W·a⁰ + b)</b> 한 줄 (교수님: "수학은 언어다")</li>
<li>출력층은 softmax: 10개 값을 합이 1인 확률로 바꿔 가장 큰 것을 답으로</li>
</ul>""")
+ _sec("③ 손실 (얼마나 틀렸나)", """<ul>
<li>정답과 출력의 차이를 숫자 하나로 만든 것. 회귀는 MSE(차이를 <b>제곱</b>해 평균), 분류는 교차 엔트로피(로그 사용)</li>
<li>제곱하는 이유: 그냥 더하면 +와 −가 상쇄, 절댓값은 0에서 미분 불가, 제곱은 부호가 없어지고 미분 가능 (교수님 3번 반복)</li>
<li>loss = cost: 최적화에서 "줄일 비용"이라는 뜻</li>
</ul>""")
+ _sec("④ 역전파 (누구 책임인가)", """<ul>
<li>손실을 각 가중치로 미분하면 "이 가중치를 조금 키우면 손실이 얼마나 변하나"(기울기)가 나온다</li>
<li>출력층에서 시작해 체인 룰로 한 층씩 앞으로 거슬러 가며 계산 → 그래서 <b>역</b>전파</li>
<li>softmax + 교차 엔트로피의 출력층 기울기는 간단히 <b>예측 − 정답</b></li>
<li>직관(9/19): 정답 뉴런 값을 올리려면 ① 편향 올리기 ② 강하게 켜진 앞 뉴런과의 가중치 올리기 ③ 앞 층 출력 바꾸기(직접 못 하니 그 앞 가중치로 → 거슬러 올라감)</li>
</ul>""")
+ _sec("⑤ 옵티마이저 (얼마나 고치나)", """<ul>
<li>새 가중치 = 기존 가중치 − <b>학습률</b> × 기울기 (경사 하강). 학습률이 크면 발산, 작으면 느림</li>
<li>SGD(배치로 랜덤하게) → 모멘텀(가던 방향 가속) → Nesterov(먼저 가 보고 기울기) → AdaGrad/RMSProp(축마다 스케일 맞춤) → Adam/Nadam(합친 것, 실무에서 주로)</li>
</ul>""")
+ _sec("⑥ epoch · 배치 · 검증", """<ul>
<li><b>배치</b>: 한 번에 처리하는 묶음(기본 32). 배치마다 기울기 평균으로 한 번 고침</li>
<li><b>epoch</b>: 훈련 데이터 전체를 한 바퀴. 55,000개 / 32 ≈ 1,719 스텝</li>
<li><b>검증 세트</b>: 훈련 도중 epoch마다 성능을 보려고 떼어 둔 데이터. <b>테스트 세트</b>는 맨 마지막에 한 번</li>
<li>훈련 정확도는 오르는데 검증 정확도가 떨어지기 시작하면 <b>과적합</b></li>
</ul>""")
+ _sec("케라스 코드와 연결", "<p>위 과정이 케라스 세 줄에 숨어 있다: <code>model = Sequential([...])</code>(①②), <code>model.compile(loss=③, optimizer=⑤, metrics=[...])</code>, <code>model.fit(X, y, epochs=⑥)</code>(③④⑤를 반복). 6장의 사용자 정의 훈련 반복은 이 fit 안을 직접 쓴 것.</p>")
+ _sec("스스로 점검", "<ol><li>활성화 함수가 없으면 왜 안 되나?</li><li>Dense(100)이 입력 300개를 받으면 파라미터는 몇 개?</li><li>역전파는 왜 출력층부터 시작하나?</li><li>epoch와 배치의 차이는?</li></ol>")
+ _sec("더 보기", f"{_q('가중합')} · {_q('활성화 함수')} · {_q('역전파')} · {_q('옵티마이저 계보')} · {_q('파라미터 개수 계산 모음')}"))

    # ================================================================== 2장
    card("2장. 케라스로 첫 신경망: Fashion MNIST 분류", "2장 fashion mnist sequential summary compile fit history evaluate predict 함수형 api 저장 복원 콜백 10장",
code='''import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1) 데이터: 이미 train/test로 나뉘어 있음
fashion_mnist = keras.datasets.fashion_mnist
(X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()
print(X_train_full.shape, X_train_full.dtype)        # (60000, 28, 28) uint8

# 2) 검증 세트 5000개 떼기 + 0~1로 스케일
X_valid, X_train = X_train_full[:5000] / 255., X_train_full[5000:] / 255.
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]
X_test = X_test / 255.
class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

# 3) 모델
model = keras.models.Sequential([
    keras.layers.Input(shape=[28, 28]),
    keras.layers.Flatten(),                           # 28x28 → 784
    keras.layers.Dense(300, activation="relu"),
    keras.layers.Dense(100, activation="relu"),
    keras.layers.Dense(10, activation="softmax")])
model.summary()                                       # 235,500 / 30,100 / 1,010

# 4) 컴파일 → 5) 학습
model.compile(loss="sparse_categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])
history = model.fit(X_train, y_train, epochs=30, validation_data=(X_valid, y_valid))

# 6) 학습 곡선
pd.DataFrame(history.history).plot(figsize=(8, 5)); plt.grid(True); plt.gca().set_ylim(0, 1); plt.show()

# 7) 평가와 예측
model.evaluate(X_test, y_test)
X_new = X_test[:3]
y_proba = model.predict(X_new).round(2)               # 클래스별 확률
y_pred = np.argmax(y_proba, axis=-1)                  # 가장 큰 확률의 번호
print(y_pred, np.array(class_names)[y_pred])

# 8) 저장과 복원
model.save("my_keras_model.keras")
model = keras.models.load_model("my_keras_model.keras")

# 9) 콜백
checkpoint_cb = keras.callbacks.ModelCheckpoint("my_keras_model.keras", save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True)
history = model.fit(X_train, y_train, epochs=100, validation_data=(X_valid, y_valid),
                    callbacks=[checkpoint_cb, early_stopping_cb])''',
html=_sec("이 장에서 하는 것", f"<p>옷 사진 10종을 분류하는 MLP(다층 퍼셉트론)를 케라스로 만들고, 학습·평가·예측·저장·콜백까지 한 바퀴 돈다. 교수님 노트북: {L('ch2', '이미지 분류기 만들기')} → {L('ch2', '함수형 API')} → {L('ch2', '저장과 복원')} → {L('ch2', '훈련 과정에서 콜백 사용하기')}</p>")
+ _sec("① 데이터 준비", """<ul>
<li><code>load_data()</code>는 (훈련, 테스트) 두 묶음을 준다. 이미지 하나는 28×28, 값은 0~255 정수(uint8)</li>
<li><b>/255.</b>: 0~1 실수로 맞춤 (스케일이 크면 학습이 불안정)</li>
<li><b>검증 세트</b>: 훈련 앞 5,000개를 떼어 epoch마다 성능 확인용. 테스트는 마지막에 한 번만</li>
<li><code>class_names[y]</code>: 라벨 번호 → 이름</li></ul>""")
+ _sec("② 모델 만들기 (Sequential)", """<ul>
<li><b>Flatten</b>: 28×28을 784개 한 줄로 편다. 파라미터 0</li>
<li><b>Dense(300, relu)</b>: 784×300 + 300 = <b>235,500</b>개. Dense(100): 300×100+100 = 30,100. 출력 Dense(10): 1,010. 합 266,610</li>
<li>출력층 <b>softmax</b>: 10개 클래스 확률(합 1). 은닉층은 <b>ReLU</b> (각자 독립적으로 결론)</li>
<li>만드는 법 두 가지: 리스트로 한 번에 / <code>model = Sequential()</code> 후 <code>model.add(...)</code> 반복</li>
<li><code>model.layers</code>, <code>get_layer('dense')</code>, <code>get_weights()</code>로 층과 가중치를 꺼내 볼 수 있음 (가중치는 처음에 랜덤, 편향은 0)</li></ul>""")
+ _sec("③ compile", """<ul>
<li><b>loss</b>: 라벨이 정수 0~9 → <code>sparse_categorical_crossentropy</code>. 원-핫이면 <code>categorical_crossentropy</code>, 이진 분류면 <code>binary_crossentropy</code>, 회귀면 <code>mse</code></li>
<li><b>optimizer</b>: "sgd"는 학습률 0.01의 경사 하강. 바꾸려면 <code>keras.optimizers.SGD(learning_rate=...)</code></li>
<li><b>metrics</b>: 사람이 보려고 출력하는 값, 학습엔 안 쓰임</li></ul>""")
+ _sec("④ fit과 history", """<ul>
<li>출력의 <code>1719/1719</code> = 한 epoch의 배치 수(55,000/32). loss·accuracy는 훈련, val_* 는 검증</li>
<li><code>history.history</code>: epoch별 loss·accuracy·val_loss·val_accuracy 딕셔너리 → DataFrame으로 그래프</li>
<li>검증 곡선이 훈련 곡선과 벌어지면 과적합 신호</li></ul>""")
+ _sec("⑤ 평가·예측", """<ul>
<li><code>evaluate</code> → [loss, accuracy] (Fashion은 약 0.87~0.89)</li>
<li><code>predict</code> → 각 클래스 확률. <code>np.argmax(..., axis=-1)</code>로 번호. 옛 <code>predict_classes</code>는 없어짐</li></ul>""")
+ _sec("⑥ 함수형 API (캘리포니아 집값, 회귀)", f"""<ul>
<li>층을 만들고 바로 이전 출력을 넣어 호출하면 연결: <code>hidden1 = Dense(30)(input_)</code>. 마지막에 <code>keras.Model(inputs, outputs)</code></li>
<li>Wide & Deep: 입력을 깊은 경로와 출력 직전에 <code>Concatenate</code>로 합침 → 단순 패턴도 잊지 않게</li>
<li>입력 여러 개(<code>inputs=[input_A, input_B]</code>), 출력 여러 개도 가능 → fit에도 (X_A, X_B)처럼 튜플로</li>
<li>회귀라 출력은 Dense(1), 활성화 없음, loss="mse"</li>
<li>자세히: {_q('함수형 API: 층이 곧 함수')}</li></ul>""")
+ _sec("⑦ 저장·콜백", """<ul>
<li><code>model.save("이름.keras")</code> → <code>keras.models.load_model</code>. Keras 3는 확장자 필수</li>
<li><b>ModelCheckpoint(save_best_only=True)</b>: 검증 성능이 가장 좋았을 때의 모델만 저장</li>
<li><b>EarlyStopping(patience=10, restore_best_weights=True)</b>: 10 epoch 동안 나아지지 않으면 멈추고 최고 가중치로 되돌림 → epochs를 크게 줘도 됨</li>
<li>callbacks 리스트 순서는 상관없음</li></ul>""")
+ _sec("시험 포인트", "<ul><li>파라미터 수 계산(235,500)과 이유(편향)</li><li>검증 세트를 나누는 이유</li><li>loss / optimizer / metrics 각각의 역할</li><li>숫자 모델을 Fashion에 써도 되는 이유 (입력·출력 크기가 같음)</li><li>ReLU vs softmax</li><li>콜백 save_best_only = 최고일 때의 가중치</li></ul>")
+ _sec("스스로 점검", "<ol><li>Flatten을 빼면 무엇을 대신 해야 하나?</li><li>라벨을 원-핫으로 바꾸면 loss는?</li><li>val_loss가 계속 오르면 무엇을 의심하고 어떻게 하나?</li><li>함수형 API가 필요한 구조의 예는?</li></ol>")
+ _sec("더 보기", f"{_q('Fashion MNIST 데이터')} · {_q('summary')} · {_q('compile 기본')} · {_q('학습 곡선')} · {_q('콜백')} · {_q('wide deep')}"))

    # ================================================================== 3장
    card("3장. 필기 숫자 인식 (MNIST): 원-핫 · 16-16-10 · 내 글씨 · 데이터 증강", "3장 mnist 필기 숫자 원핫 to_categorical categorical_crossentropy reshape 784 16 13002 손글씨 과적합 데이터 증강",
code='''import tensorflow as tf
from tensorflow import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.utils import to_categorical
import numpy as np

(X_train, y_train), (X_test, y_test) = mnist.load_data()
print(X_train.shape)                                  # (60000, 28, 28)

X_train = X_train.reshape(60000, 784)                 # Flatten 대신 직접 펴기
X_test = X_test.reshape(10000, 784)
X_train = X_train.astype("float32") / 255
X_test = X_test.astype("float32") / 255

Y_train = to_categorical(y_train, 10)                 # 3 → [0,0,0,1,0,0,0,0,0,0]
Y_test = to_categorical(y_test, 10)

model = Sequential([
    keras.layers.Input(shape=(784,)),
    Dense(16), Activation("relu"),
    Dense(16), Activation("relu"),
    Dense(10), Activation("softmax")])
model.summary()                                       # 12,560 + 272 + 170 = 13,002

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(X_train, Y_train, batch_size=128, epochs=5, verbose=1)
score = model.evaluate(X_test, Y_test)
print("Test accuracy:", score[1])

idx = 0
print(np.argmax(model.predict(X_test[idx:idx+1])), y_test[idx])   # 예측 vs 정답''',
html=_sec("이 장에서 하는 것", f"<p>2장 복습 후, 숫자 0~9 손글씨(MNIST)를 작은 신경망(16-16-10)으로 인식하고, 마우스로 쓴 내 글씨를 넣어 본 뒤 잘 안 맞는 이유와 해결책(데이터 증강)을 본다. 교수님 노트북: {L('ch3', '필기체 숫자 인식')} → {L('ch3', '신경망 준비하기')} → {L('ch3', 'See if it recognizes my handwriting')} → {L('ch3', 'image transformation')}</p>")
+ _sec("① 2장과 다른 점 (9/19 수업 실습이 바로 이것)", """<table>
<tr><th></th><th>2장 Fashion</th><th>3장 MNIST</th></tr>
<tr><td>펴기</td><td>Flatten 층</td><td>reshape(60000, 784) 직접</td></tr>
<tr><td>라벨</td><td>정수 그대로</td><td>to_categorical로 원-핫</td></tr>
<tr><td>loss</td><td>sparse_categorical_crossentropy</td><td>categorical_crossentropy</td></tr>
<tr><td>은닉층</td><td>300, 100</td><td>16, 16</td></tr>
<tr><td>활성화</td><td>Dense 안에</td><td>Activation 층으로 따로</td></tr></table>
<p>수업 실습: Fashion 모델에서 Flatten을 빼고 reshape로, sparse를 categorical로 바꿔 보기 → 둘 다 짝을 맞춰 바꿔야 함 (안 맞으면 <code>Shapes (None, 10) and (None, 1) are incompatible</code>)</p>""")
+ _sec("② 원-핫 인코딩을 쓰는 이유", "<p>라벨을 그냥 숫자로 두면 신경망은 곱하고 더하면서 '9가 1보다 크다' 같은 없는 크기 관계를 배울 수 있다(교수님 비유: TV=0, 냉장고=1이면 냉장고가 더 큰가?). 칸을 클래스 수만큼 만들고 해당 칸만 1로 하면 그런 오해가 없고, 출력 10개와 모양도 같아진다.</p>")
+ _sec("③ 16-16-10의 파라미터", "<p>784×16+16 = 12,560, 16×16+16 = 272, 16×10+10 = 170 → <b>13,002</b>개. 이 13,002개가 cost 함수의 입력이고, 경사 하강은 13,002차원에서 최저점을 찾는 일 (9/19).</p>")
+ _sec("④ 은닉층이 하는 일 (직관)", "<p>8은 동그라미 두 개, 9는 위 동그라미 + 세로선… 첫 은닉층은 짧은 획·엣지를, 다음 층은 그 조합(동그라미·긴 선)을 찾지 않을까 하는 가정. 꼭 그렇게 되는 건 아님. 사람이 규칙을 짜서는 숫자를 인식할 수 없어서(사람마다 3을 다르게 씀) 학습시킨다.</p>")
+ _sec("⑤ 내 글씨는 왜 잘 못 맞히나 → 데이터 증강", f"""<ul>
<li>MNIST는 미국 사람들 글씨 → 그 스타일에 <b>과적합</b>. 내가 쓴 숫자는 위치·굵기·기울기가 달라 분포가 다름</li>
<li>해결: 기존 이미지를 회전·이동해서 데이터를 늘리고(<b>데이터 증강</b>) 다시 훈련 (9/19 과제)</li>
<li>교수님 노트북은 torchvision의 RandomRotation(±30°), RandomAffine(10% 이동)으로 60,000장을 더 만들어 120,000장으로 학습</li>
<li>코드: {_q('데이터 증강 코드')}</li></ul>""")
+ _sec("⑥ Fashion 모델 vs 숫자 모델", "<p>노트북 끝: Fashion으로 학습한 모델과 숫자로 학습한 모델에 같은 손글씨를 넣어 비교 → 같은 구조여도 무엇으로 학습했느냐가 결과를 정한다.</p>")
+ _sec("시험 포인트", "<ul><li>원-핫 / 정수 라벨과 loss의 짝</li><li>Flatten ↔ reshape</li><li>13,002 계산</li><li>내 글씨를 못 맞히는 이유(과적합·분포 차이)와 데이터 증강</li></ul>")
+ _sec("스스로 점검", "<ol><li>to_categorical을 안 하고 categorical_crossentropy를 쓰면?</li><li>reshape(60000, 784)를 안 하고 Dense에 넣으면?</li><li>데이터 증강으로 정확도가 오르는 이유는?</li></ol>")
+ _sec("더 보기", f"{_q('sparse vs categorical')} · {_q('원-핫')} · {_q('MNIST')} · {_q('데이터 증강 코드')}"))

    # ================================================================== 4장 (1)
    card("4장 (1). 깊은 신경망 훈련: 초기화 · 활성화 · 배치 정규화 · 드롭아웃 · 전이 학습", "4장 11장 기울기 소실 초기화 he glorot lecun 활성화 relu leaky elu selu 배치 정규화 드롭아웃 전이 학습 과적합",
code='''import tensorflow as tf
from tensorflow import keras

(X_train_full, y_train_full), (X_test, y_test) = keras.datasets.fashion_mnist.load_data()
X_train_full, X_test = X_train_full / 255., X_test / 255.
X_valid, X_train = X_train_full[:5000], X_train_full[5000:]
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]

# 초기화 + 활성화 (세트로)
he_dense = keras.layers.Dense(10, activation="relu", kernel_initializer="he_normal")

# 배치 정규화: 활성화 뒤에 (가장 간단)
model = keras.models.Sequential([
    keras.layers.Input(shape=[28, 28]),
    keras.layers.Flatten(),
    keras.layers.BatchNormalization(),
    keras.layers.Dense(300, activation="relu", kernel_initializer="he_normal"),
    keras.layers.BatchNormalization(),
    keras.layers.Dense(100, activation="relu", kernel_initializer="he_normal"),
    keras.layers.BatchNormalization(),
    keras.layers.Dense(10, activation="softmax")])

# 배치 정규화: 활성화 앞에 (Dense는 활성화 없이, 편향 없이)
model_b = keras.models.Sequential([
    keras.layers.Input(shape=[28, 28]),
    keras.layers.Flatten(),
    keras.layers.Dense(300, kernel_initializer="he_normal", use_bias=False),
    keras.layers.BatchNormalization(),
    keras.layers.Activation("relu"),
    keras.layers.Dense(10, activation="softmax")])

# 드롭아웃
model_d = keras.models.Sequential([
    keras.layers.Input(shape=[28, 28]),
    keras.layers.Flatten(),
    keras.layers.Dropout(rate=0.2),
    keras.layers.Dense(300, activation="relu", kernel_initializer="he_normal"),
    keras.layers.Dropout(rate=0.2),
    keras.layers.Dense(10, activation="softmax")])

model.compile(loss="sparse_categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_valid, y_valid))''',
html=_sec("이 장에서 하는 것", f"<p>층을 깊게 쌓을 때 생기는 문제(기울기 소실·폭주, 훈련 비용, 과적합)와 해결 도구를 하나씩 케라스 코드로 넣어 본다. 교수님 노트북: {L('ch4', '심층 신경망의 주요 요소에 대한 이해')} → {L('ch4', 'Initializer')} → {L('ch4', 'Activation')} → {L('ch4', '배치 정규화')} → {L('ch4', 'Optimizer')} → {L('ch4', 'Dropout')}. 9/26 줌 보강에서 설명.</p>")
+ _sec("① 문제", """<ul>
<li><b>기울기 소실</b>: 역전파로 앞(아래)층으로 갈수록 기울기가 0에 가까워져 앞층이 거의 안 배움. 원인: sigmoid를 거치면 출력의 평균·분산이 입력과 달라짐(He 등)</li>
<li><b>기울기 폭주</b>: RNN처럼 되먹임 구조에서 계속 커짐 (마이크 하울링 비유)</li>
<li><b>훈련 비용</b>: 레이블링·컴퓨팅·시간. <b>과적합</b>: 훈련 데이터에만 맞음</li>
<li>해결책들은 <b>대체가 아니라 같이</b> 씀</li></ul>""")
+ _sec("② 가중치 초기화", """<table>
<tr><th>이름</th><th>분산</th><th>짝 활성화</th><th>케라스</th></tr>
<tr><td>Glorot (Xavier)</td><td>1/fan_avg</td><td>없음·tanh·sigmoid·softmax</td><td>기본값 (glorot_uniform)</td></tr>
<tr><td>He</td><td>2/fan_in</td><td>ReLU 계열</td><td>kernel_initializer="he_normal"</td></tr>
<tr><td>LeCun</td><td>1/fan_in</td><td>SELU</td><td>"lecun_normal"</td></tr></table>
<p>fan_in = 앞에서 들어오는 연결 수, fan_out = 뒤로 나가는 연결 수 (부채 모양). 랜덤으로 뽑되 <b>분포</b>를 맞춰 층마다 출력의 분산이 유지되게 → 기울기 소실 완화. "여러분이 아무것도 안 줬을 때 사실 Glorot를 쓰고 있던 거야"</p>""")
+ _sec("③ 활성화 함수", """<ul>
<li><b>ReLU</b>: max(0, z). 빠르고 소실이 적음. 단점: 음수 쪽 기울기 0 → 영원히 0만 내는 <b>죽은 ReLU</b></li>
<li><b>LeakyReLU</b>: 음수에도 작은 기울기(<code>negative_slope=0.2</code>). leak = 조금씩 샌다</li>
<li><b>ELU</b>: 음수 쪽을 지수 함수로(−1에 수렴), 0 근처에서 매끄러움. <b>SELU</b>: ELU를 스케일 조정 → 조건(LeCun 초기화, Dense만 쌓기)이 맞으면 스스로 평균 0·분산 1 유지</li>
<li>대체로 SELU > ELU > LeakyReLU > ReLU > tanh > sigmoid (교과서 기준, 속도가 중요하면 ReLU)</li></ul>""")
+ _sec("④ 배치 정규화", """<ul>
<li>배치마다 층 입력의 평균을 0, 분산을 1로 맞춘 뒤 학습되는 γ(스케일)·β(이동)로 조정</li>
<li>이유: 어떤 뉴런은 ±10,000, 어떤 뉴런은 ±10이 나오면 뒤층에서 큰 값이 더 중요한 것처럼 취급됨 → 같은 스케일로</li>
<li>효과: 기울기 소실 감소, 큰 학습률 가능, 규제 효과. 파라미터는 특성마다 4개(γ, β는 학습 / 이동평균·이동분산은 학습 안 함)</li>
<li>퀴즈: 입력 바로 뒤의 BN → MNIST는 이미 같은 스케일이라 의미 없음 (문제는 없음)</li>
<li>활성화 앞에 넣을 땐 Dense에 activation 없이, <code>use_bias=False</code> (BN이 평균을 빼므로 편향이 무의미)</li></ul>""")
+ _sec("⑤ 드롭아웃 · 규제", f"""<ul>
<li><b>Dropout(rate=0.2)</b>: 훈련 때 매 스텝 뉴런의 20%를 랜덤으로 끔 → 특정 뉴런에 기대지 못하게 (반의 '철수' 비유). 평가·예측 땐 자동으로 꺼짐</li>
<li>그래서 훈련 정확도가 검증보다 낮게 나올 수 있음</li>
<li><b>L1·L2 규제</b>: 가중치 크기에 벌점 → 자세히 {_q('L1 L2 규제 자세히')}</li></ul>""")
+ _sec("⑥ 전이 학습 · 오토인코더", f"""<ul>
<li>비슷한 문제로 이미 훈련된 모델의 앞단(일반 특징)을 가져와 <b>동결</b>(trainable=False)하고 뒷단만 새로 학습 → 데이터·시간 절약. 어느 정도 되면 풀고 미세 조정</li>
<li>IBM Watson은 SVM 기반이라 병원마다 처음부터 다시 훈련 → 실패 사례</li>
<li>오토인코더 784→20→784: 입력을 그대로 복원하도록 학습. 정상 데이터로 학습하면 이상한 입력은 복원이 잘 안 됨 → 이상 탐지</li>
<li>코드: {_q('전이 학습')}</li></ul>""")
+ _sec("시험 포인트", "<ul><li>초기화-활성화 짝 (He-ReLU, LeCun-SELU, Glorot 기본값)</li><li>배치 정규화의 역할·위치·입력층 퀴즈</li><li>드롭아웃이 과적합을 줄이는 이유</li><li>Week4 과제(ELU+He+BN+NAG)가 이 장</li></ul>")
+ _sec("스스로 점검", "<ol><li>sigmoid로 깊게 쌓으면 왜 학습이 안 되나? (과제 변형 연습 4번 결과: 정확도 0.10)</li><li>BN을 활성화 앞에 넣을 때 use_bias=False인 이유는?</li><li>드롭아웃은 예측할 때도 작동하나?</li></ol>")
+ _sec("더 보기", f"{_q('초기화와 활성화 함수는 세트')} · {_q('배치 정규화')} · {_q('드롭아웃')} · {_q('죽은 렐루')} · {_q('Week4 변형')}"))

    # ================================================================== 4장 (2)
    card("4장 (2). 옵티마이저와 NumPy로 직접 짠 역전파", "4장 옵티마이저 numpy 역전파 feedforward 손실 경사 gradient sigmoid softmax d_output 체인 룰 sgd momentum nesterov adagrad rmsprop adam nadam 학습률",
code='''import numpy as np

def sigmoid(z):  return 1 / (1 + np.exp(-z))
def softmax(z):
    e = np.exp(z - z.max(axis=1, keepdims=True))
    return e / e.sum(axis=1, keepdims=True)

rng = np.random.default_rng(42)
X = rng.random((5, 784))                       # 이미지 5장 (펴진 상태)
Y = np.eye(10)[[3, 1, 4, 1, 5]]                # 원-핫 정답
W1, b1 = rng.normal(0, 0.1, (784, 16)), np.zeros(16)
W2, b2 = rng.normal(0, 0.1, (16, 16)), np.zeros(16)
W3, b3 = rng.normal(0, 0.1, (16, 10)), np.zeros(10)
lr = 0.5

for step in range(3):
    # 순전파: Z = 앞 출력 @ W + b,  A = 활성화(Z)
    Z1 = X @ W1 + b1;   A1 = sigmoid(Z1)
    Z2 = A1 @ W2 + b2;  A2 = sigmoid(Z2)
    Z3 = A2 @ W3 + b3;  output = softmax(Z3)
    loss = -np.mean(np.sum(Y * np.log(output + 1e-9), axis=1))   # 교차 엔트로피

    # 역전파 (체인 룰): 출력층은 softmax+CE라 '예측 - 정답'
    d_output = (output - Y) / len(X)
    dW3 = A2.T @ d_output;        db3 = d_output.sum(axis=0)
    dA2 = d_output @ W3.T;        dZ2 = dA2 * A2 * (1 - A2)     # sigmoid 미분 = a(1-a)
    dW2 = A1.T @ dZ2;             db2 = dZ2.sum(axis=0)
    dA1 = dZ2 @ W2.T;             dZ1 = dA1 * A1 * (1 - A1)
    dW1 = X.T @ dZ1;              db1 = dZ1.sum(axis=0)

    # 경사 하강: 가중치 -= 학습률 * 기울기
    for p, g in [(W1, dW1), (b1, db1), (W2, dW2), (b2, db2), (W3, dW3), (b3, db3)]:
        p -= lr * g
    print(step, round(loss, 4))''',
html=_sec("이 장에서 하는 것", f"<p>케라스가 fit 안에서 하는 순전파·손실·역전파·가중치 갱신을 NumPy로 한 단계씩 직접 계산한다. 교수님: \"요 노트북을 준 이유는 체인 룰로 기울기 구하는 과정을 보라고, 코드까지 보면 좋고\" (9/26). 노트북: {L('opt', 'feed forward')} → {L('opt', '손실 구하기')} → {L('opt', '경사 구하기 & Backpropagation')} → {L('opt', 'Gradients 정리')} → {L('opt', 'sigmoid 와 softmax')}</p>")
+ _sec("① 순전파", "<p>층마다 두 단계: <b>Z = A_앞 @ W + b</b> (곱하고 더하기) → <b>A = 활성화(Z)</b>. 마지막 층은 softmax로 확률.</p>")
+ _sec("② 손실", "<p>교차 엔트로피 −Σ y·log(ŷ): 정답 칸의 확률이 1에 가까울수록 0에 가까움. MSE는 (출력−정답)²의 평균.</p>")
+ _sec("③ 역전파 단계 (노트북 소제목 순서)", """<ol>
<li><b>출력층 Z에 대한 기울기</b>: softmax + 교차 엔트로피를 같이 미분하면 <b>output − Y</b> (그래서 둘을 짝으로 씀)</li>
<li><b>출력층 가중치 기울기</b>: ∂L/∂W3 = ∂L/∂Z3 × ∂Z3/∂W3, 그런데 Z3 = A2@W3라서 ∂Z3/∂W3 = A2 → <code>A2.T @ d_output</code> (앞 activation의 전치와 내적)</li>
<li><b>히든2 activation 기울기</b>: <code>d_output @ W3.T</code> (뒤에서 온 기울기를 가중치로 되돌려 보냄)</li>
<li><b>히든2 Z 기울기</b>: × sigmoid 미분 a(1−a)</li>
<li>같은 방식으로 히든1까지 → 모든 W, b의 기울기</li></ol>
<p>sigmoid 미분 a(1−a)는 최대 0.25 → 층마다 곱해지면 점점 작아짐 = <b>기울기 소실</b>의 정체</p>""")
+ _sec("④ 가중치 갱신", "<p><b>W ← W − η × dW</b>. η(에타)가 학습률. 이 한 줄을 다르게 하는 게 옵티마이저.</p>")
+ _sec("⑤ 옵티마이저 비교", """<table>
<tr><th>이름</th><th>아이디어</th><th>케라스</th></tr>
<tr><td>SGD</td><td>배치로 경사 하강. 느리지만 오래 돌리면 품질 좋음</td><td>SGD(learning_rate=0.01)</td></tr>
<tr><td>모멘텀</td><td>지난 기울기를 누적해 같은 방향이면 가속</td><td>SGD(momentum=0.9)</td></tr>
<tr><td>Nesterov (NAG)</td><td>모멘텀만큼 먼저 가 본 곳의 기울기 사용 → 더 빨리</td><td>SGD(momentum=0.9, nesterov=True)</td></tr>
<tr><td>AdaGrad</td><td>기울기 제곱 누적으로 나눠 축마다 스케일 맞춤. 너무 일찍 멈춤</td><td>Adagrad</td></tr>
<tr><td>RMSProp</td><td>최근 기울기만 반영(지수 이동 평균)해 그 문제 해결</td><td>RMSprop(rho=0.9)</td></tr>
<tr><td>Adam</td><td>모멘텀 + RMSProp (+ 초기 보정)</td><td>Adam(beta_1=0.9, beta_2=0.999)</td></tr>
<tr><td>Nadam</td><td>Nesterov + Adam</td><td>Nadam</td></tr></table>""")
+ _sec("⑥ sigmoid와 softmax", "<ul><li>sigmoid: 숫자 하나를 0~1로 (각자). 이진 분류 출력</li><li>softmax: 벡터를 합이 1인 확률 분포로 (함께). 다중 분류 출력</li></ul>")
+ _sec("스스로 점검", "<ol><li>출력층 기울기가 '예측 − 정답'이 되는 조건은?</li><li>dW3를 구할 때 A2를 전치하는 이유는?</li><li>sigmoid 층이 많으면 왜 앞쪽 기울기가 작아지나?</li><li>NAG와 모멘텀의 차이는?</li></ol>")
+ _sec("더 보기", f"{_q('NumPy')} · {_q('역전파를 자기 말로')} · {_q('옵티마이저 계보')} · {_q('옵티마이저만 바꿔 비교')}"))

    # ================================================================== 5장 (1)
    card("5장 (1). 텐서플로 기초: 텐서 · 연산 · 타입 · 변수 · 래그드 · 희소", "5장 12장 텐서 constant 연산 넘파이 변환 타입 변환 cast 문자열 유니코드 variable assign ragged sparse reorder",
code='''import tensorflow as tf
import numpy as np

t = tf.constant([[1., 2., 3.], [4., 5., 6.]])     # 행렬
print(t.shape, t.dtype)                            # (2, 3) float32
print(tf.constant(42))                             # 스칼라: shape=(), int32

print(t[:, 1:])                                    # 슬라이싱
print(t[..., 1, tf.newaxis])                       # 축 추가해 모양 유지
print(t + 10, tf.square(t), t @ tf.transpose(t))   # 브로드캐스팅, 원소별, 행렬곱
print(tf.reduce_mean(t), tf.reduce_sum(t))         # np.mean, np.sum 대신

a = np.array([2., 4., 5.])
print(tf.constant(a), t.numpy(), np.square(t))     # 넘파이 ↔ 텐서

t2 = tf.constant(40., dtype=tf.float64)
print(tf.constant(2.0) + tf.cast(t2, tf.float32))  # 타입은 직접 맞춰야 함

print(tf.constant("café"))                         # b'caf\\xc3\\xa9' (UTF-8)
u = tf.constant([ord(c) for c in "café"])          # [99 97 102 233]
print(tf.strings.unicode_encode(u, "UTF-8"))

v = tf.Variable([[1., 2., 3.], [4., 5., 6.]])
v.assign(2 * v); v[0, 1].assign(42.); v[:, 2].assign([0., 1.])
v.scatter_nd_update(indices=[[0, 0], [1, 2]], updates=[100., 200.])
print(v)

r = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6]])  # 행마다 길이가 다름
print(r, r.to_tensor())

s = tf.SparseTensor(indices=[[0, 1], [1, 0], [2, 3]], values=[1., 2., 3.], dense_shape=[3, 4])
print(tf.sparse.to_dense(s), tf.sparse.to_dense(s * 2.))
s5 = tf.SparseTensor(indices=[[0, 2], [0, 1]], values=[1., 2.], dense_shape=[3, 4])
print(tf.sparse.to_dense(tf.sparse.reorder(s5)))''',
html=_sec("이 장에서 하는 것", f"<p>케라스 아래에 있는 텐서플로를 직접 다룬다. 넘파이와 거의 같지만 GPU·자동 미분·그래프가 되는 '텐서'. 10/3 줌 보강. 노트북: {L('ch5', '텐서와 연산')} → {L('ch5', '타입 변환')} → {L('ch5', '문자열')} → {L('ch5', '변수')} → {L('ch5', 'Ragged Tensor(비정형) & Sparse Tensor(희소)')}</p>")
+ _sec("① 텐서플로란", "<ul><li>구글이 만든 넘파이 비슷한 라이브러리 + GPU/TPU, 분산, 계산 그래프(JIT), 자동 미분, 옵티마이저</li><li>스칼라(숫자) → 벡터(1차원) → 행렬(2차원) → 텐서(3차원 이상). TensorFlow = 텐서가 흐른다</li><li>케라스는 TF·PyTorch 위의 공통 상위 API</li></ul>")
+ _sec("② 텐서와 연산", """<ul>
<li><code>tf.constant</code>: 바꿀 수 없는 텐서. 연산하면 항상 새 텐서</li>
<li>기본 dtype: <b>float32 / int32</b> (넘파이는 64비트)</li>
<li>슬라이싱은 넘파이와 같음. <code>t[..., 1]</code>은 1차원으로 풀리고, <code>tf.newaxis</code>를 붙이면 세로 모양 유지</li>
<li>이름이 다른 것: np.mean → <b>tf.reduce_mean</b>, np.sum → tf.reduce_sum, np.log → tf.math.log, t.T → tf.transpose, np.dot → tf.matmul(@)</li>
<li><code>t @ tf.transpose(t)</code>: (2×3)@(3×2) = (2×2). 앞의 열 수 = 뒤의 행 수</li></ul>""")
+ _sec("③ 타입 변환이 자동으로 안 되는 이유 (교수님 질문 · 보너스)", "<p>int32 + float32, float32 + float64 모두 에러. <b>속도</b> 때문: 모든 연산에 '타입이 다르면 바꾼다'는 if가 들어가면 같은 타입이어도 매번 검사 → 수많은 데이터·층에서 느려짐. 사용자 의도와 다른 변환도 막음. → <code>tf.cast</code>로 직접.</p>")
+ _sec("④ 문자열", "<ul><li><code>tf.constant(\"café\")</code> → UTF-8 바이트 <code>b'caf\\xc3\\xa9'</code> (é는 2바이트)</li><li>코드값 [99, 97, 102, 233] ↔ <code>unicode_encode / unicode_decode</code>, 글자 수는 <code>tf.strings.length(..., unit=\"UTF8_CHAR\")</code></li><li>길이가 다른 문자열 여러 개를 디코드하면 래그드 텐서. \"나중에 필요하면 보면 될 것 같아\"</li></ul>")
+ _sec("⑤ 변수 tf.Variable", "<ul><li>가중치처럼 계속 바꿀 값. 바꿀 땐 <b>assign</b> (<code>v[1] = ...</code>는 TypeError)</li><li><code>v = v * 2</code>는 에러는 없지만 Variable이 아니라 새 Tensor가 됨</li><li>assign_add, scatter_nd_update(여러 위치 한 번에)</li></ul>")
+ _sec("⑥ 래그드·희소 텐서 (\"이 두 가지는 꼭 기억\")", """<ul>
<li><b>래그드</b>: 행마다 길이가 다른 데이터. 만드는 법 3가지(from_value_rowids / from_row_lengths / from_row_splits), 계산할 땐 to_tensor()</li>
<li><b>희소</b>: 대부분 0인 데이터(MNIST는 펜이 지난 곳 말고 다 0)를 0이 아닌 것만 저장 → 메모리 절약. indices·values·dense_shape</li>
<li>희소 텐서는 곱하기 외에는 안 됨(<code>s + 1.</code> 에러) → to_dense 후 계산, 행렬곱은 sparse_dense_matmul</li>
<li>s6 에러 = 인덱스 정렬 안 됨 → <code>tf.sparse.reorder</code></li></ul>""")
+ _sec("시험 포인트", "<ul><li>자동 형변환이 없는 이유와 tf.cast</li><li>Variable은 assign</li><li>희소 텐서 정렬 에러</li><li>reduce_* 이름</li></ul>")
+ _sec("스스로 점검", "<ol><li>tf.constant(2) + tf.constant(2.0)의 결과는?</li><li>v = v * 2 와 v.assign(v * 2)의 차이는?</li><li>희소 텐서를 쓰는 이유는?</li></ol>")
+ _sec("더 보기", f"{_q('자동 형변환')} · {_q('Variable과 assign')} · {_q('희소 텐서')} · {_q('래그드')}"))

    # ================================================================== 5장 (2)
    card("5장 (2). 사용자 정의 손실 · 활성화 · 초기화 · 규제 · 제약 · 지표", "5장 사용자 정의 손실 huber create_huber HuberLoss get_config custom_objects my_softplus initializer regularizer constraint 지표 metric 스트리밍 precision HuberMetric",
code='''import tensorflow as tf
from tensorflow import keras
from keras.saving import register_keras_serializable
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

housing = fetch_california_housing()
X_train_full, X_test, y_train_full, y_test = train_test_split(housing.data, housing.target.reshape(-1, 1), random_state=42)
X_train, X_valid, y_train, y_valid = train_test_split(X_train_full, y_train_full, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_valid_scaled = scaler.transform(X_valid)
input_shape = X_train.shape[1:]

# 1) 손실 클래스 (threshold까지 저장됨)
class HuberLoss(keras.losses.Loss):
    def __init__(self, threshold=1.0, **kwargs):
        self.threshold = threshold
        super().__init__(**kwargs)
    def call(self, y_true, y_pred):
        error = y_true - y_pred
        is_small_error = tf.abs(error) < self.threshold
        squared_loss = tf.square(error) / 2
        linear_loss = self.threshold * tf.abs(error) - self.threshold ** 2 / 2
        return tf.where(is_small_error, squared_loss, linear_loss)
    def get_config(self):
        base_config = super().get_config()
        return {**base_config, "threshold": self.threshold}

# 2) 활성화·초기화·규제·제약
def my_softplus(z):
    return tf.math.log(1.0 + tf.exp(z))
def my_glorot_initializer(shape, dtype=tf.float32):
    stddev = tf.sqrt(2. / (shape[0] + shape[1]))
    return tf.random.normal(shape, stddev=stddev, dtype=dtype)
def my_l1_regularizer(weights):
    return tf.reduce_sum(tf.abs(0.01 * weights))
def my_positive_weights(weights):
    return tf.where(weights < 0., tf.zeros_like(weights), weights)

model = keras.models.Sequential([
    keras.layers.Input(shape=input_shape),
    keras.layers.Dense(30, activation="selu", kernel_initializer="lecun_normal"),
    keras.layers.Dense(1, activation=my_softplus,
                       kernel_initializer=my_glorot_initializer,
                       kernel_regularizer=my_l1_regularizer,
                       kernel_constraint=my_positive_weights)])
model.compile(loss=HuberLoss(2.), optimizer="nadam", metrics=["mae"])
model.fit(X_train_scaled, y_train, epochs=2, validation_data=(X_valid_scaled, y_valid))

# 3) 저장·로드: 우리가 만든 것은 custom_objects로 알려 줘야 함
model.save("my_model_with_many_custom_parts.keras")
model = keras.models.load_model("my_model_with_many_custom_parts.keras",
    custom_objects={"HuberLoss": HuberLoss, "my_softplus": my_softplus,
                    "my_glorot_initializer": my_glorot_initializer,
                    "my_l1_regularizer": my_l1_regularizer,
                    "my_positive_weights": my_positive_weights})
print(model.loss.threshold)                        # 2.0

# 4) 스트리밍 지표
precision = keras.metrics.Precision()
print(float(precision([0, 1, 1, 1, 0, 1, 0, 1], [1, 1, 0, 1, 0, 1, 0, 1])))   # 0.8
print(float(precision([0, 1, 0, 0, 1, 0, 1, 1], [1, 0, 1, 1, 0, 0, 0, 0])))   # 0.5 (누적)
precision.reset_state()''',
html=_sec("이 장에서 하는 것", f"<p>케라스에 없는 손실·활성화·초기화·규제·제약·지표를 직접 만들어 끼우고, 저장·로드하는 법. 10/3·10/10. 노트북: {L('ch5', '사용자 정의 손실 함수')} → {L('ch5', '사용자 정의 요소를 가진 모델을 저장하고 로드하기')} → {L('ch5', '손실함수 Class')} → {L('ch5', '그외 사용자 정의 함수')} → {L('ch5', '사용자 정의 지표')} → {L('ch5', '스트리밍 지표')}</p>")
+ _sec("① 후버 손실 3단계", f"""<ol>
<li><b>함수</b> huber_fn: |오차|&lt;1이면 제곱/2, 아니면 |오차|−0.5. MSE는 큰 오차에서 폭주하니 큰 구간은 직선으로. <b>if 대신 tf.where</b> → 분기 없이 원소별로 둘 다 계산 후 고름(속도)</li>
<li><b>함수를 만드는 함수</b> create_huber(threshold): 기준을 바꿀 수 있음. 하지만 threshold가 모델에 저장 안 됨 → 로드할 때 <code>custom_objects={{"huber_fn": create_huber(2.0)}}</code>처럼 기억해서 다시 줘야 함</li>
<li><b>클래스</b> HuberLoss(keras.losses.Loss): <b>__init__</b>(값 저장, super 호출) · <b>call</b>(손실 계산, 매 배치) · <b>get_config</b>(save할 때 → threshold도 저장). 로드 땐 클래스 이름만</li></ol>
<p>자세히: {_q('후버 손실 3단계')}</p>""")
+ _sec("② 저장 파일에는 '이름'만", "<p>.keras 파일 안에는 가중치와 함께 <code>\"huber_fn\"</code> 같은 <b>문자열</b>만 들어 있음. 그래서 로드할 때 그 이름이 실제로 어떤 파이썬 함수/클래스인지 <code>custom_objects</code>로 알려 줘야 함. 케라스 내장 층·손실은 케라스가 이미 알아서 필요 없음. <code>@register_keras_serializable()</code>을 붙이면 등록돼서 생략 가능.</p>")
+ _sec("③ 그 밖의 사용자 정의 요소", """<table>
<tr><th>요소</th><th>예</th><th>넣는 자리</th></tr>
<tr><td>활성화</td><td>my_softplus: log(1+eᶻ)</td><td>activation=</td></tr>
<tr><td>초기화</td><td>my_glorot_initializer: 표준편차 √(2/(fan_in+fan_out))</td><td>kernel_initializer=</td></tr>
<tr><td>규제</td><td>my_l1_regularizer: Σ|0.01·w|를 손실에 더함</td><td>kernel_regularizer=</td></tr>
<tr><td>제약</td><td>my_positive_weights: 음수 가중치를 0으로</td><td>kernel_constraint=</td></tr></table>
<p>값(factor 등)을 저장하고 싶으면 클래스로 만들고 <code>__call__</code> + <code>get_config</code>.</p>""")
+ _sec("④ 손실 vs 지표", "<ul><li>손실: 미분 가능해야 하고 역전파에 쓰임</li><li>지표: 사람이 보는 값, 미분 안 돼도 됨 (정확도처럼)</li></ul>")
+ _sec("⑤ 스트리밍 지표 (10/10 ★★★)", """<ul>
<li><b>정밀도</b> = 양성이라고 한 것 중 진짜 양성 비율 TP/(TP+FP)</li>
<li>배치1 80%, 배치2 0% → 평균 40%는 틀림. 전체로 보면 8개 중 4개 = <b>50%</b></li>
<li>그래서 배치마다 TP·FP를 <b>누적</b>하는 지표가 필요 = 스트리밍 지표. <code>result()</code>로 현재 값, <code>reset_state()</code>로 초기화(교수님 노트북은 reset_states)</li>
<li>직접 만들기 HuberMetric(keras.metrics.Metric): <code>add_weight</code>로 total·count 변수 → <code>update_state</code>(누적) → <code>result</code>(total/count) → <code>get_config</code></li></ul>""")
+ _sec("시험 포인트", "<ul><li>후버: tf.where 이유, 3단계의 차이, create_huber의 문제점</li><li>custom_objects가 필요한 이유</li><li>클래스에서 꼭 만들 메서드 3개</li><li>정밀도 개념과 40% vs 50%</li></ul>")
+ _sec("스스로 점검", "<ol><li>loss=huber_fn 과 loss=create_huber(2.0)의 차이는?</li><li>get_config는 언제 불리나?</li><li>정확도와 정밀도의 차이는?</li></ol>")
+ _sec("더 보기", f"{_q('사용자 정의 손실')} · {_q('custom_objects')} · {_q('스트리밍')} · {_q('5장 함수·클래스 한 줄 설명')}"))

    # ================================================================== 6장 (1)
    card("6장 (1). 사용자 정의 층과 모델", "6장 사용자 정의 층 lambda MyDense build call get_config add_weight MyMultiLayer gaussian noise training ResidualBlock ResidualRegressor keras.Model",
code='''import tensorflow as tf
from tensorflow import keras

# 가중치 없는 층
exponential_layer = keras.layers.Lambda(lambda x: tf.exp(x))

# 가중치 있는 층
class MyDense(keras.layers.Layer):
    def __init__(self, units, activation=None, **kwargs):
        super().__init__(**kwargs)
        self.units = units
        self.activation = keras.activations.get(activation)
    def build(self, batch_input_shape):
        self.kernel = self.add_weight(name="kernel", shape=[batch_input_shape[-1], self.units],
                                      initializer="glorot_normal")
        self.bias = self.add_weight(name="bias", shape=[self.units], initializer="zeros")
        super().build(batch_input_shape)
    def call(self, X):
        return self.activation(X @ self.kernel + self.bias)
    def get_config(self):
        base_config = super().get_config()
        return {**base_config, "units": self.units,
                "activation": keras.activations.serialize(self.activation)}

# 입력 2개 → 출력 3개
class MyMultiLayer(keras.layers.Layer):
    def call(self, X):
        X1, X2 = X
        return X1 + X2, X1 * X2, X1 / X2

# 훈련 때만 다르게
class MyGaussianNoise(keras.layers.Layer):
    def __init__(self, stddev, **kwargs):
        super().__init__(**kwargs)
        self.stddev = stddev
    def call(self, X, training=None):
        if training:
            return X + tf.random.normal(tf.shape(X), stddev=self.stddev)
        return X

# 사용자 정의 모델
class ResidualBlock(keras.layers.Layer):
    def __init__(self, n_layers, n_neurons, **kwargs):
        super().__init__(**kwargs)
        self.hidden = [keras.layers.Dense(n_neurons, activation="elu", kernel_initializer="he_normal")
                       for _ in range(n_layers)]
    def call(self, inputs):
        Z = inputs
        for layer in self.hidden:
            Z = layer(Z)
        return inputs + Z

class ResidualRegressor(keras.Model):
    def __init__(self, output_dim, **kwargs):
        super().__init__(**kwargs)
        self.hidden1 = keras.layers.Dense(30, activation="elu", kernel_initializer="he_normal")
        self.block1 = ResidualBlock(2, 30)
        self.block2 = ResidualBlock(2, 30)
        self.out = keras.layers.Dense(output_dim)
    def call(self, inputs):
        Z = self.hidden1(inputs)
        for _ in range(1 + 3):
            Z = self.block1(Z)
        Z = self.block2(Z)
        return self.out(Z)

x = tf.ones((2, 8))
print(MyDense(3, activation="relu")(x).shape, ResidualRegressor(1)(x).shape)
print([t.shape for t in MyMultiLayer()((tf.ones((2, 4)), tf.ones((2, 4)) * 2))])''',
html=_sec("이 장에서 하는 것", f"<p>층과 모델을 클래스로 직접 만든다. 캘리포니아 집값(회귀) 데이터로 실습. 10/10. 노트북: {L('ch6', '사용자 정의 층')} → {L('ch6', '사용자 정의 Layer 2 - Dense Layer')} → {L('ch6', '사용자 정의 Layer 3')} → {L('ch6', '사용자 정의 Layer 4')} → {L('ch6', '사용자 정의 모델')}</p>")
+ _sec("① 가중치가 없는 층 → Lambda", "<p>입력에 정해진 계산만(예: e^x). 출력값이 양수이고 스케일이 크게 다를 때 출력층에 exp를 붙이면 유용.</p>")
+ _sec("② 가중치가 있는 층 → keras.layers.Layer 상속 (메서드가 언제 불리나)", """<table>
<tr><th>메서드</th><th>언제</th><th>하는 일</th></tr>
<tr><td>__init__</td><td>층을 만들 때</td><td>units·activation 같은 설정 저장, super().__init__(**kwargs)</td></tr>
<tr><td>build</td><td>처음 데이터가 들어올 때 (입력 크기를 알게 될 때)</td><td>add_weight로 kernel(가중치)·bias 생성</td></tr>
<tr><td>call</td><td>순전파 할 때마다 (교수님 질문 ★★★)</td><td>X @ kernel + bias → 활성화</td></tr>
<tr><td>get_config</td><td>save 할 때</td><td>units·activation도 저장되게 반환</td></tr></table>
<p><code>**kwargs</code>: name, dtype 같은 부모(Layer)가 아는 인자를 그대로 넘기려고. {_q('* 와 **')}</p>""")
+ _sec("③ 여러 입력·출력 층, 훈련 때만 다른 층", "<ul><li>MyMultiLayer: 입력을 (X1, X2)로 받아 세 결과 반환. 가중치가 없으니 call만. 함수형 API로 연결</li><li>MyGaussianNoise: <code>call(self, X, training=None)</code> → fit 할 땐 노이즈(강건해짐, 규제 효과), predict 할 땐 그대로</li></ul>")
+ _sec("④ 사용자 정의 모델 → keras.Model 상속", "<ul><li><b>ResidualBlock</b>: Dense 몇 개를 거친 결과에 원래 입력을 더함(<code>inputs + Z</code>, 스킵 연결). 하나의 층처럼 반복해서 끼워 쓰기 쉬움</li><li><b>ResidualRegressor</b>: __init__에서 층을 만들고 call에서 연결 순서를 코드로 씀 → 반복문·조건문도 쓸 수 있음(Sequential·함수형으론 어려운 구조)</li><li>저장·로드 땐 역시 custom_objects에 클래스 이름</li></ul>")
+ _sec("시험 포인트", "<ul><li>build / call / get_config 각각 언제</li><li>training 인자의 역할</li><li>잔차 블록이 하는 일</li><li>Lambda vs Layer 상속의 기준(가중치 유무)</li></ul>")
+ _sec("스스로 점검", "<ol><li>MyDense에서 kernel의 shape가 [입력 크기, units]인 이유는?</li><li>노이즈 층을 예측 때도 켜 두면?</li><li>keras.Model을 상속하면 Sequential보다 무엇이 좋은가?</li></ol>")
+ _sec("더 보기", f"{_q('사용자 정의 층')} · {_q('훈련 때만 노이즈')} · {_q('6장 함수·클래스 한 줄 설명')}"))

    # ================================================================== 6장 (2)
    card("6장 (2). 자동 미분 · 사용자 정의 훈련 반복 · tf.function · 파이썬 팁", "6장 gradienttape 편미분 수치 미분 watch 사용자 정의 훈련 반복 apply_gradients trainable_variables tf.function 데코레이터 *args **kwargs tf.where",
code='''import tensorflow as tf
from tensorflow import keras
import numpy as np

# 1) 미분
def f(w1, w2):
    return 3 * w1 ** 2 + 2 * w1 * w2
w1, w2 = tf.Variable(5.), tf.Variable(3.)
with tf.GradientTape() as tape:
    z = f(w1, w2)
print(tape.gradient(z, [w1, w2]))                  # [36, 10]

# 2) 훈련 반복 (fit 안에서 하는 일)
X_train = np.random.rand(1000, 8).astype("float32"); y_train = np.random.rand(1000, 1).astype("float32")
model = keras.models.Sequential([keras.layers.Input(shape=(8,)),
    keras.layers.Dense(30, activation="elu", kernel_initializer="he_normal",
                       kernel_regularizer=keras.regularizers.l2(0.05)),
    keras.layers.Dense(1, kernel_regularizer=keras.regularizers.l2(0.05))])

def random_batch(X, y, batch_size=32):
    idx = np.random.randint(len(X), size=batch_size)
    return X[idx], y[idx]

n_epochs, batch_size = 3, 32
n_steps = len(X_train) // batch_size
optimizer = keras.optimizers.Nadam(learning_rate=0.01)
loss_fn = keras.losses.MeanSquaredError()
mean_loss = keras.metrics.Mean()
metrics = [keras.metrics.MeanAbsoluteError()]

for epoch in range(1, n_epochs + 1):
    for step in range(1, n_steps + 1):
        X_batch, y_batch = random_batch(X_train, y_train)
        with tf.GradientTape() as tape:
            y_pred = model(X_batch, training=True)
            main_loss = tf.reduce_mean(loss_fn(y_batch, y_pred))
            loss = tf.add_n([main_loss] + model.losses)
        gradients = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))
        mean_loss(loss)
        for metric in metrics:
            metric(y_batch, y_pred)
    print(f"epoch {epoch}: loss {float(mean_loss.result()):.4f} mae {float(metrics[0].result()):.4f}")
    for metric in [mean_loss] + metrics:
        metric.reset_state()

# 3) tf.function
@tf.function
def tf_cube(x):
    return x ** 3
print(tf_cube(tf.constant(2.0)))''',
html=_sec("이 장에서 하는 것", f"<p>미분을 텐서플로가 자동으로 하게 하고(GradientTape), 그걸로 fit을 직접 짠 뒤(사용자 정의 훈련 반복), 함수를 그래프로 바꿔 빠르게 한다(tf.function). 10/10. 노트북: {L('ch6', '자동 미분을 사용하여 그레이디언트 계산하기')} → {L('ch6', '변수가 x 하나가 아닌 여러개 일때')} → {L('ch6', '사용자 정의 훈련 반복')} → {L('ch6', '텐서플로 함수')} → {L('ch6', 'Tips')}</p>")
+ _sec("① 미분 복습", "<ul><li>미분 = 그 점의 기울기. y = 3x² + 3이면 dy/dx = 6x, x=7 → <b>42</b></li><li>수치 미분: (f(x+0.001) − f(x)) / 0.001 ≈ 42.003 (작게 할수록 정확하지만 파라미터마다 계산해야 해서 비현실적)</li><li>편미분: 한 변수로만, 나머지는 상수. z = 3w₁² + 2w₁w₂, (5,3) → ∂z/∂w₁ = 6w₁+2w₂ = <b>36</b>, ∂z/∂w₂ = 2w₁ = <b>10</b>. 변수 여러 개면 '그래디언트'</li></ul>")
+ _sec("② GradientTape (\"주의사항\")", "<ul><li>with 블록 안의 계산을 기록 → 블록 <b>밖에서</b> <code>tape.gradient(z, [w1, w2])</code></li><li>미분할 값은 <b>tf.Variable</b>. 상수면 <b>None</b></li><li>상수를 쓰려면 <code>tape.watch(c1)</code></li><li>gradient는 한 번 부르면 테이프가 지워짐(여러 번이면 persistent=True)</li></ul>")
+ _sec("③ 사용자 정의 훈련 반복 (줄마다 의미)", """<ol>
<li><code>random_batch</code>: 배치 32개를 랜덤으로 뽑기</li>
<li><code>model(X_batch, training=True)</code>: 순전파(예측). training=True라서 드롭아웃·BN·노이즈가 훈련 모드</li>
<li><code>loss_fn</code> + <code>model.losses</code>: 주 손실 + 규제 손실(L2 등) 합</li>
<li><code>tape.gradient(loss, model.trainable_variables)</code>: 모든 학습 변수에 대한 기울기 = 역전파</li>
<li><code>optimizer.apply_gradients(zip(...))</code>: 가중치 갱신(옵티마이저 종류에 따라 계산 다름)</li>
<li><code>mean_loss</code>, <code>metrics</code>: 출력용(학습과 무관). epoch 끝에 <code>reset_state</code></li></ol>
<p>"fit하면 일어나는, 말로만 들었던 순전파·역전파를 직접 프로그램" → 이걸 이해하면 fit이 어떻게 돌아가는지 안다. 에폭 = 전체 한 바퀴, 배치 = 그 안의 묶음.</p>""")
+ _sec("④ tf.function과 데코레이터", "<ul><li>파이썬 함수를 계산에 최적화된 <b>그래프</b>로 바꿈 → 수업 예에서 약 33ms → 2ms (15배 이상)</li><li>변수가 텐서여야 이득. 넘파이 연산은 혜택 없음</li><li>매번 <code>tf.function(f)</code> 하는 걸 잊지 않게 정의 위에 <code>@tf.function</code> = <b>데코레이터</b>(함수를 받아 감싼 새 함수를 돌려주는 함수)</li><li>입력 타입마다 그래프를 따로 만듦(콘크리트 함수, 다형성)</li></ul>")
+ _sec("⑤ 파이썬 팁 (노트북 끝 Tips)", f"<ul><li><code>tf.where(조건, a, b)</code></li><li>함수도 변수에 담아 리턴 가능(gimeAddFunction) → create_huber와 같은 원리</li><li><code>*Names</code> 튜플, <code>**Names</code> 딕셔너리. hi2 TypeError → {_q('hi2')}</li><li>데코레이터 f1: 실행 전후로 Started/End 출력</li></ul>")
+ _sec("시험 포인트", "<ul><li>편미분 36, 10 계산</li><li>GradientTape 주의사항(Variable / None / watch)</li><li>훈련 반복 각 줄의 의미, apply_gradients</li><li>tf.function과 데코레이터</li><li>*args / **kwargs</li></ul>")
+ _sec("스스로 점검", "<ol><li>tape.gradient를 with 블록 안에서 부르면?</li><li>model.losses에는 무엇이 들어 있나?</li><li>훈련 반복에서 training=True를 빼면?</li><li>데코레이터를 자기 말로 설명하면?</li></ol>")
+ _sec("더 보기", f"{_q('GradientTape 주의사항')} · {_q('사용자 정의 훈련 반복')} · {_q('tf.function과 데코레이터')}"))

    # ================================================================== 7장
    card("7장. 합성곱 신경망 (CNN)", "7장 14장 cnn 합성곱 convolution 필터 커널 특성 맵 패딩 same valid 스트라이드 풀링 max average 파라미터 Conv2D MaxPool2D 엣지 소벨 수용장 lenet vgg resnet",
code='''import tensorflow as tf
from tensorflow import keras
import numpy as np
from sklearn.datasets import load_sample_image

# 1) 필터를 직접 만들어 합성곱
china = load_sample_image("china.jpg") / 255
flower = load_sample_image("flower.jpg") / 255
images = np.array([china, flower]).astype(np.float32)   # (2, 427, 640, 3)
batch_size, height, width, channels = images.shape

filters = np.zeros(shape=(7, 7, channels, 2), dtype=np.float32)   # (높이, 너비, 입력 채널, 필터 수)
filters[:, 3, :, 0] = 1                                 # 세로선
filters[3, :, :, 1] = 1                                 # 가로선
outputs = tf.nn.conv2d(images, filters, strides=1, padding="SAME")
print(outputs.shape)                                    # (2, 427, 640, 2)

# 2) 크기 변화
x = tf.random.normal((1, 28, 28, 1))
print(keras.layers.Conv2D(8, 3, padding="valid")(x).shape)          # 26
print(keras.layers.Conv2D(8, 3, padding="same")(x).shape)           # 28
print(keras.layers.Conv2D(8, 3, strides=2, padding="same")(x).shape) # 14
print(keras.layers.MaxPool2D(pool_size=2)(x).shape)                 # 14

# 3) Fashion MNIST CNN
(X_train_full, y_train_full), (X_test, y_test) = keras.datasets.fashion_mnist.load_data()
X_train_full = X_train_full[..., np.newaxis] / 255.     # 채널 축 추가 (28, 28, 1)
X_test = X_test[..., np.newaxis] / 255.
X_train, X_valid = X_train_full[:-5000], X_train_full[-5000:]
y_train, y_valid = y_train_full[:-5000], y_train_full[-5000:]

model = keras.models.Sequential([
    keras.layers.Input(shape=[28, 28, 1]),
    keras.layers.Conv2D(32, kernel_size=3, padding="same", activation="relu"),
    keras.layers.MaxPool2D(2),
    keras.layers.Conv2D(64, kernel_size=3, padding="same", activation="relu"),
    keras.layers.MaxPool2D(2),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(10, activation="softmax")])
model.summary()                                         # 320, 18,496, 401,536, 1,290 = 421,642
model.compile(loss="sparse_categorical_crossentropy", optimizer="nadam", metrics=["accuracy"])
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_valid, y_valid))
model.evaluate(X_test, y_test)''',
html=_sec("이 장에서 하는 것", f"<p>이미지를 784로 펴지 않고 2차원 그대로 보는 합성곱 층과 풀링 층을 이해하고, CNN으로 Fashion MNIST·숫자를 분류해 MLP와 비교한다. 10/17. 노트북: {L('ch7a', '합성곱이란 무엇인가?')} → {L('ch7a', '합성곱 층')} → {L('ch7a', 'VALID vs SAME 패딩')} → {L('ch7a', '풀링 층')} → {L('ch7a', 'CNN으로 패션 MNIST 문제 풀기')} / {L('ch7b', 'Convolution')} → {L('ch7b', 'CNN을 이용한 Digit Recognition')} → {L('ch7b', 'MLP 과 CNN 의 예측 비교')}</p>")
+ _sec("① 왜 CNN인가", "<ul><li>MLP는 이미지를 784로 펴서 <b>이웃 픽셀 정보</b>를 버림. 큰 컬러 사진(1024×768×3)이면 Dense 가중치가 폭발</li><li>고양이 실험(Hubel & Wiesel): 시각 뉴런은 시야의 일부(<b>국부 수용장</b>), 특정 각도의 선에만 반응 → 작은 필터를 이미지 전체에 밀며 보는 구조</li></ul>")
+ _sec("② 합성곱과 용어", "<ul><li>필터(=커널=디텍터)를 이미지에 얹고 원소끼리 곱해 모두 더한 값 하나 → 한 칸씩 옮기며 반복 → 결과 = <b>특성 맵</b></li><li>소벨 필터 [-1,0,1]/[-2,0,2]/[-1,0,1]: 고른 영역은 0, 경계만 큰 값 → 엣지(면과 면의 경계)</li><li>세로선 필터 → 세로 경계, 가로선 필터 → 가로 경계. 필터 여러 개 → 특성 맵 여러 장</li><li>입력이 여러 채널(RGB)이면 필터 하나가 모든 채널을 관통해 계산 → 특성 맵 1장</li><li><b>CNN에선 필터 값을 사람이 정하지 않고 학습</b> (\"컨볼루션은 엣지 디텍션 용도로 쓰는 게 아니야\")</li></ul>")
+ _sec("③ 패딩 · 스트라이드 · 출력 크기", """<ul>
<li><b>valid</b>: 패딩 없음 → 출력 = 입력 − 커널 + 1 (28, 3×3 → 26)</li>
<li><b>same</b>: 0을 둘러 채워 (스트라이드 1이면) 크기 유지 → "same = 해상도 같게"</li>
<li><b>스트라이드 2</b>: 두 칸씩 → 크기 절반 (차원 축소)</li>
<li>공식: valid = ⌊(입력 − 커널)/스트라이드⌋ + 1, same = ⌈입력/스트라이드⌉</li></ul>""")
+ _sec("④ 풀링", "<ul><li>목적: 데이터 양을 줄임(계산·메모리·뒤 연결 감소), 작은 위치 변화에 덜 민감</li><li>MaxPool2D(2): 2×2에서 최댓값 → 가로·세로 절반, 전체 1/4</li><li>max가 average보다 보통 더 잘 맞고 더 빠름(큰 값만 고르면 됨)</li><li><b>파라미터 0</b> (\"그냥 칸만 있는 거야\")</li><li>깊이 방향 풀링(채널 방향), 전역 평균 풀링(특성 맵마다 평균 하나)도 있음</li></ul>")
+ _sec("⑤ 파라미터 수 (이미지 크기와 무관)", "<ul><li>Conv2D = (커널 높이 × 너비 × <b>입력 채널</b> + 1) × 필터 수</li><li>conv1: (3×3×1+1)×32 = <b>320</b>, conv2: (3×3×<b>32</b>+1)×64 = <b>18,496</b> (앞 층 필터 32개 = 입력 채널 32)</li><li>Flatten 뒤 Dense(128): 7×7×64 = 3,136 → 401,536. 합계 421,642</li><li>이미지 크기가 식에 없음 → 사진이 커져도 합성곱 층 파라미터는 그대로</li></ul>")
+ _sec("⑥ CNN 구조 흐름", "<ul><li>합성곱 → 풀링 → 합성곱 → 풀링 … → Flatten → Dense → softmax. 뒤로 갈수록 크기는 줄고 필터 수는 늘림(32 → 64 → 128)</li><li>3×3을 연속으로 쌓으면 5×5·7×7을 보는 효과 + 파라미터 적음(27 vs 49)</li><li>LeNet-5 → AlexNet → VGG → GoogLeNet → ResNet(잔차 연결). ImageNet 대회는 사람보다 정확해져서 끝남, 학습된 가중치를 공개 → 전이 학습</li><li>비전 과제: 분류 → 분류+위치 → 객체 검출 → 분할 (분류만으로 자율주행은 안 됨)</li></ul>")
+ _sec("⑦ 코드에서 주의", "<ul><li>Conv2D 입력은 (높이, 너비, 채널) → 흑백 MNIST는 <code>[..., np.newaxis]</code>로 채널 1 추가</li><li>7-2 노트북의 <code>keras.layers.core</code> import는 지금 버전에서 에러 → <code>keras.layers</code></li></ul>")
+ _sec("시험 포인트", "<ul><li>파라미터 320·18,496과 이유, 이미지 크기와 무관</li><li>same / valid, 스트라이드, 출력 크기</li><li>풀링의 목적·파라미터 0·max가 나은 이유</li><li>필터는 학습됨</li><li>MLP 대비 CNN의 장점</li></ul>")
+ _sec("스스로 점검", "<ol><li>입력 (32, 32, 3)에 Conv2D(16, 5, padding='valid')를 쓰면 출력 크기와 파라미터 수는? (28×28×16, (5×5×3+1)×16 = 1,216)</li><li>풀링층에 파라미터가 없는 이유는?</li><li>3×3 두 번과 5×5 한 번의 차이는?</li></ol>")
+ _sec("더 보기", f"{_q('합성곱 = 필터로 엣지 찾기')} · {_q('패딩 · 스트라이드 · 풀링')} · {_q('CNN 파라미터')} · {_q('CNN 구조')}"))

    # ================================================================== 시험 당일
    card("시험 당일 순서", "시험 당일 순서 체크리스트 colab 시작 제출 마크다운 시간",
html=_sec("시작하자마자", """<ol>
<li>교수님 Colab을 열고 <b>사본 저장/본인 이름</b> 확인, 런타임 유형(GPU) 확인</li>
<li>맨 위 import 셀부터 순서대로 실행 (중간부터 돌리면 NameError)</li>
<li>문제를 전부 훑어보고 쉬운 것(집계 한 줄, 사양대로 모델)부터</li></ol>""")
+ _sec("문제 유형별", """<table>
<tr><th>유형</th><th>할 일</th><th>사이트</th></tr>
<tr><td>Pandas 집계</td><td>value_counts / nunique / groupby().agg / 필터 / 정렬 / pivot_table</td><td>Pandas, [Week3] 연습</td></tr>
<tr><td>사양대로 모델</td><td>Import → Data → Model → Compile → Learning → Evaluation 셀 나누기, 끝에 "정리" 마크다운</td><td>[Week4] 연습, 빈칸 채우기</td></tr>
<tr><td>값 바꿔 비교</td><td>하나만 바꾸고 결과 비교 + 이유</td><td>바꾸면 이렇게 된다</td></tr>
<tr><td>에러 수정</td><td>첫 에러부터, 원인·수정을 마크다운으로</td><td>노트북 에러 수정</td></tr>
<tr><td>설명 서술</td><td>무엇을·왜·어떻게를 자기 말로 짧게</td><td>교수님 강조, 6주차 형식</td></tr></table>""")
+ _sec("서술 쓰는 틀", "<ul><li>개념: \"○○는 ~하는 것이다. ~때문에 쓴다.\" (단어를 단어로 설명하지 않기)</li><li>결과: \"정확도가 a에서 b로 바뀌었다. ~때문이다.\"</li><li>에러: \"~해서 ○○Error가 났다. ~로 고쳤다.\"</li></ul>")
+ _sec("시간이 오래 걸릴 때", "<ul><li>epochs를 줄여서 먼저 돌아가는지 확인 → 마지막에 원래 값으로</li><li>탐색(그리드 등)은 데이터 일부로</li></ul>")
+ _sec("끝내기 전에", "<ol><li>모든 셀이 출력까지 있는지(실행 결과가 남아 있어야 함)</li><li>마크다운 설명 빠진 곳 없는지</li><li>.ipynb 제출 = 시험 종료이므로 마지막에</li></ol>"))

    # ================================================================== 보강: 데이터 증강, L1/L2
    card("데이터 증강 코드 (9/19 과제)", "데이터 증강 augmentation RandomRotation RandomTranslation 회전 이동 torchvision 손글씨 개선 과제",
code='''import tensorflow as tf
from tensorflow import keras
import numpy as np

(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()
X_train = X_train[..., np.newaxis].astype("float32") / 255     # (60000, 28, 28, 1)
X_test = X_test[..., np.newaxis].astype("float32") / 255

# 방법 1) 케라스 층으로: 훈련 때만 랜덤 변형 (predict 때는 그대로)
augment = keras.Sequential([
    keras.layers.RandomRotation(30 / 360),          # ±30도 (값은 한 바퀴 대비 비율)
    keras.layers.RandomTranslation(0.1, 0.1),       # 위아래·좌우 10% 이동
])
model = keras.Sequential([
    keras.layers.Input(shape=(28, 28, 1)),
    augment,
    keras.layers.Flatten(),
    keras.layers.Dense(16, activation="relu"),
    keras.layers.Dense(16, activation="relu"),
    keras.layers.Dense(10, activation="softmax")])
model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(X_train, y_train, epochs=1, batch_size=128)

# 방법 2) 교수님 노트북처럼 변형한 이미지를 미리 만들어 데이터에 붙이기
X_aug = augment(X_train[:1000], training=True).numpy()   # 변형본 (예시로 1000장)
X_big = np.concatenate([X_train[:1000], X_aug], axis=0)
y_big = np.concatenate([y_train[:1000], y_train[:1000]], axis=0)
print(X_big.shape, y_big.shape)                           # (2000, 28, 28, 1)''',
html="""<ul>
<li><b>왜</b>: MNIST 글씨 스타일에 과적합 → 내가 쓴 숫자(위치·기울기가 다름)를 못 맞힘. 회전·이동한 이미지를 더 보여 주면 변화에 강해짐</li>
<li><b>교수님 노트북 방식</b>: torchvision의 <code>RandomRotation(degrees=(-30, 30))</code>, <code>RandomAffine(translate=(0.1, 0.1))</code>로 60,000장 변형본을 만들어 원본과 합쳐 120,000장 → <code>reshape(120000, 784)</code> 후 학습 (Colab엔 torchvision이 있음)</li>
<li><b>케라스 층 방식</b>: 모델 안에 Random 층을 넣으면 매 epoch 다른 변형을 자동으로, 예측 땐 꺼짐</li>
<li>주의: 변형본을 붙였으면 라벨도 똑같이 붙여야 하고, reshape 개수(120000)도 바뀜 (3장 노트북 에러 <code>cannot reshape array of size ... into shape (120000,784)</code>는 앞 셀 실패 때문)</li>
</ul>""")

    card("L1 L2 규제 자세히", "L1 L2 규제 regularizer kernel_regularizer l1 l2 l1_l2 가중치 감쇠 과적합 model.losses",
code='''import tensorflow as tf
from tensorflow import keras

layer_l2 = keras.layers.Dense(100, activation="elu", kernel_initializer="he_normal",
                              kernel_regularizer=keras.regularizers.l2(0.01))
layer_l1 = keras.layers.Dense(100, kernel_regularizer=keras.regularizers.l1(0.01))
layer_both = keras.layers.Dense(100, kernel_regularizer=keras.regularizers.l1_l2(l1=0.01, l2=0.01))

model = keras.Sequential([keras.layers.Input(shape=(8,)), layer_l2, keras.layers.Dense(1)])
model(tf.ones((1, 8)))
print(model.losses)           # 규제 손실: fit이 주 손실에 자동으로 더함 (사용자 정의 훈련 반복의 model.losses)''',
html="""<ul>
<li><b>목적</b>: 가중치가 너무 커지지 않게 손실에 벌점을 더해 과적합을 줄임 (교수님은 9/26에 "다음에 설명"하고 넘어감)</li>
<li><b>L2</b>: 벌점 = 계수 × Σw² → 가중치를 전체적으로 작게(0 근처로) 만듦. 가장 흔함 (가중치 감쇠)</li>
<li><b>L1</b>: 벌점 = 계수 × Σ|w| → 쓸모없는 가중치를 정확히 0으로 만들어 희소한 모델</li>
<li><b>계수(0.01 등)</b>: 크면 규제가 세서 과소적합, 작으면 효과 약함</li>
<li>5장의 my_l1_regularizer가 바로 L1을 직접 구현한 것 (Σ|0.01·w|)</li>
<li>드롭아웃·조기 종료·데이터 증강과 함께 과적합을 줄이는 방법</li>
</ul>""")
