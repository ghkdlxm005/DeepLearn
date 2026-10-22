# 5·6장(텐서플로 저수준 · 사용자 정의)과 7장(CNN) 예제. 교수님 노트북 코드를 기준으로 정리.
# snippets.py에서 register(add)로 불러온다.

SECTIONS_TF = [
    ("tf", "텐서플로 기초"),
    ("custom", "사용자 정의"),
    ("cnn", "CNN"),
]

def register(add):
    # ---------------- 텐서플로 기초 (5장)
    add("tf", "텐서 만들기 · 모양 · 타입", "tensor 텐서 constant shape dtype numpy 변환 스칼라 행렬",
"""t = tf.constant([[1., 2., 3.], [4., 5., 6.]])   # 2x3 행렬 텐서
print(t.shape)     # (2, 3)
print(t.dtype)     # float32  (넘파이 기본은 float64)
print(t.numpy())   # 넘파이 배열로
s = tf.constant(42)          # 스칼라도 가능
a = np.array([2., 4., 5.])
print(tf.constant(a))        # 넘파이 → 텐서 (float64 유지)""",
"텐서는 넘파이 배열과 비슷하지만 바꿀 수 없음(immutable). 기본 타입이 32비트.")

    add("tf", "텐서 인덱싱 · 슬라이싱", "인덱싱 슬라이싱 newaxis ... ellipsis indexing slicing",
"""t = tf.constant([[1., 2., 3.], [4., 5., 6.]])
print(t[:, 1:])                 # 모든 행, 1열부터 → [[2,3],[5,6]]
print(t[..., 1, tf.newaxis])    # 1열만 뽑고 차원 하나 추가 → shape (2, 1)
print(t[..., 1])                # newaxis 없으면 shape (2,)""",
"... 은 앞쪽 모든 차원, tf.newaxis는 크기 1짜리 차원을 새로 추가.")

    add("tf", "텐서 연산 (넘파이와 비교)", "연산 square transpose matmul 행렬곱 @ reduce_mean reduce_sum 넘파이 비교",
"""t = tf.constant([[1., 2., 3.], [4., 5., 6.]])
print(t + 10)                       # 원소마다 더하기
print(tf.square(t))                 # 원소마다 제곱
print(t @ tf.transpose(t))          # 행렬곱 = tf.matmul(t, tf.transpose(t)) → (2,2)
print(tf.reduce_mean(t), tf.reduce_sum(t), tf.reduce_max(t))""",
html="""<table>
<tr><th>넘파이</th><th>텐서플로</th></tr>
<tr><td><code>np.mean()</code> / <code>np.sum()</code> / <code>np.max()</code></td><td><code>tf.reduce_mean()</code> / <code>tf.reduce_sum()</code> / <code>tf.reduce_max()</code></td></tr>
<tr><td><code>np.log()</code></td><td><code>tf.math.log()</code></td></tr>
<tr><td><code>a.T</code></td><td><code>tf.transpose(t)</code></td></tr>
<tr><td><code>np.square()</code>, <code>np.exp()</code>, <code>np.sqrt()</code>, <code>reshape</code></td><td><code>tf.square()</code>, <code>tf.exp()</code>, <code>tf.sqrt()</code>, <code>tf.reshape()</code> (이름 같음)</td></tr>
</table>""")

    add("tf", "타입 변환 (tf.cast)", "cast 타입 변환 dtype float32 float64 int32 InvalidArgumentError",
"""try:
    tf.constant(2.0) + tf.constant(40)          # float32 + int32 → 에러
except tf.errors.InvalidArgumentError as ex:
    print("에러:", type(ex).__name__)
t2 = tf.constant(40., dtype=tf.float64)
print(tf.constant(2.0) + tf.cast(t2, tf.float32))   # 직접 맞춰 줘야 함""",
"텐서는 타입을 자동으로 바꿔 주지 않음 (성능 저하, 의도치 않은 변환 방지). 필요하면 tf.cast.")

    add("tf", "변수 (tf.Variable)", "variable 변수 assign 가중치 변경 scatter_nd_update",
"""v = tf.Variable([[1., 2., 3.], [4., 5., 6.]])
v.assign(2 * v)                 # 전체 바꾸기
v[0, 1].assign(42)              # 한 칸 바꾸기
v[:, 2].assign([0., 1.])        # 한 열 바꾸기
v.scatter_nd_update(indices=[[0, 0], [1, 2]], updates=[100., 200.])
print(v.numpy())
# v[1] = [7., 8., 9.]  ← 이렇게 = 로는 못 바꿈 (TypeError)""",
"텐서(constant)는 못 바꾸고, 학습 중 바뀌어야 하는 가중치는 Variable로 만든다.")

    add("tf", "래그드 텐서 · 희소 텐서", "ragged sparse 래그드 희소 비정형 to_tensor to_dense SparseTensor reorder",
"""r = tf.RaggedTensor.from_row_lengths(values=[3, 1, 4, 1, 5, 9, 2, 6], row_lengths=[4, 0, 3, 1])
print(r)                 # [[3,1,4,1], [], [5,9,2], [6]]  (행마다 길이가 다름)
print(r.to_tensor())     # 빈 칸을 0으로 채운 일반 텐서

s = tf.SparseTensor(indices=[[0, 1], [1, 0], [2, 3]], values=[1., 2., 3.], dense_shape=[3, 4])
print(tf.sparse.to_dense(s))   # 대부분 0인 3x4 행렬
print(tf.sparse.to_dense(s * 2.0))
# s + 1. 은 에러 → tf.sparse.to_dense(s) + 1.
s5 = tf.SparseTensor(indices=[[0, 2], [0, 1]], values=[1., 2.], dense_shape=[3, 4])
print(tf.sparse.to_dense(tf.sparse.reorder(s5)))   # 인덱스가 정렬 안 됐으면 reorder""",
"래그드: 길이가 제각각인 리스트의 리스트. 희소: 0이 대부분인 텐서를 0 아닌 값의 위치만 저장해 메모리 절약.")

    add("tf", "문자열 텐서", "string 문자열 unicode utf-8 encode decode ord",
"""s = tf.constant("café")                         # UTF-8 바이트 문자열로 저장
u = tf.constant([ord(c) for c in "café"])      # 유니코드 코드 포인트
b = tf.strings.unicode_encode(u, "UTF-8")
print(tf.strings.length(b, unit="UTF8_CHAR"))  # 4
p = tf.constant(["Café", "Coffee", "caffè", "咖啡"])
print(tf.strings.unicode_decode(p, "UTF8"))    # 래그드 텐서로 나옴""")


    # ---------------- 작년 같은 교수님 시험(머신러닝, 2025-1) Pandas 문항 유형
    add("pandas", "작년 시험 유형: 직종별·연도별 연봉 집계 상위 10개", "작년 시험 기출 중간고사 직종별 연도별 상위 10개 groupby 두개 정렬 sort_values 2024년",
"""df = pd.read_csv('/content/Salary2024.csv')        # Colab 업로드 경로

# a. 직종별 연봉을 연도별로 각각 집계 → 평균 상위 10개
a = df.groupby(['job_title', 'work_year'])['salary_in_usd'].agg(['min', 'max', 'mean'])
a = a.sort_values(by='mean', ascending=False)      # ← 결과를 다시 저장해야 정렬이 반영됨
a.head(10)

# b. 2024년 직종 평균 상위 10개
b = df[df['work_year'] == 2024]                     # ← 2024년만 먼저 거르기
b.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False).head(10)""",
"작년 답안에서 자주 틀린 두 곳: ① sort_values()는 원본을 바꾸지 않음 → 변수에 다시 넣거나 이어서(.head) 써야 함 ② '2024년' 조건이 있으면 groupby 전에 df[df['work_year'] == 2024]로 거르기.")

    # ---------------- 사용자 정의 (5·6장)
    add("custom", "캘리포니아 주택 데이터 준비 (5·6장 공통)", "california housing 회귀 데이터 X_train_scaled StandardScaler 준비",
"""from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
housing = fetch_california_housing()
X_train_full, X_test, y_train_full, y_test = train_test_split(
    housing.data, housing.target.reshape(-1, 1), random_state=42)
X_train, X_valid, y_train, y_valid = train_test_split(X_train_full, y_train_full, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_valid_scaled = scaler.transform(X_valid)
X_test_scaled = scaler.transform(X_test)
input_shape = X_train.shape[1:]      # (8,)""",
"StandardScaler: z = (x − 평균) / 표준편차. 평균·표준편차는 훈련 세트로만 계산(fit)하고 검증·테스트엔 transform만.")

    add("custom", "사용자 정의 손실 함수 (Huber)", "custom loss huber 사용자 정의 손실 함수 tf.where",
"""def huber_fn(y_true, y_pred):
    error = y_true - y_pred
    is_small_error = tf.abs(error) < 1
    squared_loss = tf.square(error) / 2          # 오차가 작으면 MSE처럼
    linear_loss = tf.abs(error) - 0.5            # 크면 MAE처럼 (이상치 영향 줄임)
    return tf.where(is_small_error, squared_loss, linear_loss)

model = keras.models.Sequential([
    keras.layers.Input(shape=input_shape),
    keras.layers.Dense(30, activation="selu", kernel_initializer="lecun_normal"),
    keras.layers.Dense(1),
])
model.compile(loss=huber_fn, optimizer="nadam", metrics=["mae"])
model.fit(X_train_scaled, y_train, epochs=2, validation_data=(X_valid_scaled, y_valid))""",
"loss 자리에 문자열 대신 함수 이름을 그대로 넣으면 됨. tf.where(조건, A, B) = 조건이 참이면 A, 아니면 B.")

    add("custom", "사용자 정의 요소가 있는 모델 저장 · 불러오기", "save load custom_objects 저장 불러오기 사용자 정의 매핑",
"""model.save("my_model_with_a_custom_loss.keras")
model = keras.models.load_model("my_model_with_a_custom_loss.keras",
                                custom_objects={"huber_fn": huber_fn})""",
"케라스가 모르는 함수·클래스는 불러올 때 custom_objects로 이름 → 실제 함수를 알려줘야 함.")

    add("custom", "매개변수가 있는 손실 (create_huber, 클로저)", "threshold 매개변수 클로저 closure create_huber 함수를 반환",
"""def create_huber(threshold=1.0):
    def huber_fn(y_true, y_pred):
        error = y_true - y_pred
        is_small_error = tf.abs(error) < threshold
        squared_loss = tf.square(error) / 2
        linear_loss = threshold * tf.abs(error) - threshold ** 2 / 2
        return tf.where(is_small_error, squared_loss, linear_loss)
    return huber_fn          # 함수를 돌려줌 (변수가 함수를 가질 수 있음)

model.compile(loss=create_huber(2.0), optimizer="nadam", metrics=["mae"])
model.save("my_model_with_a_custom_loss_threshold_2.keras")
model = keras.models.load_model("my_model_with_a_custom_loss_threshold_2.keras",
                                custom_objects={"huber_fn": create_huber(2.0)})""",
"단점: threshold 값(2.0)이 저장되지 않아서 불러올 때 다시 알려줘야 함 → 손실 클래스로 해결.")

    add("custom", "손실 함수 클래스 (keras.losses.Loss 상속)", "loss class 클래스 상속 get_config HuberLoss call",
"""class HuberLoss(keras.losses.Loss):
    def __init__(self, threshold=1.0, **kwargs):
        self.threshold = threshold
        super().__init__(**kwargs)
    def call(self, y_true, y_pred):
        error = y_true - y_pred
        is_small_error = tf.abs(error) < self.threshold
        squared_loss = tf.square(error) / 2
        linear_loss = self.threshold * tf.abs(error) - self.threshold ** 2 / 2
        return tf.where(is_small_error, squared_loss, linear_loss)
    def get_config(self):                          # 저장할 설정값
        base_config = super().get_config()
        return {**base_config, "threshold": self.threshold}

model.compile(loss=HuberLoss(3.), optimizer="nadam", metrics=["mae"])
model.fit(X_train_scaled, y_train, epochs=2, validation_data=(X_valid_scaled, y_valid))
model.save("my_model_with_a_custom_loss_class.keras")
m2 = keras.models.load_model("my_model_with_a_custom_loss_class.keras",
                             custom_objects={"HuberLoss": HuberLoss})
print(m2.loss.threshold)       # 3.0 이 저장되어 있음""",
"get_config()에 넣은 값은 모델과 함께 저장됨 → 불러올 때 threshold를 다시 줄 필요 없음.")

    add("custom", "사용자 정의 활성화 · 초기화 · 규제 · 제한", "custom activation initializer regularizer constraint softplus 양수 가중치",
"""from tensorflow.keras.utils import register_keras_serializable

def my_softplus(z):                                   # 활성화 함수
    return tf.math.log(1.0 + tf.exp(z))

@register_keras_serializable()
class MyGlorotInitializer(keras.Initializer):         # 초기화
    def __call__(self, shape, dtype=tf.float32):
        stddev = tf.sqrt(2. / (shape[0] + shape[1]))
        return tf.random.normal(shape, stddev=stddev, dtype=dtype)
    def get_config(self):
        return {}

@register_keras_serializable()
class MyL1Regularizer(keras.Regularizer):             # 규제
    def __call__(self, weights):
        return tf.reduce_sum(tf.abs(0.01 * weights))
    def get_config(self):
        return {}

@register_keras_serializable()
class MyPositiveWeights(keras.constraints.Constraint):  # 제한: 음수 가중치를 0으로
    def __call__(self, weights):
        return tf.where(weights < 0., tf.zeros_like(weights), weights)
    def get_config(self):
        return {}

model = keras.models.Sequential([
    keras.layers.Input(shape=input_shape),
    keras.layers.Dense(30, activation="selu", kernel_initializer="lecun_normal"),
    keras.layers.Dense(1, activation=my_softplus,
                       kernel_initializer=MyGlorotInitializer(),
                       kernel_regularizer=MyL1Regularizer(),
                       kernel_constraint=MyPositiveWeights())
])
model.compile(loss="mse", optimizer="nadam", metrics=["mae"])
model.fit(X_train_scaled, y_train, epochs=2, validation_data=(X_valid_scaled, y_valid))""",
"Dense의 activation / kernel_initializer / kernel_regularizer / kernel_constraint 자리에 직접 만든 함수·객체를 넣을 수 있음.")

    add("custom", "손실 vs 지표 · 스트리밍 지표 (Precision)", "metric 지표 손실 차이 precision 정밀도 streaming 스트리밍 reset_state result",
"""precision = keras.metrics.Precision()
print(precision([0, 1, 1, 1, 0, 1, 0, 1], [1, 1, 0, 1, 0, 1, 0, 1]))   # 1번째 배치: 0.8
print(precision([0, 1, 0, 0, 1, 0, 1, 1], [1, 0, 1, 1, 0, 0, 0, 0]))   # 누적: 0.5 (배치 평균 0.4가 아님)
print(precision.result())       # 지금까지 전체 기준
print(precision.variables)      # 누적 중인 TP, FP
precision.reset_state()         # 초기화""",
html="""<table>
<tr><th></th><th>손실 (loss)</th><th>지표 (metric)</th></tr>
<tr><td>용도</td><td>경사 하강법으로 학습에 사용</td><td>사람이 성능을 확인</td></tr>
<tr><td>조건</td><td>미분 가능해야 함</td><td>미분 안 돼도 됨, 이해하기 쉬워야 함</td></tr>
<tr><td>예</td><td>crossentropy, mse, huber</td><td>accuracy, mae, precision</td></tr>
</table><p>정밀도 = TP / (TP + FP): 참이라고 예측한 것 중 진짜 참인 비율. 스트리밍 지표는 배치마다 평균내지 않고 지금까지 전체로 계산.</p>""")

    add("custom", "사용자 정의 지표 클래스 (HuberMetric)", "custom metric 지표 클래스 add_weight update_state result",
"""class HuberMetric(keras.metrics.Metric):
    def __init__(self, threshold=1.0, **kwargs):
        super().__init__(**kwargs)
        self.threshold = threshold
        self.huber_fn = create_huber(threshold)
        self.total = self.add_weight(name="total", initializer="zeros")   # 누적 합
        self.count = self.add_weight(name="count", initializer="zeros")   # 누적 개수
    def update_state(self, y_true, y_pred, sample_weight=None):
        metric = self.huber_fn(y_true, y_pred)
        self.total.assign_add(tf.reduce_sum(metric))
        self.count.assign_add(tf.cast(tf.size(y_true), tf.float32))
    def result(self):
        return self.total / self.count
    def get_config(self):
        base_config = super().get_config()
        return {**base_config, "threshold": self.threshold}

m = HuberMetric(2.)
m(tf.constant([[2.]]), tf.constant([[10.]]))                 # total 14, count 1
m(tf.constant([[0.], [5.]]), tf.constant([[1.], [9.25]]))    # total 21, count 3
print(m.result())    # 7.0""")

    add("custom", "Lambda 층 (가중치 없는 층)", "lambda layer 람다 층 exp 지수 가중치 없는",
"""exponential_layer = keras.layers.Lambda(lambda x: tf.exp(x))
print(exponential_layer(tf.constant([-1., 0., 1., 2., 3.])))
model = keras.models.Sequential([
    keras.layers.Input(shape=input_shape),
    keras.layers.Dense(30, activation="relu"),
    keras.layers.Dense(1),
    exponential_layer                 # 출력을 항상 양수로
])
model.compile(loss="mse", optimizer="sgd")
model.fit(X_train_scaled, y_train, epochs=2, validation_data=(X_valid_scaled, y_valid))""",
"가중치가 없으면 Lambda, 가중치가 있으면 keras.layers.Layer를 상속해서 만듦.")

    add("custom", "사용자 정의 층 (MyDense: build · call)", "custom layer 사용자 정의 층 build call add_weight kernel bias Layer 상속",
"""class MyDense(keras.layers.Layer):
    def __init__(self, units, activation=None, **kwargs):
        super().__init__(**kwargs)
        self.units = units
        self.activation = keras.activations.get(activation)
    def build(self, batch_input_shape):                 # 입력 크기를 알게 되면 가중치 생성
        self.kernel = self.add_weight(name="kernel", shape=[batch_input_shape[-1], self.units],
                                      initializer="he_normal")
        self.bias = self.add_weight(name="bias", shape=[self.units], initializer="zeros")
    def call(self, X):                                  # 실제 계산
        return self.activation(X @ self.kernel + self.bias)
    def get_config(self):
        base_config = super().get_config()
        return {**base_config, "units": self.units,
                "activation": keras.activations.serialize(self.activation)}

model = keras.models.Sequential([
    keras.layers.Input(shape=input_shape),
    MyDense(30, activation="relu"),
    MyDense(1)
])
model.compile(loss="mse", optimizer="nadam")
model.fit(X_train_scaled, y_train, epochs=2, validation_data=(X_valid_scaled, y_valid))
model.save("my_model_with_a_custom_layer.keras")
model = keras.models.load_model("my_model_with_a_custom_layer.keras", custom_objects={"MyDense": MyDense})""",
"__init__: 설정 저장 / build: 가중치 만들기 / call: 계산(z = X·W + b 후 활성화) / get_config: 저장할 설정.")

    add("custom", "입력이 여러 개인 층 (MyMultiLayer)", "multi input 다중 입력 층 함수형 split",
"""class MyMultiLayer(keras.layers.Layer):
    def call(self, X):
        X1, X2 = X
        return X1 + X2, X1 * X2, X1 / X2

X1, X2 = np.array([[3., 6.], [2., 7.]]), np.array([[6., 12.], [4., 3.]])
print(MyMultiLayer()((X1, X2)))

input_A = keras.layers.Input(shape=[4])
input_B = keras.layers.Input(shape=[4])
hidden = MyMultiLayer()((input_A, input_B))
hidden_A = keras.layers.Dense(30, activation="selu")(hidden[0])
hidden_B = keras.layers.Dense(30, activation="selu")(hidden[1])
concat = keras.layers.Concatenate()((hidden_A, hidden_B))
output = keras.layers.Dense(1)(concat)
model = keras.models.Model(inputs=[input_A, input_B], outputs=[output])
model.compile(loss="mse", optimizer="nadam")
model.fit((X_train_scaled[:, :4], X_train_scaled[:, 4:]), y_train, epochs=2)""")

    add("custom", "훈련 · 예측 때 다르게 동작하는 층 (training)", "training 인자 훈련 테스트 다르게 노이즈 gaussian noise dropout",
"""class AddGaussianNoise(keras.layers.Layer):
    def __init__(self, stddev, **kwargs):
        super().__init__(**kwargs)
        self.stddev = stddev
    def call(self, X, training=None):
        if training:                                   # fit 중에만 노이즈 추가
            noise = tf.random.normal(tf.shape(X), stddev=self.stddev)
            return X + noise
        else:                                          # evaluate·predict 때는 그대로
            return X
    def compute_output_shape(self, batch_input_shape):
        return batch_input_shape

model = keras.models.Sequential([
    keras.layers.Input(shape=input_shape),
    AddGaussianNoise(stddev=1.0),
    keras.layers.Dense(30, activation="selu"),
    keras.layers.Dense(1)
])
model.compile(loss="mse", optimizer="nadam")
model.fit(X_train_scaled, y_train, epochs=2, validation_data=(X_valid_scaled, y_valid))""",
"Dropout·BatchNormalization도 이렇게 training에 따라 다르게 동작함.")

    add("custom", "사용자 정의 모델 (ResidualBlock · 서브클래싱)", "custom model 서브클래싱 subclassing ResidualBlock 잔차 residual skip keras.Model 상속",
"""class ResidualBlock(keras.layers.Layer):
    def __init__(self, n_layers, n_neurons, **kwargs):
        super().__init__(**kwargs)
        self.hidden = [keras.layers.Dense(n_neurons, activation="elu", kernel_initializer="he_normal")
                       for _ in range(n_layers)]
    def call(self, inputs):
        Z = inputs
        for layer in self.hidden:
            Z = layer(Z)
        return inputs + Z                   # 입력을 출력에 더함 (잔차 연결)

class ResidualRegressor(keras.Model):
    def __init__(self, output_dim, **kwargs):
        super().__init__(**kwargs)
        self.hidden1 = keras.layers.Dense(30, activation="relu", kernel_initializer="he_normal")
        self.block1 = ResidualBlock(2, 30)
        self.block2 = ResidualBlock(2, 30)
        self.out = keras.layers.Dense(output_dim)
    def call(self, inputs):
        Z = self.hidden1(inputs)
        for _ in range(1 + 3):              # 같은 블록을 4번 반복 사용
            Z = self.block1(Z)
        Z = self.block2(Z)
        return self.out(Z)

model = ResidualRegressor(1)
model.compile(loss="mse", optimizer="nadam")
model.fit(X_train_scaled, y_train, epochs=2)
print(model.evaluate(X_test_scaled, y_test))""",
"keras.Model을 상속하고 __init__에서 층을 만들고 call에서 연결. 반복문·조건문을 자유롭게 쓸 수 있음.")

    add("custom", "자동 미분 (GradientTape)", "gradienttape 자동 미분 기울기 gradient tape watch 편미분 derivative",
"""# y = 3x² + 3 → dy/dx = 6x → x=7이면 42
x = tf.Variable(7.0)
with tf.GradientTape() as tape:
    y = 3 * x ** 2 + 3
print(tape.gradient(y, x))          # 42.0

# 변수 2개: z = 3·w1² + 2·w1·w2 → (∂z/∂w1, ∂z/∂w2) = (6w1+2w2, 2w1) = (36, 10)
def f(w1, w2):
    return 3 * w1 ** 2 + 2 * w1 * w2
w1, w2 = tf.Variable(5.), tf.Variable(3.)
with tf.GradientTape() as tape:
    z = f(w1, w2)
print(tape.gradient(z, [w1, w2]))   # [36.0, 10.0]

# constant는 기록 안 됨 → None. tape.watch로 강제 기록
c1, c2 = tf.constant(5.), tf.constant(3.)
with tf.GradientTape() as tape:
    tape.watch(c1); tape.watch(c2)
    z = f(c1, c2)
print(tape.gradient(z, [c1, c2]))""",
"수치 미분 (f(x+ε)−f(x))/ε 은 파라미터마다 계산해야 해서 느림. GradientTape는 계산을 기록해 두고 한 번에 모든 기울기를 구함.")

    add("custom", "사용자 정의 훈련 반복 (fit 직접 구현)", "custom training loop 훈련 반복 apply_gradients trainable_variables random_batch fit 직접",
"""def random_batch(X, y, batch_size=32):
    idx = np.random.randint(len(X), size=batch_size)
    return X[idx], y[idx]

l2_reg = keras.regularizers.l2(0.05)
model = keras.models.Sequential([
    keras.layers.Input(shape=input_shape),
    keras.layers.Dense(30, activation="elu", kernel_initializer="he_normal", kernel_regularizer=l2_reg),
    keras.layers.Dense(1, kernel_regularizer=l2_reg)
])
n_epochs, batch_size = 2, 32
n_steps = len(X_train) // batch_size
optimizer = keras.optimizers.Nadam(learning_rate=0.01)
loss_fn = keras.losses.MeanSquaredError()
mean_loss = keras.metrics.Mean()

for epoch in range(1, n_epochs + 1):
    for step in range(1, n_steps + 1):
        X_batch, y_batch = random_batch(X_train_scaled, y_train)
        with tf.GradientTape() as tape:
            y_pred = model(X_batch)                                  # ① 순전파
            main_loss = tf.reduce_mean(loss_fn(y_batch, y_pred))     # ② 손실
            loss = tf.add_n([main_loss] + model.losses)              #    + 규제 손실
        gradients = tape.gradient(loss, model.trainable_variables)  # ③ 기울기 (역전파)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))  # ④ 가중치 갱신
        mean_loss(loss)
    print(f"Epoch {epoch}/{n_epochs} - loss: {mean_loss.result():.4f}")
    mean_loss.reset_state()""",
"fit()이 안에서 하는 일: 배치 뽑기 → 예측 → 손실 → 기울기 → 갱신을 반복.")

    add("custom", "텐서플로 함수 (tf.function)", "tf.function 그래프 graph concrete function 콘크리트 데코레이터 빠르게",
"""def cube(x):
    return x ** 3
tf_cube = tf.function(cube)          # 그래프로 변환한 함수
print(tf_cube(tf.constant(2.0)))     # 8.0

@tf.function                         # 데코레이터로 써도 같음
def quick_computation(x):
    aux = tf.eye(100)
    result = tf.zeros(100)
    for i in range(1, 100):
        aux = tf.matmul(x, aux) / i
        result = result + aux
    return result

x = tf.random.uniform(shape=[100, 100], minval=-1, maxval=1)
print(quick_computation(x).shape)
concrete_function = tf_cube.get_concrete_function(tf.constant(2.0))   # 입력 타입별 그래프
print(concrete_function.graph.get_operations())""",
"일반 파이썬 함수를 계산 그래프로 바꿔 빠르게 실행. 입력 타입·모양마다 콘크리트 함수가 따로 만들어짐(다형성).")

    add("custom", "파이썬 팁 (클로저 · *args · **kwargs · 데코레이터)", "python 파이썬 closure args kwargs decorator 데코레이터 가변인자",
"""def gimeAddFunction():           # 함수를 돌려주는 함수
    def f(a, b):
        return a + b
    return f
print(gimeAddFunction()(7, 9))   # 16

def hi(*names):                  # *args: 여러 개를 튜플로
    print(type(names), names)
hi("이순신", "안중근")

def hi3(**names):                # **kwargs: 이름=값 을 딕셔너리로
    for key, value in names.items():
        print(key, "is", value)
hi3(MyName="김철수", YourName="이영희")

def f1(func):                    # 데코레이터: 함수를 감싸는 함수
    def wrapper(*args, **kwargs):
        print("Started"); func(*args, **kwargs); print("End")
    return wrapper
@f1
def f2(a, b):
    print(a + b)
f2(3, 5)""")

    # ---------------- CNN (7장)
    add("cnn", "합성곱 직접 해보기 (tf.nn.conv2d + 필터)", "convolution 합성곱 conv2d filter 필터 수직선 수평선 특성맵 feature map load_sample_image",
"""from sklearn.datasets import load_sample_image
china = load_sample_image("china.jpg") / 255
flower = load_sample_image("flower.jpg") / 255
images = np.array([china, flower])
batch_size, height, width, channels = images.shape     # (2, 427, 640, 3)

filters = np.zeros(shape=(7, 7, channels, 2), dtype=np.float32)   # [높이, 너비, 입력채널, 출력채널]
filters[:, 3, :, 0] = 1     # 가운데 세로줄만 1 → 수직선 감지
filters[3, :, :, 1] = 1     # 가운데 가로줄만 1 → 수평선 감지

outputs = tf.nn.conv2d(images, filters, strides=1, padding="SAME")
print(outputs.shape)        # (2, 427, 640, 2): 이미지마다 특성맵 2장
plt.imshow(outputs[0, :, :, 0], cmap="gray"); plt.axis("off"); plt.show()""",
"images: [배치, 높이, 너비, 채널] / filters: [높이, 너비, 입력 채널, 출력 채널(필터 개수)].")

    add("cnn", "Conv2D 층", "conv2d 합성곱 층 filters kernel_size strides padding 출력 shape",
"""conv = keras.layers.Conv2D(filters=2, kernel_size=7, strides=1, padding="SAME", activation="relu")
conv_outputs = conv(images.astype(np.float32))
print(conv_outputs.shape)      # (2, 427, 640, 2)
# filters: 필터 개수 = 출력 특성맵 수 / kernel_size: 필터 크기 / strides: 이동 간격""",
"필터 값은 처음에 랜덤이고 학습하면서 스스로 정해짐(직접 정할 필요 없음).")

    add("cnn", "패딩 (SAME vs VALID) · 스트라이드 · 출력 크기", "padding 패딩 same valid stride 스트라이드 출력 크기 계산 feature map size",
"""def feature_map_size(input_size, kernel_size, strides=1, padding="SAME"):
    if padding == "SAME":
        return (input_size - 1) // strides + 1             # = ceil(입력 / 스트라이드)
    else:
        return (input_size - kernel_size) // strides + 1   # VALID: 패딩 없음

print(feature_map_size(28, 3, 1, "SAME"))    # 28
print(feature_map_size(28, 3, 1, "VALID"))   # 26
print(feature_map_size(28, 3, 2, "SAME"))    # 14
for pad in ["valid", "same"]:
    for s in [1, 2]:
        out = keras.layers.Conv2D(1, kernel_size=7, strides=s, padding=pad)(images.astype(np.float32))
        print(pad, "stride", s, "→", out.shape)""",
html="""<table>
<tr><th>설정</th><th>출력 크기 (입력 28, 커널 3)</th></tr>
<tr><td>SAME, stride 1</td><td>28 (가장자리에 0을 채워 크기 유지)</td></tr>
<tr><td>VALID, stride 1</td><td>28 − 3 + 1 = 26 (패딩 없음, 줄어듦)</td></tr>
<tr><td>SAME, stride 2</td><td>14 (2칸씩 이동해 절반)</td></tr>
<tr><td>MaxPool 2×2</td><td>절반 (28 → 14 → 7)</td></tr>
</table>""")

    add("cnn", "풀링 (Max · Average · Global Average)", "pooling 풀링 maxpool max pooling 최대 평균 avgpool global average 전역",
"""cropped = np.array([img[150:220, 130:250] for img in images], dtype=np.float32)   # (2, 70, 120, 3)
max_pool = keras.layers.MaxPool2D(pool_size=2)          # 2x2 칸에서 최댓값
avg_pool = keras.layers.AvgPool2D(pool_size=2)          # 2x2 칸의 평균
global_avg_pool = keras.layers.GlobalAvgPool2D()        # 특성맵 전체 평균 → 채널당 숫자 1개
print(max_pool(cropped).shape)          # (2, 35, 60, 3)  가로세로 절반
print(avg_pool(cropped).shape)          # (2, 35, 60, 3)
print(global_avg_pool(cropped).shape)   # (2, 3)""",
"풀링은 가중치가 없음(파라미터 0). 크기를 줄여 계산량·과대적합을 줄이고, 위치가 조금 달라도 같은 결과를 내게 함.")

    add("cnn", "CNN으로 Fashion MNIST (교수님 7-1 구조)", "cnn 모델 fashion mnist conv2d maxpooling flatten dense dropout 합성곱 신경망",
"""(X_train_full, y_train_full), (X_test, y_test) = keras.datasets.fashion_mnist.load_data()
X_train, X_valid = X_train_full[:-5000], X_train_full[-5000:]
y_train, y_valid = y_train_full[:-5000], y_train_full[-5000:]
X_mean = X_train.mean(axis=0, keepdims=True)
X_std = X_train.std(axis=0, keepdims=True) + 1e-7
X_train = (X_train - X_mean) / X_std          # 표준화 (평균 0, 표준편차 1)
X_valid = (X_valid - X_mean) / X_std
X_test = (X_test - X_mean) / X_std
X_train = X_train[..., np.newaxis]            # (55000, 28, 28) → (55000, 28, 28, 1) 채널 추가
X_valid = X_valid[..., np.newaxis]
X_test = X_test[..., np.newaxis]

model = keras.models.Sequential([
    keras.layers.Input(shape=[28, 28, 1]),
    keras.layers.Conv2D(32, kernel_size=(3, 3), padding="same"),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),
    keras.layers.Conv2D(64, kernel_size=(3, 3), padding="same"),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation="softmax")
])
model.summary()
model.compile(loss="sparse_categorical_crossentropy", optimizer="nadam", metrics=["accuracy"])
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_valid, y_valid))
print(model.evaluate(X_test, y_test))
y_pred = model.predict(X_test[:10])
print(np.argmax(y_pred, axis=-1), y_test[:10])""",
"Conv2D 입력은 [높이, 너비, 채널] 3차원이어야 해서 흑백 이미지에 채널 차원(1)을 붙임.")

    add("cnn", "CNN 파라미터 수 계산", "cnn 파라미터 계산 conv2d params 320 18496 3136 summary",
html="""<p><b>Conv2D</b> = (커널 높이 × 커널 너비 × 입력 채널 + 1) × 필터 수 &nbsp;·&nbsp; 풀링·Flatten·Dropout = 0</p>
<table>
<tr><th>층</th><th>출력 모양</th><th>계산</th><th>파라미터</th></tr>
<tr><td>Conv2D(32, 3×3, same)</td><td>(28, 28, 32)</td><td>(3×3×1 + 1) × 32</td><td>320</td></tr>
<tr><td>MaxPooling2D(2×2)</td><td>(14, 14, 32)</td><td>-</td><td>0</td></tr>
<tr><td>Conv2D(64, 3×3, same)</td><td>(14, 14, 64)</td><td>(3×3×32 + 1) × 64</td><td>18,496</td></tr>
<tr><td>MaxPooling2D(2×2)</td><td>(7, 7, 64)</td><td>-</td><td>0</td></tr>
<tr><td>Flatten</td><td>(3136)</td><td>7 × 7 × 64</td><td>0</td></tr>
<tr><td>Dense(128)</td><td>(128)</td><td>3136 × 128 + 128</td><td>401,536</td></tr>
<tr><td>Dense(10)</td><td>(10)</td><td>128 × 10 + 10</td><td>1,290</td></tr>
<tr><td colspan="3">합계</td><td>421,642</td></tr>
</table>
<p>합성곱 층은 필터를 이미지 전체에 같이 쓰기 때문에(가중치 공유) 파라미터가 적음. 파라미터 대부분은 Flatten 뒤 Dense에 있음.</p>""")

    add("cnn", "MLP vs CNN (숫자 인식, 교수님 7-2)", "mlp cnn 비교 숫자 mnist reshape 28 28 1 완전연결 fully connected",
"""from tensorflow.keras.utils import to_categorical
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

# MLP: 784개 한 줄로 펴서 입력 → 공간(위치) 정보가 사라짐
Xm_train = X_train.reshape(60000, 784).astype("float32") / 255
Xm_test = X_test.reshape(10000, 784).astype("float32") / 255
mlp = keras.Sequential([
    keras.layers.Input(shape=(784,)),
    keras.layers.Dense(32, activation="relu"),
    keras.layers.Dense(32, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])
mlp.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
mlp.fit(Xm_train, to_categorical(y_train, 10), batch_size=128, epochs=5, verbose=2)
print("MLP:", mlp.evaluate(Xm_test, to_categorical(y_test, 10), verbose=0)[1])

# CNN: 28x28x1 그대로 입력 → 주변 픽셀 관계(선·곡선)를 봄
Xc_train = X_train.reshape(-1, 28, 28, 1).astype("float32") / 255
Xc_test = X_test.reshape(-1, 28, 28, 1).astype("float32") / 255
cnn = keras.Sequential([
    keras.layers.Input(shape=(28, 28, 1)),
    keras.layers.Conv2D(32, kernel_size=(3, 3), padding="same"),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),
    keras.layers.Conv2D(64, kernel_size=(3, 3), padding="same"),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation="softmax")
])
cnn.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
cnn.fit(Xc_train, y_train, epochs=2, verbose=2)
print("CNN:", cnn.evaluate(Xc_test, y_test, verbose=0)[1])""",
"MLP는 원-핫 + categorical, CNN은 정수 레이블 + sparse_categorical로 교수님 노트북 그대로 둠.")

    add("cnn", "합성곱 커널 예시 (scipy convolve)", "kernel 커널 sobel 소벨 엣지 edge 필터 예시 convolve scipy",
"""from scipy.ndimage import convolve      # (옛 코드: scipy.ndimage.filters → 이제 scipy.ndimage)
k1 = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])        # 세로 경계
k2 = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])        # 가로 경계
k3 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])   # 모든 방향 경계
img = keras.datasets.mnist.load_data()[0][0][0].astype(float)
for k in (k1, k2, k3):
    res = convolve(img, k)
    plt.imshow(res, cmap="gray"); plt.axis("off"); plt.show()""")
