# Week4 과제("다음과 같은 신경망을 만들어 mnist 숫자 인식을 학습하시오")와 같은 형식의 변형 연습 10문제
# 각 답은 혼자서 돌아가도록 import·데이터 준비까지 포함. 결과 수치는 실제 실행값(RESULTS)으로 채움.

SECTIONS_PRACTICE = [("practice", "Week4 변형 연습")]

_DATA_MNIST = '''import tensorflow as tf
from tensorflow import keras
import numpy as np

(X_train_full, y_train_full), (X_test, y_test) = keras.datasets.mnist.load_data()
X_train_full = X_train_full.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0
X_train, X_valid = X_train_full[:-5000], X_train_full[-5000:]
y_train, y_valid = y_train_full[:-5000], y_train_full[-5000:]
'''
_DATA_FASHION = _DATA_MNIST.replace("keras.datasets.mnist", "keras.datasets.fashion_mnist")

_EVAL = '''
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"테스트 정확도: {test_acc:.4f}")'''

P = []   # (번호, 제목, kw, 문제 html, 답 code, 정리 html)

def _spec(intro, items):
    return f"<p>{intro}</p><ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"

# ---------------------------------------------------------------- 1
P.append((1, "Fashion MNIST · ReLU · He · Adam · 배치 정규화 · 드롭아웃", "fashion relu he adam batchnormalization dropout 0.2 300 100",
_spec("Fashion MNIST를 학습하는 신경망을 만들고 테스트 정확도를 확인하시오.",
      ["Hidden: 300개, 100개 (2개)", "Activation: ReLU, Initializer: He", "각 은닉층 뒤 배치 정규화, 출력층 앞 Dropout 0.2",
       "Optimizer: Adam (learning_rate=0.001)", "Output: Softmax 10개, 10 epoch"]),
_DATA_FASHION + '''
model = keras.Sequential([
    keras.layers.Input(shape=(28, 28)),
    keras.layers.Flatten(),
    keras.layers.Dense(300, activation="relu", kernel_initializer="he_normal"),
    keras.layers.BatchNormalization(),
    keras.layers.Dense(100, activation="relu", kernel_initializer="he_normal"),
    keras.layers.BatchNormalization(),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation="softmax")
])
model.compile(loss="sparse_categorical_crossentropy",
              optimizer=keras.optimizers.Adam(learning_rate=0.001),
              metrics=["accuracy"])
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_valid, y_valid))''' + _EVAL,
"""<ul><li>데이터만 <code>fashion_mnist</code>로 바뀜 (입력 28×28, 출력 10개는 같음 → 9/12 "숫자 모델을 Fashion에 써도 되나?" → 된다)</li>
<li>Fashion은 숫자보다 어려워서 정확도가 낮게 나옴</li>
<li>Dropout은 학습 때만 동작, evaluate·predict 때는 꺼짐</li></ul>"""))

# ---------------------------------------------------------------- 2
P.append((2, "은닉층 3개 · SELU · LeCun · Nadam", "selu lecun_normal nadam 3층 256 128 64 자기 정규화",
_spec("MNIST 숫자 인식 신경망을 만드시오.",
      ["Hidden: 256개, 128개, 64개 (3개)", "Activation: SELU, Initializer: LeCun normal", "배치 정규화 없음",
       "Optimizer: Nadam", "Output: Softmax, 10 epoch"]),
_DATA_MNIST + '''
model = keras.Sequential([keras.layers.Input(shape=(28, 28)), keras.layers.Flatten()])
for n in [256, 128, 64]:
    model.add(keras.layers.Dense(n, activation="selu", kernel_initializer="lecun_normal"))
model.add(keras.layers.Dense(10, activation="softmax"))
model.compile(loss="sparse_categorical_crossentropy",
              optimizer=keras.optimizers.Nadam(),
              metrics=["accuracy"])
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_valid, y_valid))''' + _EVAL,
"""<ul><li>SELU는 LeCun 초기화와 세트 (9/26 "초기화와 활성화는 같이 간다")</li>
<li>SELU는 스스로 평균 0·분산 1을 유지하도록 만든 활성화라 배치 정규화 없이 씀</li>
<li>Nadam = Nesterov + Adam</li>
<li>층을 반복문으로 <code>model.add</code> 해도 됨 (Sequential 두 번째 방법)</li></ul>"""))

