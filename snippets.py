# 사이트 내용 원본. build.py가 이 목록으로 index.html을 만들고, test.py가 code를 실제로 실행해 본다.
# kw: 검색에 걸릴 다른 표현들 (한글/영문/줄임말)

SECTIONS = [
    ("concept", "개념 + 예제"),
    ("change", "바꾸면 이렇게 된다"),
    ("mock", "모의시험 답안"),
    ("notebook", "교수님 노트북"),
    ("start", "시작"),
    ("data", "데이터"),
    ("model", "모델 만들기"),
    ("compile", "컴파일·옵티마이저"),
    ("train", "학습·평가"),
    ("tf", "텐서플로 기초"),
    ("custom", "사용자 정의"),
    ("cnn", "CNN"),
    ("tune", "튜닝·평가"),
    ("pandas", "Pandas"),
    ("numpy", "NumPy 신경망"),
    ("error", "에러 해결"),
    ("words", "한 줄 정리"),
]

S = []
def add(sec, title, kw, code="", note="", html="", out=""):
    S.append(dict(sec=sec, title=title, kw=kw, code=code.strip("\n"), note=note, html=html, out=out))

# ---------------- 시작
add("start", "import 세트", "임포트 import 라이브러리 시작 tensorflow keras numpy pandas matplotlib",
"""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
print(tf.__version__)""")

add("start", "랜덤 시드 고정", "seed 시드 재현 random",
"""np.random.seed(42)
tf.random.set_seed(42)""",
"같은 결과가 나오게 할 때. 모델을 새로 만들기 직전에 실행.")

add("start", "로컬 주피터에 텐서플로 설치", "install 설치 pip anaconda 아나콘다 ModuleNotFoundError tensorflow 없음",
"""# Anaconda Prompt 또는 노트북 셀에서
!pip install tensorflow""",
"설치 후 Kernel → Restart. Colab은 이미 설치되어 있음.")

add("start", "Colab 단축키", "shortcut 단축키 셀 추가 마크다운 실행 colab 코랩 jupyter 주피터",
html="""<table>
<tr><th>할 일</th><th>Colab</th><th>(참고) 주피터</th></tr>
<tr><td>실행하고 다음 셀로</td><td><kbd>Shift</kbd>+<kbd>Enter</kbd></td><td>같음</td></tr>
<tr><td>실행만 (그 자리)</td><td><kbd>Ctrl</kbd>+<kbd>Enter</kbd></td><td>같음</td></tr>
<tr><td>아래에 코드 셀 추가</td><td><kbd>Ctrl</kbd>+<kbd>M</kbd> → <kbd>B</kbd></td><td><kbd>Esc</kbd> → <kbd>B</kbd></td></tr>
<tr><td>위에 코드 셀 추가</td><td><kbd>Ctrl</kbd>+<kbd>M</kbd> → <kbd>A</kbd></td><td><kbd>Esc</kbd> → <kbd>A</kbd></td></tr>
<tr><td>마크다운 셀로 바꾸기</td><td><kbd>Ctrl</kbd>+<kbd>M</kbd> → <kbd>M</kbd></td><td><kbd>Esc</kbd> → <kbd>M</kbd></td></tr>
<tr><td>코드 셀로 바꾸기</td><td><kbd>Ctrl</kbd>+<kbd>M</kbd> → <kbd>Y</kbd></td><td><kbd>Esc</kbd> → <kbd>Y</kbd></td></tr>
<tr><td>셀 삭제</td><td><kbd>Ctrl</kbd>+<kbd>M</kbd> → <kbd>D</kbd></td><td><kbd>Esc</kbd> → <kbd>D</kbd> <kbd>D</kbd></td></tr>
<tr><td>실행 중단</td><td><kbd>Ctrl</kbd>+<kbd>M</kbd> → <kbd>I</kbd></td><td><kbd>Esc</kbd> → <kbd>I</kbd> <kbd>I</kbd></td></tr>
<tr><td>처음부터 다시 실행</td><td>런타임 → 다시 시작 및 모두 실행</td><td>Kernel → Restart &amp; Run All</td></tr>
</table>""")

add("start", "Colab 시험 요령 (받은 노트북에 작성 → .ipynb 제출)", "colab 코랩 시험 제출 다운로드 ipynb gpu 런타임 업로드 content 드라이브 사본 gemini ai 끄기",
html="""<ol>
<li><b>열자마자 사본 저장</b>: 파일 → <b>Drive에 사본 저장</b>. 공유받은 원본은 저장이 안 될 수 있음. 작성 중에도 <kbd>Ctrl</kbd>+<kbd>S</kbd> 자주</li>
<li><b>AI 기능 끄기 (AI 사용 금지 시험)</b>: Colab에는 Gemini 코드 자동완성·생성 기능이 들어 있음. 도구 → 설정 → <b>AI 지원</b>에서 AI 자동완성 표시 해제, 생성형 AI 기능 숨기기를 켜 두기 (메뉴 이름은 Colab 버전에 따라 조금 다를 수 있음). 회색 글씨로 코드가 저절로 제안되면 켜져 있는 것</li>
<li><b>GPU (CNN이 느리면)</b>: 런타임 → 런타임 유형 변경 → <b>T4 GPU</b>. 바꾸면 런타임이 초기화되니 <b>시작할 때</b> 바꿀 것</li>
<li><b>CSV 등 파일</b>: 왼쪽 📁 → 업로드 → 경로는 <code>/content/파일명</code>. 런타임이 끊기면 업로드한 파일도 사라짐</li>
<li><b>오래 걸리는 셀</b>: <code>verbose=2</code>, epoch는 문제에 적힌 대로. 탭을 오래 비우면 런타임이 끊길 수 있음</li>
<li><b>제출 전</b>: 런타임 → <b>다시 시작 및 모두 실행</b> → 에러 없이 끝까지 → 출력(정확도·그래프)이 보이는지 확인 → 파일 → <b>다운로드 → .ipynb 다운로드</b> → 파일 이름 확인 후 제출 (제출하면 끝)</li>
<li><b>손글씨 그리기 셀</b>(<code>google.colab.output</code>)은 Colab에서는 그대로 동작</li>
</ol>""")

