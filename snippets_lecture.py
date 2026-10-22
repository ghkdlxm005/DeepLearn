# 교수님 강조 (수업 녹음 9/12 ~ 10/17 받아쓰기 + 9/26 줌 보강 기록(노션)을 정리)
# 강조 기준: ★★★ 교수님이 중요/시험이라고 하거나 수업 중 직접 질문함, ★★ 반복·길게 설명, ★ 언급
# 받아쓰기는 자동 인식이라 말이 틀린 곳이 있어 교수님 노트북·교과서와 맞춰 정리함.

SECTIONS_LECTURE = [("lecture", "교수님 강조")]


def _qa(rows):
    """[(날짜, 별, 질문, 답)] → 표"""
    tr = "".join(f"<tr><td>{d}</td><td>{s}</td><td>{q}</td><td class=\"ans\">{a}</td></tr>" for d, s, q, a in rows)
    bar = ('<div class="qa-bar"><button class="qa-toggle" type="button" aria-pressed="false">답 가리기 (연습)</button>'
           '<span class="qa-hint">가린 뒤 질문을 보고 직접 써 본 다음, 답 칸을 누르면 하나씩 보입니다</span></div>')
    return f"{bar}<table class=\"qa\"><tr><th>날짜</th><th>강조</th><th>교수님 질문</th><th>답 (핵심만, 시험엔 자기 말로)</th></tr>{tr}</table>"