# ---------------------------------------------------------------- 3
P.append((3, "LeakyReLU · He · RMSProp · 배치 정규화를 활성화 앞에", "leakyrelu negative_slope rmsprop batchnormalization 활성화 앞 use_bias False",
_spec("MNIST 숫자 인식 신경망을 만드시오.",
      ["Hidden: 200개, 100개", "Activation: LeakyReLU (기울기 0.2), Initializer: He",
       "배치 정규화를 <b>활성화 함수 앞</b>에 적용", "Optimizer: RMSprop (learning_rate=0.001)", "10 epoch"]),
_DATA_MNIST + '''
model = keras.Sequential([
    keras.layers.Input(shape=(28, 28)),
    keras.layers.Flatten(),
    keras.layers.Dense(200, kernel_initializer="he_normal", use_bias=False),
    keras.layers.BatchNormalization(),
    keras.layers.LeakyReLU(negative_slope=0.2),
    keras.layers.Dense(100, kernel_initializer="he_normal", use_bias=False),
    keras.layers.BatchNormalization(),
    keras.layers.LeakyReLU(negative_slope=0.2),
    keras.layers.Dense(10, activation="softmax")
])
model.compile(loss="sparse_categorical_crossentropy",
              optimizer=keras.optimizers.RMSprop(learning_rate=0.001),
              metrics=["accuracy"])
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_valid, y_valid))''' + _EVAL,
"""<ul><li>활성화를 Dense 안에 넣지 않고 따로 층으로 빼야 BN을 그 사이에 넣을 수 있음 (Week4 제출본과 같은 구조)</li>
<li>BN이 평균을 빼므로 Dense의 편향은 의미 없음 → <code>use_bias=False</code></li>
<li>LeakyReLU 기울기 인자: Keras 3은 <code>negative_slope</code> (교수님 4장 코드의 <code>alpha=0.2</code>는 아직 돌아가지만 경고가 뜸)</li></ul>"""))

# ---------------------------------------------------------------- 4
P.append((4, "sigmoid · 기본 초기화 · 기본 SGD → ReLU와 비교", "sigmoid 기울기 소실 vanishing 비교 sgd 기본 glorot relu 차이",
_spec("같은 구조에서 활성화만 바꿔 정확도를 비교하고, 차이의 이유를 쓰시오.",
      ["Hidden: 100개 × 4개 (깊게)", "A: Activation sigmoid / B: Activation ReLU (+He)",
       "Initializer: A는 지정 안 함(기본값), Optimizer: SGD (learning_rate=0.01)", "각 5 epoch"]),
_DATA_MNIST + '''
def build(act, init):
    model = keras.Sequential([keras.layers.Input(shape=(28, 28)), keras.layers.Flatten()])
    for _ in range(4):
        model.add(keras.layers.Dense(100, activation=act, kernel_initializer=init))
    model.add(keras.layers.Dense(10, activation="softmax"))
    model.compile(loss="sparse_categorical_crossentropy",
                  optimizer=keras.optimizers.SGD(learning_rate=0.01), metrics=["accuracy"])
    return model

for act, init in [("sigmoid", "glorot_uniform"), ("relu", "he_normal")]:
    model = build(act, init)
    model.fit(X_train, y_train, epochs=5, validation_data=(X_valid, y_valid), verbose=0)
    print(act, "테스트 정확도:", round(model.evaluate(X_test, y_test, verbose=0)[1], 4))''',
"""<ul><li>sigmoid는 5 epoch 동안 거의 학습이 안 됨(정확도 약 10%) → <b>기울기 소실</b>: 층을 깊게 쌓으면 역전파 때 앞층의 기울기가 0에 가까워짐 (9/19·9/26)</li>
<li>초기화를 지정 안 하면 기본값 Glorot(glorot_uniform) (9/26 "여러분이 아무것도 안 줬을 때 사실 이걸 쓰고 있던 거야")</li>
<li>ReLU는 He 초기화와 세트</li></ul>"""))