# ---------------- 데이터
add("data", "MNIST 불러오기 · 정규화 · 검증 세트 분리", "mnist 숫자 손글씨 load_data 255 정규화 normalize validation 검증 split 나누기",
"""(X_train_full, y_train_full), (X_test, y_test) = keras.datasets.mnist.load_data()
X_train_full = X_train_full / 255.0          # 0~255 → 0~1
X_test = X_test / 255.0
X_train, X_valid = X_train_full[:-5000], X_train_full[-5000:]
y_train, y_valid = y_train_full[:-5000], y_train_full[-5000:]
print(X_train.shape, X_valid.shape, X_test.shape)   # (55000,28,28) (5000,28,28) (10000,28,28)""")

add("data", "Fashion MNIST + 클래스 이름", "fashion 패션 의류 class_names 클래스 이름",
"""(X_train_full, y_train_full), (X_test, y_test) = keras.datasets.fashion_mnist.load_data()
X_valid, X_train = X_train_full[:5000] / 255., X_train_full[5000:] / 255.
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]
X_test = X_test / 255.
class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]""")

add("data", "이미지 보기", "imshow 그림 이미지 출력 plot 시각화",
"""plt.imshow(X_train[0], cmap="binary")
plt.title(str(y_train[0]))
plt.axis("off")
plt.show()""")

add("data", "원-핫 인코딩", "one-hot 원핫 to_categorical categorical 레이블",
"""from tensorflow.keras.utils import to_categorical
Y_train = to_categorical(y_train, 10)
Y_test = to_categorical(y_test, 10)""",
"원-핫으로 바꿨으면 loss는 categorical_crossentropy. 정수 그대로면 sparse_categorical_crossentropy.")

add("data", "784 벡터로 펴기 (NumPy용)", "reshape flatten 784 펴기 벡터 astype float32",
"""X_train_flat = X_train.reshape(-1, 784).astype("float32")
X_test_flat = X_test.reshape(-1, 784).astype("float32")""")

add("data", "CSV 읽기", "csv read_csv 파일 읽기 업로드 content 경로",
"""df = pd.read_csv("Salary2024.csv")             # 노트북과 같은 폴더 (로컬 주피터)
# df = pd.read_csv("/content/Salary2024.csv")  # Colab에 업로드한 경우""")

add("data", "캘리포니아 주택 (회귀) + 스케일링", "california housing 회귀 regression StandardScaler 스케일 train_test_split",
"""from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
housing = fetch_california_housing()
X_train_full, X_test, y_train_full, y_test = train_test_split(housing.data, housing.target, random_state=42)
X_train, X_valid, y_train, y_valid = train_test_split(X_train_full, y_train_full, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)   # fit은 훈련 세트에만
X_valid = scaler.transform(X_valid)
X_test = scaler.transform(X_test)""")

# ---------------- 모델
add("model", "문제 문구 → 코드", "사양 spec 변환 표 initializer activation optimizer he elu nag momentum 배치정규화 dropout",
html="""<table>
<tr><th>문제에 적힌 것</th><th>코드</th></tr>
<tr><td>Hidden 300개</td><td><code>keras.layers.Dense(300, ...)</code></td></tr>
<tr><td>Activation: ReLU / ELU / sigmoid / tanh</td><td><code>activation="relu"</code> / <code>"elu"</code> / <code>"sigmoid"</code> / <code>"tanh"</code></td></tr>
<tr><td>Activation: SELU</td><td><code>activation="selu", kernel_initializer="lecun_normal"</code></td></tr>
<tr><td>Activation: LeakyReLU</td><td>Dense 다음 줄 <code>keras.layers.LeakyReLU(alpha=0.2)</code></td></tr>
<tr><td>Initializer: He</td><td><code>kernel_initializer="he_normal"</code></td></tr>
<tr><td>Initializer: Glorot(Xavier)</td><td>기본값 (안 써도 됨) / <code>"glorot_normal"</code></td></tr>
<tr><td>Initializer: LeCun</td><td><code>kernel_initializer="lecun_normal"</code></td></tr>
<tr><td>배치정규화 적용</td><td>Dense 다음 줄 <code>keras.layers.BatchNormalization()</code></td></tr>
<tr><td>Dropout 0.2</td><td><code>keras.layers.Dropout(0.2)</code></td></tr>
<tr><td>L2 규제</td><td><code>kernel_regularizer=keras.regularizers.l2(0.01)</code></td></tr>
<tr><td>Optimizer: SGD</td><td><code>optimizer="sgd"</code></td></tr>
<tr><td>Momentum 0.9</td><td><code>keras.optimizers.SGD(learning_rate=0.01, momentum=0.9)</code></td></tr>
<tr><td>NAG (Nesterov)</td><td><code>keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)</code></td></tr>
<tr><td>Adam / RMSprop / Nadam / Adagrad</td><td><code>optimizer="adam"</code> / <code>"rmsprop"</code> / <code>"nadam"</code> / <code>"adagrad"</code></td></tr>
<tr><td>Output: Softmax (10개)</td><td><code>keras.layers.Dense(10, activation="softmax")</code></td></tr>
</table>""")

add("model", "기본 모델 (은닉 300·100)", "sequential 시퀀셜 모델 dense 은닉층 hidden relu softmax 기본",
"""model = keras.Sequential([
    keras.layers.Input(shape=(28, 28)),
    keras.layers.Flatten(),                          # 28x28 → 784
    keras.layers.Dense(300, activation="relu"),
    keras.layers.Dense(100, activation="relu"),
    keras.layers.Dense(10, activation="softmax")     # 0~9
])
model.summary()""")

