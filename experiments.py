# 실험 결과(results.json) → "바꾸면 이렇게 된다" 표.
# 기준: Fashion MNIST, Flatten → Dense(300, relu) → Dense(100, relu) → Dense(10, softmax),
#       SGD(learning_rate=0.01), batch_size=32, epochs=10, 기본 초기화(Glorot), seed 42
import json, os

BASE_DESC = ("기준 모델: Fashion MNIST · 300-100 ReLU · SGD(lr 0.01) · batch 32 · 10 epoch · 기본 초기화. "
             "한 번에 하나만 바꿔서 실행 (CPU, seed 42). 정확도는 같은 설정이라도 실행마다 ±0.5%p 정도 달라질 수 있음.")

# 그룹: (키, 제목, 검색 키워드, [(실험키, 바꾼 것, 코드)], 해석 HTML)
GROUPS = [
 ("epochs", "epochs를 바꾸면", "epoch 에포크 에폭 반복 횟수 epochs",
  [("epochs5", "epochs=5", "model.fit(..., epochs=5)"), ("base", "epochs=10 (기준)", ""), ("epochs20", "epochs=20", "model.fit(..., epochs=20)")],
  ""),
 ("bs", "batch_size를 바꾸면", "batch 배치 batch_size 배치크기 미니배치",
  [("base", "batch_size=32 (기준)", ""), ("bs128", "batch_size=128", "model.fit(..., batch_size=128)"), ("bs1024", "batch_size=1024", "model.fit(..., batch_size=1024)")],
  ""),
 ("lr", "학습률을 바꾸면", "learning rate 학습률 lr 발산 nan",
  [("lr0.001", "learning_rate=0.001", "keras.optimizers.SGD(learning_rate=0.001)"), ("base", "learning_rate=0.01 (기준)", ""), ("lr0.1", "learning_rate=0.1", "keras.optimizers.SGD(learning_rate=0.1)"), ("lr1.0", "learning_rate=1.0", "keras.optimizers.SGD(learning_rate=1.0)")],
  ""),
 ("units", "은닉층 크기를 바꾸면", "뉴런 수 은닉층 크기 units hidden 노드 개수",
  [("units30_10", "Dense(30) · Dense(10)", "Dense(30, ...), Dense(10, ...)"), ("base", "Dense(300) · Dense(100) (기준)", ""), ("units1000_500", "Dense(1000) · Dense(500)", "Dense(1000, ...), Dense(500, ...)")],
  ""),
 ("act", "활성화 함수를 바꾸면", "activation 활성화 sigmoid tanh relu elu selu leaky",
  [("base", "relu (기준)", ""), ("sigmoid", "sigmoid", "activation=\"sigmoid\""), ("tanh", "tanh", "activation=\"tanh\""), ("elu", "elu", "activation=\"elu\""),
   ("selu", "selu + lecun_normal", "activation=\"selu\", kernel_initializer=\"lecun_normal\""), ("leaky", "LeakyReLU(0.2)", "Dense(300), keras.layers.LeakyReLU(0.2)"),
   ("sigmoid_sgd_vs", "sigmoid + Adam", "activation=\"sigmoid\"  +  optimizer=\"adam\"")],
  ""),
 ("init", "초기화를 바꾸면", "initializer 초기화 he glorot random 정규분포",
  [("base", "glorot_uniform (기본값, 기준)", ""), ("he", "he_normal", "kernel_initializer=\"he_normal\""), ("bigrandom", "RandomNormal(stddev=1.0)", "kernel_initializer=keras.initializers.RandomNormal(stddev=1.0)")],
  ""),
 ("bn", "배치 정규화를 넣으면", "batch normalization 배치정규화 BN",
  [("base", "없음 (기준)", ""), ("bn", "각 Dense 뒤에 BatchNormalization()", "keras.layers.BatchNormalization()")],
  ""),
 ("drop", "드롭아웃 · L2 규제를 넣으면", "dropout 드롭아웃 l2 규제 과대적합",
  [("base", "없음 (기준)", ""), ("drop0.2", "Dropout(0.2)", "keras.layers.Dropout(0.2)"), ("drop0.5", "Dropout(0.5)", "keras.layers.Dropout(0.5)"), ("l2", "L2(0.01)", "kernel_regularizer=keras.regularizers.l2(0.01)")],
  ""),
 ("opt", "옵티마이저를 바꾸면", "optimizer 옵티마이저 sgd momentum nag adam rmsprop adagrad nadam",
  [("base", "SGD lr 0.01 (기준)", ""), ("momentum", "SGD + momentum 0.9", "SGD(learning_rate=0.01, momentum=0.9)"), ("nag", "NAG", "SGD(learning_rate=0.01, momentum=0.9, nesterov=True)"),
   ("adagrad", "Adagrad lr 0.01", "Adagrad(learning_rate=0.01)"), ("rmsprop", "RMSprop lr 0.001", "RMSprop(learning_rate=0.001)"), ("adam", "Adam lr 0.001", "Adam(learning_rate=0.001)"), ("nadam", "Nadam lr 0.001", "Nadam(learning_rate=0.001)")],
  ""),
 ("nonorm", "255로 나누지 않으면", "정규화 normalize 255 스케일 전처리 나누기",
  [("base", "/ 255. (기준)", ""), ("nonorm", "나누지 않음 (0~255 그대로)", "X_train = X_train_full[5000:]  # /255 없음")],
  ""),
]