# ---------------------------------------------------------------- 5
P.append((5, "Flatten 빼고 reshape · 원-핫 · categorical_crossentropy (9/19 수업 실습)", "flatten reshape 784 원핫 to_categorical categorical_crossentropy 9/19 실습 변형",
_spec("Week4 모델을 다음처럼 바꾸시오.",
      ["Flatten 층을 쓰지 말고 데이터를 (샘플 수, 784)로 reshape해서 입력", "라벨을 원-핫으로 바꾸고 손실은 categorical_crossentropy",
       "나머지(200·100, ELU, He, NAG 0.9, 배치 정규화)는 Week4와 같음", "10 epoch"]),
_DATA_MNIST + '''
X_train, X_valid, X_test = X_train.reshape(-1, 784), X_valid.reshape(-1, 784), X_test.reshape(-1, 784)
y_train, y_valid, y_test = (keras.utils.to_categorical(y, 10) for y in (y_train, y_valid, y_test))

model = keras.Sequential([
    keras.layers.Input(shape=(784,)),
    keras.layers.Dense(200, kernel_initializer="he_normal", use_bias=False),
    keras.layers.BatchNormalization(),
    keras.layers.Activation("elu"),
    keras.layers.Dense(100, kernel_initializer="he_normal", use_bias=False),
    keras.layers.BatchNormalization(),
    keras.layers.Activation("elu"),
    keras.layers.Dense(10, activation="softmax")
])
model.compile(loss="categorical_crossentropy",
              optimizer=keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True),
              metrics=["accuracy"])
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_valid, y_valid))''' + _EVAL,
"""<ul><li>입력 모양이 (784,)로 바뀌므로 <code>Input(shape=(784,))</code></li>
<li>원-핫 라벨 + categorical_crossentropy, 정수 라벨 + sparse_categorical_crossentropy. 섞으면 <code>Shapes ... are incompatible</code> 에러</li>
<li>결과는 Week4와 거의 같음 (같은 모델을 다르게 표현했을 뿐)</li></ul>"""))

# ---------------------------------------------------------------- 6
P.append((6, "옵티마이저만 바꿔 비교 (9/26 실습 · 10/10 \"옵티마이저 바꿔 보기\")", "옵티마이저 비교 sgd momentum nesterov adagrad rmsprop adam nadam 학습률 발산 learning rate 1.0",
_spec("Week4 모델에서 옵티마이저만 바꿔 3 epoch 검증 정확도를 비교하시오. 학습률을 1.0으로 키우면 어떻게 되는지도 확인하시오.",
      ["SGD / SGD+모멘텀 0.9 / NAG / Adagrad / RMSprop / Adam / Nadam", "Adam(learning_rate=1.0)"]),
_DATA_MNIST + '''
def build():
    return keras.Sequential([
        keras.layers.Input(shape=(28, 28)), keras.layers.Flatten(),
        keras.layers.Dense(200, kernel_initializer="he_normal", use_bias=False),
        keras.layers.BatchNormalization(), keras.layers.Activation("elu"),
        keras.layers.Dense(100, kernel_initializer="he_normal", use_bias=False),
        keras.layers.BatchNormalization(), keras.layers.Activation("elu"),
        keras.layers.Dense(10, activation="softmax")])

optimizers = {
    "SGD": lambda: keras.optimizers.SGD(learning_rate=0.01),
    "모멘텀": lambda: keras.optimizers.SGD(learning_rate=0.01, momentum=0.9),
    "NAG": lambda: keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True),
    "Adagrad": lambda: keras.optimizers.Adagrad(learning_rate=0.01),
    "RMSprop": lambda: keras.optimizers.RMSprop(learning_rate=0.001),
    "Adam": lambda: keras.optimizers.Adam(learning_rate=0.001),
    "Nadam": lambda: keras.optimizers.Nadam(learning_rate=0.001),
    "Adam lr=1.0": lambda: keras.optimizers.Adam(learning_rate=1.0),
}
for name, make in optimizers.items():
    model = build()
    model.compile(loss="sparse_categorical_crossentropy", optimizer=make(), metrics=["accuracy"])
    h = model.fit(X_train, y_train, epochs=3, validation_data=(X_valid, y_valid), verbose=0)
    print(f"{name:12s} val_accuracy {h.history['val_accuracy'][-1]:.4f}")''',
"""<ul><li>옵티마이저 객체는 모델마다 <b>새로 만들어야</b> 함 (그래서 lambda로 매번 생성)</li>
<li>기본 SGD는 3 epoch에선 느림 → 모멘텀·NAG로 빨라짐. Adam·Nadam이 보통 빠르게 좋음 (9/26)</li>
<li>학습률이 너무 크면 크게 흔들리다 발산 → 정확도가 떨어짐 (9/26 "너무 크면 발산")</li></ul>"""))

