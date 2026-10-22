# 빈칸 채우기: 시험 노트북의 주석 문장 → 들어갈 코드. 변수 이름은 교수님 수업 노트북과 동일하게.
# (2장: X_train_full·model·history·X_new·y_proba / 4장 NumPy: w_1·z_1·a_1·d_output / 5·6장: X_train_scaled·huber_fn·loss_fn·n_steps / 7장: images·filters·outputs·X_mean)

SECTIONS_FILL = [("fill", "빈칸 채우기")]

N2 = "변수 이름: 2. 케라스 노트북과 동일"
N4 = "변수 이름: 4. 신경망 요소 노트북과 동일"
NO = "변수 이름: 4. 신경망요소-Optimizer(NumPy) 노트북과 동일"
N5 = "변수 이름: 5. 사용자 정의 모델 노트북과 동일"
N6 = "변수 이름: 6. 사용자 정의 모델 2 노트북과 동일"
N7 = "변수 이름: 7-1 / 7-2 CNN 노트북과 동일"
NE = "변수 이름: 작년 같은 교수님 시험 노트북과 동일 (fprs, tprs, thresholds, pred_proba_class1, scores_df, plotROC)"

def register(add):
    F = lambda title, kw, code, note="": add("fill", title, kw + " 빈칸 주석 채우기 시험", code, note)

    # ---- 데이터
    F("# 데이터 로딩 (Fashion MNIST) · 정규화 · 학습/검증 분리", "데이터 로딩 load_data fashion 정규화 255 학습 검증 분리 X_train_full",
"""fashion_mnist = keras.datasets.fashion_mnist
(X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()
X_valid, X_train = X_train_full[:5000] / 255., X_train_full[5000:] / 255.
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]
X_test = X_test / 255.
class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]""", N2)

    F("# 데이터 로딩 (MNIST) · 784로 펴기 · 원-핫 인코딩", "mnist 숫자 reshape 784 to_categorical 원핫 nb_classes Y_train",
"""from keras.datasets import mnist
from keras.utils import to_categorical
(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255
nb_classes = 10
Y_train = to_categorical(y_train, nb_classes)
Y_test = to_categorical(y_test, nb_classes)""", "변수 이름: 3·4장 MNIST 노트북과 동일 (원-핫은 대문자 Y_train / Y_test)")

    F("# 데이터 로딩 (캘리포니아 주택) · 스케일링", "california housing 회귀 StandardScaler X_train_scaled 스케일",
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
input_shape = X_train.shape[1:]""", N5)

    # ---- 2장 기본
    F("# 모델 생성 (시퀀셜)", "모델 생성 sequential dense 은닉층 model",
"""model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=[28, 28]),
    keras.layers.Dense(300, activation="relu"),
    keras.layers.Dense(100, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])