def load(path):
    return json.load(open(path)) if os.path.exists(path) else {}

def table(rows, R):
    h = ('<div style="overflow-x:auto"><table><tr><th>바꾼 것</th><th>테스트 정확도</th><th>훈련 정확도</th>'
         '<th>검증 정확도</th><th>훈련−검증</th><th>마지막 loss</th><th>시간</th></tr>')
    for key, label, _ in rows:
        r = R.get(key)
        if not r:
            h += f'<tr><td>{label}</td><td colspan="6">실험 중</td></tr>'; continue
        H = r["hist"]; tr, va = H["accuracy"][-1], H["val_accuracy"][-1]; lo = H["loss"][-1]
        lo_s = "nan (발산)" if lo != lo else f"{lo:.3f}"
        cls = ' class="base"' if key in ("base", "cnn_base") else ""
        h += (f'<tr{cls}><td>{label}</td><td class="n">{r["test_acc"]:.3f}</td><td class="n">{tr:.3f}</td>'
              f'<td class="n">{va:.3f}</td><td class="n">{tr-va:+.3f}</td><td class="n">{lo_s}</td><td class="n">{r["time"]:.0f}초</td></tr>')
    return h + '</table></div>'

def group_html(gkey, R):
    for k, title, kw, rows, expl in GROUPS:
        if k == gkey:
            expl = EXPL.get(k, expl)
            return f'<h3>실험: {title}</h3>' + table(rows, R) + (f'<div>{expl}</div>' if expl else '')
    return ""

def items(R):
    out = []
    for k, title, kw, rows, expl in GROUPS:
        code = "\n".join(f"# {lab}\n{c}" for _, lab, c in rows if c)
        expl = EXPL.get(k, expl)
        html = table(rows, R) + (f'<div style="margin-top:8px">{expl}</div>' if expl else '')
        out.append(dict(sec="change", title=title, kw=kw + " 바꾸면 비교 실험 결과", code=code, note=BASE_DESC, html=html, out="", extra=""))
    return out