# ---------------------------------------------------------------- 7
P.append((7, "콜백: ModelCheckpoint · EarlyStopping (9/12·9/19)", "callback 콜백 earlystopping patience restore_best_weights modelcheckpoint save_best_only epochs 100",
_spec("Week4 모델을 다음 조건으로 학습하시오.",
      ["epochs=100으로 주되, 검증 손실이 5 epoch 동안 나아지지 않으면 멈추고 가장 좋았던 가중치로 되돌릴 것",
       "가장 좋은 모델을 <code>best_mnist.keras</code>로 저장", "저장한 모델을 불러와 테스트 정확도 확인"]),
_DATA_MNIST + '''
model = keras.Sequential([
    keras.layers.Input(shape=(28, 28)), keras.layers.Flatten(),
    keras.layers.Dense(200, kernel_initializer="he_normal", use_bias=False),
    keras.layers.BatchNormalization(), keras.layers.Activation("elu"),
    keras.layers.Dense(100, kernel_initializer="he_normal", use_bias=False),
    keras.layers.BatchNormalization(), keras.layers.Activation("elu"),
    keras.layers.Dense(10, activation="softmax")])
model.compile(loss="sparse_categorical_crossentropy",
              optimizer=keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True),
              metrics=["accuracy"])

checkpoint_cb = keras.callbacks.ModelCheckpoint("best_mnist.keras", save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True)
history = model.fit(X_train, y_train, epochs=100, validation_data=(X_valid, y_valid),
                    callbacks=[checkpoint_cb, early_stopping_cb])
print("실제로 돈 epoch:", len(history.history["loss"]))

model = keras.models.load_model("best_mnist.keras")''' + _EVAL,
"""<ul><li>EarlyStopping 기본 감시값은 <code>val_loss</code> → validation_data가 있어야 함</li>
<li>save_best_only = 점수가 아니라 <b>가장 좋았을 때의 가중치(모델)</b>를 저장</li>
<li>callbacks 리스트 순서는 상관없음 (9/19)</li></ul>"""))

# ---------------------------------------------------------------- 8
P.append((8, "L2 규제 · 드롭아웃 · 학습 곡선 그리기", "l2 규제 regularizer kernel_regularizer dropout 과적합 history 학습 곡선 pandas plot",
_spec("Fashion MNIST로 다음 모델을 만들고 학습 곡선을 그리시오.",
      ["Hidden: 300개, 100개, ReLU, He", "각 은닉층에 L2 규제 0.0001", "각 은닉층 뒤 Dropout 0.3",
       "Optimizer: Adam, 10 epoch", "history로 loss·accuracy·val_loss·val_accuracy 그래프"]),
_DATA_FASHION + '''import pandas as pd
import matplotlib.pyplot as plt

model = keras.Sequential([
    keras.layers.Input(shape=(28, 28)), keras.layers.Flatten(),
    keras.layers.Dense(300, activation="relu", kernel_initializer="he_normal",
                       kernel_regularizer=keras.regularizers.l2(0.0001)),
    keras.layers.Dropout(0.3),
    keras.layers.Dense(100, activation="relu", kernel_initializer="he_normal",
                       kernel_regularizer=keras.regularizers.l2(0.0001)),
    keras.layers.Dropout(0.3),
    keras.layers.Dense(10, activation="softmax")])
model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_valid, y_valid))

pd.DataFrame(history.history).plot(figsize=(8, 5))
plt.grid(True); plt.xlabel("epoch"); plt.show()''' + _EVAL,
"""<ul><li>L2 규제: 가중치가 커지지 않게 손실에 벌점을 더함 (10/10 사용자 정의 훈련 반복의 <code>model.losses</code>가 이것)</li>
<li>드롭아웃: 학습 때 뉴런을 랜덤하게 끊어 특정 뉴런에 의존하지 않게 함 → 과적합 감소 (9/26 '철수' 비유)</li>
<li>Dropout 때문에 훈련 정확도가 검증 정확도보다 낮게 나올 수 있음 (훈련 때만 끊기므로)</li></ul>"""))