add("model", "He 초기화 / 르쿤 / 랜덤 정규분포", "initializer 초기화 he_normal kernel_initializer glorot xavier lecun RandomNormal",
"""model = keras.Sequential([
    keras.layers.Input(shape=(28, 28)),
    keras.layers.Flatten(),
    keras.layers.Dense(300, activation="relu", kernel_initializer="he_normal"),
    keras.layers.Dense(100, activation="relu", kernel_initializer="he_normal"),
    keras.layers.Dense(10, activation="softmax")
])
# 다른 초기화
# kernel_initializer="glorot_uniform"   (기본값)
# kernel_initializer="lecun_normal"     (SELU와 함께)
# kernel_initializer=keras.initializers.RandomNormal(mean=0.0, stddev=0.05)""",
"짝: ReLU·ELU·LeakyReLU → He / sigmoid·tanh·softmax → Glorot / SELU → LeCun")

add("model", "ELU · SELU · sigmoid 모델", "elu selu sigmoid tanh 활성화 activation 바꾸기",
"""model_elu = keras.Sequential([
    keras.layers.Input(shape=(28, 28)),
    keras.layers.Flatten(),
    keras.layers.Dense(300, activation="elu", kernel_initializer="he_normal"),
    keras.layers.Dense(100, activation="elu", kernel_initializer="he_normal"),
    keras.layers.Dense(10, activation="softmax")
])
model_selu = keras.Sequential([
    keras.layers.Input(shape=(28, 28)),
    keras.layers.Flatten(),
    keras.layers.Dense(300, activation="selu", kernel_initializer="lecun_normal"),
    keras.layers.Dense(100, activation="selu", kernel_initializer="lecun_normal"),
    keras.layers.Dense(10, activation="softmax")
])""")

add("model", "LeakyReLU", "leaky relu 리키렐루 리키 alpha negative_slope 죽은 relu dying",
"""model = keras.Sequential([
    keras.layers.Input(shape=(28, 28)),
    keras.layers.Flatten(),
    keras.layers.Dense(300, kernel_initializer="he_normal"),
    keras.layers.LeakyReLU(alpha=0.2),               # activation 문자열이 아니라 층으로
    keras.layers.Dense(100, kernel_initializer="he_normal"),
    keras.layers.LeakyReLU(alpha=0.2),
    keras.layers.Dense(10, activation="softmax")
])""",
"경고가 나오면 alpha 대신 negative_slope=0.2 (Keras 3).")

add("model", "배치 정규화 (Dense 뒤)", "batch normalization 배치정규화 배치 정규화 BN BatchNormalization",
"""model = keras.Sequential([
    keras.layers.Input(shape=(28, 28)),
    keras.layers.Flatten(),
    keras.layers.Dense(300, activation="relu", kernel_initializer="he_normal"),
    keras.layers.BatchNormalization(),
    keras.layers.Dense(100, activation="relu", kernel_initializer="he_normal"),
    keras.layers.BatchNormalization(),
    keras.layers.Dense(10, activation="softmax")
])""")

add("model", "배치 정규화 (활성화 앞, Week4 방식)", "batch normalization 배치정규화 활성화 앞 use_bias Activation week4 과제",
"""model = keras.Sequential([
    keras.layers.Input(shape=(28, 28)),
    keras.layers.Flatten(),
    keras.layers.Dense(200, kernel_initializer="he_normal", use_bias=False),
    keras.layers.BatchNormalization(),
    keras.layers.Activation("elu"),
    keras.layers.Dense(100, kernel_initializer="he_normal", use_bias=False),
    keras.layers.BatchNormalization(),
    keras.layers.Activation("elu"),
    keras.layers.Dense(10, activation="softmax")
])""",
"BN의 β가 편향 역할을 하므로 use_bias=False (안 써도 동작은 같음).")

add("model", "Dropout", "dropout 드롭아웃 드랍아웃 과대적합 overfitting 규제",
"""model = keras.Sequential([
    keras.layers.Input(shape=(28, 28)),
    keras.layers.Flatten(),
    keras.layers.Dense(300, activation="relu", kernel_initializer="he_normal"),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(100, activation="relu", kernel_initializer="he_normal"),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation="softmax")
])""",
"비율 10~50%. 학습할 때만 꺼지고 evaluate·predict 때는 모두 사용.")

add("model", "L1 · L2 규제", "l1 l2 regularizer 규제 kernel_regularizer 가중치 감쇠",
"""model = keras.Sequential([
    keras.layers.Input(shape=(28, 28)),
    keras.layers.Flatten(),
    keras.layers.Dense(300, activation="relu", kernel_initializer="he_normal",
                       kernel_regularizer=keras.regularizers.l2(0.01)),
    keras.layers.Dense(100, activation="relu", kernel_initializer="he_normal",
                       kernel_regularizer=keras.regularizers.l1(0.01)),
    keras.layers.Dense(10, activation="softmax")
])
# 둘 다: keras.regularizers.l1_l2(l1=0.01, l2=0.01)""",
"L1은 가중치를 0으로 만들어 희소하게, L2는 가중치를 작게 유지.")

add("model", "함수형 API (와이드 & 딥)", "functional 함수형 wide deep 와이드 딥 concatenate Input Model",
"""input_ = keras.layers.Input(shape=[8])
hidden1 = keras.layers.Dense(30, activation="relu")(input_)
hidden2 = keras.layers.Dense(30, activation="relu")(hidden1)
concat = keras.layers.concatenate([input_, hidden2])
output = keras.layers.Dense(1)(concat)
model_wd = keras.Model(inputs=[input_], outputs=[output])
model_wd.summary()""")

add("model", "입력 2개 모델", "다중 입력 multi input 입력 두개 wide_input deep_input",
"""input_A = keras.layers.Input(shape=[5], name="wide_input")
input_B = keras.layers.Input(shape=[6], name="deep_input")
hidden1 = keras.layers.Dense(30, activation="relu")(input_B)
hidden2 = keras.layers.Dense(30, activation="relu")(hidden1)
concat = keras.layers.concatenate([input_A, hidden2])
output = keras.layers.Dense(1, name="output")(concat)
model_ab = keras.Model(inputs=[input_A, input_B], outputs=[output])
model_ab.compile(loss="mse", optimizer=keras.optimizers.SGD(learning_rate=1e-3))
# fit할 때 튜플로: model_ab.fit((X_train[:, :5], X_train[:, 2:]), y_train, epochs=20)""")