model.summary()""", N2)

    F("# 모델 컴파일", "compile 컴파일 loss optimizer metrics",
"""model.compile(loss="sparse_categorical_crossentropy",
              optimizer="sgd",
              metrics=["accuracy"])""", N2 + " · 원-핫(Y_train)이면 loss='categorical_crossentropy'")

    F("# 학습", "학습 fit history epochs validation_data",
"""history = model.fit(X_train, y_train, epochs=30,
                    validation_data=(X_valid, y_valid))""", N2)

    F("# 평가", "평가 evaluate 테스트 정확도 score",
"""model.evaluate(X_test, y_test)
# 3·4장 스타일:
# score = model.evaluate(X_test, Y_test)
# print('Test score:', score[0])
# print('Test accuracy:', score[1])""", N2)

    F("# 예측 (새 샘플 3개)", "예측 predict X_new y_proba y_pred argmax class_names",
"""X_new = X_test[:3]
y_proba = model.predict(X_new)
y_proba.round(2)
y_pred = np.argmax(model.predict(X_new), axis=-1)
np.array(class_names)[y_pred]""", N2)

    F("# 학습 곡선 그리기", "학습곡선 history plot DataFrame 그래프 loss accuracy",
"""import pandas as pd
pd.DataFrame(history.history).plot(figsize=(8, 5))
plt.grid(True)
plt.gca().set_ylim(0, 1)
plt.show()""", N2)

    F("# 모델 생성 (함수형 API, 와이드 & 딥)", "함수형 functional wide deep concatenate input_ hidden1 hidden2 concat output",
"""input_ = keras.layers.Input(shape=X_train.shape[1:])
hidden1 = keras.layers.Dense(30, activation="relu")(input_)
hidden2 = keras.layers.Dense(30, activation="relu")(hidden1)
concat = keras.layers.concatenate([input_, hidden2])
output = keras.layers.Dense(1)(concat)
model = keras.models.Model(inputs=[input_], outputs=[output])""", N2 + " (캘리포니아 주택 데이터)")

    F("# 저장과 복원", "save load 저장 복원 my_keras_model model2",
"""model.save("my_keras_model.keras")
model2 = keras.models.load_model("my_keras_model.keras")""", N2)

    F("# 훈련 과정에서 콜백 사용하기 (체크포인트 · 조기 종료)", "callback 콜백 checkpoint_cb early_stopping_cb ModelCheckpoint EarlyStopping",
"""model = keras.models.Sequential([
    keras.layers.Dense(30, activation="relu", input_shape=[8]),
    keras.layers.Dense(30, activation="relu"),
    keras.layers.Dense(1)
])
model.compile(loss="mse", optimizer=keras.optimizers.SGD(learning_rate=1e-3))
checkpoint_cb = keras.callbacks.ModelCheckpoint("my_keras_model.keras", save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True)
history = model.fit(X_train, y_train, epochs=100,
                    validation_data=(X_valid, y_valid),
                    callbacks=[checkpoint_cb, early_stopping_cb])
model = keras.models.load_model("my_keras_model.keras")  # 최상의 모델로 롤백
mse_test = model.evaluate(X_test, y_test)""", N2 + " (캘리포니아 주택 데이터, 스케일링한 X_train 사용)")

    # ---- 4장
    F("# 초기화를 바꿔 학습하고 손실 비교 (h_he · plot_loss)", "initializer he_normal h_he plot_loss 비교 history 초기화 활성화",
"""np.random.seed(42)
tf.random.set_seed(42)
model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=[28, 28]),
    keras.layers.Dense(300, activation="relu", kernel_initializer='he_normal'),
    keras.layers.Dense(100, activation="relu", kernel_initializer='he_normal'),
    keras.layers.Dense(10, activation="softmax")
])
model.compile(loss="sparse_categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])
h_he = model.fit(X_train, y_train, epochs=20, validation_data=(X_valid, y_valid))
model.evaluate(X_test, y_test)

def plot_loss(*args, figsize=(10, 5)):          # 노트북에 이미 있는 함수
    def plot_ind_loss(history, label):
        plt.plot(history.history['loss'], label=label)
        plt.title('loss over epochs'); plt.ylabel('loss'); plt.xlabel('epochs'); plt.legend()
    plt.figure(figsize=figsize)
    for i, fstr in enumerate(args):
        f = globals().get(fstr) if isinstance(fstr, str) else fstr
        fstr = fstr if isinstance(fstr, str) else i
        plot_ind_loss(f, fstr)

plot_loss("history", "h_he")      # 변수 이름을 문자열로 전달""",
N4 + " · 다른 실험도 h_random, h_sigmoid, h_leaky, h_leaky_he, h_selu 처럼 이름을 붙여 plot_loss에 넘김")

    F("# 배치 정규화 적용 모델", "batch normalization 배치정규화 BatchNormalization elu he_normal",
"""model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=[28, 28]),
    keras.layers.BatchNormalization(),
    keras.layers.Dense(300, activation="elu", kernel_initializer='he_normal'),
    keras.layers.BatchNormalization(),
    keras.layers.Dense(100, activation="elu", kernel_initializer='he_normal'),
    keras.layers.BatchNormalization(),
    keras.layers.Dense(10, activation="softmax")
])
model.compile(loss="sparse_categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])
model.fit(X_train, y_train, epochs=20, validation_data=(X_valid, y_valid))
model.evaluate(X_test, y_test)""", N4)

    F("# Optimizer 지정 (Momentum · NAG · Adam)", "optimizer 옵티마이저 momentum nag nesterov adam beta_1 beta_2",
"""optimizer = keras.optimizers.SGD(learning_rate=0.001, momentum=0.9)                 # Momentum
optimizer = keras.optimizers.SGD(learning_rate=0.001, momentum=0.9, nesterov=True)  # NAG
optimizer = keras.optimizers.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999)     # Adam
model.compile(loss="sparse_categorical_crossentropy",
              optimizer=optimizer,
              metrics=["accuracy"])""", N4 + " · 셋 중 쓰는 한 줄만 남김")

    F("# Dropout 적용", "dropout 드롭아웃 rate",
"""model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=[28, 28]),
    keras.layers.Dense(300, activation="relu", kernel_initializer='he_normal'),
    keras.layers.Dense(100, activation="relu", kernel_initializer='he_normal'),
    keras.layers.Dropout(rate=0.2),
    keras.layers.Dense(10, activation="softmax")
])""", N4)

    # ---- NumPy 신경망
    F("# feed forward (z_1, a_1, ... output)", "feed forward 순전파 numpy z_1 a_1 w_1 b_1 sigmoid softmax output",
"""w_1 = np.random.rand(16, 784)   # (# of neurons, # of inputs)
b_1 = np.random.rand(16)
w_2 = np.random.rand(16, 16)
b_2 = np.random.rand(16)
w_o = np.random.rand(10, 16)
b_o = np.random.rand(10)

z_1 = np.dot(w_1, X_train.T)
z_1 = z_1.T + b_1
a_1 = sigmoid(z_1)
z_2 = np.dot(w_2, a_1.T)
z_2 = z_2.T + b_2
a_2 = sigmoid(z_2)
z_o = np.dot(w_o, a_2.T)
z_o = z_o.T + b_o
output = softmax(z_o)""", NO + " · X_train은 (60000, 784)로 편 상태, sigmoid·softmax 함수는 노트북에 정의됨")

    F("# 손실 구하기 (cross entropy)", "손실 loss cross_entropy_loss 교차 엔트로피 numpy",
"""def cross_entropy_loss(y_actual, y_pred):
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    return -np.sum(y_actual * np.log(y_pred)) / len(y_actual)

loss = cross_entropy_loss(Y_train, output)
print("Loss:", loss)""", NO)

    F("# Backpropagation (출력층 → 은닉층 경사)", "backpropagation 역전파 경사 gradient d_output d_weight_o d_bias_o d_layer2 d_layer1",
"""# Gradient of the output layer
d_output = output - Y_train
# Gradient of the output layer weights and biases
d_weight_o = np.dot(d_output.T, a_2) / len(Y_train)
d_bias_o = np.sum(d_output, axis=0) / len(Y_train)
# Gradient of the second hidden layer
d_layer2 = np.dot(d_output, w_o) * (a_2 * (1 - a_2))
# Gradient of the second hidden layer weights and biases
d_weight_2 = np.dot(d_layer2.T, a_1) / len(Y_train)
d_bias_2 = np.sum(d_layer2, axis=0) / len(Y_train)
# Gradient of the first hidden layer
d_layer1 = np.dot(d_layer2, w_2) * (a_1 * (1 - a_1))
# Gradient of the first hidden layer weights and biases
d_weight_1 = np.dot(d_layer1.T, X_train) / len(Y_train)
d_bias_1 = np.sum(d_layer1, axis=0) / len(Y_train)""", NO + " (주석도 노트북과 같음)")

    F("# Optimization step (가중치 갱신)", "optimization step 가중치 갱신 update learning_rate numpy",
"""learning_rate = 0.01
w_1 = w_1 - learning_rate * d_weight_1
b_1 = b_1 - learning_rate * d_bias_1
w_2 = w_2 - learning_rate * d_weight_2
b_2 = b_2 - learning_rate * d_bias_2
w_o = w_o - learning_rate * d_weight_o
b_o = b_o - learning_rate * d_bias_o""", NO)

    # ---- 5·6장
    F("# 사용자 정의 손실 함수 (huber_fn) 로 학습", "huber_fn 사용자 정의 손실 custom loss compile nadam mae",
"""def huber_fn(y_true, y_pred):
    error = y_true - y_pred
    is_small_error = tf.abs(error) < 1
    squared_loss = tf.square(error) / 2
    linear_loss  = tf.abs(error) - 0.5
    return tf.where(is_small_error, squared_loss, linear_loss)

model = keras.models.Sequential([
    keras.layers.Input(shape=input_shape),
    keras.layers.Dense(30, activation="selu", kernel_initializer="lecun_normal"),
    keras.layers.Dense(1),
])
model.compile(loss=huber_fn, optimizer="nadam", metrics=["mae"])
model.fit(X_train_scaled, y_train, epochs=2,
          validation_data=(X_valid_scaled, y_valid))""", N5)

    F("# 사용자 정의 요소를 가진 모델을 저장하고 로드하기", "custom_objects 저장 로드 사용자 정의 huber",
"""model.save("my_model_with_a_custom_loss.keras")
model = keras.models.load_model("my_model_with_a_custom_loss.keras",
                                custom_objects={"huber_fn": huber_fn})""", N5)

    F("# 사용자 정의 Layer (MyDense) 로 모델 만들기", "MyDense 사용자 정의 층 build call kernel bias",
"""class MyDense(tf.keras.layers.Layer):
    def __init__(self, units, activation=None, **kwargs):
        super().__init__(**kwargs)
        self.units = units
        self.activation = tf.keras.activations.get(activation)

    def build(self, batch_input_shape):
        self.kernel = self.add_weight(
            name="kernel", shape=[batch_input_shape[-1], self.units],
            initializer="he_normal")
        self.bias = self.add_weight(
            name="bias", shape=[self.units], initializer="zeros")

    def call(self, X):
        return self.activation(X @ self.kernel + self.bias)

    def get_config(self):
        base_config = super().get_config()
        return {**base_config, "units": self.units,
                "activation": tf.keras.activations.serialize(self.activation)}

model = keras.models.Sequential([
    keras.layers.Input(shape=input_shape),
    MyDense(30, activation="relu"),
    MyDense(1)
])
model.compile(loss="mse", optimizer="nadam")
model.fit(X_train_scaled, y_train, epochs=2, validation_data=(X_valid_scaled, y_valid))
model.evaluate(X_test_scaled, y_test)""", N6)

    F("# GradientTape로 그레이디언트 계산하기", "gradienttape 자동 미분 tape gradient w1 w2 dy_dx",
"""x = tf.Variable(7.0)
a = 3
b = 3
with tf.GradientTape() as tape:
  y = a * x ** 2 + b
dy_dx = tape.gradient(y, x)
print(dy_dx)                          # 42

def f(w1, w2):
    return 3 * w1 ** 2 + 2 * w1 * w2
w1, w2 = tf.Variable(5.), tf.Variable(3.)
with tf.GradientTape() as tape:
    z = f(w1, w2)
gradients = tape.gradient(z, [w1, w2])
gradients                             # [36, 10]""", N6)

    F("# 사용자 정의 훈련 반복", "custom training loop 훈련 반복 n_epochs n_steps random_batch loss_fn mean_loss apply_gradients",
"""def random_batch(X, y, batch_size=32):
    idx = np.random.randint(len(X), size=batch_size)
    return X[idx], y[idx]

l2_reg = keras.regularizers.l2(0.05)
model = keras.models.Sequential([
    keras.layers.Dense(30, activation="elu", kernel_initializer="he_normal",
                       kernel_regularizer=l2_reg),
    keras.layers.Dense(1, kernel_regularizer=l2_reg)
])
n_epochs = 5
batch_size = 32
n_steps = len(X_train) // batch_size
optimizer = keras.optimizers.Nadam(learning_rate=0.01)
loss_fn = keras.losses.MeanSquaredError()
mean_loss = keras.metrics.Mean()
metrics = [keras.metrics.MeanAbsoluteError()]

for epoch in range(1, n_epochs + 1):
    print("Epoch {}/{}".format(epoch, n_epochs))
    for step in range(1, n_steps + 1):
        X_batch, y_batch = random_batch(X_train_scaled, y_train)
        with tf.GradientTape() as tape:
            y_pred = model(X_batch)
            main_loss = tf.reduce_mean(loss_fn(y_batch, y_pred))
            loss = tf.add_n([main_loss] + model.losses)
        gradients = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))
        mean_loss(loss)
        for metric in metrics:
            metric(y_batch, y_pred)
    print("loss:", float(mean_loss.result()), [float(m.result()) for m in metrics])
    for metric in [mean_loss] + metrics:
        metric.reset_state()""", N6)

    # ---- 7장
    F("# 2개의 필터를 만들고 합성곱 하기 (수직선 · 수평선)", "filters 필터 conv2d images outputs 수직선 수평선 load_sample_image china flower",
"""from sklearn.datasets import load_sample_image
china = load_sample_image("china.jpg") / 255
flower = load_sample_image("flower.jpg") / 255
images = np.array([china, flower])
batch_size, height, width, channels = images.shape

filters = np.zeros(shape=(7, 7, channels, 2), dtype=np.float32)
filters[:, 3, :, 0] = 1  # 수직선
filters[3, :, :, 1] = 1  # 수평선
outputs = tf.nn.conv2d(images, filters, strides=1, padding="SAME")
plt.imshow(outputs[0, :, :, 1], cmap="gray"); plt.axis("off"); plt.show()""", N7)

    F("# 풀링 층 (max_pool · avg_pool · global_avg_pool)", "pooling 풀링 max_pool avg_pool global_avg_pool cropped_images",
"""def crop(images):
    return images[150:220, 130:250]
cropped_images = np.array([crop(image) for image in images], dtype=np.float32)
max_pool = keras.layers.MaxPool2D(pool_size=2)
output = max_pool(cropped_images)
avg_pool = keras.layers.AvgPool2D(pool_size=2)
output_avg = avg_pool(cropped_images)
global_avg_pool = keras.layers.GlobalAvgPool2D()
global_avg_pool(cropped_images)""", N7)

    F("# CNN용 데이터 준비 (표준화 · 채널 차원 추가)", "cnn 데이터 X_mean X_std newaxis 표준화 채널",
"""(X_train_full, y_train_full), (X_test, y_test) = keras.datasets.fashion_mnist.load_data()
X_train, X_valid = X_train_full[:-5000], X_train_full[-5000:]
y_train, y_valid = y_train_full[:-5000], y_train_full[-5000:]
X_mean = X_train.mean(axis=0, keepdims=True)
X_std = X_train.std(axis=0, keepdims=True) + 1e-7
X_train = (X_train - X_mean) / X_std
X_valid = (X_valid - X_mean) / X_std
X_test = (X_test - X_mean) / X_std
X_train = X_train[..., np.newaxis]
X_valid = X_valid[..., np.newaxis]
X_test = X_test[..., np.newaxis]""", N7)

    F("# CNN 모델 생성 · 학습 · 예측", "cnn 모델 Conv2D MaxPooling2D model.add Flatten Dense Dropout Activation nadam",
"""from tensorflow.keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import MaxPooling2D, Conv2D

model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3), input_shape=[28, 28, 1], padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, kernel_size=(3,3), padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(10))
model.add(Activation('softmax'))
model.summary()

model.compile(loss="sparse_categorical_crossentropy", optimizer="nadam", metrics=["accuracy"])
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_valid, y_valid))
score = model.evaluate(X_test, y_test)
X_new = X_test[:10]
y_pred = model.predict(X_new)
ind = np.argmax(y_pred[0])
print(class_names[ind])""", N7 + " (7-2 노트북의 from keras.layers.core 는 에러 → keras.layers 로)")

    # ---- 작년 시험 형식 (평가 · 탐색)
    F("# 레이블 값이 1일때의 예측 확률 및 fprs, tprs, thresholds 구하기", "roc_curve fprs tprs thresholds pred_proba_class1 예측 확률 레이블 1",
"""from sklearn.metrics import roc_curve, roc_auc_score
# 케라스 분류 모델: softmax 출력의 1번 열 = 레이블 1일 확률
pred_proba_class1 = model.predict(X_test)[:, 1]
# sklearn 분류기라면: pred_proba_class1 = lr_clf.predict_proba(X_test)[:, 1]
fprs, tprs, thresholds = roc_curve(y_test == 1, pred_proba_class1)   # 정답이 1인가(이진)""", NE)

    F("# ROC curve 그리기 (plotROC 사용)", "plotROC roc 그리기 그래프 fprs tprs",
"""def plotROC(fprs, tprs):                       # 시험 노트북에 주어지는 함수
    plt.plot(fprs, tprs, label='ROC')
    plt.plot([0, 1], [0, 1], 'k--', label='Random')
    plt.legend()
    start, end = plt.xlim()
    plt.xticks(np.round(np.arange(start, end, 0.1), 2))
    plt.xlim(0, 1); plt.ylim(0, 1)
    plt.xlabel('FPR( 1 - Specificity )'); plt.ylabel('TPR( Recall )')

plotROC(fprs, tprs)
plt.show()""", NE)

    F("# AUC 구하기 · 좋은 순서로 나열", "auc roc_auc_score 비교 순서 정렬 나열",
"""auc = roc_auc_score(y_test == 1, pred_proba_class1)
print("AUC:", round(auc, 4))
# 모델 여러 개 비교: aucs = {"모델A": auc_a, "모델B": auc_b, ...}
aucs = {"model": auc}
sorted(aucs.items(), key=lambda x: x[1], reverse=True)""", NE)

    F("# GridSearchCV 결과 추출하여 DataFrame으로 변환", "cv_results_ scores_df grid 결과 DataFrame rank_test_score mean_test_score params",
"""# grid_dtree(또는 grid)가 fit된 GridSearchCV 객체일 때
scores_df = pd.DataFrame(grid_dtree.cv_results_)
scores_df[['params', 'mean_test_score', 'rank_test_score',
           'split0_test_score', 'split1_test_score', 'split2_test_score']]
print(grid_dtree.best_params_, grid_dtree.best_score_)""", NE)

    F("# 구한 최적 parameter 조합으로 모델 생성하여 학습", "최적 파라미터 best_params_ 재학습 best_estimator_ refit",
"""best_params = grid_dtree.best_params_            # 예: {'max_depth': 3, 'min_samples_split': 2}
dt_clf2 = DecisionTreeClassifier(random_state=11, **best_params)   # ** : 딕셔너리를 인자로 풀어 넣음
dt_clf2.fit(X_train, y_train)
# 또는 refit=True면 이미 최적 모델: grid_dtree.best_estimator_""", NE + " · ** 사용법은 '변수 앞의 * · **' 카드 참고")

    F("# 업로드한 CSV 읽기", "csv 업로드 read_csv datafile content df",
"""datafile = '/content/Salary2024.csv'
df = pd.read_csv(datafile)
df.head(10)""", "변수 이름: 작년 시험·Week3 과제와 동일 (datafile, df)")

    # ---- * / ** 실습 예제
    add("custom", "변수 앞의 * · ** (교수님 노트북에 나온 곳 전부)", "별표 asterisk * ** args kwargs 언패킹 unpacking 가변인자 packing 딕셔너리 풀기",
"""# ① 함수 정의: *args → 여러 위치 인자를 튜플로 모음 (6장 Tips)
def hi(*Names):
    for name in Names:
        print("%s %s" % (name[0], name[1:3]), end=' ')
    print(type(Names), Names)             # <class 'tuple'> ('이순신', '안중근')
hi('이순신', '안중근')

def hi2(Names):                           # * 없으면 인자 1개만 받음
    print(type(Names), Names)
# hi2('이순신', '안중근')  → TypeError (인자 2개)

# ② 함수 정의: **kwargs → 이름=값 인자를 딕셔너리로 모음
def hi3(**Names):
    for key, value in Names.items():
        print("{0} is {1}".format(key, value))
hi3(MyName="김철수", YourName='이영희')

# ③ 데코레이터: 받은 인자를 그대로 넘김 (*args, **kwargs)
def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        func(*args, **kwargs)              # 호출할 때 * ** = 다시 풀어서 전달
        print("End")
    return wrapper
@f1
def f(a, b=9):
    print(a, b)
f('oo', b=10)

# ④ 사용자 정의 층·손실: 케라스 기본 인자(name, dtype 등)를 부모에게 그대로 전달
class MyLayer(keras.layers.Layer):
    def __init__(self, units, **kwargs):
        super().__init__(**kwargs)
        self.units = units
    def get_config(self):
        base_config = super().get_config()
        return {**base_config, "units": self.units}   # ⑤ 딕셔너리 합치기
print(MyLayer(3, name="my").get_config()["name"])

# ⑥ 호출할 때 풀기: 리스트·튜플 → 위치 인자, 딕셔너리 → 키워드 인자
params = [3500, 10000, "=" * 5]
print("{}/{} [{}]".format(*params))        # 6장 progress_bar의 fmt.format(*params)
best = {"max_depth": 3, "min_samples_split": 2}
print(dict(**best))
first, *rest = [1, 2, 3, 4]                # ⑦ 나머지 모으기: first=1, rest=[2,3,4]
print(first, rest)

# ⑧ 4장 plot_loss(*args): 넘긴 개수만큼 그래프
def show(*args, figsize=(10, 5)):          # *args 뒤의 인자는 이름으로만 넘길 수 있음
    print(len(args), args, figsize)
show("history", "h_he", "h_random")""",
"곱하기 a * b, 거듭제곱 x ** 2 와 다름: 변수·인자 '앞'에 붙으면 묶기/풀기.")
