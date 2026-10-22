# 개념 사전. snippets.py 맨 앞에 붙는다.
# 항목 형식: (제목, 검색 키워드, 한 줄 뜻, 비유, 코드에서 어디, 바꾸면/주의)

C = [
("신경망 · 뉴런 · 층", "neural network neuron layer 뉴런 층 레이어 신경망 은닉층 hidden",
 "입력 숫자들에 각자 가중치를 곱해 더하고(z = w·x + b), 그 값을 활성화 함수에 넣어 출력하는 계산 단위가 뉴런. 뉴런을 여러 개 모은 것이 층, 층을 여러 개 쌓은 것이 신경망.",
 "숫자 사진 784픽셀을 보고 \"이건 3 같다\"는 결론까지 여러 단계의 투표를 거치는 것. 앞층은 선·곡선 같은 작은 특징을, 뒤층은 그걸 조합한 큰 특징을 본다.",
 "<code>keras.layers.Dense(300, ...)</code> = 뉴런 300개짜리 층 하나. 입력층과 출력층 사이 층들을 은닉층(hidden layer)이라고 부름.",
 "뉴런·층이 많을수록 복잡한 패턴을 배울 수 있지만, 파라미터가 늘어 느려지고 과대적합 위험이 커짐."),

("가중치(weight) · 편향(bias) · 파라미터", "weight bias 가중치 편향 파라미터 parameter params",
 "가중치는 입력 하나하나를 얼마나 중요하게 볼지 정하는 숫자, 편향은 더한 결과에 마지막으로 더하는 숫자. 학습이란 이 숫자들을 조금씩 고쳐서 정답에 가까워지게 하는 것.",
 "시험 점수를 과목별 반영 비율(가중치)로 합산하고 기본 점수(편향)를 더하는 것과 같음.",
 "<code>model.summary()</code>의 Param # 이 가중치+편향 개수. <code>model.layers[1].get_weights()</code>로 실제 값 확인.",
 "Dense(300) ← 입력 784개면 784×300 + 300 = 235,500개."),

("Flatten", "flatten 펴기 평탄화 28x28 784",
 "28×28 그림(2차원)을 784개짜리 한 줄(1차원)로 펴는 층. 계산은 안 하고 모양만 바꿈.",
 "바둑판 칸을 왼쪽 위부터 한 줄로 늘어놓는 것.",
 "<code>keras.layers.Flatten()</code> (보통 첫 층). Dense는 한 줄짜리 입력만 받기 때문에 필요.",
 "파라미터 0개."),

("활성화 함수 (activation)", "activation 활성화 함수 relu sigmoid tanh softmax elu selu",
 "뉴런이 더한 값(z)을 그대로 내보내지 않고 한 번 변형하는 함수. 이게 없으면 층을 아무리 쌓아도 직선(선형) 계산 한 번과 같아져서 복잡한 것을 못 배움.",
 "신호를 얼마나 세게 다음으로 넘길지 정하는 밸브.",
 "<code>Dense(300, activation=\"relu\")</code>",
 "<ul><li><b>sigmoid</b>: 0~1로 압축. 기울기가 최대 0.25라 층이 깊으면 학습이 느려짐(기울기 소실)</li><li><b>tanh</b>: −1~1. sigmoid보다 조금 나음</li><li><b>ReLU</b>: 음수는 0, 양수는 그대로. 빠르고 기본값으로 많이 씀</li><li><b>LeakyReLU</b>: 음수에도 아주 작은 기울기 → 뉴런이 0에 갇혀 죽는 문제 완화</li><li><b>ELU</b>: 음수 쪽을 부드러운 곡선으로</li><li><b>SELU</b>: ELU를 스케일 조정. 르쿤 초기화와 세트</li><li><b>softmax</b>: 출력층 전용. 10개 숫자를 합이 1인 확률로 바꿈</li></ul>"),

("softmax · 출력층", "softmax 출력층 output 확률 클래스 분류 argmax",
 "마지막 층의 10개 값을 \"각 클래스일 확률\"(합 = 1)로 바꾸는 함수. 가장 큰 확률의 클래스가 예측값.",
 "10명 후보의 득표를 득표율(%)로 바꾸는 것.",
 "<code>Dense(10, activation=\"softmax\")</code> → 예측: <code>np.argmax(model.predict(X), axis=-1)</code>",
 "출력 뉴런 수 = 클래스 수. 회귀(숫자 예측)는 <code>Dense(1)</code>에 활성화 없음."),

("손실 함수 (loss)", "loss 손실 함수 cross entropy 크로스엔트로피 교차엔트로피 mse sparse categorical",
 "예측이 정답과 얼마나 틀렸는지를 숫자 하나로 나타낸 것. 학습은 이 숫자를 줄이는 방향으로 가중치를 고치는 과정.",
 "채점표. 많이 틀릴수록 점수(loss)가 커짐.",
 "<code>model.compile(loss=\"sparse_categorical_crossentropy\", ...)</code>",
 "<ul><li><b>sparse_categorical_crossentropy</b>: 분류, 정답이 정수(0~9)</li><li><b>categorical_crossentropy</b>: 분류, 정답이 원-핫 벡터</li><li><b>mse</b>(평균제곱오차): 숫자를 맞히는 회귀. 차이를 제곱해 부호를 없앰</li><li>분류에 교차 엔트로피를 쓰는 이유: softmax와 함께 쓰면 미분이 (예측 − 정답)으로 간단해짐</li></ul>"),

("옵티마이저 (optimizer) · 경사 하강법", "optimizer 옵티마이저 경사하강법 gradient descent sgd adam momentum 최적화",
 "손실을 줄이는 방향(기울기)을 보고 가중치를 실제로 얼마나, 어떻게 고칠지 정하는 규칙. 기본은 경사 하강법: 새 가중치 = 지금 가중치 − 학습률 × 기울기.",
 "눈 감고 산에서 내려갈 때, 발밑 경사를 느껴 내리막 쪽으로 한 걸음씩 가는 것. 옵티마이저는 그 걸음 방식.",
 "<code>optimizer=\"sgd\"</code> 또는 <code>keras.optimizers.Adam(learning_rate=0.001)</code>",
 "<ul><li><b>SGD</b>: 배치마다 기울기만큼 이동. 느리지만 결국 잘 도착</li><li><b>Momentum</b>: 가던 방향으로 관성 → 빨라짐</li><li><b>NAG</b>: 관성만큼 먼저 가본 자리의 기울기 사용 → 덜 흔들림</li><li><b>AdaGrad</b>: 방향마다 걸음 크기 자동 조절. 너무 빨리 작아져 멈춤</li><li><b>RMSProp</b>: 최근 기울기만 반영해 AdaGrad 보완</li><li><b>Adam</b>: Momentum + RMSProp. 가장 많이 씀</li></ul>"),

("학습률 (learning rate, η)", "learning rate 학습률 lr eta 에타 발산 nan",
 "기울기를 보고 가중치를 한 번에 얼마나 크게 고칠지 정하는 비율.",
 "내리막을 걸을 때 보폭.",
 "<code>keras.optimizers.SGD(learning_rate=0.01)</code>",
 "너무 작으면 아주 느리게 학습, 너무 크면 골짜기를 넘어 튀어서 발산(loss가 nan). 실험: 0.01 → 0.867 / 0.001 → 0.821 / 0.1 → 0.853 / 1.0 → 0.100(발산)."),

("epoch · batch · step", "epoch 에포크 에폭 batch 배치 batch_size step 스텝 반복",
 "<b>batch</b>: 가중치를 한 번 고칠 때 보는 샘플 묶음(기본 32장). <b>step</b>: 배치 하나로 가중치를 한 번 고치는 것. <b>epoch</b>: 훈련 데이터 전체를 한 바퀴 다 보는 것.",
 "문제집 55,000문제를 32문제씩 풀고 채점·복습(step)하고, 문제집을 한 권 끝내면 1 epoch.",
 "<code>model.fit(X, y, epochs=10, batch_size=32)</code> → 1 epoch = 55,000 ÷ 32 ≈ 1,719 step",
 "epoch↑: 더 배우지만 어느 순간부터 과대적합. batch↑: 한 epoch 동안 고치는 횟수가 줄어 같은 epoch에선 덜 배움, 대신 빠름. 실험: batch 32 → 0.867 / 128 → 0.840 / 1024 → 0.770."),

("훈련 · 검증 · 테스트 세트", "train validation test 훈련 검증 테스트 세트 validation_data valid 나누기",
 "<b>훈련</b>: 가중치를 고치는 데 쓰는 데이터. <b>검증</b>: 학습 중에 성능을 확인만 하는 데이터(설정 고르기, 과대적합 감시). <b>테스트</b>: 다 끝나고 마지막에 한 번 실력 확인.",
 "교과서 문제(훈련), 모의고사(검증), 수능(테스트).",
 "<code>X_train, X_valid = X_train_full[:-5000], X_train_full[-5000:]</code> → <code>fit(..., validation_data=(X_valid, y_valid))</code> → <code>evaluate(X_test, y_test)</code>",
 "fit 출력의 <code>val_accuracy</code>가 검증 정확도."),

("과대적합 (overfitting)", "overfitting 과대적합 과적합 일반화 val_loss 오버피팅",
 "훈련 데이터에만 지나치게 맞춰져서 새 데이터에서는 성능이 떨어지는 상태.",
 "기출문제 답만 외워서 새 문제를 못 푸는 학생. 교수님 예: MNIST로 학습한 모델이 미국식 손글씨에 맞춰져서 한국 사람 글씨를 잘 못 맞힘.",
 "<code>history.history</code>에서 훈련 정확도는 계속 오르는데 val_accuracy는 그대로거나 val_loss가 오르면 신호.",
 "막는 법: 드롭아웃, L1/L2 규제, 조기 종료, 데이터 늘리기(증강), 모델 줄이기."),

("역전파 (backpropagation)", "backpropagation 역전파 체인룰 chain rule 기울기 계산 미분",
 "출력에서 생긴 오차를 뒤쪽 층부터 앞쪽 층으로 거꾸로 전달하면서, 각 가중치가 오차에 얼마나 책임이 있는지(기울기)를 계산하는 방법. 미분의 연쇄 법칙(체인 룰)을 씀.",
 "결과가 틀렸을 때 마지막 담당자부터 거꾸로 \"누가 얼마나 잘못했나\" 따져 올라가는 것.",
 "케라스에서는 <code>fit()</code> 안에서 자동으로 일어남. NumPy 노트북의 <code>d_output = output - Y_train</code> → <code>d_weight_o = np.dot(d_output.T, a_2)</code>가 직접 구현한 부분.",
 "역전파로 기울기를 구하고 → 옵티마이저가 그 기울기로 가중치를 고침."),

("기울기 소실 · 폭주", "vanishing gradient exploding 기울기 소실 폭주 그래디언트",
 "<b>소실</b>: 역전파로 앞쪽 층까지 갈수록 기울기가 0에 가까워져 앞쪽 층이 거의 학습되지 않는 현상. <b>폭주</b>: 반대로 점점 커져 가중치가 튀어 버리는 현상(RNN처럼 되먹임 구조에서 주로).",
 "말 전달 게임에서 뒤로 갈수록 말이 작아져서 맨 앞 사람에게는 아무것도 안 들리는 것.",
 "원인: sigmoid처럼 기울기가 작은 활성화(최대 0.25)가 층마다 곱해짐, 층마다 값의 평균·분산이 달라짐.",
 "해결 4가지(11장): 초기화(He 등) · ReLU 계열 활성화 · 배치 정규화 · (폭주엔) 기울기 클리핑."),

("가중치 초기화 (initializer)", "initializer 초기화 he glorot xavier lecun kernel_initializer fan_in fan_out",
 "학습 시작 전에 가중치를 어떤 랜덤 값으로 채울지 정하는 방법. 값의 크기를 잘 잡으면 층을 지나도 신호 크기가 유지돼 기울기 소실이 줄어듦.",
 "달리기 출발선 위치. 잘 서면 처음부터 잘 달림.",
 "<code>Dense(300, activation=\"relu\", kernel_initializer=\"he_normal\")</code>",
 "<ul><li><b>Glorot(Xavier)</b>: 케라스 기본값. 분산 = 1 / ((입력수+출력수)/2). sigmoid·tanh와 짝</li><li><b>He</b>: 분산 = 2 / 입력수. ReLU 계열과 짝</li><li><b>LeCun</b>: 분산 = 1 / 입력수. SELU와 짝</li><li>초기화와 활성화는 세트로 고름</li></ul>"),

("배치 정규화 (Batch Normalization)", "batch normalization 배치정규화 배치 정규화 BN 표준화 normalization",
 "층을 지날 때마다 그 배치의 값들을 평균 0, 분산 1로 맞춰 준 뒤, 학습 가능한 두 값(γ 스케일, β 이동)으로 다시 조정하는 층.",
 "반마다 시험 난이도가 달라 점수 범위가 제각각일 때, 표준점수로 바꿔 같은 기준으로 비교하는 것. 어떤 뉴런은 −10000~10000, 어떤 뉴런은 −10~10이면 큰 쪽만 영향을 주니 범위를 맞춰 줌.",
 "Dense 다음 줄에 <code>keras.layers.BatchNormalization()</code> 한 줄 추가.",
 "효과: 기울기 소실 감소, 학습이 빠르고 안정적, 큰 학습률 사용 가능. 수업 퀴즈: 입력 바로 뒤 BN은 MNIST처럼 이미 같은 범위(0~255)인 데이터엔 효과가 거의 없음. 파라미터 = 입력 수 × 4(γ, β는 학습, 이동평균·이동분산은 학습 안 함)."),

("드롭아웃 (Dropout)", "dropout 드롭아웃 드랍아웃 과대적합 규제",
 "학습할 때마다 뉴런 일부를 랜덤하게 꺼서(출력 0) 학습하는 방법. 특정 뉴런 몇 개에만 의존하지 않게 만들어 과대적합을 줄임. 예측(evaluate·predict) 때는 끄지 않고 모두 사용.",
 "교수님 비유: 반에서 철수만 답하면 철수가 없는 날 아무도 못 맞힘. 철수를 가끔 빼고 수업하면 다른 학생들도 답을 하게 됨.",
 "<code>keras.layers.Dropout(0.2)</code> → 20%를 끔. 보통 0.1~0.5.",
 "비율을 너무 크게 하면 덜 학습됨."),

("L1 · L2 규제", "l1 l2 regularization regularizer 규제 가중치 감쇠 weight decay",
 "손실에 \"가중치가 크면 벌점\"을 더해서 가중치가 지나치게 커지지 않게 막는 방법. L2는 가중치 제곱을, L1은 절댓값을 벌점으로 씀.",
 "답안을 너무 복잡하게 쓰면 감점하는 채점 기준.",
 "<code>Dense(100, activation=\"relu\", kernel_regularizer=keras.regularizers.l2(0.01))</code>",
 "L1은 많은 가중치를 0으로 만들어 희소한 모델이 됨. 값(0.01)이 크면 너무 단순해져 정확도가 떨어짐."),

("조기 종료 (EarlyStopping) · 콜백", "early stopping 조기종료 조기 종료 callback 콜백 patience checkpoint",
 "검증 성능이 더 좋아지지 않으면 학습을 자동으로 멈추는 기능. 콜백은 학습 도중에 자동으로 실행되는 기능을 말함.",
 "모의고사 점수가 10번 연속 안 오르면 공부 방법을 그만두고, 가장 잘 봤던 때 상태로 돌아가는 것.",
 "<code>keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True)</code> → <code>fit(..., callbacks=[...])</code>",
 "epochs를 크게 잡아도 알아서 멈추므로 epoch 수를 따로 고민할 필요가 줄어듦."),

("원-핫 인코딩", "one-hot 원핫 원 핫 to_categorical 인코딩 레이블",
 "정답 숫자를 \"해당 자리만 1, 나머지 0\"인 벡터로 바꾸는 것. 3 → [0,0,0,1,0,0,0,0,0,0].",
 "10칸짜리 체크박스에서 정답 칸 하나만 체크.",
 "<code>to_categorical(y_train, 10)</code>",
 "원-핫이면 loss는 categorical_crossentropy, 정수 그대로면 sparse_categorical_crossentropy."),

("전이 학습 · 오토인코더", "transfer learning 전이학습 autoencoder 오토인코더 동결 freeze",
 "<b>전이 학습</b>: 이미 학습된 모델의 앞쪽 층을 가져와(동결) 쓰고 뒤쪽만 새 문제에 맞게 학습. <b>오토인코더</b>: 784 → 20 → 784처럼 입력을 압축했다 복원하도록 학습한 모델.",
 "전이 학습: 영어를 잘하는 사람이 독일어를 빨리 배우는 것. 오토인코더: 정상 상태를 외워 두고, 복원이 잘 안 되면 이상하다고 판단(이상 탐지).",
 "동결: <code>layer.trainable = False</code>",
 "전이 학습은 데이터와 학습 시간을 크게 줄임. 교수님 예: IBM 왓슨은 이게 안 돼서 병원마다 다시 학습해야 했음."),

("Pandas: DataFrame · Series · groupby", "pandas dataframe series groupby 판다스 데이터프레임 시리즈 그룹",
 "<b>DataFrame</b>: 엑셀 시트 같은 표(행 × 열). <b>Series</b>: 그 표의 열 하나. <b>groupby</b>: 어떤 열 값이 같은 행끼리 묶어서 그룹마다 계산.",
 "groupby = 엑셀 피벗/부분합. \"직급별 평균 연봉\"처럼 '~별'이 나오면 groupby.",
 "<code>df[\"열\"]</code> → Series / <code>df.groupby(\"기준열\")[\"계산열\"].mean()</code>",
 "<ul><li><b>value_counts()</b>: 값마다 몇 개인지</li><li><b>nunique()</b>: 종류가 몇 개인지</li><li><b>agg([\"min\",\"max\",\"mean\"])</b>: 여러 계산을 한 번에</li><li><b>df[조건]</b>: 조건에 맞는 행만</li></ul>"),
]