EXPL = {
 "epochs": "<ul><li>epoch를 늘리면 정확도가 오르지만 오르는 폭은 점점 줄어듦 (5→10: +2.3%p, 10→20: +1.0%p)</li><li>훈련−검증 차이가 −0.006 → +0.004 → +0.017로 커짐 → 오래 할수록 훈련 데이터에 맞춰지기 시작(과대적합 신호)</li><li>시간은 epoch에 비례 (25초 → 51초 → 106초)</li><li><b>답안 한 줄</b>: epoch를 늘리면 더 학습되어 정확도가 오르지만, 일정 이상에서는 개선이 작아지고 과대적합 위험이 커진다. 조기 종료로 적당한 지점에서 멈추는 것이 좋다.</li></ul>",
 "bs": "<ul><li>batch를 키우면 한 epoch 동안 가중치를 고치는 횟수가 줄어듦 (32 → 1,719번, 128 → 430번, 1024 → 54번)</li><li>그래서 같은 10 epoch에서는 덜 학습되어 정확도가 떨어짐 (0.867 → 0.840 → 0.770)</li><li>대신 한 번에 많이 처리해서 빠름 (51초 → 23초 → 10초)</li><li><b>답안 한 줄</b>: 배치 크기를 키우면 학습 속도는 빨라지지만 epoch당 업데이트 횟수가 줄어 같은 epoch에서는 정확도가 낮아진다. 큰 배치를 쓰려면 epoch나 학습률을 늘려야 한다.</li></ul>",
 "lr": "<ul><li>0.001: 너무 작아서 10 epoch 안에 덜 내려감 (loss 0.505, 정확도 0.821)</li><li>0.1: 훈련 정확도는 0.915로 가장 높지만 테스트는 0.853으로 기준보다 낮음 → 크게 움직이며 요동, 훈련 데이터에 과하게 맞춤</li><li>1.0: loss가 nan → <b>발산</b>. 정확도 0.10 = 10개 중 아무거나 찍는 수준</li><li><b>답안 한 줄</b>: 학습률이 너무 작으면 학습이 느리고, 너무 크면 최적점을 지나쳐 요동하거나 발산(loss=nan)한다.</li></ul>",
 "units": "<ul><li>30·10: 파라미터 23,970개로 작아서 표현력이 부족 → 0.844</li><li>1000·500: 파라미터 1,290,510개(기준의 약 5배)인데 정확도는 0.866으로 거의 같고 시간은 3배 (147초)</li><li><b>답안 한 줄</b>: 뉴런이 너무 적으면 패턴을 충분히 못 배우고, 많이 늘려도 일정 이상에서는 정확도 개선 없이 계산량과 과대적합 위험만 커진다.</li></ul>",
 "act": "<ul><li>sigmoid가 0.792로 가장 낮음 → 도함수 최대 0.25라 기울기가 작아 SGD로는 학습이 느림 (기울기 소실)</li><li>tanh·ELU·SELU·LeakyReLU는 0.857~0.860, ReLU 0.867로 비슷</li><li><b>sigmoid + Adam = 0.877</b>: 같은 sigmoid라도 Adam이 걸음 크기를 자동으로 키워 주면 따라잡음 → sigmoid의 문제는 \"느리게 배운다\"는 것</li><li><b>답안 한 줄</b>: sigmoid는 기울기가 작아 깊어질수록 학습이 느려지고(기울기 소실), ReLU 계열은 양수에서 기울기가 1이라 빠르게 학습된다.</li></ul>",
 "init": "<ul><li>He(0.863)와 기본 Glorot(0.867)는 거의 같음 → 층이 2개뿐인 얕은 모델이라 초기화 차이가 작음 (깊은 모델일수록 차이가 커짐)</li><li>표준편차 1.0으로 크게 초기화하면 0.721로 크게 떨어짐 → 시작부터 층 출력이 너무 커져 학습이 불안정</li><li><b>답안 한 줄</b>: 초기 가중치가 너무 크거나 작으면 층을 지나며 신호가 커지거나 사라져 학습이 어렵다. He·Glorot 초기화는 층마다 분산을 유지해 이를 막는다.</li></ul>",
 "bn": "<ul><li>정확도 0.867 → 0.875, loss 0.332 → 0.202: 같은 10 epoch에 훨씬 많이 학습됨</li><li>훈련 정확도 0.929로 빠르게 올라 훈련−검증 차이도 커짐 (+0.046)</li><li>파라미터 +1,600개(BN 층의 γ·β·이동평균·이동분산), 시간 약간 증가 (51 → 59초)</li><li><b>답안 한 줄</b>: 배치 정규화는 층마다 출력의 분포를 맞춰 학습을 빠르고 안정적으로 만든다.</li></ul>",
 "drop": "<ul><li>Dropout 0.2: 테스트 0.867로 기준과 같음. <b>훈련 정확도(0.865)가 검증(0.878)보다 낮음</b> → 드롭아웃은 학습 중에만 뉴런을 꺼서, 훈련 정확도는 일부가 꺼진 상태로 계산되기 때문</li><li>Dropout 0.5: 절반을 꺼서 10 epoch로는 덜 학습 (0.854)</li><li>L2(0.01): 0.824. loss가 높은 건 벌점이 더해져서</li><li>이 모델은 원래 훈련−검증 차이가 0.004로 과대적합이 거의 없어서, 규제가 정확도를 올리지 못함. 규제는 과대적합이 생길 때(오래 학습, 큰 모델) 효과가 있음</li><li><b>답안 한 줄</b>: 드롭아웃과 L2는 과대적합을 줄이는 규제로, 과대적합이 없는 상황에서 너무 강하게 쓰면 오히려 덜 학습된다.</li></ul>",
 "opt": "<ul><li>관성·적응형 옵티마이저는 같은 10 epoch에 loss를 더 많이 줄임 (SGD 0.332 → Momentum 0.232, NAG 0.228, Adam 0.218, Nadam 0.212)</li><li>테스트 정확도: Momentum 0.881 · NAG 0.876 · Adam 0.875 · Adagrad 0.874 · Nadam 0.872 · SGD 0.867 · RMSprop 0.855</li><li>RMSprop은 훈련 0.899인데 검증 0.865 → 요동하며 훈련 데이터에 더 맞춤</li><li>Adagrad의 \"너무 일찍 멈춤\"은 오래 학습할 때 나타나는 단점이라 10 epoch에서는 안 보임</li><li><b>답안 한 줄</b>: 모멘텀·Adam 같은 옵티마이저는 SGD보다 빠르게 수렴해 같은 epoch에서 손실이 더 낮다.</li></ul>",
 "nonorm": "<ul><li>255로 나누지 않으면 입력이 0~255로 커서 가중치 합이 지나치게 커짐 → loss가 nan으로 <b>발산</b>, 정확도 0.10</li><li><b>답안 한 줄</b>: 입력 스케일이 크면 학습이 불안정해져 발산할 수 있으므로 0~1로 정규화한다.</li></ul>",
}


