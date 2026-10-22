# 교수님 노트북 8개를 처음부터 실제로 실행해서 나온 에러 (TF 2.21 / Keras 3, 2026-10-23 실행)
# 10/10 과제 형식: "실습 노트북을 돌리고, 에러를 고친 뒤, 그 에러가 뭐였는지 텍스트 박스에 쓰기"

SECTIONS_NBERR = [("nberr", "노트북 에러 수정")]


def _card(msg, cause, write, extra=""):
    return (f"<p><b>에러 메시지</b></p><pre class=\"out\"><code>{msg}</code></pre>"
            f"<p><b>원인</b>: {cause}</p>"
            f"<p><b>텍스트 박스에 쓸 문장 (예시, 자기 말로 바꿔 쓰기)</b></p><blockquote>{write}</blockquote>{extra}")


def register(add):
    def _a(title, kw, code="", html=""):
        add("nberr", title, kw + " 에러 수정 원인 노트북 실행 과제 텍스트 박스", code=code, html=html)

    _a("한눈에: 교수님 노트북에서 실제로 나는 에러", "에러 목록 요약 한눈에 전체",
html="""<p>노트북 8개를 처음부터 끝까지 실행한 결과. <b>일부러 에러를 보여 주는 셀</b>(교수님이 바로 아래에 고친 셀이나 "왜 예외가 발생했을까?"를 둔 곳)과 <b>버전이 바뀌어서 나는 에러</b>가 섞여 있음.</p>
<table>
<tr><th>노트북</th><th>셀 코드</th><th>에러</th><th>한 줄 원인 → 수정</th></tr>
<tr><td>5장</td><td><code>tf.constant(2.0) + t2</code></td><td>InvalidArgumentError</td><td>float32 + float64, 자동 형변환 없음 → <code>tf.cast(t2, tf.float32)</code></td></tr>
<tr><td>5장</td><td><code>v[1] = [7., 8., 9.]</code></td><td>TypeError</td><td>Variable은 = 로 대입 불가 → <code>v[1].assign([7., 8., 9.])</code></td></tr>
<tr><td>5장</td><td><code>s6 = tf.sparse.to_dense(s5)</code> 후 <code>s6</code></td><td>InvalidArgumentError → NameError</td><td>희소 텐서 인덱스가 정렬 안 됨 → <code>tf.sparse.reorder(s5)</code></td></tr>
<tr><td>6장</td><td><code>hi2('이순신', '안중근')</code></td><td>TypeError</td><td>매개변수에 * 가 없어 하나만 받음 → <code>def hi2(*Names)</code></td></tr>
<tr><td>7-2</td><td><code>from keras.layers.core import ...</code></td><td>ModuleNotFoundError</td><td>Keras 3에서 core 경로가 없어짐 → <code>from keras.layers import ...</code></td></tr>
<tr><td>7-2</td><td><code>mlp.save('/content/drive/MyDrive/mlp')</code></td><td>ValueError</td><td>Keras 3는 확장자 필수 → <code>'... /mlp.keras'</code> (+ 드라이브 마운트)</td></tr>
<tr><td>7-2</td><td><code>Image.open('/content/digit.png')</code></td><td>FileNotFoundError</td><td>이미지 파일을 안 올림 → 업로드하거나 MNIST 이미지로 대신</td></tr>
<tr><td>3·4장</td><td>그림 그리기(<code>draw</code>), <code>torchvision</code></td><td>NameError 등</td><td>Colab 전용 기능. Colab에선 위 셀부터 순서대로 실행하면 됨</td></tr>
</table>
<p><b>경고(에러 아님)</b>: <code>input_shape=</code>를 층에 넣음, <code>LeakyReLU(alpha=)</code>, <code>scipy.ndimage.filters</code> → 돌아가지만 새 방식으로 바꾸면 좋음 (아래 카드)</p>
<p><b>NameError가 줄줄이 나오면</b>: 맨 처음 에러 하나 때문에 변수가 안 만들어진 것. <b>첫 번째 에러만 고치면</b> 뒤는 사라짐</p>""")

    _a("[5장] tf.constant(2.0) + t2 → InvalidArgumentError", "float32 float64 자동 형변환 tf.cast InvalidArgumentError AddV2 double float",
"""t2 = tf.constant(40., dtype=tf.float64)
# tf.constant(2.0) + t2                    # 에러
print(tf.constant(2.0) + tf.cast(t2, tf.float32))   # 42.0""",
_card("InvalidArgumentError: cannot compute AddV2 as input #1(zero-based) was expected to be a float tensor but is a double tensor [Op:AddV2]",
      "tf.constant(2.0)은 float32, t2는 float64(double). 텐서플로는 타입을 자동으로 바꿔 주지 않음(속도·의도치 않은 변환 방지)",
      "float32 텐서와 float64 텐서를 더해서 에러가 났다. 텐서플로는 자동 형변환을 하지 않으므로 tf.cast로 t2를 float32로 바꿔서 더했다."))

    _a("[5장] v[1] = [7., 8., 9.] → TypeError", "variable assign 대입 item assignment ResourceVariable TypeError",
"""v = tf.Variable([[1., 2., 3.], [4., 5., 6.]])
# v[1] = [7., 8., 9.]                      # 에러
v[1].assign([7., 8., 9.])
print(v)""",
_card("TypeError: 'ResourceVariable' object does not support item assignment",
      "tf.Variable은 = 부호로 원소에 값을 넣을 수 없음. 값을 바꿀 땐 assign을 써야 함 (교수님 노트북 위 마크다운: \"= 부호로 assign을 할 수 없다\")",
      "tf.Variable의 일부를 = 로 바꾸려고 해서 에러가 났다. 변수 값은 assign()으로 바꿔야 하므로 v[1].assign([7., 8., 9.])로 고쳤다."))

    _a("[5장] 희소 텐서 s6 → InvalidArgumentError, 그 다음 NameError", "sparse 희소 텐서 reorder 정렬 인덱스 to_dense s5 s6 NameError",
"""s5 = tf.SparseTensor(indices=[[0, 2], [0, 1]],
                     values=[1., 2.],
                     dense_shape=[3, 4])
s6 = tf.sparse.to_dense(tf.sparse.reorder(s5))     # 인덱스를 정렬한 뒤 변환
print(s6)""",
_card("indices[1] = [0,1] is out of order. Many sparse ops require sorted indices.\n    Use `tf.sparse.reorder` to create a correctly ordered copy.\n...\nNameError: name 's6' is not defined",
      "인덱스 [0,2] 다음에 [0,1]이 와서 (행, 열) 순서가 정렬되어 있지 않음. try에서 to_dense가 실패해 s6이 만들어지지 않았고, 그래서 마지막 줄 s6에서 NameError",
      "희소 텐서의 인덱스가 순서대로 정렬되어 있지 않아 to_dense에서 에러가 났고, 그 때문에 s6이 만들어지지 않아 NameError도 났다. tf.sparse.reorder로 정렬한 뒤 변환했다."))

    _a("[6장] hi2('이순신', '안중근') → TypeError", "*args 별표 가변 인자 hi hi2 hi3 TypeError positional argument",
"""def hi2(*Names):                 # * 를 붙이면 여러 개를 튜플로 받음
    for name in Names:
        print("%s %s" % (name[0], name[1:3]), end=' ')
    print("\\n")
    print(type(Names), Names)

hi2('이순신', '안중근')
# 또는 * 없이 두고 하나로 묶어서 넘기기: hi2_원래(['이순신', '안중근'])""",
_card("TypeError: hi2() takes 1 positional argument but 2 were given",
      "hi2는 매개변수 앞에 * 가 없어서 인자를 하나만 받는데 두 개를 넘김 (바로 위 hi는 *Names라서 됨, 10/10 \"별표 하나는 뭘 할 것 같아?\")",
      "hi2는 인자를 하나만 받도록 정의됐는데 두 개를 넘겨서 에러가 났다. 매개변수를 *Names로 바꿔 여러 값을 튜플로 받게 했다."))

    _a("[7-2] from keras.layers.core import ... → ModuleNotFoundError", "keras.layers.core ModuleNotFoundError import 경로 keras 3 Dense Dropout Activation Flatten NameError model",
"""from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, MaxPooling2D, Conv2D

input_shape = (28, 28, 1)
model = Sequential()
model.add(keras.layers.Input(shape=input_shape))          # input_shape= 대신 Input 층 (경고 없애기)
model.add(Conv2D(32, kernel_size=(3, 3), padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, kernel_size=(3, 3), padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(10))
model.add(Activation('softmax'))
model.summary()""",
_card("ModuleNotFoundError: No module named 'keras.layers.core'\n(이후 셀) NameError: name 'model' is not defined",
      "예전 Keras는 Dense 등이 keras.layers.core에 있었지만 지금 Keras 3에는 그 경로가 없음. import가 실패해 model이 안 만들어져서 뒤 셀(compile·fit·evaluate·predict)이 전부 NameError",
      "keras.layers.core 모듈이 현재 버전에 없어서 import 에러가 났고, 그래서 model이 정의되지 않아 뒤 셀들도 NameError가 났다. from keras.layers import로 경로를 바꿨다."))

    _a("[7-2] mlp.save('/content/drive/MyDrive/mlp') → ValueError", "save 저장 확장자 .keras h5 ValueError drive mount 드라이브",
"""# Colab에서 드라이브에 저장하려면 먼저 마운트
# from google.colab import drive
# drive.mount('/content/drive')
mlp = keras.Sequential([keras.layers.Input(shape=(784,)), keras.layers.Dense(10, activation="softmax")])
mlp.save('mlp.keras')                               # 확장자 .keras
mlp2 = keras.models.load_model('mlp.keras')
print(mlp2.count_params())""",
_card("ValueError: Invalid filepath extension for saving. Please add either a `.keras` extension for the native Keras format (recommended) or a `.h5` extension.",
      "Keras 3는 저장할 때 파일 이름에 .keras(또는 .h5) 확장자가 꼭 있어야 함. 드라이브 경로를 쓰려면 drive.mount도 먼저 해야 함",
      "모델 저장 경로에 확장자가 없어서 에러가 났다. 현재 Keras는 .keras 확장자가 필요하므로 'mlp.keras'로 저장했다."))

    _a("[7-2] Image.open('/content/digit.png') → FileNotFoundError (+ scipy 경고)", "FileNotFoundError digit.png 파일 업로드 convolve scipy.ndimage.filters deprecated np_img",
"""import numpy as np
from scipy.ndimage import convolve                    # filters 경로는 곧 없어짐
import matplotlib.pyplot as plt
from tensorflow import keras

(X_train, y_train), _ = keras.datasets.mnist.load_data()
np_img = X_train[0].astype(float)                      # digit.png 대신 MNIST 숫자 하나
k1 = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
res = convolve(np_img, k1)
plt.subplot(1, 2, 1); plt.imshow(np_img, cmap='gray')
plt.subplot(1, 2, 2); plt.imshow(res, cmap='gray')
plt.show()""",
_card("FileNotFoundError: [Errno 2] No such file or directory: '/content/digit.png'\n(이후 셀) NameError: name 'np_img' is not defined",
      "digit.png 파일을 Colab에 올리지 않아서 이미지를 못 읽음 → np_img가 안 만들어져 아래 합성곱·풀링 셀이 NameError. 그리고 scipy.ndimage.filters는 곧 없어질 경로라 경고",
      "digit.png 파일이 없어서 에러가 났다. 파일을 업로드하거나, MNIST 이미지 하나를 np_img로 써서 필터를 적용했다."))

    _a("경고(에러는 아님): input_shape · LeakyReLU(alpha) · predict_classes · np_utils", "경고 warning UserWarning input_shape alpha negative_slope predict_classes np_utils to_categorical deprecated",
"""model = keras.Sequential([
    keras.layers.Input(shape=(28, 28)),                 # Flatten(input_shape=[28, 28]) 대신
    keras.layers.Flatten(),
    keras.layers.Dense(100, kernel_initializer="he_normal"),
    keras.layers.LeakyReLU(negative_slope=0.2),         # LeakyReLU(alpha=0.2) 대신
    keras.layers.Dense(10, activation="softmax")])
X_new = np.zeros((3, 28, 28), dtype="float32")
y_pred = np.argmax(model.predict(X_new, verbose=0), axis=-1)   # predict_classes 대신
y_onehot = keras.utils.to_categorical([3, 1, 4], 10)           # np_utils.to_categorical 대신
print(y_pred, y_onehot.shape)""",
html="""<table>
<tr><th>옛 코드 (교수님 노트북)</th><th>나오는 것</th><th>새 방식</th></tr>
<tr><td><code>Flatten(input_shape=[28, 28])</code>, <code>Dense(30, input_shape=[8])</code></td><td>UserWarning (실행은 됨)</td><td>맨 앞에 <code>keras.layers.Input(shape=...)</code></td></tr>
<tr><td><code>LeakyReLU(alpha=0.2)</code> (4장)</td><td>UserWarning: alpha is deprecated</td><td><code>LeakyReLU(negative_slope=0.2)</code></td></tr>
<tr><td><code>model.predict_classes(X_new)</code> (2장, 주석 처리됨)</td><td>AttributeError (없어진 함수)</td><td><code>np.argmax(model.predict(X_new), axis=-1)</code></td></tr>
<tr><td><code>from keras.utils import np_utils</code> (7-2, 주석 처리됨)</td><td>ImportError</td><td><code>from keras.utils import to_categorical</code></td></tr>
<tr><td><code>from scipy.ndimage.filters import convolve</code> (7-2)</td><td>DeprecationWarning</td><td><code>from scipy.ndimage import convolve</code></td></tr>
</table>
<p>경고는 빨간 글씨여도 실행은 끝난 것. 시험에서 "에러를 고쳐라"면 진짜 에러(Traceback이 있고 셀이 멈춘 것)부터</p>""")

    _a("Colab 전용 셀 (내 PC 주피터에서만 나는 에러)", "google.colab eval_js 그림 그리기 draw canvas torchvision drawing.png colab 전용 로컬",
html="""<ul>
<li><b>3·4장·Optimizer·7-2의 숫자 그리기</b>: <code>from google.colab.output import eval_js</code> → Colab에서만 됨. 내 PC 주피터에선 <code>ModuleNotFoundError: No module named 'google.colab'</code>, 이어서 <code>draw</code>·<code>digit</code> NameError</li>
<li><b>데이터 증강 셀</b>: <code>from torchvision import transforms</code> → Colab엔 설치돼 있음. 로컬이면 <code>pip install torchvision</code></li>
<li><b>drawing.png</b>: 그리기 셀을 먼저 실행해야 파일이 생김</li>
<li>시험은 교수님이 주는 Colab에서 보므로 이 셀들은 <b>위에서부터 순서대로 실행</b>하면 됨. 중간 셀부터 돌리면 위에서 만든 변수가 없어서 NameError</li>
</ul>""")