def concept_items():
    out = []
    for title, kw, what, like, where, change in C:
        html = (f'<p><b>뜻</b> · {what}</p>'
                f'<p><b>비유</b> · {like}</p>'
                f'<p><b>코드에서</b> · {where}</p>'
                + (f'<div><b>바꾸면 · 참고</b> · {change}</div>' if change else ''))
        out.append(dict(sec="concept", title=title, kw=kw, code="", note="", html=html, out=""))
    return out

READ = '''# ① 데이터 불러오기: 훈련용 60,000장, 테스트용 10,000장 (그림 + 정답)
(X_train_full, y_train_full), (X_test, y_test) = keras.datasets.fashion_mnist.load_data()

# ② 정규화: 픽셀 0~255 → 0~1로 (큰 숫자 그대로 넣으면 학습이 불안정)
# ③ 검증 세트 분리: 앞 5,000장은 학습 중 확인용, 나머지 55,000장으로 학습
X_valid, X_train = X_train_full[:5000] / 255., X_train_full[5000:] / 255.
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]
X_test = X_test / 255.

# ④ 모델 구조: 층을 위에서 아래로 쌓음
model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=[28, 28]),       # 28x28 그림 → 784개 한 줄
    keras.layers.Dense(300, activation="relu"),       # 은닉층1: 뉴런 300개, ReLU
    keras.layers.Dense(100, activation="relu"),       # 은닉층2: 뉴런 100개
    keras.layers.Dense(10, activation="softmax")      # 출력층: 10개 클래스 확률
])

# ⑤ 학습 방법 정하기: 무엇을 줄일지(loss), 어떻게 고칠지(optimizer), 무엇을 볼지(metrics)
model.compile(loss="sparse_categorical_crossentropy",  # 정답이 0~9 정수인 분류
              optimizer="sgd",                          # 경사 하강법
              metrics=["accuracy"])                     # 정확도 표시

# ⑥ 학습: 전체 데이터를 10바퀴(epoch), 32장씩(batch) 보며 가중치 수정
history = model.fit(X_train, y_train, epochs=10, batch_size=32,
                    validation_data=(X_valid, y_valid))  # 매 epoch마다 검증 정확도 확인

# ⑦ 평가: 한 번도 안 본 테스트 데이터로 최종 실력 확인 → [loss, accuracy]
model.evaluate(X_test, y_test)

# ⑧ 예측: 확률 10개 중 가장 큰 것의 번호가 예측 클래스
y_proba = model.predict(X_test[:3])
y_pred = np.argmax(y_proba, axis=-1)'''