add("model", "전이 학습 (층 재사용 · 동결)", "transfer learning 전이학습 전이 학습 freeze 동결 trainable 재사용",
"""model_B = keras.Sequential(model.layers[:-1])            # 출력층 빼고 재사용
model_B.add(keras.layers.Dense(5, activation="softmax"))  # 새 출력층
for layer in model_B.layers[:-1]:
    layer.trainable = False                                # 동결
model_B.compile(loss="sparse_categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])
# 몇 epoch 학습 후 동결 풀고 다시 compile → 작은 학습률로 미세 조정""")

add("model", "오토인코더 (784 → 20 → 784)", "autoencoder 오토인코더 인코더 디코더 encoder decoder 이상 탐지 anomaly",
"""encoder = keras.Sequential([keras.layers.Input(shape=(784,)),
                            keras.layers.Dense(20, activation="relu")])
decoder = keras.Sequential([keras.layers.Input(shape=(20,)),
                            keras.layers.Dense(784, activation="sigmoid")])
autoencoder = keras.Sequential([encoder, decoder])
autoencoder.compile(loss="mse", optimizer="adam")
# autoencoder.fit(X, X, epochs=5)   # 입력 = 정답""")

add("model", "파라미터 수 계산", "summary 파라미터 params param 개수 계산 trainable non-trainable",
html="""<p><b>Dense</b> = 입력 수 × 뉴런 수 + 뉴런 수 &nbsp;·&nbsp; <b>BatchNormalization</b> = 입력 수 × 4 (γ·β 훈련 가능, 이동평균·분산 훈련 불가) &nbsp;·&nbsp; Flatten·Dropout = 0</p>
<table>
<tr><th>층</th><th>계산</th><th>값</th></tr>
<tr><td>Dense(300) ← 784</td><td>784×300+300</td><td>235,500</td></tr>
<tr><td>Dense(100) ← 300</td><td>300×100+100</td><td>30,100</td></tr>
<tr><td>Dense(10) ← 100</td><td>100×10+10</td><td>1,010</td></tr>
<tr><td colspan="2">합계</td><td>266,610</td></tr>
<tr><td>Dense(200, use_bias=False) ← 784</td><td>784×200</td><td>156,800</td></tr>
<tr><td>BatchNormalization(200)</td><td>200×4</td><td>800</td></tr>
</table>""")

# ---------------- compile
add("compile", "compile 기본 + 손실 함수 고르기", "compile 컴파일 loss 손실 sparse_categorical_crossentropy categorical binary mse metrics accuracy",
"""model.compile(loss="sparse_categorical_crossentropy",
              optimizer="sgd",
              metrics=["accuracy"])""",
html="""<table>
<tr><th>상황</th><th>출력층</th><th>loss</th></tr>
<tr><td>레이블이 정수 0~9</td><td>Dense(10, softmax)</td><td><code>sparse_categorical_crossentropy</code></td></tr>
<tr><td>레이블이 원-핫</td><td>Dense(10, softmax)</td><td><code>categorical_crossentropy</code></td></tr>
<tr><td>이진 분류</td><td>Dense(1, sigmoid)</td><td><code>binary_crossentropy</code></td></tr>
<tr><td>회귀(숫자 예측)</td><td>Dense(1)</td><td><code>mse</code></td></tr>
</table>""")

add("compile", "SGD · Momentum · NAG", "sgd momentum 모멘텀 nesterov 네스테로프 nag 확률적 경사하강법",
"""opt_sgd = keras.optimizers.SGD(learning_rate=0.01)
opt_momentum = keras.optimizers.SGD(learning_rate=0.01, momentum=0.9)
opt_nag = keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss="sparse_categorical_crossentropy", optimizer=opt_nag, metrics=["accuracy"])""")

add("compile", "Adam · RMSprop · Nadam · Adagrad", "adam rmsprop nadam adagrad 아담 옵티마이저 optimizer beta",
"""opt_adam = keras.optimizers.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999)
opt_rms = keras.optimizers.RMSprop(learning_rate=0.001, rho=0.9)
opt_nadam = keras.optimizers.Nadam(learning_rate=0.001)
opt_adagrad = keras.optimizers.Adagrad(learning_rate=0.01)
model.compile(loss="sparse_categorical_crossentropy", optimizer=opt_adam, metrics=["accuracy"])
# 기본값 그대로면 문자열로: optimizer="adam" / "rmsprop" / "nadam" / "adagrad\"""",
"옵티마이저 객체는 모델마다 새로 만들기 (한 객체를 두 모델에 같이 쓰면 에러).")

# ---------------- train
add("train", "학습 (fit)", "fit 학습 훈련 epochs 에포크 batch_size 배치 validation_data verbose",
"""history = model.fit(X_train, y_train, epochs=5, batch_size=32,
                    validation_data=(X_valid, y_valid), verbose=2)""",
"verbose=2면 epoch당 한 줄만 출력. 1epoch 스텝 수 = 55000/32 = 1719.")

add("train", "테스트 정확도 출력 (evaluate)", "evaluate 평가 정확도 accuracy 테스트 test 출력",
"""test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"테스트 정확도: {test_acc:.4f}")""")

add("train", "예측 (predict + argmax)", "predict 예측 argmax predict_classes 확률 클래스",
"""y_proba = model.predict(X_test[:5])
print(y_proba.round(2))
y_pred = np.argmax(y_proba, axis=-1)
print("예측:", y_pred)
print("정답:", y_test[:5])
# Fashion MNIST면 이름으로: np.array(class_names)[y_pred]""")

add("train", "학습 곡선 그리기", "history 학습곡선 그래프 plot loss accuracy val_loss 시각화",
"""pd.DataFrame(history.history).plot(figsize=(8, 5))
plt.grid(True)
plt.gca().set_ylim(0, 1)
plt.xlabel("epoch")
plt.show()""")

add("train", "두 모델 손실 비교 그래프", "비교 compare 손실 loss 그래프 두개 여러 모델 plot legend",
"""h1 = history          # 첫 번째 모델 fit 결과
h2 = history          # 두 번째 모델 fit 결과 (예: h2 = model2.fit(...))
plt.plot(h1.history["loss"], label="model 1")
plt.plot(h2.history["loss"], label="model 2")
plt.xlabel("epoch"); plt.ylabel("loss"); plt.legend()
plt.show()""")