# ---------------------------------------------------------------- 9
P.append((9, "같은 모델을 함수형 API로 (9/12)", "함수형 api functional keras.Model input week4 변환 층을 함수처럼",
_spec("Week4 모델(200·100, ELU, He, BN, NAG 0.9)을 Sequential이 아닌 함수형 API로 다시 만들고 summary로 같은지 확인하시오.", []),
_DATA_MNIST + '''
input_ = keras.layers.Input(shape=(28, 28))
x = keras.layers.Flatten()(input_)
for n in [200, 100]:
    x = keras.layers.Dense(n, kernel_initializer="he_normal", use_bias=False)(x)
    x = keras.layers.BatchNormalization()(x)
    x = keras.layers.Activation("elu")(x)
output = keras.layers.Dense(10, activation="softmax")(x)
model = keras.Model(inputs=[input_], outputs=[output])
model.summary()

model.compile(loss="sparse_categorical_crossentropy",
              optimizer=keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True),
              metrics=["accuracy"])
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_valid, y_valid))''' + _EVAL,
"""<ul><li>층을 만들고 바로 <code>(이전 출력)</code>을 넣어 호출하면 연결됨 → 마지막에 <code>keras.Model(inputs, outputs)</code></li>
<li>파라미터 수: Dense 784×200 = 156,800 (use_bias=False), BN 200×4 = 800, Dense 200×100 = 20,000, BN 400, 출력 100×10+10 = 1,010 → 합계 179,010</li></ul>"""))

# ---------------------------------------------------------------- 10
P.append((10, "같은 데이터를 CNN으로 (10/17)", "cnn conv2d maxpool2d mnist 합성곱 파라미터 320 18496 reshape 채널",
_spec("MNIST를 CNN으로 학습하고, 각 층의 파라미터 수를 설명하시오.",
      ["Conv2D 32개, 3×3, padding same, ReLU → MaxPool 2", "Conv2D 64개, 3×3, padding same, ReLU → MaxPool 2",
       "Flatten → Dense 128 ReLU → Dropout 0.5 → Dense 10 Softmax", "Optimizer: Adam, 5 epoch"]),
_DATA_MNIST + '''
X_train, X_valid, X_test = X_train[..., np.newaxis], X_valid[..., np.newaxis], X_test[..., np.newaxis]   # (N, 28, 28, 1)

model = keras.Sequential([
    keras.layers.Input(shape=(28, 28, 1)),
    keras.layers.Conv2D(32, 3, padding="same", activation="relu"),
    keras.layers.MaxPool2D(2),
    keras.layers.Conv2D(64, 3, padding="same", activation="relu"),
    keras.layers.MaxPool2D(2),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(10, activation="softmax")])
model.summary()
model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
history = model.fit(X_train, y_train, epochs=5, validation_data=(X_valid, y_valid))''' + _EVAL,
"""<ul><li>Conv2D는 채널 축이 필요 → <code>[..., np.newaxis]</code>로 (28, 28) → (28, 28, 1)</li>
<li>파라미터: conv1 (3×3×1+1)×32 = 320, conv2 (3×3×32+1)×64 = 18,496, 풀링 0, Dense 7×7×64×128+128 = 401,536, 출력 1,290</li>
<li>MLP보다 정확도가 높음: 이웃 픽셀(2차원 구조)을 그대로 봄 (10/17)</li></ul>"""))


def register(add, results=None):
    results = results or {}
    for no, title, kw, q, code, summ in P:
        r = results.get(str(no))
        res = f"<p class=\"res\"><b>실제 실행 결과</b>: {r}</p>" if r else ""
        html = f"<h3 class=\"pq\">문제</h3>{q}<h3 class=\"pq\">정리 (마크다운에 쓸 요점)</h3>{summ}{res}"
        add("practice", f"[Week4] 연습 {no}. {title}", kw + " week4 변형 연습 문제 과제 형식 mnist 신경망",
            code=code, html=html)