def read_item():
    return dict(sec="concept", title="기본 코드 한 줄씩 읽기",
                kw="코드 설명 한줄씩 읽기 주석 흐름 순서 파이프라인 전체 구조 이해",
                code=READ, note="수업 노트북(2. 케라스를 사용한 인공 신경망 소개)과 같은 흐름. 시험 코드도 거의 이 순서.",
                html="", out="")

# 개념 → 같이 보여줄 예제(snippets.py 제목), 교수님 노트북 위치(파일 키, 제목 텍스트), 실험 키
LINK = {
 "신경망 · 뉴런 · 층": dict(ex=["기본 모델 (은닉 300·100)"], nb=[("ch2", "이미지 분류기 만들기")], exp=["units"]),
 "가중치(weight) · 편향(bias) · 파라미터": dict(ex=["층 · 가중치 꺼내 보기"], nb=[("ch2", "이미지 분류기 만들기")], exp=[]),
 "Flatten": dict(ex=["기본 모델 (은닉 300·100)"], nb=[("ch2", "이미지 분류기 만들기")], exp=[]),
 "활성화 함수 (activation)": dict(ex=["ELU · SELU · sigmoid 모델", "LeakyReLU"], nb=[("ch4", "Activation"), ("opt", "sigmoid 와 softmax")], exp=["act"]),
 "softmax · 출력층": dict(ex=["예측 (predict + argmax)"], nb=[("opt", "sigmoid 와 softmax")], exp=[]),
 "손실 함수 (loss)": dict(ex=["compile 기본 + 손실 함수 고르기"], nb=[("opt", "손실 구하기")], exp=[]),
 "옵티마이저 (optimizer) · 경사 하강법": dict(ex=["SGD · Momentum · NAG", "Adam · RMSprop · Nadam · Adagrad"], nb=[("ch4", "Optimizer")], exp=["opt"]),
 "학습률 (learning rate, η)": dict(ex=["SGD · Momentum · NAG"], nb=[], exp=["lr"]),
 "epoch · batch · step": dict(ex=["학습 (fit)"], nb=[("ch2", "이미지 분류기 만들기")], exp=["epochs", "bs"]),
 "훈련 · 검증 · 테스트 세트": dict(ex=["MNIST 불러오기 · 정규화 · 검증 세트 분리"], nb=[("ch2", "이미지 분류기 만들기")], exp=["nonorm"]),
 "과대적합 (overfitting)": dict(ex=["학습 곡선 그리기"], nb=[("ch4", "Dropout")], exp=["epochs"]),
 "역전파 (backpropagation)": dict(ex=["역전파 · 가중치 갱신"], nb=[("opt", "경사 구하기 & Backpropagation")], exp=[]),
 "기울기 소실 · 폭주": dict(ex=["ELU · SELU · sigmoid 모델"], nb=[("ch4", "심층 신경망의 주요 요소에 대한 이해")], exp=["act"]),
 "가중치 초기화 (initializer)": dict(ex=["He 초기화 / 르쿤 / 랜덤 정규분포"], nb=[("ch4", "Initializer")], exp=["init"]),
 "배치 정규화 (Batch Normalization)": dict(ex=["배치 정규화 (Dense 뒤)", "배치 정규화 (활성화 앞, Week4 방식)"], nb=[("ch4", "배치 정규화")], exp=["bn"]),
 "드롭아웃 (Dropout)": dict(ex=["Dropout"], nb=[("ch4", "Dropout")], exp=["drop"]),
 "L1 · L2 규제": dict(ex=["L1 · L2 규제"], nb=[], exp=["drop"]),
 "조기 종료 (EarlyStopping) · 콜백": dict(ex=["조기 종료 (EarlyStopping)", "체크포인트 (ModelCheckpoint)"], nb=[("ch2", "훈련 과정에서 콜백 사용하기")], exp=[]),
 "원-핫 인코딩": dict(ex=["원-핫 인코딩"], nb=[("ch4", "MNIST Data")], exp=[]),
 "전이 학습 · 오토인코더": dict(ex=["전이 학습 (층 재사용 · 동결)", "오토인코더 (784 → 20 → 784)"], nb=[], exp=[]),
 "Pandas: DataFrame · Series · groupby": dict(ex=["그룹별 최소·최대·평균 (groupby + agg)"], nb=[], exp=[]),
}