add("train", "옵티마이저 여러 개 한 번에 비교", "for 반복 비교 optimizer 옵티마이저 실험 여러개 결과 표",
"""def build_model():
    return keras.Sequential([
        keras.layers.Input(shape=(28, 28)),
        keras.layers.Flatten(),
        keras.layers.Dense(300, activation="relu", kernel_initializer="he_normal"),
        keras.layers.Dense(100, activation="relu", kernel_initializer="he_normal"),
        keras.layers.Dense(10, activation="softmax")
    ])

optimizers = {
    "SGD": lambda: keras.optimizers.SGD(learning_rate=0.01),
    "Momentum": lambda: keras.optimizers.SGD(learning_rate=0.01, momentum=0.9),
    "NAG": lambda: keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True),
    "Adam": lambda: keras.optimizers.Adam(learning_rate=0.001),
}
results, histories = {}, {}
for name, make_opt in optimizers.items():
    m = build_model()
    m.compile(loss="sparse_categorical_crossentropy", optimizer=make_opt(), metrics=["accuracy"])
    histories[name] = m.fit(X_train, y_train, epochs=3, validation_data=(X_valid, y_valid), verbose=0)
    results[name] = m.evaluate(X_test, y_test, verbose=0)[1]
    print(name, results[name])

for name, h in histories.items():
    plt.plot(h.history["val_loss"], label=name)
plt.legend(); plt.xlabel("epoch"); plt.ylabel("val_loss"); plt.show()""")

add("train", "조기 종료 (EarlyStopping)", "early stopping 조기종료 조기 종료 patience restore_best_weights callback 콜백",
"""early_stopping_cb = keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True)
history = model.fit(X_train, y_train, epochs=100,
                    validation_data=(X_valid, y_valid),
                    callbacks=[early_stopping_cb], verbose=2)
print("실제 학습한 epoch 수:", len(history.history["loss"]))""")

add("train", "체크포인트 (ModelCheckpoint)", "checkpoint 체크포인트 save_best_only 최상 모델 저장 callback 콜백",
"""checkpoint_cb = keras.callbacks.ModelCheckpoint("my_keras_model.keras", save_best_only=True)
history = model.fit(X_train, y_train, epochs=10,
                    validation_data=(X_valid, y_valid),
                    callbacks=[checkpoint_cb], verbose=2)
model = keras.models.load_model("my_keras_model.keras")   # 최상의 모델로 되돌리기""")

add("train", "모델 저장 · 불러오기", "save load 저장 불러오기 load_model keras h5",
"""model.save("my_model.keras")
model2 = keras.models.load_model("my_model.keras")""",
"파일 이름은 .keras 또는 .h5로 끝나야 함.")

add("train", "층 · 가중치 꺼내 보기", "layers get_weights 가중치 weights bias 편향 get_layer shape",
"""print(model.layers)
hidden1 = model.layers[1]
weights, biases = hidden1.get_weights()
print(weights.shape, biases.shape)""")

# ---------------- pandas
add("pandas", "데이터 훑어보기", "head tail info describe shape columns 행 열 개수 요약",
"""df = pd.read_csv("Salary2024.csv")
print(df.shape)        # (행, 열)
df.head()              # 앞 5줄
# df.tail(), df.info(), df.describe(), df.columns""")

add("pandas", "항목별 개수 (value_counts)", "value_counts 개수 몇명 빈도 count 세기",
"""df["job_title"].value_counts()
# 비율로: df["job_title"].value_counts(normalize=True)
# 상위 10개: df["job_title"].value_counts().head(10)""")

add("pandas", "종류 수 · 종류 목록 (nunique / unique)", "nunique unique 종류 몇개 고유값 중복 제거",
"""print(df["job_title"].nunique())    # 종류 수
print(df["job_title"].unique())     # 종류 목록""")

add("pandas", "그룹별 최소·최대·평균 (groupby + agg)", "groupby 그룹 agg min max mean 최소 최대 평균 집계",
"""df.groupby("job_title")["salary_in_usd"].agg(["min", "max", "mean"])
# 평균만: df.groupby("job_title")["salary_in_usd"].mean()
# 여러 기준: df.groupby(["experience_level", "work_models"])["salary_in_usd"].mean()""")

add("pandas", "그룹 평균 상위 N개", "정렬 sort_values 상위 top 내림차순 ascending 높은 순 nlargest",
"""df.groupby("job_title")["salary_in_usd"].mean().sort_values(ascending=False).head(5)
# 같은 결과: df.groupby("job_title")["salary_in_usd"].mean().nlargest(5)""")

add("pandas", "조건으로 행 거르기", "필터 filter 조건 boolean 불리언 and or & | 이상 이하 같은",
"""high = df[df["salary_in_usd"] >= 200000]
remote_high = df[(df["work_models"] == "Remote") & (df["salary_in_usd"] >= 200000)]
us_or_ca = df[(df["company_location"] == "United States") | (df["company_location"] == "Canada")]
print(len(remote_high))
# 여러 값 중 하나: df[df["company_size"].isin(["Large", "Medium"])]""")

add("pandas", "열 선택 · 새 열 만들기", "열 선택 column 새 열 추가 계산 컬럼",
"""sub = df[["job_title", "salary_in_usd"]]
df["salary_k"] = df["salary_in_usd"] / 1000
df["is_remote"] = df["work_models"] == "Remote\"""")

add("pandas", "loc · iloc", "loc iloc 인덱싱 위치 행 선택 슬라이싱",
"""df.iloc[0:5, 0:3]                              # 위치로
df.loc[df["work_year"] == 2024, ["job_title", "salary_in_usd"]]   # 조건 + 열 이름""")

add("pandas", "정렬", "sort_values 정렬 오름차순 내림차순 ascending",
"""df.sort_values("salary_in_usd", ascending=False).head(10)
df.sort_values(["work_year", "salary_in_usd"], ascending=[True, False])""")

