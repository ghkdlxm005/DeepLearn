# CNN "바꾸면" 실험: 교수님 7-1 노트북 구조(Conv32-Pool-Conv64-Pool-Dense128-Dropout0.2, nadam)를 기준으로 하나씩 변경
import json, time, os
os.environ["TF_CPP_MIN_LOG_LEVEL"]="3"
import numpy as np, tensorflow as tf
from tensorflow import keras
L=keras.layers
(Xf, yf), (Xt, yt) = keras.datasets.fashion_mnist.load_data()
Xtr, Xv = Xf[:-5000], Xf[-5000:]; ytr, yv = yf[:-5000], yf[-5000:]
m_, s_ = Xtr.mean(axis=0, keepdims=True), Xtr.std(axis=0, keepdims=True)+1e-7
Xtr, Xv, Xte = [((x-m_)/s_)[..., np.newaxis].astype("float32") for x in (Xtr, Xv, Xt)]
def cnn(f=(32,64), k=3, act=None, pool=True, pad="same", stride=1, dense=128, drop=0.2):
    ly=[L.Input(shape=(28,28,1))]
    for n in f:
        ly.append(L.Conv2D(n, kernel_size=k, padding=pad, strides=stride, activation=act))
        if pool: ly.append(L.MaxPooling2D(pool_size=2))
    ly += [L.Flatten(), L.Dense(dense, activation="relu"), L.Dropout(drop), L.Dense(10, activation="softmax")]
    return keras.Sequential(ly)
def fcn():
    return keras.Sequential([L.Input(shape=(28,28,1)), L.Flatten(), L.Dense(200, activation="relu"), L.Dense(100, activation="relu"), L.Dense(10, activation="softmax")])
EXPS=[("cnn_base", lambda: cnn()), ("fcn", fcn), ("cnn_relu", lambda: cnn(act="relu")),
      ("cnn_nopool", lambda: cnn(pool=False)), ("cnn_small", lambda: cnn(f=(8,16))), ("cnn_big", lambda: cnn(f=(64,128))),
      ("cnn_k5", lambda: cnn(k=5)), ("cnn_valid", lambda: cnn(pad="valid")), ("cnn_stride2", lambda: cnn(pool=False, stride=2))]
out=json.load(open("results_cnn.json")) if os.path.exists("results_cnn.json") else {}
for name, mk in EXPS:
    if name in out: continue
    np.random.seed(42); tf.random.set_seed(42); keras.backend.clear_session()
    m=mk(); m.compile(loss="sparse_categorical_crossentropy", optimizer="nadam", metrics=["accuracy"])
    t=time.time(); h=m.fit(Xtr, ytr, epochs=5, validation_data=(Xv,yv), verbose=0); el=time.time()-t
    tl, ta = m.evaluate(Xte, yt, verbose=0)
    out[name]=dict(test_acc=float(ta), test_loss=float(tl), time=el, params=int(m.count_params()), hist={k:[float(x) for x in v] for k,v in h.history.items()})
    json.dump(out, open("results_cnn.json","w"))
    print(name, round(ta,4), "params", m.count_params(), f"{el:.0f}s", flush=True)
print("DONE")