# ---------------- 5·6·7장 개념 (텐서플로 저수준 · 사용자 정의 · CNN)
C += [
("텐서 (Tensor)", "tensor 텐서 tf.constant 차원 스칼라 벡터 행렬 넘파이",
 "여러 차원으로 된 숫자 묶음. 0차원은 스칼라(숫자 하나), 1차원은 벡터, 2차원은 행렬, 3차원 이상은 n차원 텐서. 텐서플로가 계산하는 기본 단위.",
 "엑셀로 치면 숫자 한 칸(0차원) → 한 줄(1차원) → 표 한 장(2차원) → 표 여러 장 묶음(3차원). 컬러 사진 묶음은 [사진 수, 높이, 너비, 색 3개] 4차원.",
 "<code>tf.constant([[1., 2., 3.], [4., 5., 6.]])</code> → shape (2, 3), dtype float32",
 "넘파이 배열과 거의 같지만 ① 값을 바꿀 수 없고 ② 기본 타입이 32비트이며 ③ 타입을 자동으로 바꿔 주지 않음(<code>tf.cast</code> 필요). 연산 이름이 조금 다름: <code>np.mean</code> → <code>tf.reduce_mean</code>."),

("변수 (tf.Variable)", "variable 변수 assign 가중치 바뀌는 값",
 "값을 바꿀 수 있는 텐서. 학습 중에 계속 고쳐져야 하는 가중치·편향이 Variable.",
 "텐서는 인쇄된 표, Variable은 연필로 쓴 표(지우고 다시 쓸 수 있음).",
 "<code>v = tf.Variable([[1., 2.], [3., 4.]])</code> → <code>v.assign(2 * v)</code>, <code>v[0, 1].assign(42)</code>",
 "<code>v[1] = ...</code> 처럼 = 로는 못 바꾸고 assign을 써야 함. GradientTape는 Variable만 자동으로 기록함."),

("래그드 · 희소 · 문자열 텐서", "ragged sparse string 래그드 희소 비정형 문자열",
 "<b>래그드</b>: 행마다 길이가 다른 텐서(리스트의 리스트). <b>희소</b>: 대부분 0인 텐서를 0이 아닌 값의 위치와 값만 저장. <b>문자열</b>: UTF-8 바이트로 저장.",
 "희소 텐서 = 빈칸이 많은 출석부에서 출석한 사람 이름만 적어두는 것.",
 "<code>tf.RaggedTensor.from_row_lengths(...)</code>, <code>tf.SparseTensor(indices, values, dense_shape)</code>",
 "희소 텐서는 곱셈은 되지만 + 1. 같은 덧셈은 안 됨 → <code>tf.sparse.to_dense()</code> 후 계산. 인덱스가 정렬 안 되어 있으면 <code>tf.sparse.reorder()</code>."),

("사용자 정의 손실 함수 (Huber)", "custom loss huber 후버 사용자 정의 손실 이상치",
 "케라스에 없는 손실을 직접 함수로 만들어 쓰는 것. Huber 손실은 오차가 작으면 제곱(MSE처럼), 크면 절댓값(MAE처럼)으로 계산해 이상치에 덜 휘둘림.",
 "작은 실수는 꼼꼼히 감점하고, 말도 안 되는 큰 실수 하나 때문에 점수가 폭발하지는 않게 하는 채점 기준.",
 "<code>def huber_fn(y_true, y_pred): ...</code> → <code>model.compile(loss=huber_fn)</code>. 불러올 때 <code>custom_objects={\"huber_fn\": huber_fn}</code>",
 "threshold를 바꾸려면 함수를 돌려주는 함수(create_huber) 또는 <code>keras.losses.Loss</code> 상속 클래스. 클래스는 <code>get_config()</code>로 threshold까지 저장됨."),

("손실 vs 지표 · 스트리밍 지표", "loss metric 손실 지표 차이 streaming 스트리밍 precision 정밀도",
 "<b>손실</b>: 학습(경사 하강)에 쓰는 값, 미분 가능해야 함. <b>지표</b>: 사람이 성능을 보는 값, 미분 안 돼도 됨. <b>스트리밍 지표</b>: 배치마다 따로 평균내지 않고 지금까지 본 전체로 계산하는 지표.",
 "배치1 정밀도 80%, 배치2 0%라서 평균 40%가 아니라, 전체 8개 예측 중 4개 맞음 = 50%로 계산하는 것.",
 "<code>keras.metrics.Precision()</code> → <code>result()</code>, <code>reset_state()</code>. 직접 만들 땐 <code>keras.metrics.Metric</code> 상속 + <code>update_state / result</code>",
 "정밀도 = TP / (TP + FP). compile의 <code>metrics=[...]</code>에 넣음."),

("사용자 정의 층 (Layer)", "custom layer 사용자 정의 층 build call lambda add_weight",
 "Dense처럼 쓰는 층을 직접 만드는 것. 가중치가 없으면 <code>Lambda</code>, 있으면 <code>keras.layers.Layer</code>를 상속해 <code>build</code>(가중치 만들기)와 <code>call</code>(계산)을 작성.",
 "레고 블록을 직접 깎아 만드는 것. 다른 블록과 똑같이 끼워 쓸 수 있음.",
 "<code>class MyDense(keras.layers.Layer)</code> → <code>build</code>에서 <code>add_weight</code>, <code>call</code>에서 <code>X @ kernel + bias</code>",
 "훈련 때와 예측 때 다르게 동작시키려면 <code>call(self, X, training=None)</code> (Dropout·BN이 이렇게 동작)."),

("사용자 정의 모델 · 잔차 블록", "custom model subclassing 서브클래싱 residual 잔차 skip connection keras.Model",
 "<code>keras.Model</code>을 상속해 <code>__init__</code>에서 층을 만들고 <code>call</code>에서 순서를 정하는 방식(서브클래싱 API). 반복문·조건문 같은 자유로운 구조가 가능. <b>잔차 블록</b>은 층을 거친 결과에 원래 입력을 더하는 구조.",
 "잔차 연결 = 시험지를 고칠 때 원본을 지우지 않고 수정 사항만 덧붙이는 것. 원래 신호가 그대로 전달돼 깊어도 학습이 잘 됨.",
 "<code>return inputs + Z</code> (ResidualBlock), <code>for _ in range(4): Z = self.block1(Z)</code>",
 "시퀀셜 API로도 같은 블록을 여러 번 넣어 비슷하게 만들 수 있음."),

("자동 미분 (GradientTape)", "gradienttape 자동 미분 기울기 gradient tape watch 편미분",
 "계산 과정을 녹화(tape)해 두었다가, 각 변수에 대한 기울기(미분값)를 한 번에 자동으로 계산해 주는 기능. 역전파를 자동으로 해 주는 도구.",
 "길을 걸으며 경로를 녹화해 두고, 나중에 \"어느 방향으로 얼마나 기울었는지\"를 녹화에서 바로 읽어내는 것.",
 "<code>with tf.GradientTape() as tape: y = 3 * x ** 2 + 3</code> → <code>tape.gradient(y, x)</code> (x=7 → 42)",
 "Variable만 기록됨. constant는 None → <code>tape.watch(c)</code>. 수치 미분 (f(x+ε)−f(x))/ε 은 파라미터마다 따로 해야 해서 느림."),

("사용자 정의 훈련 반복", "custom training loop 훈련 반복 fit 직접 apply_gradients",
 "<code>fit()</code>이 안에서 하는 일을 직접 코드로 쓰는 것: 배치 뽑기 → 예측 → 손실 → 기울기(GradientTape) → 옵티마이저로 갱신.",
 "자동 세탁기(fit) 대신 손빨래로 각 단계를 직접 하는 것. 번거롭지만 단계마다 원하는 대로 바꿀 수 있음.",
 "<code>gradients = tape.gradient(loss, model.trainable_variables)</code> → <code>optimizer.apply_gradients(zip(gradients, model.trainable_variables))</code>",
 "규제 손실은 <code>model.losses</code>에 따로 있어서 직접 더해야 함 (<code>tf.add_n([main_loss] + model.losses)</code>)."),

("텐서플로 함수 (tf.function)", "tf.function 그래프 graph 콘크리트 concrete 빠르게",
 "파이썬 함수를 텐서플로 계산 그래프로 바꿔 더 빠르게 실행하게 하는 기능.",
 "매번 레시피를 읽으며 요리(파이썬)하는 대신, 한 번 정리한 작업 순서표(그래프)대로 바로 만드는 것.",
 "<code>tf_cube = tf.function(cube)</code> 또는 함수 위에 <code>@tf.function</code>",
 "입력 타입·모양이 바뀌면 그에 맞는 그래프(콘크리트 함수)를 새로 만듦(다형성). <code>get_concrete_function()</code>으로 확인."),

("합성곱 (Convolution) · 필터 · 특성맵", "convolution 합성곱 필터 filter kernel 커널 특성맵 feature map 수용장",
 "작은 필터(예: 3×3)를 이미지 위에서 한 칸씩 옮기며 겹치는 칸끼리 곱해 더하는 계산. 필터 모양에 맞는 패턴(선, 모서리)이 있는 곳에서 큰 값이 나옴. 결과 그림이 특성맵.",
 "돋보기(필터)로 사진을 한 칸씩 훑으며 \"여기 세로선 있나?\"를 확인해 지도(특성맵)에 표시하는 것.",
 "<code>keras.layers.Conv2D(filters=32, kernel_size=3, padding=\"same\")</code> / 직접: <code>tf.nn.conv2d(images, filters, strides=1, padding=\"SAME\")</code>",
 "필터 개수 = 출력 특성맵 수. 필터 값은 학습으로 정해짐. MLP와 달리 이미지를 펴지 않아 위치 정보(주변 픽셀 관계)를 유지."),

("패딩 · 스트라이드", "padding 패딩 same valid stride 스트라이드 출력 크기",
 "<b>패딩</b>: 가장자리에 0을 채워 넣는 것. SAME은 출력 크기를 입력과 같게, VALID는 채우지 않음(작아짐). <b>스트라이드</b>: 필터를 몇 칸씩 건너뛰며 옮길지.",
 "스트라이드 2 = 돋보기를 두 칸씩 건너뛰며 보는 것 → 결과 지도가 절반 크기.",
 "<code>Conv2D(..., strides=1, padding=\"same\")</code>",
 "출력 크기 — SAME: ⌈입력 / 스트라이드⌉ · VALID: (입력 − 커널) / 스트라이드 + 1. 예) 28, 커널 3: SAME 28, VALID 26, SAME+stride 2 → 14."),

("풀링 (Pooling)", "pooling 풀링 max pooling 최대 평균 average global 서브샘플링",
 "특성맵을 작은 칸(예: 2×2)으로 나눠 칸마다 최댓값(Max) 또는 평균(Average)만 남겨 크기를 줄이는 층. 가중치 없음.",
 "사진을 축소할 때 4칸마다 가장 진한 점 하나만 남기는 것. 조금 움직여도 결과가 비슷함.",
 "<code>keras.layers.MaxPooling2D(pool_size=2)</code> → 가로세로 절반. <code>GlobalAvgPool2D()</code> → 특성맵마다 숫자 1개",
 "효과: 계산량·파라미터 감소, 과대적합 감소, 위치가 조금 달라도 같은 결과(이동 불변성). 대신 정보 일부가 사라짐."),

("CNN 구조 · MLP와 비교", "cnn 구조 합성곱 신경망 mlp 비교 lenet 완전연결 fully connected",
 "합성곱 + 풀링을 몇 번 반복해 특징을 뽑고, Flatten 후 Dense로 분류하는 신경망. 앞쪽은 선·모서리, 뒤쪽은 더 큰 모양을 봄.",
 "MLP는 사진을 한 줄로 찢어 읽는 것, CNN은 사진을 그대로 놓고 부분부분 훑어보는 것.",
 "Conv2D(32) → MaxPool → Conv2D(64) → MaxPool → Flatten → Dense(128) → Dropout → Dense(10, softmax)",
 "파라미터 = (커널 높이×너비×입력 채널 + 1) × 필터 수. 필터를 이미지 전체에서 공유해 파라미터가 적음. 입력은 [28, 28, 1]처럼 채널 차원이 필요(<code>X[..., np.newaxis]</code>)."),
]