add("pandas", "결측치", "결측치 null nan isnull dropna fillna 빈값 missing",
"""df.isnull().sum()            # 열별 결측치 개수
df_clean = df.dropna()       # 결측 행 삭제
df_filled = df.fillna(0)     # 0으로 채우기""")

add("pandas", "피벗 테이블", "pivot_table 피벗 교차표 crosstab 두 기준",
"""df.pivot_table(index="experience_level", columns="work_models",
               values="salary_in_usd", aggfunc="mean")
# 개수 교차표: pd.crosstab(df["experience_level"], df["company_size"])""")

add("pandas", "그래프 (막대 · 히스토그램)", "plot bar 막대 그래프 hist 히스토그램 시각화 차트",
"""df.groupby("work_year")["salary_in_usd"].mean().plot(kind="bar")
plt.ylabel("mean salary (USD)")
plt.show()
df["salary_in_usd"].plot(kind="hist", bins=30)
plt.show()""")

add("pandas", "문자열 포함 검색", "str contains 포함 문자열 검색 대소문자",
"""ml = df[df["job_title"].str.contains("Machine Learning")]
print(len(ml))""")

add("pandas", "중복 · 인덱스 정리", "drop_duplicates 중복 reset_index rename 이름 바꾸기",
"""df_unique = df.drop_duplicates()
g = df.groupby("job_title")["salary_in_usd"].mean().reset_index()   # 시리즈 → 표
g = g.rename(columns={"salary_in_usd": "mean_salary"})""")

# ---------------- numpy
add("numpy", "sigmoid · softmax · 교차 엔트로피", "sigmoid softmax cross entropy 교차엔트로피 손실 함수 구현 numpy",
"""def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))   # 오버플로 방지
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)

def cross_entropy_loss(y_actual, y_pred):
    y_pred = np.clip(y_pred, 1e-15, 1 - 1e-15)              # log(0) 방지
    return -np.sum(y_actual * np.log(y_pred)) / len(y_actual)""")

add("numpy", "순전파 (784 → 16 → 16 → 10)", "순전파 feedforward forward 가중치 초기화 xavier 세이비어 dot",
"""from tensorflow.keras.utils import to_categorical
Xb = X_train[:64].reshape(64, 784)
Yb = to_categorical(y_train[:64], 10)
w_1 = np.random.randn(16, 784) * np.sqrt(2 / (784 + 16)); b_1 = np.zeros(16)
w_2 = np.random.randn(16, 16) * np.sqrt(2 / (16 + 16));   b_2 = np.zeros(16)
w_o = np.random.randn(10, 16) * np.sqrt(2 / (16 + 10));   b_o = np.zeros(10)

a_1 = sigmoid(np.dot(w_1, Xb.T).T + b_1)         # (64, 16)
a_2 = sigmoid(np.dot(w_2, a_1.T).T + b_2)        # (64, 16)
output = softmax(np.dot(w_o, a_2.T).T + b_o)     # (64, 10)
print(cross_entropy_loss(Yb, output))""")

add("numpy", "역전파 · 가중치 갱신", "역전파 backpropagation backprop gradient 기울기 체인룰 chain rule 갱신 update",
"""lr = 1.0
for i in range(200):
    a_1 = sigmoid(np.dot(w_1, Xb.T).T + b_1)
    a_2 = sigmoid(np.dot(w_2, a_1.T).T + b_2)
    output = softmax(np.dot(w_o, a_2.T).T + b_o)

    d_output = output - Yb                                       # softmax + CE 미분
    d_w_o = np.dot(d_output.T, a_2) / len(Yb); d_b_o = np.sum(d_output, axis=0) / len(Yb)
    d_l2 = np.dot(d_output, w_o) * (a_2 * (1 - a_2))             # sigmoid 미분
    d_w_2 = np.dot(d_l2.T, a_1) / len(Yb);     d_b_2 = np.sum(d_l2, axis=0) / len(Yb)
    d_l1 = np.dot(d_l2, w_2) * (a_1 * (1 - a_1))
    d_w_1 = np.dot(d_l1.T, Xb) / len(Yb);      d_b_1 = np.sum(d_l1, axis=0) / len(Yb)

    w_o -= lr * d_w_o; b_o -= lr * d_b_o
    w_2 -= lr * d_w_2; b_2 -= lr * d_b_2
    w_1 -= lr * d_w_1; b_1 -= lr * d_b_1
    if i % 50 == 0:
        print(i, cross_entropy_loss(Yb, output))""")

