# 실험 재현용: "바꾸면 이렇게 된다" 결과(results.json)를 만드는 스크립트. python run_experiments.py (CPU 약 30분)
import json, time, os, sys
os.environ["TF_CPP_MIN_LOG_LEVEL"]="3"
import numpy as np, tensorflow as tf
from tensorflow import keras
(Xf, yf), (Xt, yt) = keras.datasets.fashion_mnist.load_data()
RAW = (Xf, Xt)
Xv, Xtr = Xf[:5000]/255., Xf[5000:]/255.; yv, ytr = yf[:5000], yf[5000:]; Xte = Xt/255.
def build(units=(300,100), act="relu", init="glorot_uniform", bn=False, drop=0.0, l2=None, leaky=False):
    L=[keras.layers.Input(shape=(28,28)), keras.layers.Flatten()]
    for u in units:
        kw=dict(kernel_initializer=init)
        if l2: kw["kernel_regularizer"]=keras.regularizers.l2(l2)
        if leaky: L += [keras.layers.Dense(u, **kw), keras.layers.LeakyReLU(negative_slope=0.2)]
        else: L.append(keras.layers.Dense(u, activation=act, **kw))
        if bn: L.append(keras.layers.BatchNormalization())
        if drop: L.append(keras.layers.Dropout(drop))
    L.append(keras.layers.Dense(10, activation="softmax"))
    return keras.Sequential(L)
def opt(name, lr=None):
    if name=="sgd": return keras.optimizers.SGD(learning_rate=lr or 0.01)
    if name=="momentum": return keras.optimizers.SGD(learning_rate=lr or 0.01, momentum=0.9)
    if name=="nag": return keras.optimizers.SGD(learning_rate=lr or 0.01, momentum=0.9, nesterov=True)
    if name=="adam": return keras.optimizers.Adam(learning_rate=lr or 0.001)
    if name=="rmsprop": return keras.optimizers.RMSprop(learning_rate=lr or 0.001)
    if name=="adagrad": return keras.optimizers.Adagrad(learning_rate=lr or 0.01)
    if name=="nadam": return keras.optimizers.Nadam(learning_rate=lr or 0.001)
EXPS = [
 ("base", {}, {}),
 ("epochs5", {}, {"epochs":5}), ("epochs20", {}, {"epochs":20}),
 ("bs128", {}, {"bs":128}), ("bs1024", {}, {"bs":1024}),
 ("lr0.001", {}, {"lr":0.001}), ("lr0.1", {}, {"lr":0.1}), ("lr1.0", {}, {"lr":1.0}),
 ("units30_10", {"units":(30,10)}, {}), ("units1000_500", {"units":(1000,500)}, {}),
 ("sigmoid", {"act":"sigmoid"}, {}), ("tanh", {"act":"tanh"}, {}), ("elu", {"act":"elu"}, {}),
 ("selu", {"act":"selu","init":"lecun_normal"}, {}), ("leaky", {"leaky":True}, {}),
 ("he", {"init":"he_normal"}, {}),
 ("bigrandom", {"init":keras.initializers.RandomNormal(stddev=1.0)}, {}),
 ("bn", {"bn":True}, {}), ("drop0.2", {"drop":0.2}, {}), ("drop0.5", {"drop":0.5}, {}),
 ("l2", {"l2":0.01}, {}),
 ("momentum", {}, {"opt":"momentum"}), ("nag", {}, {"opt":"nag"}), ("adam", {}, {"opt":"adam"}),
 ("rmsprop", {}, {"opt":"rmsprop"}), ("adagrad", {}, {"opt":"adagrad"}), ("nadam", {}, {"opt":"nadam"}),
 ("nonorm", {}, {"nonorm":True}),
 ("sigmoid_sgd_vs", {"act":"sigmoid","init":"glorot_uniform"}, {"opt":"adam"}),
]
out = json.load(open("results.json")) if os.path.exists("results.json") else {}
for name, mk, tk in EXPS:
    if name in out: continue
    np.random.seed(42); tf.random.set_seed(42); keras.backend.clear_session()
    m = build(**mk)
    m.compile(loss="sparse_categorical_crossentropy", optimizer=opt(tk.get("opt","sgd"), tk.get("lr")), metrics=["accuracy"])
    a,b,c = (Xtr,Xv,Xte)
    if tk.get("nonorm"): a,b,c = Xf[5000:].astype("float32"), Xf[:5000].astype("float32"), Xt.astype("float32")
    t=time.time()
    h = m.fit(a, ytr, epochs=tk.get("epochs",10), batch_size=tk.get("bs",32), validation_data=(b,yv), verbose=0)
    el=time.time()-t
    tl, ta = m.evaluate(c, yt, verbose=0)
    H={k:[float(x) for x in v] for k,v in h.history.items()}
    out[name]=dict(test_acc=float(ta), test_loss=float(tl), time=el, params=int(m.count_params()), hist=H)
    json.dump(out, open("results.json","w"))
    print(name, round(ta,4), "train", round(H["accuracy"][-1],4), "val", round(H["val_accuracy"][-1],4), "loss", round(H["loss"][-1],4), f"{el:.0f}s", flush=True)
print("DONE")