LINK.update({
 "텐서 (Tensor)": dict(ex=["텐서 만들기 · 모양 · 타입", "텐서 연산 (넘파이와 비교)"], nb=[("ch5", "텐서"), ("ch5", "연산")], exp=[]),
 "변수 (tf.Variable)": dict(ex=["변수 (tf.Variable)"], nb=[("ch5", "변수")], exp=[]),
 "래그드 · 희소 · 문자열 텐서": dict(ex=["래그드 텐서 · 희소 텐서"], nb=[("ch5", "Ragged Tensor"), ("ch5", "문자열")], exp=[]),
 "사용자 정의 손실 함수 (Huber)": dict(ex=["사용자 정의 손실 함수 (Huber)", "손실 함수 클래스 (keras.losses.Loss 상속)"], nb=[("ch5", "사용자 정의 손실 함수"), ("ch5", "손실함수 Class")], exp=[]),
 "손실 vs 지표 · 스트리밍 지표": dict(ex=["손실 vs 지표 · 스트리밍 지표 (Precision)"], nb=[("ch5", "사용자 정의 지표"), ("ch5", "스트리밍 지표")], exp=[]),
 "사용자 정의 층 (Layer)": dict(ex=["사용자 정의 층 (MyDense: build · call)"], nb=[("ch6", "사용자 정의 층"), ("ch6", "사용자 정의 Layer 2")], exp=[]),
 "사용자 정의 모델 · 잔차 블록": dict(ex=["사용자 정의 모델 (ResidualBlock · 서브클래싱)"], nb=[("ch6", "사용자 정의 모델")], exp=[]),
 "자동 미분 (GradientTape)": dict(ex=["자동 미분 (GradientTape)"], nb=[("ch6", "자동 미분을 사용하여 그레이디언트 계산하기"), ("ch6", "GradientTape")], exp=[]),
 "사용자 정의 훈련 반복": dict(ex=["사용자 정의 훈련 반복 (fit 직접 구현)"], nb=[("ch6", "사용자 정의 훈련 반복")], exp=[]),
 "텐서플로 함수 (tf.function)": dict(ex=["텐서플로 함수 (tf.function)"], nb=[("ch6", "텐서플로 함수")], exp=[]),
 "합성곱 (Convolution) · 필터 · 특성맵": dict(ex=["합성곱 직접 해보기 (tf.nn.conv2d + 필터)", "Conv2D 층"], nb=[("ch7a", "합성곱이란 무엇인가"), ("ch7b", "Convolution")], exp=["cnn_filters"]),
 "패딩 · 스트라이드": dict(ex=["패딩 (SAME vs VALID) · 스트라이드 · 출력 크기"], nb=[("ch7a", "VALID vs SAME 패딩")], exp=["cnn_pad"]),
 "풀링 (Pooling)": dict(ex=["풀링 (Max · Average · Global Average)"], nb=[("ch7a", "풀링 층"), ("ch7b", "Pooling")], exp=["cnn_pool"]),
 "CNN 구조 · MLP와 비교": dict(ex=["CNN으로 Fashion MNIST (교수님 7-1 구조)"], nb=[("ch7a", "CNN으로 패션 MNIST 문제 풀기"), ("ch7b", "MLP 과 CNN 의 예측 비교")], exp=["cnn_vs"]),
})
# 기존 개념에 3장 노트북 연결 추가
for _k in ["신경망 · 뉴런 · 층", "원-핫 인코딩"]:
    LINK[_k]["nb"] = LINK[_k]["nb"] + [("ch3", "필기체 숫자 인식")]