# ---------------- error
add("error", "자주 나는 에러", "에러 error 오류 안됨 해결 경고 warning",
html="""<table>
<tr><th>에러 / 증상</th><th>해결</th></tr>
<tr><td><code>No module named 'tensorflow'</code></td><td><code>!pip install tensorflow</code> 후 커널 재시작</td></tr>
<tr><td><code>predict_classes</code> 없음</td><td><code>np.argmax(model.predict(X), axis=-1)</code></td></tr>
<tr><td><code>lr</code> 인자 에러</td><td><code>learning_rate=</code></td></tr>
<tr><td><code>model.save</code> 확장자 에러</td><td>파일명 끝에 <code>.keras</code></td></tr>
<tr><td><code>Shapes (None, 10) and (None, 1) are incompatible</code></td><td>정수 레이블이면 <code>sparse_categorical_crossentropy</code>, 원-핫이면 <code>categorical_crossentropy</code></td></tr>
<tr><td><code>Do not pass an input_shape</code> 경고</td><td>첫 줄에 <code>keras.layers.Input(shape=(28, 28))</code> (경고라 무시해도 동작함)</td></tr>
<tr><td>LeakyReLU <code>alpha</code> 경고</td><td><code>negative_slope=0.2</code></td></tr>
<tr><td><code>FileNotFoundError</code> (CSV)</td><td>로컬은 노트북과 같은 폴더에 두고 파일명만, Colab은 <code>/content/</code></td></tr>
<tr><td><code>KeyError: '열이름'</code></td><td><code>df.columns</code>로 정확한 철자 확인</td></tr>
<tr><td>옵티마이저 관련 <code>Unknown variable</code></td><td>옵티마이저 객체를 모델마다 새로 만들기</td></tr>
<tr><td>정확도 10% 근처에서 안 오름</td><td>/255 했는지, loss 종류, 출력층 softmax 확인</td></tr>
<tr><td>학습이 너무 오래 걸림</td><td>epochs 줄이기, <code>verbose=2</code></td></tr>
<tr><td><code>No module named 'keras.layers.core'</code></td><td><code>from keras.layers import Dense, Dropout, Flatten, Activation</code> (core 빼기)</td></tr>
<tr><td><code>scipy.ndimage.filters</code> 경고·에러</td><td><code>from scipy.ndimage import convolve</code></td></tr>
<tr><td>Conv2D <code>expected ndim=4</code></td><td>채널 차원 추가: <code>X[..., np.newaxis]</code> 또는 <code>X.reshape(-1, 28, 28, 1)</code></td></tr>
<tr><td>불러오기 <code>Could not locate function 'huber_fn'</code></td><td><code>load_model(..., custom_objects={"huber_fn": huber_fn})</code></td></tr>
<tr><td>GradientTape 결과가 <code>None</code></td><td>변수가 constant → <code>tf.Variable</code>로 만들거나 <code>tape.watch(c)</code></td></tr>
<tr><td><code>InvalidArgumentError</code> (float32 + int32)</td><td><code>tf.cast(t, tf.float32)</code>로 타입 맞추기</td></tr>
<tr><td><code>'ResourceVariable' object does not support item assignment</code></td><td><code>v[1] = ...</code> 대신 <code>v[1].assign(...)</code></td></tr>
<tr><td><code>google.colab</code> 에러</td><td>Colab 전용 코드(손글씨 그리기). 로컬에서는 그 셀 건너뛰기</td></tr>
</table>""")

# ---------------- words
add("words", "기법 한 줄 정리 (마크다운 답안용)", "정리 설명 한줄 마크다운 he relu elu 배치정규화 adam 모멘텀 nag dropout 조기종료",
html="""<ul>
<li><b>He 초기화</b>: ReLU 계열에 맞게 처음 가중치 크기(분산 2/fan_in)를 잡아 학습이 잘 시작되게 함</li>
<li><b>Glorot(Xavier) 초기화</b>: 케라스 기본값. 분산 1/fan_avg. sigmoid·tanh와 짝</li>
<li><b>ReLU</b>: 0보다 작으면 0, 크면 그대로. sigmoid보다 기울기 소실이 적음</li>
<li><b>LeakyReLU</b>: 음수에도 작은 기울기를 줘서 뉴런이 죽는(출력 0에 갇히는) 문제를 줄임</li>
<li><b>ELU</b>: 음수 쪽을 지수함수로 부드럽게. 평균이 0에 가까워 학습이 안정적</li>
<li><b>SELU</b>: 스케일된 ELU. 르쿤 초기화와 함께 쓰면 층마다 스스로 정규화됨</li>
<li><b>배치 정규화</b>: 미니배치마다 층 출력의 평균 0, 분산 1로 맞춘 뒤 γ·β로 조정. 학습이 빠르고 안정적</li>
<li><b>Momentum</b>: 이전에 가던 방향으로 관성을 줘 더 빨리 내려감</li>
<li><b>NAG</b>: 관성 방향으로 먼저 가본 위치의 기울기를 써서 진동이 줄고 더 빨리 수렴</li>
<li><b>AdaGrad</b>: 많이 움직인 방향은 학습률을 줄임. 너무 일찍 멈추는 단점</li>
<li><b>RMSProp</b>: 최근 기울기만 반영(지수 이동평균)해 AdaGrad 단점 보완</li>
<li><b>Adam</b>: Momentum + RMSProp. 실무에서 가장 많이 씀</li>
<li><b>Nadam</b>: Adam + Nesterov</li>
<li><b>Dropout</b>: 학습 때 뉴런 일부를 랜덤하게 꺼서 특정 뉴런 의존을 줄이고 과대적합 방지</li>
<li><b>L1 / L2 규제</b>: 가중치가 커지지 않게 벌점. L1은 0으로 만들어 희소하게</li>
<li><b>조기 종료</b>: 검증 손실이 더 안 좋아지면 학습을 멈추고 가장 좋았던 가중치로 되돌림</li>
<li><b>전이 학습</b>: 학습된 모델의 앞쪽 층을 재사용(동결)하고 출력층만 새로 학습</li>
<li><b>데이터 증강</b>: 회전·이동 등으로 훈련 이미지를 늘려 일반화 향상</li>
</ul>""")

add("words", "문제점 한 줄 정리", "기울기 소실 폭주 vanishing exploding 과대적합 overfitting 과적합 문제점",
html="""<ul>
<li><b>기울기 소실</b>: 역전파 중 아래층으로 갈수록 기울기가 0에 가까워져 학습이 안 됨. sigmoid 도함수 최대 0.25가 층마다 곱해지는 것이 원인 → 초기화, ReLU 계열, 배치 정규화로 완화</li>
<li><b>기울기 폭주</b>: 기울기가 점점 커져 발산. RNN처럼 되먹임 구조에서 주로 발생</li>
<li><b>과대적합</b>: 훈련 데이터에만 맞고 새 데이터에 약함. loss는 줄어드는데 val_loss가 오르면 신호 → Dropout, 규제, 조기 종료, 데이터 증강</li>
<li><b>학습률</b>: 너무 크면 발산, 너무 작으면 매우 느림</li>
<li><b>softmax + 교차 엔트로피</b>: 미분이 (예측 − 정답)으로 간단해서 분류에 씀. 회귀는 MSE</li>
</ul>""")

add("words", "옵티마이저 비교표", "옵티마이저 비교 수렴 속도 품질 표 11-2",
html="""<table>
<tr><th>옵티마이저</th><th>수렴 속도</th><th>수렴 품질</th></tr>
<tr><td>SGD</td><td>느림</td><td>좋음</td></tr>
<tr><td>Momentum / NAG</td><td>보통</td><td>좋음</td></tr>
<tr><td>Adagrad</td><td>빠름</td><td>나쁨 (너무 일찍 멈춤)</td></tr>
<tr><td>RMSprop / Adam / Nadam</td><td>빠름</td><td>보통~좋음</td></tr>
</table>""")