# ---------------- CNN 실험 (results_cnn.json)
CNN_DESC = ("기준 CNN: 교수님 7-1 노트북 구조 — Conv2D(32,3×3,same) → MaxPool → Conv2D(64,3×3,same) → MaxPool → Flatten → "
            "Dense(128, relu) → Dropout(0.2) → Dense(10). Fashion MNIST 표준화, Nadam, 5 epoch, CPU, seed 42.")
CNN_GROUPS = [
 ("cnn_vs", "MLP 대신 CNN을 쓰면", "cnn mlp fcn 비교 완전연결 합성곱",
  [("fcn", "MLP (Flatten → Dense 200 → 100)", "keras.layers.Flatten(), Dense(200), Dense(100), Dense(10)"), ("cnn_base", "CNN (교수님 구조, 기준)", "")]),
 ("cnn_act", "합성곱 층에 ReLU를 넣으면", "cnn activation relu 활성화 conv2d",
  [("cnn_base", "Conv2D 활성화 없음 (교수님 코드 그대로, 기준)", ""), ("cnn_relu", "Conv2D(..., activation=\"relu\")", "keras.layers.Conv2D(32, kernel_size=(3, 3), padding=\"same\", activation=\"relu\")")]),
 ("cnn_filters", "필터 수 · 커널 크기를 바꾸면", "filters 필터 개수 kernel_size 커널 크기 conv2d",
  [("cnn_small", "필터 8 · 16", "Conv2D(8, ...), Conv2D(16, ...)"), ("cnn_base", "필터 32 · 64 (기준)", ""), ("cnn_big", "필터 64 · 128", "Conv2D(64, ...), Conv2D(128, ...)"), ("cnn_k5", "kernel_size=5", "Conv2D(32, kernel_size=(5, 5), ...)")]),
 ("cnn_pool", "풀링을 빼거나 스트라이드로 바꾸면", "pooling 풀링 제거 stride 스트라이드 maxpooling",
  [("cnn_base", "MaxPooling2D(2) (기준)", ""), ("cnn_nopool", "풀링 없음", "# MaxPooling2D 줄 삭제"), ("cnn_stride2", "풀링 대신 Conv2D(strides=2)", "Conv2D(32, kernel_size=(3, 3), strides=2, padding=\"same\")")]),
 ("cnn_pad", "패딩을 VALID로 바꾸면", "padding 패딩 valid same",
  [("cnn_base", "padding=\"same\" (기준)", ""), ("cnn_valid", "padding=\"valid\"", "Conv2D(32, kernel_size=(3, 3), padding=\"valid\")")]),
]
CNN_EXPL = {
 "cnn_vs": "<ul><li>CNN 0.900 vs MLP 0.865: 같은 5 epoch에서 CNN이 3.5%p 높음</li><li>MLP는 그림을 784개 한 줄로 펴서 주변 픽셀 관계(위치 정보)를 잃고, CNN은 그림 모양 그대로 필터로 훑어 선·모서리 같은 공간 패턴을 잡음</li><li>대신 CNN은 계산이 많아 느림 (43초 → 137초)</li><li><b>답안 한 줄</b>: CNN은 이미지의 공간 구조를 유지한 채 지역 특징을 추출하므로 이미지 분류에서 MLP보다 정확도가 높다.</li></ul>",
 "cnn_act": "<ul><li>교수님 코드는 Conv2D에 activation이 없음(선형). ReLU를 넣으면 0.900 → 0.911</li><li>활성화가 없으면 합성곱 층은 곱하고 더하기만 하는 선형 계산이라, 층을 쌓아도 복잡한 패턴 표현이 제한됨 (MaxPooling이 약간의 비선형성은 줌)</li><li><b>답안 한 줄</b>: 합성곱 층 뒤에 ReLU 같은 비선형 활성화를 넣어야 층을 쌓는 효과가 커진다.</li></ul>",
 "cnn_filters": "<ul><li>필터 8·16 / 32·64 / 64·128 모두 약 0.90 → 이 데이터에서는 필터 수가 정확도에 큰 영향이 없음</li><li>필터를 줄이면 파라미터 103,018개·72초, 늘리면 878,730개·314초 → <b>계산량과 시간만 크게 달라짐</b></li><li>커널 3×3 → 5×5도 0.901로 거의 같음</li><li><b>답안 한 줄</b>: 필터 수를 늘리면 더 많은 특징을 뽑을 수 있지만 파라미터와 계산량이 늘어나며, 데이터가 단순하면 정확도 향상은 작다.</li></ul>",
 "cnn_pool": "<ul><li>풀링을 빼면 특성맵이 28×28로 그대로 남아 Flatten 뒤 Dense 입력이 50,176개 → 파라미터 <b>6,442,762개(15배)</b>, 시간 688초(5배), 정확도는 0.852로 오히려 하락 (훈련 0.912 / 검증 0.858)</li><li>풀링 대신 strides=2: 크기는 똑같이 줄지만 0.871로 MaxPooling(0.900)보다 낮음</li><li><b>답안 한 줄</b>: 풀링은 특성맵 크기를 줄여 파라미터·계산량을 크게 줄이고, 작은 위치 변화에 둔감하게 만들어 일반화에 도움을 준다.</li></ul>",
 "cnn_pad": "<ul><li>VALID는 가장자리를 채우지 않아 층마다 크기가 줄어듦: 28 → 26 → 풀링 13 → 11 → 풀링 5</li><li>마지막 특성맵 5×5×64 = 1,600 (SAME은 7×7×64 = 3,136) → 파라미터 225,034개로 절반, 정확도 0.894로 약간 낮음</li><li><b>답안 한 줄</b>: VALID 패딩은 출력 크기가 줄어 계산량은 적지만 가장자리 정보가 줄어들고, SAME은 크기를 유지한다.</li></ul>",
}