def register(add):
    def _a(sec, title, kw, code="", html="", **k):
        add(sec, title, kw + " 녹음 수업 교수님 강조 질문", code=code, html=html, **k)

    # ------------------------------------------------------------------ 한눈에
    _a("lecture", "시험 관련 언급 모음", "시험 형식 규칙 중간고사 채점 과제 형식 서술",
html="""<ul>
<li><b>형식</b>: 교수님이 준 Colab 노트북에 직접 작성해서 제출. 지난번(머신러닝 중간고사)과 같은 방식 (10/10)</li>
<li><b>허용</b>: 구글 검색 O, GPT 같은 AI X (9/19 학생 질문에 교수님 답)</li>
<li><b>채점</b>: "여러분들이 이해했는지 안 했는지 읽어보면 되니까" → 설명을 <b>자기 말로</b> (10/10)</li>
<li><b>어려운 점</b>: "시험은 항상 어렵습니다. 사실 <b>쓰는 게</b> 어렵습니다. 그래서 과제 할 때 (직접) 해라" (10/17)</li>
<li><b>체인 룰 노트북</b>: "요 노트북을 준 이유는 요거(체인 룰로 기울기 구하는 과정)를 보라고, 코드까지 보면 좋고" (9/26)</li>
<li><b>설명 연습</b>: 역전파 그림을 보고 "여러분 말로 설명할 수 있어야" 한다며 5분 설명 연습을 시킴 (9/19)</li>
<li><b>과제 형식</b>
  <ul><li>9/12: 실습 복습 + 노트북에 <b>마크다운으로 설명</b> 써서 제출</li>
  <li>9/19: 손글씨 숫자 인식을 <b>데이터 증강</b>으로 개선</li>
  <li>9/26: 옵티마이저 실험 코드를 각자 돌려 보고 복습 (명절 보강이라 수업 중 실습 생략)</li>
  <li>10/10: 실습 노트북을 처음부터 돌리고 <b>에러를 고친 뒤, 그 에러가 뭐였는지 텍스트 박스에 쓰기</b></li></ul></li>
<li><b>수업 중 실습 지시 (변형형)</b>: Flatten 빼고 reshape로 784 입력 / sparse → categorical로 바꾸기 (9/19), 옵티마이저 바꿔 보기 (10/10), metrics MAE → MSE (10/10)</li>
<li><b>정의형 질문에 단어로 답하지 말 것</b>: "정밀도가 뭐냐고 물었는데 정밀도라고 답하면 어떡합니까", "단어 보고 단어를 얘기하는 거지" → 개념(무엇을, 왜)으로 설명 (10/10)</li>
</ul>""")

    _a("lecture", "교수님이 수업 중 던진 질문 → 답 (전체)", "질문 답 퀴즈 서술형 예상문제 왜 그럴까 한눈에",
html=_qa([
 ("9/12", "★★★", "활성화 함수는 왜 쓰나?", "가중합을 받아 그 뉴런의 출력(결론)을 결정. 가중치=곱하기, Σ=합하기, 활성화=결론. 비선형이 없으면 층을 쌓아도 선형 하나와 같음"),
 ("9/12", "★★★", "(퀴즈) ReLU와 softmax의 차이?", "ReLU는 뉴런 하나씩 독립적으로(음수→0, 양수→그대로). softmax는 출력 전체를 함께 보고 합이 1인 확률로 → '이 중 제일 센 놈'. 그래서 은닉층엔 ReLU, 출력층엔 softmax"),
 ("9/12", "★★★", "오차를 왜 제곱하나?", "그냥 빼서 더하면 +와 −가 상쇄됨. 절댓값은 0에서 미분 불가. 제곱은 부호가 없어지고 2차 함수라 미분 가능 → 경사하강으로 최저점 찾기"),
 ("9/12", "★★★", "Dense(300) 파라미터가 왜 235,500개?", "784×300(가중치) + 300(뉴런마다 편향 1개)"),
 ("9/12", "★★★", "검증(validation) 세트는 왜 나누나?", "테스트는 훈련이 끝난 뒤. 오래 걸리는 훈련 도중에 잘 되는지 epoch마다 확인하고, 계속할지 멈출지 판단하려고"),
 ("9/12", "★★★", "숫자(MNIST) 모델을 Fashion MNIST에 써도 되나?", "된다. 입력(28×28=784)과 출력(10클래스)이 같으므로. 성능이 부족하면 은닉 뉴런을 늘림(대신 느려짐)"),
 ("9/12", "★★★", "loss / optimizer / metrics는 각각 뭐?", "loss: 예측과 정답의 오차(줄일 대상). optimizer: 역전파로 구한 기울기를 얼마만큼 어떻게 적용할지. metrics: 사람이 보려고 출력하는 값, 학습엔 안 쓰임"),
 ("9/12", "★★★", "(퀴즈) 함수형 API에서 입력이 여러 개 가능한가?", "가능. inputs=[입력A, 입력B]처럼 리스트로. 출력도 여러 개 가능"),
 ("9/12", "★★", "하이퍼파라미터란? epoch를 많이 하면 무조건 좋나?", "사람이 바깥에서 정하는 값(층 수, 뉴런 수, 활성화, 학습률, epoch, 배치 크기). 많이 돌린다고 무조건 좋진 않음 → 과적합 가능성"),
 ("9/12", "★★", "첫 번째 AI 겨울은 왜?", "Minsky가 단층 퍼셉트론은 XOR을 못 푼다고 증명. 층을 쌓으면 되지만 가중치를 사람이 찾을 수 없었음 → 역전파로 해결"),
 ("9/19", "★★★", "라벨은 숫자 하나인데 출력은 10개. 그대로 돌려도 되나?", "sparse_categorical_crossentropy는 정수 라벨을 알아서 처리해서 됨. categorical_crossentropy는 출력과 모양이 같은 원-핫 라벨이 필요"),
 ("9/19", "★★★", "원-핫 인코딩이 뭐지?", "범주를 클래스 수만큼 칸으로 만들고 해당 칸만 1, 나머지 0. 숫자 라벨(TV=0, 냉장고=1)은 신경망이 크기·순서로 오해하므로"),
 ("9/19", "★★★", "손실 함수는 왜 이렇게 많을까?", "정답의 형태(정수/원-핫/연속값)와 문제(분류/회귀/이상치)가 달라서. '이것만 이해해도 충분한 레벨업'"),
 ("9/19", "★★★", "앞에 Flatten 층은 왜 있나?", "28×28 이미지를 784개 1차원으로 펴서 Dense에 넣으려고. 숫자 MNIST 노트북은 Flatten 대신 미리 reshape(60000, 784)"),
 ("9/19", "★★★", "'베스트 스코어를 보존한다'는 게 뭐야?", "점수가 아니라 점수가 가장 좋았을 때의 <b>가중치</b>를 저장(save_best_only=True)"),
 ("9/19", "★★★", "callbacks 리스트 안의 순서가 중요한가?", "중요하지 않음. 케라스가 콜백 종류를 보고 알아서 처리"),
 ("9/19", "★★★", "일부 연결을 끊으면 성능이 좋아질까?", "꼭은 아니지만 좋아지는 경우가 많음. 과적합이 줄어서 (→ 나중에 배울 Dropout)"),
 ("9/19", "★★★", "왜 cost(비용)라고 부르나?", "최적화 분야에서 온 말. 여러 요인을 바꿨을 때 드는 비용을 최소화하는 문제로 보기 때문"),
 ("9/19", "★★★", "손으로 그린 숫자를 모델이 못 알아보면?", "데이터 증강: 이동·회전 등으로 변형해 데이터를 늘리고 다시 훈련 (기존 데이터와 내 데이터의 분포가 달라서)"),
 ("9/19", "★★", "마지막에 더한 숫자 하나는 뭐?", "편향(bias). '흥분 잘하는 뉴런 / 침착한 뉴런' → 뉴런마다 활성화되기 쉬운 정도"),
 ("9/19", "★★", "softmax는 뭐라고?", "출력층 맨 끝. 출력 10개를 합이 1인 확률로 만들어 가장 센 것을 고름. 옆 뉴런과 함께 계산"),
 ("9/26", "★★★", "(퀴즈) 입력층 바로 뒤의 배치 정규화는 의미가 있을까?", "MNIST는 784개 픽셀이 모두 0~255로 이미 같은 스케일 → 넣어도 문제는 없지만 의미 없음. 스케일이 제각각인 데이터라면 도움이 됨"),
 ("9/26", "★★", "왜 오차를 제곱한다고 했지? (9/12·9/19에 이어 세 번째)", "합치면 +와 −가 상쇄되니까 부호를 없애려고. 분류는 제곱 대신 로그를 쓰는 교차 엔트로피, 회귀는 MSE"),
 ("9/26", "★★", "기울기 소실은 왜 생기나?", "역전파로 앞(아래)층으로 갈수록 기울기가 0에 가까워짐. sigmoid를 거치면 출력의 평균·분산이 입력과 달라지는 게 주원인"),
 ("9/26", "★★", "드롭아웃을 하면 왜 더 잘 되나?", "한 뉴런(반의 '철수')이 결론을 주도하면 나머지는 들러리 → 랜덤하게 끊으면 다른 뉴런도 일을 해서 과적합이 줄어듦"),
 ("10/3", "★★★", "텐서플로는 왜 자동 형변환을 안 하나?", "속도. 변환하려면 모든 연산에 '타입이 다른가?' if 검사가 들어가 같은 타입도 느려짐. 데이터·층이 엄청 많아서 → tf.cast로 사람이 맞춤"),
 ("10/3", "★★★", "(보너스) 둘 다 실수인데 float32 + float64는 왜 에러?", "TF 기본 dtype은 float32/int32(넘파이는 64). 같은 실수여도 타입이 달라 자동 변환 안 함. constant라서가 아님"),
 ("10/3", "★★★", "후버 손실에서 if 대신 tf.where를 쓴 이유?", "속도. 분기(점프)가 없어 파이프라인에 순서대로 흐름. 두 값을 다 계산해도 병렬(GPU)이라 더 빠름"),
 ("10/3", "★★★", "희소 텐서 s6은 왜 에러가 났나?", "인덱스가 행·열 순서로 정렬 안 됨 → 순서 바꾸거나 tf.sparse.reorder"),
 ("10/3", "★★", "넘파이 배열 기본 타입은?", "float64 / int64. TF는 아무것도 안 하면 32비트"),
 ("10/10", "★★★", "정밀도(precision)의 개념은?", "모델이 양성이라고 한 것 중 실제 양성 비율 TP/(TP+FP). 암이라고 불러낸 사람 중 진짜 암 환자 비율 (놓친 건 재현율)"),
 ("10/10", "★★★", "배치별 정밀도 80%, 0% → 평균 40%가 맞나?", "틀림. 전체로 봐야 함: 양성 예측 8개 중 4개 맞음 = 50%. 그래서 누적하는 스트리밍 지표(keras.metrics.Precision)"),
 ("10/10", "★★★", "*, **는 뭘 할 것 같아?", "*: 위치 인자 여러 개를 튜플로 받음. **: 이름=값 인자를 딕셔너리로 받음. super().__init__(**kwargs)로 부모에게 그대로 넘김"),
 ("10/10", "★★★", "층의 call은 언제 쓰이나?", "순전파(피드포워드) 할 때. 입력을 받아 출력을 계산"),
 ("10/10", "★★★", "노이즈를 왜 넣을까? 훈련 때만 넣는 걸 어떻게 자동화?", "열악한 상황에서 훈련하면 강건해짐(규제). call(self, X, training=None)에서 training일 때만 노이즈"),
 ("10/10", "★★★", "에폭은 뭐야? (배치와 구분)", "에폭: 전체 데이터를 한 번 다 도는 것. 배치: 그 안에서 한 번에 처리하는 묶음(32개)"),
 ("10/10", "★★★", "데코레이터 알아?", "함수를 받아 앞뒤에 기능을 덧붙인 새 함수를 돌려주는 함수. @tf.function을 붙이면 자동으로 그래프 함수가 됨"),
 ("10/10", "★★", "손실과 지표를 왜 따로 쓰나?", "손실은 그래디언트를 만들어 학습에, 지표는 사람이 진행 상황을 보려고"),
 ("10/17", "★★★", "포토샵 누끼(엣지)는 어떻게 따나?", "이웃 픽셀 사이의 밝기 차이를 필터로 계산"),
 ("10/17", "★★★", "소벨 필터를 적용하면 왜 경계만 밝게 나오나?", "고른 영역은 곱의 합이 0으로 상쇄, 경계에서만 양쪽 값이 달라 큰 값"),
 ("10/17", "★★★", "이미지가 커져도 가중치가 늘었나 줄었나? 왜?", "안 늘어남. 파라미터 = 필터 개수×(필터 크기×입력 채널)+필터 개수. 이미지 크기가 식에 없음"),
 ("10/17", "★★★", "max와 average 풀링 중 어느 게 나을까? 어느 게 빠를까?", "해 보니 max가 더 잘 맞음. max가 빠름(가장 큰 값만, average는 더하고 나눠야 함)"),
 ("10/17", "★★★", "풀링층에 파라미터가 있다? 없다?", "없음(0). 칸 안에서 최댓값을 고를 뿐 학습할 게 없음"),
 ("10/17", "★★★", "conv1 파라미터는 왜 320? conv2는 왜 32를 곱하나?", "(3×3×1+1)×32=320. 앞 층 필터 32개 = 입력 채널 32 → (3×3×32+1)×64=18,496"),
 ("10/17", "★★★", "직접 만든 필터(0행 1, 6행 −1)는 어떤 엣지를 잡나?", "위아래 밝기가 바뀌는 가로(수평) 엣지. 열 방향으로 넣으면 세로 엣지"),
 ("10/17", "★★★", "3×3 conv를 연속으로 쌓는 이유는?", "더 넓게 봄(3×3 두 번=5×5, 세 번=7×7), 비선형이 여러 번, 파라미터는 적음(27 vs 49)"),
 ("10/17", "★★★", "ImageNet 대회는 왜 없어졌나?", "정확도가 사람보다 높아져서 더 할 의미가 없음"),
 ("10/17", "★★★", "분류만으로 자율주행이 될까?", "안 됨. 분류는 출력이 하나. 여러 물체와 위치가 필요 → 객체 검출, 실제로는 분할까지"),
]))

    # ------------------------------------------------------------------ 신경망 기초 (9/12, 9/19)
    _a("lecture", "★★★ 뉴런 한 개의 계산: 가중합 + 편향 → 활성화 (9/12·9/19)", "뉴런 수식 가중합 편향 bias 활성화 함수 activation 퍼셉트론 TLU 계단 함수",
"""import numpy as np
x = np.array([0.2, 0.8, 0.5])      # 앞 뉴런들의 출력(activation)
w = np.array([0.4, -0.6, 0.9])     # 가중치
b = 0.1                            # 편향
z = x @ w + b                      # 가중합 + 편향
a = max(0, z)                      # 활성화(ReLU) → 이 뉴런의 출력
print(z, a)""",
html="""<ul>
<li>순서: 입력 × <b>가중치</b> → <b>Σ 합</b> → +<b>편향</b> → <b>활성화 함수</b> → 출력</li>
<li>"가중치는 곱할 때, Σ는 합할 때, <b>결론을 내는 게 활성화 함수</b>" (9/12)</li>
<li>합계로 결론을 내지 않음 → 합계에 활성화 함수를 적용해서 결론 (9/19)</li>
<li><b>편향 비유</b>: 살짝만 건드려도 흥분하는 뉴런 / 아무리 건드려도 침착한 뉴런 → 뉴런마다 활성화되기 쉬운 정도</li>
<li>행렬로 쓰면 a¹ = σ(W·a⁰ + b), W는 (16×784). "수학은 언어다" — 식을 읽을 줄 알면 누구나 같게 이해하고 바로 코드로 짤 수 있음</li>
<li>입력 픽셀 값도 activation이라고 부름 (뉴런의 출력값 = activation)</li>
</ul>""")

    _a("lecture", "★★★ ReLU vs softmax (9/12 퀴즈) · sigmoid → ReLU (9/19)", "relu softmax sigmoid 차이 퀴즈 출력층 은닉층 vanishing gradient 기울기 소실",
"""z = tf.constant([[2.0, -1.0, 0.5]])
print(tf.nn.relu(z))        # [2, 0, 0.5]  각자 따로: 음수 → 0, 양수 → 그대로
print(tf.nn.softmax(z))     # 합이 1인 확률: 셋을 함께 보고 제일 센 쪽이 큼
print(tf.nn.sigmoid(z))     # 각자 0~1로 눌러 줌""",
html="""<ul>
<li><b>ReLU</b>: 뉴런 하나씩 <b>독립적으로</b> 출력 결정. 다른 뉴런과 비교 안 함</li>
<li><b>softmax</b>: 출력 10개를 <b>함께</b> 보고 합이 1인 확률로 → "이 중에 제일 센 놈이 누구야" (3번 이상 반복)</li>
<li>은닉층에 softmax? → 뉴런끼리 경쟁시키는 셈. 은닉층은 각 특성마다 반응해야 하므로 ReLU</li>
<li><b>sigmoid의 문제</b>: 층을 깊게 쌓으면 역전파 때 앞쪽 층의 기울기가 사라짐(기울기 소실) → 학습이 안 됨</li>
<li><b>ReLU</b>(Rectified Linear Unit): 생물학적 뉴런처럼(0/1) 했더니 안 돼서 변형한 것</li>
</ul>""")

    _a("lecture", "★★★ 오차를 제곱하는 이유 · cost라는 이름 · 경사하강 · 옵티마이저 (9/12·9/19)", "손실 오차 제곱 이유 mse cost 비용 경사하강법 gradient descent optimizer 학습률 극소점",
html="""<ul>
<li><b>제곱하는 이유</b>: 그냥 더하면 +오차와 −오차가 상쇄. 절댓값은 0에서 미분이 안 됨. 제곱은 부호가 사라지고 2차 함수라 미분 가능 → 최저점을 찾아 각 가중치를 얼마나 고칠지 결정</li>
<li><b>왜 cost(비용)?</b> 최적화 분야 용어. 프로젝트에서 사람을 더 뽑을지, 좋은 컴퓨터를 살지, 기간을 늘릴지에 따른 비용을 최소화하듯 오차를 최소화</li>
<li>cost 함수의 입력은 파라미터 13,002개, 출력은 숫자 하나 (훈련 데이터 전체 평균)</li>
<li><b>경사하강</b>: 각 변수로 미분해서 기울기를 구하고 내려가는 방향으로 이동. 어려운 점: 극소점이 여러 개, 너무 많이 가면 지나침</li>
<li><b>옵티마이저</b>: 구한 기울기를 <b>얼마만큼, 어떻게</b> 적용할지 정함. 기울기가 3이라고 3을 그대로 적용하지 않음(학습률)</li>
</ul>""")

    _a("lecture", "★★★ 역전파를 자기 말로 (9/19, 5분 설명 연습)", "역전파 backpropagation 직관 설명 서술 체인룰 가중치 편향 조정",
html="""<p>교수님: "여러분 말로 설명할 수 있어야 한다" → 서술형 대비 1순위</p>
<p><b>상황</b>: 숫자 2를 넣었는데 '2' 출력 뉴런이 0.2밖에 안 나옴 → 올려야 함</p>
<ol>
<li><b>편향을 올린다</b>: 가장 쉽지만, 다른 이미지가 와도 이 뉴런이 켜져 버려서 이것만으론 안 됨</li>
<li><b>가중치를 바꾼다</b>: 앞 층 뉴런과의 연결 중 특히 <b>강하게 켜진</b> 뉴런과의 가중치를 올리는 게 효과가 큼</li>
<li><b>앞 층의 출력을 바꾼다</b>: 직접은 못 바꾸므로 그 앞 층의 가중치·편향으로 조절해야 함 → <b>뒤에서 앞으로 전파</b>(역전파)</li>
</ol>
<ul>
<li>나머지 9개 출력은 내려야 함 → 출력 뉴런마다 조정량이 나옴</li>
<li>실제로는 배치의 여러 이미지에 대해 미분으로 조정량을 구하고 <b>평균</b>. 평균을 얼마나·어떻게 적용할지는 옵티마이저</li>
<li>예전엔 유전 알고리즘(점수 높은 애들만 자손을 남김)으로 가중치를 찾았지만, 정답과 함께 넣는 역전파가 훨씬 빠름 (9/12)</li>
</ul>""")

    _a("lecture", "★★★ 파라미터 개수 계산 모음 (9/12·9/19·10/17)", "파라미터 개수 param summary 235500 13002 266610 421642 편향 계산 공식",
"""m = keras.Sequential([keras.layers.Input(shape=(28, 28)), keras.layers.Flatten(),
                      keras.layers.Dense(300, activation="relu"),
                      keras.layers.Dense(100, activation="relu"),
                      keras.layers.Dense(10, activation="softmax")])
print([l.count_params() for l in m.layers], m.count_params())   # [0, 235500, 30100, 1010] 266610

m2 = keras.Sequential([keras.layers.Input(shape=(784,)),
                       keras.layers.Dense(16, activation="relu"),
                       keras.layers.Dense(16, activation="relu"),
                       keras.layers.Dense(10, activation="softmax")])
print([l.count_params() for l in m2.layers], m2.count_params())  # [12560, 272, 170] 13002""",
html="""<ul>
<li><b>Dense</b>: (입력 수 × 뉴런 수) + 뉴런 수(편향). 784×300+300 = <b>235,500</b></li>
<li>Fashion MNIST MLP 300-100-10: 235,500 + 30,100 + 1,010 = <b>266,610</b> (Flatten은 0)</li>
<li>숫자 MNIST 16-16-10: 12,560 + 272 + 170 = <b>13,002</b> ← 받아쓰기엔 13,200처럼 들렸지만 정답은 13,002</li>
<li><b>Conv2D</b>: (필터 높이×너비×입력 채널 + 1) × 필터 개수 → 320, 18,496 (CNN 카드 참고)</li>
<li>학습되는 것 = 이 가중치와 편향(파라미터)</li>
</ul>""")

    _a("lecture", "★★ XOR와 첫 번째 AI 겨울 (9/12, 직접 손계산)", "xor 퍼셉트론 minsky 민스키 ai 겨울 빙하기 다층 퍼셉트론 계단 함수 손계산",
"""import numpy as np
step = lambda z: (z >= 0).astype(int)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
h = step(X @ np.array([[1, 1], [1, 1]]) + np.array([-1.5, -0.5]))   # 은닉 뉴런 2개 (AND, OR)
y = step(h @ np.array([-1, 1]) - 0.5)                               # OR 이면서 AND 아님
print(y)     # [0 1 1 0]  = XOR""",
html="""<ul>
<li>단층 퍼셉트론은 AND·OR·NOT은 되지만 <b>XOR은 안 됨</b> (Minsky 증명) → 첫 번째 AI 겨울</li>
<li>층을 하나 더 쌓으면 풀림. 그런데 층이 많으면 가중치를 사람이 못 찾음 → <b>역전파</b>로 컴퓨터가 찾게 함</li>
<li>(1,1) 대입: 은닉1 = 2−1.5 > 0 → 1, 은닉2 = 2−0.5 > 0 → 1, 출력 = −1+1−0.5 < 0 → 0</li>
</ul>""")

    # ------------------------------------------------------------------ 케라스 (9/12, 9/19)
    _a("lecture", "★★★ 검증 세트 · compile 세 가지 · epoch vs 배치 (9/12·10/10)", "validation 검증 세트 이유 compile loss optimizer metrics epoch 에폭 배치 batch",
"""X_valid, X_train = X_train_full[:5000] / 255., X_train_full[5000:] / 255.
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]
model.compile(loss="sparse_categorical_crossentropy",   # 줄일 대상 (역전파)
              optimizer="sgd",                          # 기울기를 어떻게 적용할지
              metrics=["accuracy"])                     # 사람이 보는 값
history = model.fit(X_train, y_train, epochs=30,
                    validation_data=(X_valid, y_valid))   # epoch마다 val_loss, val_accuracy 출력""",
html="""<ul>
<li><b>검증 세트</b>: 테스트는 훈련이 끝난 뒤에 함. 오래 걸리는 훈련 <b>도중에</b> 잘 되는지 보려고 일부를 떼어 epoch마다 평가 → 계속할지 멈출지 판단</li>
<li><b>/255</b>: 픽셀은 1바이트(uint8)라 0~255 → 0~1로</li>
<li><b>compile</b> 하는 순간 빠르게 계산할 수 있는 형태(그래프)로 바뀜</li>
<li><b>epoch</b> = 전체 데이터를 한 번 다 도는 것, <b>배치</b> = 한 번에 처리하는 묶음(기본 32). 스텝 수 = 55000/32 ≈ 1719</li>
<li>첫 epoch엔 loss가 크고 점점 떨어지는 게 정상. 초기화·옵티마이저를 잘못 잡으면 학습이 안 될 수 있음</li>
</ul>""")

    _a("lecture", "★★★ sparse vs categorical · 원-핫 · Flatten vs reshape (9/19 실습 과제)", "sparse_categorical_crossentropy categorical_crossentropy 원핫 one-hot to_categorical flatten reshape 784 실습 변형",
"""from tensorflow.keras.utils import to_categorical
y_onehot = to_categorical(y_train, 10)         # 정수 3 → [0,0,0,1,0,0,0,0,0,0]

# 변형 1) Flatten 빼고 직접 reshape
X_flat = X_train.reshape(-1, 28 * 28)          # (55000, 784)
m = keras.Sequential([keras.layers.Input(shape=(784,)),
                      keras.layers.Dense(300, activation="relu"),
                      keras.layers.Dense(100, activation="relu"),
                      keras.layers.Dense(10, activation="softmax")])
# 변형 2) categorical_crossentropy → 라벨도 원-핫으로
m.compile(loss="categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])
m.fit(X_flat, y_onehot, epochs=1, verbose=0)""",
html="""<ul>
<li><b>sparse_categorical_crossentropy</b>: 정답이 정수(0~9). 원-핫 없이 내부에서 맞춰 줌</li>
<li><b>categorical_crossentropy</b>: 정답이 원-핫(출력과 같은 모양). 정수 라벨 그대로면 <code>Shapes (None, 10) and (None, 1) are incompatible</code></li>
<li>숫자 MNIST 노트북은 반대: y를 원-핫으로 만들었으니 categorical. 여기서 sparse로 바꾸면 에러</li>
<li><b>원-핫이 필요한 이유</b>: TV=0, 냉장고=1처럼 숫자로 넣으면 신경망이 곱하고 더하면서 "냉장고가 TV보다 크다"는 없는 순서를 만듦</li>
<li><b>Flatten</b>: 28×28 → 784로 펴 주는 층. 숫자 MNIST는 Flatten 없이 미리 reshape(60000, 784)</li>
<li>"손실 함수는 왜 이렇게 많을까? 이것만 이해해도 충분한 레벨업"</li>
</ul>""")

    _a("lecture", "★★★ 콜백: 체크포인트 · 조기 종료 (9/12·9/19)", "callback 콜백 ModelCheckpoint save_best_only EarlyStopping patience restore_best_weights 베스트 순서",
"""checkpoint_cb = keras.callbacks.ModelCheckpoint("my_model.keras", save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True)
history = model.fit(X_train, y_train, epochs=100,
                    validation_data=(X_valid, y_valid),
                    callbacks=[checkpoint_cb, early_stopping_cb])   # 순서 상관없음""",
html="""<ul>
<li>"베스트 스코어를 보존한다" = 점수가 아니라 <b>가장 좋았을 때의 가중치</b>를 저장</li>
<li>10만 번 돌렸는데 9만 번째가 최고였다면 그 뒤는 개선 없음(오히려 과적합) → 그때 저장된 걸 씀</li>
<li><b>EarlyStopping(patience=10)</b>: 10 epoch 동안 나아지지 않으면 멈춤, restore_best_weights로 최고 가중치 복원 → epochs를 100처럼 크게 줘도 됨</li>
<li>callbacks 리스트 <b>순서는 중요하지 않음</b>: 케라스가 콜백 종류를 보고 알아서 처리</li>
<li>Colab은 12시간 VM → 드라이브에 체크포인트를 저장해 두면 끊겨도 최고 모델이 남음</li>
</ul>""")

    _a("lecture", "★★★ 함수형 API: 층이 곧 함수, 입력·출력 여러 개 (9/12)", "함수형 api functional wide deep concatenate keras.Model 입력 여러 개 다중 입력 출력 skip",
"""input_ = keras.layers.Input(shape=(8,))
hidden1 = keras.layers.Dense(30, activation="relu")(input_)    # 층을 만들고 바로 호출 = 연결
hidden2 = keras.layers.Dense(30, activation="relu")(hidden1)
concat = keras.layers.Concatenate()([input_, hidden2])        # 입력을 건너뛰어 합침
output = keras.layers.Dense(1)(concat)
model = keras.Model(inputs=[input_], outputs=[output])

input_A = keras.layers.Input(shape=(5,), name="wide_input")    # 입력 2개
input_B = keras.layers.Input(shape=(6,), name="deep_input")
h = keras.layers.Dense(30, activation="relu")(input_B)
out = keras.layers.Dense(1)(keras.layers.Concatenate()([input_A, h]))
model2 = keras.Model(inputs=[input_A, input_B], outputs=[out])
model2.summary()""",
html="""<ul>
<li>Sequential은 일렬로만 쌓음. 건너뛰거나 갈라지는 구조는 <b>함수형 API</b></li>
<li>핵심: <b>층 객체 자체가 함수</b> → 만들고 바로 (이전 층 출력)을 넣어 호출하면 연결됨. 마지막에 keras.Model(inputs, outputs)</li>
<li>건너뛰는 이유: 깊은 경로를 거치면 단순한 패턴을 잊을 수 있어서 다시 반영 (ResNet도 같은 목적)</li>
<li>퀴즈 "입력이 여러 개 가능?" → <b>가능</b>, 출력도 여러 개 가능 (예: 사진 → "사자다" + 위치)</li>
<li>"굳이 다 해보는 게 목적이 아니고 이 정도만 이해하면 될 것 같아요"</li>
</ul>""")

    _a("lecture", "★★ 저장·불러오기 · 케라스를 쓰는 이유 (9/12·9/19)", "save load_model 저장 복원 keras 이유 tensorflow pytorch 호환",
"""model.save("my_model.keras")
model2 = keras.models.load_model("my_model.keras")   # model2는 훈련한 게 아니라 파일에서 만든 모델
print(np.allclose(model.predict(X_test[:3], verbose=0), model2.predict(X_test[:3], verbose=0)))   # True""",
html="""<ul>
<li>잘 훈련한 모델을 파일로 저장해서 동료에게 넘겨줄 수 있음 (가중치 = 모델)</li>
<li>TensorFlow 모델과 PyTorch 모델은 서로 바로 못 씀 → 위에 공통 API인 <b>Keras</b>를 씌워 Keras 형식으로 저장하면 양쪽에서 읽을 수 있음. 변환은 가능하지만 귀찮고 미세한 차이 → "그 귀찮은 걸 케라스가 해준다"</li>
</ul>""")

    _a("lecture", "★★ MLP의 한계 → CNN · RNN, 데이터 증강 (9/12·9/19)", "mlp 한계 cnn rnn 이미지 순서 데이터 증강 augmentation 과제 손글씨",
html="""<ul>
<li>이미지는 <b>이웃 픽셀</b>이 중요한데 784로 일렬로 펴면 그 정보를 버림 → CNN</li>
<li>언어는 단어 <b>순서</b>가 중요 → RNN. 둘 다 같은 신경망이고 배치 방식만 다름</li>
<li>비트맵 비교로는 숫자를 못 알아봄: 사람마다 3을 다르게 씀 → 규칙을 짜는 건 불가능, 학습시킴</li>
<li><b>데이터 증강 (9/19 과제)</b>: 손으로 그린 숫자를 못 맞히는 건 훈련 데이터와 분포가 달라서 → 이동·회전 등으로 변형해 데이터를 늘리고 다시 훈련</li>
<li>은닉층 직관: 첫 층은 짧은 획·엣지, 다음 층은 동그라미·긴 선을 찾지 않을까 (꼭 그렇게 되는 건 아님)</li>
</ul>""")


    # ------------------------------------------------------------------ 깊은 신경망 훈련의 문제와 해결 (9/26)
    _a("lecture", "★★ 깊은 신경망의 4가지 문제 · 체인 룰 복습 (9/26)", "기울기 소실 vanishing gradient 폭주 exploding 과적합 overfitting 훈련 비용 체인 룰 chain rule 예측 빼기 정답 하울링",
html="""<ul>
<li><b>복습</b>: 뉴런은 두 단계 — 곱하고 더한 값 <b>Z</b>, 활성화를 거친 값 <b>A</b>. 체인 룰: ∂L/∂W = ∂L/∂Z × ∂Z/∂W (분모·분자에 같은 걸 곱해도 값은 같다)</li>
<li>softmax + 교차 엔트로피를 같이 쓰는 이유: 미분하면 <b>예측 − 정답</b>으로 간단해짐. ∂Z/∂W = 앞 층의 activation → 앞 activation(전치)과 내적</li>
<li>"요 노트북(Optimizer, NumPy 역전파)을 준 이유는 이걸 보라고" — 코드까지 따라가 보기</li>
<li><b>① 기울기 소실</b>: 앞(아래)층으로 갈수록 기울기가 0에 가까워져 학습이 안 됨. 원인: sigmoid를 거치면 출력의 평균·분산이 입력과 달라짐(He 등의 연구). tanh는 조금 나음</li>
<li><b>② 기울기 폭주</b>: RNN처럼 되먹임하는 구조에서 계속 커짐 — 마이크를 스피커 앞에 두면 삐 하는 하울링처럼</li>
<li><b>③ 훈련 비용</b>: 데이터 레이블링·컴퓨팅 비용, 몇 주씩 돌렸는데 틀리면 다시</li>
<li><b>④ 과적합</b>: MNIST는 미국 사람 글씨에 과적합 → 교수님 글씨는 잘 못 알아봄</li>
<li>해결책들(초기화·활성화·배치 정규화·옵티마이저)은 서로 <b>대체가 아니라 같이</b> 씀</li>
</ul>""")

    _a("lecture", "★★ 가중치 초기화와 활성화 함수는 세트 (9/26)", "초기화 initializer glorot xavier he lecun fan_in fan_out 팬인 팬아웃 relu leaky relu elu selu dying relu 죽은 렐루",
"""he = keras.layers.Dense(10, activation="relu", kernel_initializer="he_normal")       # ReLU ↔ He
glorot = keras.layers.Dense(10, activation="tanh")                                   # 기본값 = glorot_uniform
selu = keras.layers.Dense(10, activation="selu", kernel_initializer="lecun_normal")  # SELU ↔ LeCun
leaky = keras.layers.LeakyReLU(negative_slope=0.2)      # 0 밑에도 작은 기울기
x = tf.constant([[-3., -1., 0., 2.]])
print(tf.nn.relu(x), leaky(x), tf.nn.elu(x), tf.nn.selu(x), sep="\\n")
print(type(keras.layers.Dense(1).kernel_initializer).__name__)    # GlorotUniform""",
html="""<ul>
<li>랜덤하게 넣는 건 같지만 <b>뽑는 분포</b>를 바꿔서 입력·출력의 평균·분산을 맞추자는 아이디어</li>
<li><b>팬인</b> = 앞쪽으로 부채처럼 연결된 수, <b>팬아웃</b> = 뒤쪽 연결 수 (784→16이면 팬인 784, 팬아웃 16)</li>
<li><b>Glorot(Xavier)</b>: 분산 1/fan_avg. <b>케라스 기본값</b> → "여러분이 아무것도 안 줬을 때 사실 이걸 쓰고 있던 거야"</li>
<li><b>He</b>: ReLU용, 팬인만 사용. <b>LeCun</b>: SELU용</li>
<li>"초기화하고 액티베이션은 같이 가는 걸로 이해하면 됨"</li>
<li><b>ReLU</b>: 다이오드 정류처럼 0 밑은 0, 위는 그대로. 0 밑이 영영 0이라 <b>죽은 ReLU</b></li>
<li><b>Leaky ReLU</b>: leak = 기름탱크에서 조금씩 새듯 0 밑에도 아주 작은 기울기 → 0에서 얼마나 먼지 알려 줌</li>
<li><b>ELU</b>: 0 밑을 지수 함수로(−1에 가까워짐), <b>SELU</b>: ELU를 스케일 조정</li>
</ul>""")

    _a("lecture", "★★★ 배치 정규화 · 입력층 퀴즈 (9/26)", "배치 정규화 batch normalization BatchNormalization 평균 분산 스케일 입력층 퀴즈 의미",
"""model = keras.Sequential([
    keras.layers.Input(shape=(28, 28)),
    keras.layers.Flatten(),
    keras.layers.BatchNormalization(),            # 퀴즈: 이 자리(입력 바로 뒤)는 의미가 있을까?
    keras.layers.Dense(300, activation="relu"),
    keras.layers.BatchNormalization(),            # 층 다음에 한 줄씩
    keras.layers.Dense(100, activation="relu"),
    keras.layers.BatchNormalization(),
    keras.layers.Dense(10, activation="softmax")])
print([l.count_params() for l in model.layers])   # BN: 특성마다 γ·β·평균·분산 4개""",
html="""<ul>
<li><b>하는 일</b>: 배치(예: 20장)마다 평균을 빼서 0으로, 분산으로 나눠 크기를 맞춘 뒤 γ(스케일)·β(이동)로 조정</li>
<li><b>왜</b>: 어떤 뉴런은 −10,000~10,000, 어떤 뉴런은 −10~10이 나오면 뒤층에서 큰 쪽이 더 중요한 것처럼 취급됨. 뉴런은 서로 독립이라 <b>같은 스케일</b>이어야 함</li>
<li><b>쓰는 법</b>: 해당 층 다음에 <code>BatchNormalization()</code> 한 줄</li>
<li><b>퀴즈 답</b>: 입력층 바로 뒤의 BN → MNIST·Fashion은 784개가 모두 0~255로 이미 같은 스케일 → <b>넣어도 문제는 없지만 의미가 없음</b>. 스케일이 제각각인 데이터라면 도움이 됨</li>
</ul>""")

    _a("lecture", "★★ 전이 학습 · 사전훈련 · 오토인코더 (9/26)", "전이 학습 transfer learning 동결 freeze trainable 사전훈련 pretrain 오토인코더 autoencoder 인코더 디코더 이상 탐지 watson svm",
"""base = keras.Sequential([keras.layers.Input(shape=(28, 28)), keras.layers.Flatten(),
                         keras.layers.Dense(100, activation="relu", name="h1"),
                         keras.layers.Dense(100, activation="relu", name="h2"),
                         keras.layers.Dense(1000, activation="softmax")])     # 1000가지를 분류하던 모델
new = keras.Sequential(base.layers[:-1])                                      # 출력층만 잘라 내고
new.add(keras.layers.Dense(5, activation="softmax"))                         # 꽃 5종용 새 출력층
for layer in new.layers[:-1]:
    layer.trainable = False                    # 앞단은 잠금(동결): 역전파 때 손 안 댐
new.compile(loss="sparse_categorical_crossentropy", optimizer="adam")
print(len(new.trainable_weights))              # 2 (새 출력층의 W, b만)
# 80% 정도 맞추면 다시 풀고(trainable=True) 전체를 낮은 학습률로 미세 조정

encoder = keras.Sequential([keras.layers.Input(shape=(784,)), keras.layers.Dense(20, activation="relu")])
decoder = keras.Sequential([keras.layers.Input(shape=(20,)), keras.layers.Dense(784, activation="sigmoid")])
autoencoder = keras.Sequential([encoder, decoder])     # 784 → 20 → 784 (장구 모양), 입력 = 정답""",
html="""<ul>
<li><b>Watson 사례</b>: 퀴즈쇼에서 인간을 이겼지만 SVM(통계 기반)이라 병원마다 처음부터 다시 훈련 → 실패. 신경망이면 전이 학습이 가능</li>
<li><b>전이 학습</b>: 사진을 잘게 쪼개 보는 앞단은 그대로 쓰고 뒷단만 새 문제에 맞게 교체. 앞단은 <b>동결</b>(학습 안 함). 80% 정도 맞추면 풀고 다시 학습 → 데이터·시간 절약</li>
<li><b>비지도 사전훈련</b>: 레이블 없는 데이터로 먼저 학습. <b>보조 작업</b>: 사람/고양이 얼굴을 구분하던 모델로 직원 얼굴 인식</li>
<li><b>언어</b>: 책 문장 중간 단어를 가리고 맞히게 계속 돌림 → 단어 사이의 연관성을 이해 (사람은 고생 안 함)</li>
<li><b>오토인코더</b>: 784 → 20(인코더, 압축) → 784(디코더, 복원). 입력과 같은 게 나오게 학습. 정상 데이터로 학습해 두면 입력과 출력이 달라질 때 = 이상 (데이터센터·은행 시스템 이상 탐지)</li>
</ul>""")

    _a("lecture", "★★ 옵티마이저 계보 · 학습률 (9/26)", "옵티마이저 optimizer sgd momentum 모멘텀 nesterov 네스테로프 adagrad rmsprop adam nadam 학습률 learning rate eta 에타 발산 지수 이동 평균",
"""opts = {
    "SGD": keras.optimizers.SGD(learning_rate=0.01),
    "모멘텀": keras.optimizers.SGD(learning_rate=0.01, momentum=0.9),
    "Nesterov": keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True),
    "AdaGrad": keras.optimizers.Adagrad(learning_rate=0.01),
    "RMSProp": keras.optimizers.RMSprop(learning_rate=0.001, rho=0.9),
    "Adam": keras.optimizers.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999),
    "Nadam": keras.optimizers.Nadam(learning_rate=0.001),
}
for name, opt in opts.items():
    print(name, type(opt).__name__)
# model.compile(loss=..., optimizer=opts["Adam"], ...)""",
html="""<ul>
<li><b>기본식</b>: 새 가중치 = 기존 가중치 − <b>η</b>(학습률) × 손실의 경사 벡터. 책은 가중치를 θ(세타)로 씀</li>
<li><b>SGD</b>: 전부가 아니라 랜덤하게 뽑은 배치로 경사 하강. 느리지만 오래 돌리면 최종 품질이 좋음</li>
<li><b>모멘텀</b>: 지금까지 가던 방향을 누적(β로 세기 조절) → 같은 방향이면 더 빨리</li>
<li><b>Nesterov</b>: 모멘텀만큼 <b>먼저 가 본 자리에서</b> 경사를 구해 적용 → 더 빨리 수렴</li>
<li><b>AdaGrad</b>: 경사를 원소별로 제곱·누적해서 나눠 축마다 <b>같은 스케일</b>로 → 빠르지만 너무 일찍 멈춤</li>
<li><b>RMSProp</b>: 최근 것에 가중치를 더 주는 <b>지수 가중 이동 평균</b>으로 그 문제를 완화</li>
<li><b>Adam</b> = 모멘텀 + RMSProp (초기값 보정 포함), <b>Nadam</b> = Nesterov + Adam → 실제로 Adam·Nadam을 많이 씀</li>
<li><b>학습률</b>: 너무 크면 양쪽으로 크게 흔들리다 발산, 너무 작으면 오래 걸림</li>
<li><b>드롭아웃</b>(같은 날 언급): 반에서 철수만 답하면 철수가 없는 날 아무도 못 맞힘 → 랜덤하게 끊으면 다른 뉴런도 일을 해서 과적합이 줄어듦. L1·L2 규제는 다음에 설명</li>
</ul>""")

    # ------------------------------------------------------------------ 텐서플로 기초 (10/3)
    _a("lecture", "★★★ 자동 형변환이 없는 이유 · 기본 dtype 32비트 (10/3, 보너스 문제)", "자동 형변환 casting tf.cast dtype float32 float64 int32 넘파이 기본 타입 속도 보너스 InvalidArgumentError",
"""print(tf.constant(42).dtype, tf.constant(1.).dtype)          # int32 float32 (넘파이는 int64, float64)
try:
    tf.constant(2.0) + tf.constant(40)                       # float32 + int32 → 에러
except Exception as e: print(type(e).__name__)
try:
    tf.constant(2.0) + tf.constant(40., dtype=tf.float64)    # 둘 다 실수인데도 에러 (보너스 문제)
except Exception as e: print(type(e).__name__)
t2 = tf.constant(40., dtype=tf.float64)
print(tf.constant(2.0) + tf.cast(t2, tf.float32))            # 42.0""",
html="""<ul>
<li>질문 "TF는 왜 자동 변환을 안 할까?" → <b>속도</b>. 덧셈 함수에 '타입이 다르면 바꾼다'는 if가 들어가면 같은 타입이 와도 매번 검사 → 느려짐. 데이터·층이 엄청 많아서 속도가 중요 → "타입은 사람이 맞춰서 줘라" (이게 철학)</li>
<li>보너스 문제 "float32 + float64는 왜 에러?" → TF 기본은 32비트, 뒤에 건 64비트라 타입이 다름. constant라서가 아님</li>
<li>해결: <code>tf.cast(텐서, tf.float32)</code></li>
</ul>""")

    _a("lecture", "★★★ 희소 텐서 · 래그드 텐서 \"이 두 가지는 꼭 기억\" (10/3)", "sparse 희소 ragged 래그드 비정형 reorder to_dense from_row_splits from_row_lengths from_value_rowids 메모리",
"""s = tf.SparseTensor(indices=[[0, 1], [1, 0], [2, 3]], values=[1., 2., 3.], dense_shape=[3, 4])
print(tf.sparse.to_dense(s))
print(tf.sparse.to_dense(s * 42.))       # 곱하기는 됨,  s + 42. 은 에러
s5 = tf.SparseTensor(indices=[[0, 2], [0, 1]], values=[1., 2.], dense_shape=[3, 4])
print(tf.sparse.to_dense(tf.sparse.reorder(s5)))   # 인덱스 정렬 안 됨 → reorder

v = [3, 1, 4, 1, 5, 9, 2, 6]
r = tf.RaggedTensor.from_row_splits(v, row_splits=[0, 4, 4, 7, 8])   # 행 길이 4,0,3,1
print(r)
print(tf.RaggedTensor.from_row_lengths(v, [4, 0, 3, 1]))
print(tf.RaggedTensor.from_value_rowids(v, [0, 0, 0, 0, 2, 2, 2, 3]))
print(r.to_tensor())                      # 계산하려면 밀집 텐서로""",
html="""<ul>
<li><b>희소(sparse)</b>: MNIST는 펜이 지나간 곳 빼고 다 0 → 1000장이면 의미 없는 0까지 메모리에? → 0이 아닌 것만 저장. dense_shape를 꼭 지정</li>
<li>희소 텐서는 <b>곱하기 외에는 안 되는 걸로</b> 이해 (행렬곱은 sparse_dense_matmul)</li>
<li>s6 에러 → <b>인덱스가 (행, 열) 순서로 정렬 안 돼서</b>. 순서를 바꾸거나 reorder</li>
<li><b>래그드(ragged)</b>: 행마다 길이가 다른 데이터를 있는 것만 저장. 만드는 법 3가지(value_rowids / row_lengths / row_splits) 모두 같은 결과. 길이가 다른 문자열도 래그드</li>
</ul>""")

    _a("lecture", "★★ Variable과 assign · 슬라이싱 · 넘파이와 이름이 다른 함수 (10/3)", "tf.Variable assign 변수 constant 불변 newaxis 슬라이싱 인덱싱 reduce_mean reduce_sum matmul transpose 넘파이 차이",
"""v = tf.Variable([[1., 2., 3.], [4., 5., 6.]])
v.assign(2 * v)              # 같은 메모리에서 값 변경
v[0, 1].assign(42.)
w = v * 2                    # 에러는 없지만 결과는 tf.Variable이 아닌 새 tf.Tensor
print(type(v).__name__, type(w).__name__)

t = tf.constant([[1., 2., 3.], [4., 5., 6.]])
print(t[:, 1:])                      # [[2,3],[5,6]]
print(t[..., 1])                     # [2,5]  1차원으로 풀림
print(t[..., 1, tf.newaxis])         # [[2],[5]] 세로 모양 유지
print(t + 10, t @ tf.transpose(t))   # 브로드캐스팅, 행렬곱
print(tf.reduce_mean(t), tf.reduce_sum(t), tf.math.log(t))""",
html="""<ul>
<li>tf.constant는 <b>읽기 전용</b> → 연산하면 항상 새 텐서. 값을 계속 바꾸려면 <b>tf.Variable + assign</b> ("assign을 사용해야 된다")</li>
<li><code>v = v * 2</code>는 에러는 없지만 type이 Tensor로 바뀌고 다른 메모리의 다른 객체가 됨</li>
<li>"슬라이싱이나 인덱싱 되게 중요" — 넘파이와 같은 방식, newaxis로 모양 유지</li>
<li>넘파이와 다른 이름: np.mean → <b>tf.reduce_mean</b>, np.sum → tf.reduce_sum, np.log → tf.math.log, t.T → tf.transpose, np.dot → tf.matmul(@)</li>
<li>행렬곱은 앞 행렬의 열 수 = 뒤 행렬의 행 수 → 자기 자신과 곱하려면 transpose</li>
</ul>""")

    # ------------------------------------------------------------------ 사용자 정의 (10/3, 10/10)
    _a("lecture", "★★★ 후버 손실 3단계: 함수 → 함수를 만드는 함수 → 클래스 (10/3·10/10)", "huber 후버 손실 tf.where create_huber threshold 클로저 HuberLoss get_config custom_objects 저장 로드 __init__ call",
"""def huber_fn(y_true, y_pred):                       # 1단계: 기준 1 고정
    error = y_true - y_pred
    is_small_error = tf.abs(error) < 1
    squared_loss = tf.square(error) / 2
    linear_loss = tf.abs(error) - 0.5
    return tf.where(is_small_error, squared_loss, linear_loss)

def create_huber(threshold=1.0):                    # 2단계: 기준을 바꾸는 함수를 '만들어서 리턴'
    def huber_fn(y_true, y_pred):
        error = y_true - y_pred
        is_small_error = tf.abs(error) < threshold
        squared_loss = tf.square(error) / 2
        linear_loss = threshold * tf.abs(error) - threshold ** 2 / 2
        return tf.where(is_small_error, squared_loss, linear_loss)
    return huber_fn
# model.compile(loss=create_huber(2.0), ...)   → 로드할 때 custom_objects={"huber_fn": create_huber(2.0)} 기억해서 다시 줘야 함

class HuberLoss(keras.losses.Loss):                  # 3단계: 클래스 (꼭 만들 함수 3개)
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
# model.compile(loss=HuberLoss(2.), ...)  →  load_model(..., custom_objects={"HuberLoss": HuberLoss})
print(huber_fn(tf.constant([0., 0.]), tf.constant([0.5, 3.])), HuberLoss(2.)(tf.constant([0.]), tf.constant([3.])))""",
html="""<ul>
<li><b>후버</b>: MSE는 오차가 크면 값이 폭주 → 오차가 1보다 작으면 2차, 크면 1차(직선)</li>
<li><b>if 대신 tf.where</b> (교수님 질문) → 속도. 분기(점프) 없이 순서대로 흐름. 두 값을 다 계산해도 병렬(GPU)이라 빠름</li>
<li><code>loss=huber_fn</code>은 함수 <b>이름</b>을 넘김, <code>loss=create_huber(2.0)</code>은 함수를 <b>호출</b>해서 threshold가 박힌 새 함수를 받음 (C의 함수 포인터 비유)</li>
<li><b>2단계의 문제점</b>: threshold 값이 모델에 저장 안 됨 → 몇으로 했는지 잊거나 친구에게 안 알려 주면 못 씀</li>
<li><b>3단계 해결</b>: 클래스로. <b>__init__</b>(값 저장), <b>call</b>(손실 계산할 때마다 호출), <b>get_config</b>(save할 때 호출 → threshold도 파일에 저장). 로드 땐 클래스 이름만 알려 주면 됨</li>
<li>저장 파일엔 함수 이름(문자열)만 들어 있음 → 우리가 만든 건 <b>custom_objects</b>로 실제 함수/클래스를 알려 줘야 함 (내장 층은 케라스가 알아서)</li>
</ul>""")

    _a("lecture", "★★★ 정밀도와 스트리밍 지표: 평균 40%가 왜 틀렸나 (10/10)", "precision 정밀도 스트리밍 지표 streaming metric 누적 reset_states result 정확도 재현율 40% 50%",
"""precision = keras.metrics.Precision()
print(float(precision([0, 1, 1, 1, 0, 1, 0, 1], [1, 1, 0, 1, 0, 1, 0, 1])))   # 0.8  (양성 예측 5개 중 4개)
print(float(precision([0, 1, 0, 0, 1, 0, 1, 1], [1, 0, 1, 1, 0, 0, 0, 0])))   # 0.5  (누적: 8개 중 4개)
print(float(precision.result()))
precision.reset_state()          # 에폭이 끝나면 초기화 (교수님 버전: reset_states)
print(float(precision.result()))     # 0.0""",
html="""<ul>
<li>"정밀도를 물어봤는데 정밀도라고 답하면 어떡합니까" → <b>개념으로</b> 답할 것</li>
<li><b>정밀도</b> = 모델이 양성이라고 한 것 중 실제 양성의 비율 TP/(TP+FP). 암이라고 불러낸 사람 중 진짜 암 환자 비율. 못 잡아낸 건 관심 없음(그건 재현율)</li>
<li><b>정확도</b> = 전체 예측 중 맞춘 비율</li>
<li>배치1 80%, 배치2 0% → <b>평균 40%는 틀림</b>. 전체로 보면 양성 예측 8개 중 4개 = <b>50%</b></li>
<li>그래서 앞 배치까지 TP·FP를 <b>누적</b>하는 <b>스트리밍 지표</b> ("계속 흘러가는데 계속 반영"). result()로 현재 값, 에폭마다 reset</li>
<li>loss와 metric: 함수 모양은 비슷하지만 loss는 그래디언트를 만들어 학습에, metric은 사람이 보려고. 실습: metrics를 MAE → MSE로 바꿔도 숫자만 다르게 나옴</li>
</ul>""")

    _a("lecture", "★★★ * 와 ** : 돌리기 전에 추측해 봐 (10/10)", "*args **kwargs 별표 언패킹 가변 인자 키워드 super().__init__(**kwargs) 딕셔너리 튜플",
"""def f(*args):                 # 위치 인자 여러 개 → 튜플
    for a in args: print(a)
f(1, 2, 3)

def g(**kwargs):              # 이름=값 인자 여러 개 → 딕셔너리
    for k, v in kwargs.items(): print(k, v)
g(이름="김철수", 학번=2021)

def h(x): return x
try: h(1, 2)                  # 별표가 없으면 하나만 받음
except TypeError as e: print("TypeError:", e)""",
html="""<ul>
<li><b>*</b>: 여러 값을 한 변수(튜플)로 받아 반복문으로 하나씩 쓸 수 있음. 별표 없이 여러 개를 주면 TypeError</li>
<li><b>**</b>: <code>이름=값</code> 인자들을 key-value <b>딕셔너리</b>로 받음, .items()로 꺼냄</li>
<li>용도: 클래스를 만들 때 어떤 파라미터가 올지 모르지만 이름으로 맞춰야 할 때 → <code>super().__init__(**kwargs)</code>로 받은 걸 그대로 부모에게 넘김. get_config의 <code>{**base_config, ...}</code>도 딕셔너리 펼치기</li>
</ul>""")

    _a("lecture", "★★★ 사용자 정의 층: __init__ · build · call · get_config 는 언제 불리나 (10/10)", "사용자 정의 층 custom layer MyDense build call get_config add_weight kernel Lambda 언제 호출 순전파",
"""class MyDense(keras.layers.Layer):
    def __init__(self, units, activation=None, **kwargs):     # 처음 만들 때: 설정 저장
        super().__init__(**kwargs)
        self.units = units
        self.activation = keras.activations.get(activation)
    def build(self, batch_input_shape):                       # 처음 쓰일 때: 가중치 만들기
        self.kernel = self.add_weight(name="kernel", shape=[batch_input_shape[-1], self.units],
                                      initializer="glorot_normal")
        self.bias = self.add_weight(name="bias", shape=[self.units], initializer="zeros")
        super().build(batch_input_shape)
    def call(self, X):                                        # 순전파 할 때마다
        return self.activation(X @ self.kernel + self.bias)
    def get_config(self):                                     # save 할 때
        base_config = super().get_config()
        return {**base_config, "units": self.units,
                "activation": keras.activations.serialize(self.activation)}

exponential_layer = keras.layers.Lambda(lambda x: tf.exp(x))   # 가중치 없는 층은 Lambda로
print(MyDense(3, activation="relu")(tf.ones((2, 4))).shape, exponential_layer(tf.constant([0., 1.])))""",
html="""<ul>
<li>질문 "층의 call은 언제 쓰일까?" → <b>순전파(피드포워드)</b> 할 때. "가중치 곱하고 합하고 활성화"</li>
<li><b>build</b>: 처음 쓰일 때 입력 크기를 보고 가중치(kernel = 가중치, bias)를 만듦</li>
<li><b>get_config</b>: save 할 때 → 로드할 땐 custom_objects로 클래스 이름을 알려 줌</li>
<li>사용자 정의 손실·층·모델 공통: 기본 3~4개 함수(__init__, call, get_config, 층이면 build)</li>
<li>학습할 파라미터가 없는 층은 <b>Lambda</b>로 충분</li>
</ul>""")

    _a("lecture", "★★★ 훈련 때만 노이즈: training 인자 · 잔차 블록 (10/10)", "gaussian noise 노이즈 training 인자 훈련 추론 규제 robust residual 잔차 블록 skip connection inputs + Z",
"""class MyGaussianNoise(keras.layers.Layer):
    def __init__(self, stddev, **kwargs):
        super().__init__(**kwargs)
        self.stddev = stddev
    def call(self, X, training=None):
        if training:                                    # fit 할 때만 노이즈
            return X + tf.random.normal(tf.shape(X), stddev=self.stddev)
        return X                                        # predict 할 때는 그대로

class ResidualBlock(keras.layers.Layer):
    def __init__(self, n_layers, n_neurons, **kwargs):
        super().__init__(**kwargs)
        self.hidden = [keras.layers.Dense(n_neurons, activation="relu") for _ in range(n_layers)]
    def call(self, inputs):
        Z = inputs
        for layer in self.hidden:
            Z = layer(Z)
        return inputs + Z                               # 원래 입력을 더함 (건너뛰는 연결)

x = tf.ones((1, 3))
print(MyGaussianNoise(1.0)(x, training=False), ResidualBlock(2, 3)(x).shape)""",
html="""<ul>
<li>"노이즈를 왜 넣을까?" → 열악한 상황에서 훈련하면 <b>강건(robust)</b>해짐, 일종의 규제</li>
<li>"그걸 자동화하는 방법?" → <code>call(self, X, training=None)</code>. 훈련 땐 노이즈, 쓸 땐 안 넣는 게 더 좋은 결과</li>
<li><b>잔차 블록</b>: 층을 거치는 경로 + 거치지 않는 경로를 합침(<code>inputs + Z</code>). 하나의 층처럼 만들어 두면 네트워크에 딱딱 끼워 넣기 쉬움. "실제로 이걸 자주 쓰거든요"</li>
</ul>""")

    # ------------------------------------------------------------------ 미분 · 훈련 반복 (10/10)
    _a("lecture", "★★★ 편미분과 GradientTape 주의사항 (10/10)", "gradienttape 그래디언트 테이프 편미분 수치 미분 36 10 42 tf.Variable None watch 주의사항",
"""def f(w1, w2):
    return 3 * w1 ** 2 + 2 * w1 * w2

w1, w2 = 5., 3.
eps = 1e-6
print((f(w1 + eps, w2) - f(w1, w2)) / eps, (f(w1, w2 + eps) - f(w1, w2)) / eps)   # 수치 미분 ≈ 36, 10

w1, w2 = tf.Variable(5.), tf.Variable(3.)
with tf.GradientTape() as tape:
    z = f(w1, w2)
print(tape.gradient(z, [w1, w2]))          # [36, 10]  ← with 블록 밖에서 호출

c1, c2 = tf.constant(5.), tf.constant(3.)
with tf.GradientTape() as tape:
    z = f(c1, c2)
print(tape.gradient(z, [c1, c2]))          # [None, None]  상수는 추적 안 함

with tf.GradientTape() as tape:
    tape.watch(c1); tape.watch(c2)         # 상수를 잠시 변수처럼 추적
    z = f(c1, c2)
print(tape.gradient(z, [c1, c2]))          # [36, 10]""",
html="""<ul>
<li>미분 = 그 지점의 기울기. 수치 미분 (f(x+0.001)−f(x))/0.001 ≈ 42.003 → 작게 할수록 정밀</li>
<li><b>편미분</b>: 보고자 하는 변수 하나로만 미분, 나머지는 상수 취급. ∂f/∂w1 = 6w1+2w2 = <b>36</b>, ∂f/∂w2 = 2w1 = <b>10</b></li>
<li>변수 하나면 '기울기', 여러 개면 <b>그래디언트</b>(경사)</li>
<li><b>"주의사항" 두 번 강조</b>: 미분할 값은 <b>tf.Variable</b>이어야 함. 상수면 <b>None</b>. 변수로 안 만들려면 <b>tape.watch</b></li>
<li>GradientTape = 역전파에서 체인 룰로 했던 미분을 자동으로 해 줌</li>
</ul>""")

    _a("lecture", "★★★ 사용자 정의 훈련 반복: fit 안에서 일어나는 일 (10/10)", "custom training loop 사용자 정의 훈련 반복 fit 내부 apply_gradients trainable_variables random_batch epoch step mean_loss",
"""(Xc, yc) = (np.random.rand(1000, 8).astype("float32"), np.random.rand(1000, 1).astype("float32"))
model = keras.Sequential([keras.layers.Input(shape=(8,)), keras.layers.Dense(30, activation="relu"),
                          keras.layers.Dense(1)])
def random_batch(X, y, batch_size=32):
    idx = np.random.randint(len(X), size=batch_size)
    return X[idx], y[idx]

n_epochs, batch_size = 2, 32
n_steps = len(Xc) // batch_size
optimizer = keras.optimizers.Nadam(learning_rate=0.01)
loss_fn = keras.losses.MeanSquaredError()
mean_loss = keras.metrics.Mean()
metrics = [keras.metrics.MeanAbsoluteError()]

for epoch in range(1, n_epochs + 1):                     # 에폭: 전체를 한 번 도는 것
    for step in range(1, n_steps + 1):                   # 스텝: 배치 하나
        X_batch, y_batch = random_batch(Xc, yc)
        with tf.GradientTape() as tape:
            y_pred = model(X_batch, training=True)       # 1. 순전파(예측)
            main_loss = tf.reduce_mean(loss_fn(y_batch, y_pred))   # 2. 손실
            loss = tf.add_n([main_loss] + model.losses)  #    + 규제 손실
        gradients = tape.gradient(loss, model.trainable_variables)          # 3. 미분(역전파)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))   # 4. 가중치 수정
        mean_loss(loss)                                  # 5. 여기부턴 출력용
        for m in metrics: m(y_batch, y_pred)
    print(epoch, float(mean_loss.result()), [float(m.result()) for m in metrics])
    for m in [mean_loss] + metrics: m.reset_state()      # 에폭마다 지표 초기화""",
html="""<ul>
<li>"compile하고 fit했던 거, 말로만 들었던 순전파·역전파를 직접 프로그램" → 이해하면 "이렇게 돌아가는구나"</li>
<li>앞 예제의 z = 최종 <b>loss</b>, w1·w2 = <b>model.trainable_variables</b></li>
<li><b>apply_gradients</b> = 가중치 조정. 옵티마이저 종류(Adam, RMSProp…)에 따라 계산이 달라짐 → 실습에서 옵티마이저도 바꿔 보라고 함</li>
<li>mean_loss·metrics는 학습과 무관, 현재 상태 출력용</li>
<li>"에폭은 뭐야?" → 전체 데이터를 한 번 다 도는 것. 배치는 그 안의 묶음(32)</li>
</ul>""")

    _a("lecture", "★★★ tf.function과 데코레이터 (10/10, 속도 15배)", "tf.function 데코레이터 decorator @ 골뱅이 그래프 속도 wrapper 래퍼 함수를 만드는 함수",
"""def cube(x):
    return x ** 3
tf_cube = tf.function(cube)          # 함수를 넣으면 그래프 함수로 바뀜
print(tf_cube(tf.constant(2.0)))

@tf.function                          # 매번 tf.function(...) 할 필요 없이 정의할 때 한 번에
def tf_cube2(x):
    return x ** 3
print(tf_cube2(tf.constant(3.0)))

def my_decorator(func):               # 데코레이터 = 함수를 받아 감싼 새 함수를 돌려주는 함수
    def wrapper(*args, **kwargs):
        print("before"); r = func(*args, **kwargs); print("after"); return r
    return wrapper
@my_decorator
def hello(): print("hello")
hello()""",
html="""<ul>
<li>짠 순서대로 계산하는 게 최적이 아닐 수 있음 → TF가 계산에 최적화된 <b>그래프</b>로 바꿈. 일반 함수 약 33ms → 약 2ms, "15배 이상"</li>
<li>조건: 변수가 모두 <b>텐서</b>여야 이득. 넘파이 등은 혜택 없음</li>
<li>매번 tf.function을 불러 바꾸는 걸 잊으면 느려짐 → 정의 앞에 <b>@tf.function</b></li>
<li>"데코레이터 알아?" → 함수를 받아 앞뒤에 다른 일을 덧붙인 새 함수(wrapper)를 돌려주는 함수. "함수를 만드는 함수, 아까(create_huber) 가능하다고 했잖아"</li>
</ul>""")

    # ------------------------------------------------------------------ CNN (10/17)
    _a("lecture", "★★★ 합성곱 = 필터로 엣지 찾기 · 용어 (10/17)", "합성곱 convolution 필터 커널 디텍터 kernel detector 특성 맵 feature map 소벨 sobel 엣지 누끼 수용장 hubel wiesel",
"""import numpy as np
img = np.zeros((5, 6)); img[:, 3:] = 1.          # 왼쪽 어둡고 오른쪽 밝은 그림 (세로 경계)
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
out = np.array([[np.sum(img[i:i+3, j:j+3] * sobel_x) for j in range(4)] for i in range(3)])
print(out)     # 고른 곳은 0, 경계에 걸친 곳만 큰 값""",
html="""<ul>
<li>"포토샵에서 누끼(엣지) 어떻게 따나?" → 이웃 픽셀 사이 <b>밝기 차이</b>를 필터로 계산. 블러·샤픈도 다 합성곱 필터</li>
<li><b>합성곱</b>: 필터를 이미지에 얹고 원소끼리 곱해 모두 더함 → 한 칸 옮겨 반복. 필터와 비슷한 무늬면 큰 값</li>
<li>용어: <b>필터 = 커널 = 디텍터</b> (같은 말), 결과 = <b>특성 맵(feature map)</b>. 커널 여러 개 → 특성 맵 여러 장</li>
<li>"소벨 필터를 적용하면 왜 경계만?" → 고른 영역은 곱의 합이 0으로 상쇄, 경계는 양쪽 값이 달라 큰 값. 엣지는 '선'이 아니라 면과 면이 만나는 경계</li>
<li>X(수직) 필터 → 좌우로 바뀌는 세로 경계, Y(수평) 필터 → 위아래로 바뀌는 가로 경계</li>
<li>고양이 실험(Hubel & Wiesel): 시야의 일부, 특정 각도의 선에만 반응하는 뉴런 = <b>국부 수용장</b> → 이미지는 2차원 구조를 그대로 봐야 함</li>
</ul>""")

    _a("lecture", "★★★ 필터는 사람이 아니라 학습이 정함 · 직접 만든 필터 (10/17 실습)", "필터 직접 만들기 tf.nn.conv2d filters shape 7 7 3 2 수직선 수평선 Conv2D 학습 가중치 load_sample_image",
"""from sklearn.datasets import load_sample_image
images = np.array([load_sample_image("china.jpg"), load_sample_image("flower.jpg")]) / 255.
print(images.shape)                       # (2, 427, 640, 3)  3 = RGB
filters = np.zeros((7, 7, 3, 2), dtype=np.float32)   # (높이, 너비, 입력 채널, 필터 개수)
filters[:, 3, :, 0] = 1                   # 가운데 세로줄 → 수직선 필터
filters[3, :, :, 1] = 1                   # 가운데 가로줄 → 수평선 필터
outputs = tf.nn.conv2d(images.astype(np.float32), filters, strides=1, padding="SAME")
print(outputs.shape)                      # (2, 427, 640, 2)

conv = keras.layers.Conv2D(filters=32, kernel_size=3, strides=1, padding="same", activation="relu")
print(conv(images.astype(np.float32)).shape)   # 랜덤 필터 → "아무것도 아니네" → 학습으로 바뀜""",
html="""<ul>
<li><code>images[1, :, :, 0]</code> = 두 번째 사진의 R 채널. 사진 = R, G, B 평면 3장이 겹친 것</li>
<li>교수님이 만든 필터: 0행에 1, 6행에 −1 → "어떤 엣지를 잡을까?" → <b>가로(수평) 엣지</b>(위아래 밝기 차이). 열 방향이면 세로 엣지</li>
<li><b>강조</b>: "컨볼루션은 엣지 디텍션 용도로 쓰는 게 아니야" → 필터 값은 <b>가중치</b>. 랜덤으로 시작해서 역전파로 계속 바꿔 가며 학습</li>
<li>층 변수는 함수처럼 동작: 이미지를 넣으면 결과가 나옴</li>
</ul>""")

    _a("lecture", "★★★ 패딩 · 스트라이드 · 풀링 (10/17)", "padding same valid 패딩 제로 패딩 stride 스트라이드 pooling 풀링 max average MaxPool2D AvgPool2D 파라미터 0 다운샘플링",
"""x = tf.random.normal((1, 28, 28, 1))
print(keras.layers.Conv2D(8, 3, padding="valid")(x).shape)          # (1, 26, 26, 8) 가장자리 1칸씩 줄어듦
print(keras.layers.Conv2D(8, 3, padding="same")(x).shape)           # (1, 28, 28, 8) 같게
print(keras.layers.Conv2D(8, 3, strides=2, padding="same")(x).shape)  # (1, 14, 14, 8) 두 칸씩 → 반
pool = keras.layers.MaxPool2D(pool_size=2)
print(pool(x).shape, pool.count_params())                           # (1, 14, 14, 1) 0
print(keras.layers.MaxPool2D(pool_size=(2, 3))(x).shape)            # 가로·세로 다르게: 튜플""",
html="""<ul>
<li><b>패딩</b>: 3×3 필터를 그냥 적용하면 가장자리가 한 칸씩 줄어듦 → 바깥에 0을 채움(제로 패딩, 3×3이면 1칸, 5×5면 2칸)</li>
<li>외우는 법: <b>same = 해상도 같게</b>, <b>valid = 패딩 없음(조금이라도 줄어듦)</b></li>
<li><b>스트라이드</b>: 필터를 몇 칸씩 옮기나. 2면 해상도가 확 줄어듦 → 차원 축소에 씀</li>
<li><b>풀링</b>: 데이터 양을 줄임. 2×2, 스트라이드 2 → 가로·세로 반, 전체 1/4</li>
<li>"max와 average 중 어느 게 나을까?" → 해 보니 <b>max</b>가 더 잘 맞음. "어느 게 빠를까?" → max (가장 큰 값만, average는 더하고 나눠야)</li>
<li>"풀링에 파라미터 있다고 했죠? 없다고 했죠?" → <b>없음(0)</b>. "그냥 칸만 있는 거야" (반복)</li>
</ul>""")

    _a("lecture", "★★★ CNN 파라미터: 320 · 18,496 · 이미지 크기와 무관 (10/17)", "cnn 파라미터 개수 320 18496 421642 이미지 크기 무관 필터 개수 입력 채널 conv1 conv2 왜 32",
"""model = keras.Sequential([
    keras.layers.Input(shape=(28, 28, 1)),                 # 1 = 흑백
    keras.layers.Conv2D(32, 3, padding="same", activation="relu"),
    keras.layers.MaxPool2D(2),
    keras.layers.Conv2D(64, 3, padding="same", activation="relu"),
    keras.layers.MaxPool2D(2),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(10, activation="softmax")])
print([l.count_params() for l in model.layers], model.count_params())
# [320, 0, 18496, 0, 0, 401536, 0, 1290] 421642
for size in [28, 280]:
    m = keras.Sequential([keras.layers.Input(shape=(size, size, 1)), keras.layers.Conv2D(32, 3)])
    print(size, m.count_params())                           # 둘 다 320""",
html="""<ul>
<li><b>공식</b>: (필터 높이 × 너비 × 입력 채널 + 1) × 필터 개수</li>
<li>"왜 320?" → (3×3×1 + 1) × 32. 컬러면 3×3×3</li>
<li>"conv2는 왜 32를 곱해?" → 앞 층 필터 32개 = 특성 맵 32장 = 입력 채널 32 → (3×3×32 + 1) × 64 = <b>18,496</b></li>
<li>Dense(128): 7×7×64 = 3,136 입력 → 3,136×128+128 = 401,536. 합계 <b>421,642</b></li>
<li>"이미지가 커져도 가중치가 늘었나 줄었나? 왜?" → <b>안 늘어남</b>. 식에 이미지 크기가 없음, 같은 필터를 이미지 전체에 재사용</li>
<li>3×3 필터는 784개 전체가 아니라 9개에만 연결: 필터 16개 = 9×16+16 = 160 vs 같은 뉴런 16개 Dense = 784×16+16 = 12,560</li>
<li>28×28 흑백에선 오히려 MLP보다 많을 수 있음 → 중요한 건 1024×768 같은 큰 컬러 사진. 필터 32개는 병렬 계산 → GPU</li>
</ul>""")

    _a("lecture", "★★★ CNN 구조 · 3×3을 연속으로 쌓는 이유 · ImageNet · 비전 과제 4단계 (10/17)", "cnn 구조 lenet alexnet vgg resnet googlenet xception 3x3 연속 수용장 imagenet 사전학습 분류 위치 검출 분할 자율주행",
html="""<ul>
<li>전형적인 구조: 합성곱 → 풀링 → 합성곱 → 풀링 … → 펼쳐서 작은 Dense로 분류 (28→14→7)</li>
<li>다채널 입력: 필터 하나가 모든 채널을 관통해 계산 → 특성 맵 1장</li>
<li><b>3×3 conv를 연속으로 쌓는 이유</b> (학생 "넓게 본다"에 박수): ① 3×3 두 번 = 5×5, 세 번 = 7×7을 보는 효과 ② 비선형을 여러 번 ③ 파라미터가 적음(3×3×3 = 27 vs 7×7 = 49)</li>
<li>LeNet-5(르쿤): 32×32 입력, 5×5 conv 6개 → 풀링 → 16개 → 풀링 → FC</li>
<li>VGG 약 1억 3,800만 vs ResNet 약 6,000만 파라미터 → 구조에 따라 절반 이하로도 비슷한 성능. ResNet = 잔차(건너뛰기) 연결 ("잔차 블록 만든 거 기억나죠?")</li>
<li>"ImageNet 대회는 왜 없어졌나?" → 정확도가 <b>사람보다 높아져서</b>. 훈련된 가중치를 공개 → 불러와서 쓰면 됨(전이 학습)</li>
<li><b>비전 과제 4단계</b>: 분류(한 장 → 하나) → 분류+위치(바운딩 박스) → 객체 검출(여러 물체와 위치) → 인스턴스 분할(픽셀 영역)</li>
<li>"분류만으로 자율주행 될까?" → <b>안 됨</b>. 출력이 하나뿐. 차·사람·신호·차선과 위치가 필요 → 최소 검출, 실제로는 분할까지. 위치 라벨(x, y, w, h) 필요</li>
</ul>""")

    _a("lecture", "날짜별 수업 요약", "날짜 수업 요약 주차 9/12 9/19 10/3 10/10 10/17 진도",
html="""<table>
<tr><th>날짜</th><th>내용</th><th>노트북</th></tr>
<tr><td>9/12</td><td>뉴런·퍼셉트론·XOR·AI 겨울, 활성화 함수, 오차 제곱 이유, Fashion MNIST MLP, validation, compile 3요소, 파라미터 235,500, ReLU vs softmax 퀴즈, 함수형 API(다중 입력), 하이퍼파라미터·Playground, 저장, 콜백. 과제: 마크다운으로 설명 정리</td><td>2장</td></tr>
<tr><td>9/19</td><td>sparse vs categorical, 원-핫, Flatten, 콜백 복습, MNIST: 뉴런 수식·편향·sigmoid→ReLU·파라미터 13,002·cost·경사하강·역전파(자기 말로 설명)·softmax. 과제: 데이터 증강. 시험 규칙 문답</td><td>2·3장</td></tr>
<tr><td>9/26 줌 보강</td><td>순전파·역전파·체인 룰 복습(softmax+교차 엔트로피 미분 = 예측 − 정답), 기울기 소실·폭주, 훈련 비용, 과적합 → 초기화(Glorot·He·LeCun), 활성화(ReLU·Leaky·ELU·SELU), 배치 정규화(입력층 퀴즈), 전이 학습(Watson), 오토인코더, 옵티마이저(SGD→모멘텀→Nesterov→AdaGrad→RMSProp→Adam→Nadam), 학습률, 드롭아웃. 실습: 옵티마이저 실험 각자</td><td>4장 · Optimizer</td></tr>
<tr><td>10/3 보강</td><td>TF 개요, 텐서·dtype 32비트, 자동 형변환 없음(속도, 보너스 문제), 슬라이싱, Variable·assign, 문자열, 래그드·희소(s6 에러), 후버(tf.where)·create_huber·HuberLoss·get_config, loss vs metrics</td><td>5장</td></tr>
<tr><td>10/10</td><td>후버 3단계 실습, custom_objects, 정밀도·스트리밍 지표(40% vs 50%), *·**, Lambda·MyDense·MyGaussianNoise·ResidualBlock, 편미분·GradientTape(주의사항), 사용자 정의 훈련 반복, tf.function·데코레이터. 과제: 에러 고치고 원인 쓰기</td><td>5·6장</td></tr>
<tr><td>10/17</td><td>CNN: 누끼·엣지·소벨, 수용장, 필터·특성 맵, 파라미터(이미지 크기 무관), 패딩·스트라이드·풀링, 직접 만든 필터, Conv2D는 학습, 320·18,496, 3×3 연속, ImageNet, 비전 과제 4단계. "시험은 쓰는 게 어렵다"</td><td>7장</td></tr>
</table>""")