# ---------------- 5·6·7장 예제
import snippets_tf as _tf
_tf.register(add)
import snippets_eval as _ev
_ev.register(add)

# ---------------- Pandas 출력 예시 (Salary2024.csv 실제 실행 결과)
import json as _json, os as _os
_P = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "pandas_out.json")
if _os.path.exists(_P):
    _o = _json.load(open(_P, encoding="utf-8"))
    _map = {
        "데이터 훑어보기": "shape",
        "항목별 개수 (value_counts)": "vc",
        "종류 수 · 종류 목록 (nunique / unique)": "nunique",
        "그룹별 최소·최대·평균 (groupby + agg)": "agg",
        "그룹 평균 상위 N개": "top5",
        "조건으로 행 거르기": "filt",
        "결측치": "null",
        "피벗 테이블": "pivot",
    }
    for _s in S:
        if _s["title"] in _map:
            _s["out"] = _o[_map[_s["title"]]]


# ---------------- 개념 + 예제 / 바꾸면 이렇게 된다 (맨 앞에 배치)
import concepts as _c, experiments as _e, re as _re, html as _h
_R = _e.load(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "results.json"))
_BY = {x["title"]: x for x in S}
_NB = {"ch2": ("nb/ch2.html", "2. 케라스 신경망"), "ch3": ("nb/ch3.html", "3. 필기숫자 인식"),
       "ch4": ("nb/ch4.html", "4. 신경망 요소"), "opt": ("nb/opt.html", "4. Optimizer(NumPy 역전파)"),
       "ch5": ("nb/ch5.html", "5. 사용자 정의 모델"), "ch6": ("nb/ch6.html", "6. 사용자 정의 모델 2"),
       "ch7a": ("nb/ch7a.html", "7-1. CNN 컴퓨터 비전"), "ch7b": ("nb/ch7b.html", "7-2. CNN 숫자")}
import mock_cards as _mock
_NB_DESC = {"ch2": "10장 · Fashion MNIST 시퀀셜 API, 함수형 API(와이드&딥), 저장·복원, 콜백",
            "ch3": "10장 복습 + MNIST 필기 숫자 인식, 내 손글씨 인식, 이미지 변환",
            "ch4": "11장 · 데이터 증강, 초기화, 활성화, 배치 정규화, 옵티마이저, 드롭아웃",
            "opt": "NumPy로 순전파·손실·역전파·가중치 갱신 직접 구현, sigmoid와 softmax",
            "ch5": "12장 · 텐서와 연산, 변수, 래그드·희소 텐서, 사용자 정의 손실·함수·지표",
            "ch6": "12장 · 사용자 정의 층·모델, GradientTape, 사용자 정의 훈련 반복, tf.function",
            "ch7a": "14장 · 합성곱, Conv2D, 패딩, 풀링, CNN으로 Fashion MNIST",
            "ch7b": "MLP 복습, 합성곱·풀링 예시, CNN 숫자 인식, MLP vs CNN 비교"}
def _toc(key):
    f = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), _NB[key][0])
    if not _os.path.exists(f): return ""
    t = open(f, encoding="utf-8").read()
    rows = []
    for m in _re.finditer(r'<h([1-4])[^>]*id="([^"]+)"[^>]*>(.*?)</h[1-4]>', t, _re.S):
        txt = _re.sub(r"<[^>]+>", "", _h.unescape(m.group(3))).replace("¶", "").strip()
        if not txt or txt in ("설정",) or txt.startswith("**"): continue
        lvl = int(m.group(1))
        rows.append(f'<li style="margin-left:{(lvl-1)*14}px"><a href="{_NB[key][0]}#{m.group(2)}" target="_blank" rel="noopener">{_h.escape(txt)}</a></li>')
    return '<ul style="list-style:none;padding-left:0;columns:2;column-gap:24px">' + "".join(rows) + '</ul>'

def _anchor(key, heading):
    f = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), _NB[key][0])
    if not _os.path.exists(f): return None
    t = open(f, encoding="utf-8").read()
    for m in _re.finditer(r'<h[1-4][^>]*id="([^"]+)"[^>]*>(.*?)</h[1-4]>', t, _re.S):
        txt = _re.sub(r"<[^>]+>", "", _h.unescape(m.group(2))).replace("¶", "").strip()
        if txt == heading or txt.startswith(heading):
            return _NB[key][0] + "#" + m.group(1)
    return _NB[key][0]
_front = []
for _it in _c.concept_items():
    L = _c.LINK.get(_it["title"], {})
    _it["code"] = "\n\n".join(f"# ── {t}\n" + _BY[t]["code"] for t in L.get("ex", []) if t in _BY and _BY[t]["code"])
    ex = ""
    for g in L.get("exp", []):
        ex += _e.group_html(g, _R)
    links = []
    for key, head in L.get("nb", []):
        a = _anchor(key, head)
        if a: links.append(f'<a href="{a}" target="_blank" rel="noopener">교수님 노트북 · {_NB[key][1]} › {head}</a>')
    if links: ex += '<div class="nblinks">' + "".join(links) + '</div>'
    _it["extra"] = ex
    _front.append(_it)
_front.append(_c.read_item())
_nbitems = []
for _k, (_path, _name) in _NB.items():
    _t = _toc(_k)
    if not _t: continue
    _nbitems.append(dict(sec="notebook", title=f"교수님 노트북 · {_name}", kw="교수님 노트북 원본 강의 예제 " + _NB_DESC[_k],
        code="", note="", out="", extra="",
        html=f'<p>{_NB_DESC[_k]}</p><p><a href="{_path}" target="_blank" rel="noopener"><b>노트북 전체 열기 →</b></a></p>' + _t))
for _x in S: _x.setdefault("extra", "")
S[:0] = _front + _e.items(_R) + _mock.items() + _nbitems