def _table_params(rows, R):
    h = ('<div style="overflow-x:auto"><table><tr><th>바꾼 것</th><th>테스트 정확도</th><th>훈련 정확도</th>'
         '<th>검증 정확도</th><th>파라미터</th><th>시간</th></tr>')
    for key, label, _ in rows:
        r = R.get(key)
        if not r:
            h += f'<tr><td>{label}</td><td colspan="5">실험 중</td></tr>'; continue
        H = r["hist"]
        cls = ' class="base"' if key == "cnn_base" else ""
        h += (f'<tr{cls}><td>{label}</td><td class="n">{r["test_acc"]:.3f}</td><td class="n">{H["accuracy"][-1]:.3f}</td>'
              f'<td class="n">{H["val_accuracy"][-1]:.3f}</td><td class="n">{r["params"]:,}</td><td class="n">{r["time"]:.0f}초</td></tr>')
    return h + '</table></div>'

_old_group_html = group_html
def group_html(gkey, R):
    for k, title, kw, rows in CNN_GROUPS:
        if k == gkey:
            e = CNN_EXPL.get(k, "")
            return f'<h3>실험: {title}</h3>' + _table_params(rows, R) + (f'<div>{e}</div>' if e else '')
    return _old_group_html(gkey, R)

_old_items = items
def items(R):
    out = _old_items(R)
    for k, title, kw, rows in CNN_GROUPS:
        code = "\n".join(f"# {lab}\n{c}" for _, lab, c in rows if c)
        e = CNN_EXPL.get(k, "")
        out.append(dict(sec="change", title="CNN: " + title, kw=kw + " 바꾸면 비교 실험 결과 cnn", code=code, note=CNN_DESC,
                        html=_table_params(rows, R) + (f'<div style="margin-top:8px">{e}</div>' if e else ''), out="", extra=""))
    return out

def load(path):
    import json as _j, os as _o
    R = _j.load(open(path)) if _o.path.exists(path) else {}
    p2 = _o.path.join(_o.path.dirname(path), "results_cnn.json")
    if _o.path.exists(p2): R.update(_j.load(open(p2)))
    return R
