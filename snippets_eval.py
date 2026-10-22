# 하이퍼파라미터 탐색 · 평가 지표 (작년 같은 교수님 시험: GridSearchCV → 최적 재학습 → ROC/AUC 비교 형식의 딥러닝 버전)

SECTIONS_EVAL = [("tune", "튜닝·평가")]

def register(add):
    add("tune", "탐색용 데이터 준비 (빠르게 하려고 일부만)", "하이퍼파라미터 튜닝 준비 데이터 일부 subset fashion",
"""(X_train_full, y_train_full), (X_test, y_test) = keras.datasets.fashion_mnist.load_data()
X_train_full, X_test = X_train_full / 255., X_test / 255.
X_train, X_valid = X_train_full[:-5000], X_train_full[-5000:]
y_train, y_valid = y_train_full[:-5000], y_train_full[-5000:]
class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
# 탐색은 오래 걸리니 시험에서는 일부만 써도 됨
X_small, y_small = X_train[:10000], y_train[:10000]""")

    add("tune", "그리드 탐색 직접 구현 (for 반복 → 결과 표 → 최적 선택)", "grid search 그리드 탐색 하이퍼파라미터 최적 조합 itertools 반복 결과 표 best",
"""import itertools

def build_model(n_hidden=1, n_neurons=100, learning_rate=1e-3):
    model = keras.Sequential([keras.layers.Input(shape=(28, 28)), keras.layers.Flatten()])
    for _ in range(n_hidden):
        model.add(keras.layers.Dense(n_neurons, activation="relu", kernel_initializer="he_normal"))
    model.add(keras.layers.Dense(10, activation="softmax"))
    model.compile(loss="sparse_categorical_crossentropy",
                  optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
                  metrics=["accuracy"])
    return model

param_grid = {"n_hidden": [1, 2], "n_neurons": [100, 300], "learning_rate": [1e-3, 1e-2]}

rows = []
for n_hidden, n_neurons, lr in itertools.product(*param_grid.values()):    # 2 x 2 x 2 = 8가지
    keras.backend.clear_session()
    m = build_model(n_hidden, n_neurons, lr)
    h = m.fit(X_small, y_small, epochs=3, validation_data=(X_valid, y_valid), verbose=0)
    rows.append({"n_hidden": n_hidden, "n_neurons": n_neurons, "learning_rate": lr,
                 "val_accuracy": max(h.history["val_accuracy"])})

scores_df = pd.DataFrame(rows).sort_values("val_accuracy", ascending=False)
scores_df["rank"] = range(1, len(scores_df) + 1)
print(scores_df)
best = scores_df.iloc[0]
print("최적 조합:", best.to_dict())""",
"GridSearchCV처럼 모든 조합을 돌려 검증 정확도로 순위를 매김. 테스트 세트는 고를 때 쓰지 않고 마지막에 한 번만.")

    add("tune", "최적 하이퍼파라미터로 다시 학습", "최적 파라미터 재학습 best refit 다시 학습 조기종료",
"""best_model = build_model(int(best["n_hidden"]), int(best["n_neurons"]), float(best["learning_rate"]))
early_cb = keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)
best_model.fit(X_train, y_train, epochs=20, validation_data=(X_valid, y_valid),
               callbacks=[early_cb], verbose=2)
print("테스트 정확도:", best_model.evaluate(X_test, y_test, verbose=0)[1])""",
"작년 시험의 'GridSearchCV로 구한 최적 조합으로 DecisionTree 생성하여 학습'과 같은 단계. 탐색은 일부 데이터·짧은 epoch, 재학습은 전체 데이터.")

    add("tune", "Keras Tuner (RandomSearch)", "keras tuner kerastuner 랜덤 탐색 random search hp.Int hp.Float 자동 튜닝",
"""# Colab: !pip install -q keras-tuner
import keras_tuner as kt

def build_hp(hp):
    model = keras.Sequential([keras.layers.Input(shape=(28, 28)), keras.layers.Flatten()])
    for _ in range(hp.Int("n_hidden", 1, 3)):
        model.add(keras.layers.Dense(hp.Int("n_neurons", 50, 300, step=50), activation="relu"))
    model.add(keras.layers.Dense(10, activation="softmax"))
    lr = hp.Float("learning_rate", 1e-4, 1e-2, sampling="log")
    model.compile(loss="sparse_categorical_crossentropy",
                  optimizer=keras.optimizers.Adam(learning_rate=lr), metrics=["accuracy"])
    return model

tuner = kt.RandomSearch(build_hp, objective="val_accuracy", max_trials=5,
                        overwrite=True, directory="kt_dir", project_name="fmnist")
tuner.search(X_small, y_small, epochs=3, validation_data=(X_valid, y_valid), verbose=0)
best_hp = tuner.get_best_hyperparameters()[0]
print(best_hp.values)
tuned = tuner.hypermodel.build(best_hp)      # 최적 값으로 새 모델""",
"RandomSearch: 정해진 범위에서 랜덤하게 max_trials개만 시도 → 조합이 많을 때 그리드보다 빠름. 로컬에서는 tensorboard도 필요(Colab엔 있음).")

    add("tune", "scikit-learn GridSearchCV로 케라스 모델 탐색 (scikeras)", "gridsearchcv scikeras KerasClassifier sklearn 교차검증 cv cv_results_",
"""# Colab: !pip install -q scikeras
from scikeras.wrappers import KerasClassifier
from sklearn.model_selection import GridSearchCV

def make_clf(n_neurons=100):
    model = keras.Sequential([keras.layers.Input(shape=(28, 28)), keras.layers.Flatten(),
                              keras.layers.Dense(n_neurons, activation="relu"),
                              keras.layers.Dense(10, activation="softmax")])
    model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model

clf = KerasClassifier(model=make_clf, epochs=2, verbose=0)
grid = GridSearchCV(clf, param_grid={"model__n_neurons": [50, 100]}, cv=3, refit=True)
grid.fit(X_small[:3000], y_small[:3000])
print(grid.best_params_, grid.best_score_)
scores = pd.DataFrame(grid.cv_results_)[["params", "mean_test_score", "rank_test_score"]]
print(scores)""",
"작년 시험과 같은 GridSearchCV를 그대로 쓰는 방법. 모델 함수 인자는 model__이름 으로 넘김. 교차검증이라 시간이 오래 걸리니 데이터를 줄일 것.")

    add("tune", "혼동 행렬 · 정밀도 · 재현율 · F1 (classification_report)", "confusion matrix 혼동행렬 오차행렬 precision recall f1 정밀도 재현율 classification_report 평가 지표",
"""from sklearn.metrics import (confusion_matrix, ConfusionMatrixDisplay, classification_report,
                             accuracy_score, precision_score, recall_score, f1_score)
model = best_model                                          # 평가할 모델
y_pred = np.argmax(model.predict(X_test, verbose=0), axis=-1)

print(confusion_matrix(y_test, y_pred))                     # 행: 실제, 열: 예측
ConfusionMatrixDisplay.from_predictions(y_test, y_pred, display_labels=class_names, xticks_rotation=90)
plt.show()
print(classification_report(y_test, y_pred, target_names=class_names, digits=3))
print("accuracy", accuracy_score(y_test, y_pred))
print("precision(macro)", precision_score(y_test, y_pred, average="macro"))
print("recall(macro)", recall_score(y_test, y_pred, average="macro"))
print("F1(macro)", f1_score(y_test, y_pred, average="macro"))""",
"다중 분류는 average='macro'(클래스별 평균) 또는 'weighted'(개수 가중) 지정 필요.")

    add("tune", "ROC 곡선 · AUC (모델 여러 개 비교)", "roc auc curve roc_curve roc_auc_score fpr tpr 비교 이진 분류 one vs rest",
"""from sklearn.metrics import roc_curve, roc_auc_score

def plotROC(fprs, tprs, label):                 # 작년 시험에서 준 함수 형태
    plt.plot(fprs, tprs, label=label)

target = class_names.index("Shirt")             # 한 클래스를 양성(1)으로 보는 이진 문제로 바꿈
y_true_bin = (y_test == target).astype(int)

models = {"best_model": best_model, "tuned": tuned}    # 비교할 모델들 (tuned는 fit 후 사용)
tuned.fit(X_small, y_small, epochs=3, verbose=0)
aucs = {}
for name, m in models.items():
    proba = m.predict(X_test, verbose=0)[:, target]      # 양성 클래스일 확률
    fprs, tprs, thresholds = roc_curve(y_true_bin, proba)
    plotROC(fprs, tprs, name)
    aucs[name] = roc_auc_score(y_true_bin, proba)
plt.plot([0, 1], [0, 1], "k--", label="Random")
plt.xlabel("FPR (1 - Specificity)"); plt.ylabel("TPR (Recall)"); plt.legend(); plt.show()
print(sorted(aucs.items(), key=lambda x: x[1], reverse=True))   # AUC 좋은 순서

# 10개 클래스 전체 AUC (one-vs-rest 평균)
print(roc_auc_score(y_test, best_model.predict(X_test, verbose=0), multi_class="ovr"))""",
"ROC는 이진 분류 기준이라 클래스 하나를 양성으로 정해서 그림. AUC가 1에 가까울수록 좋고 0.5는 랜덤.")

    add("tune", "틀린 예측 이미지 보기", "틀린 오분류 misclassified 예측 틀린 이미지 시각화 확인",
"""wrong = np.where(y_pred != y_test)[0]
print("틀린 개수:", len(wrong))
plt.figure(figsize=(12, 3))
for i, idx in enumerate(wrong[:8]):
    plt.subplot(1, 8, i + 1)
    plt.imshow(X_test[idx], cmap="binary"); plt.axis("off")
    plt.title(f"{class_names[y_pred[idx]]}\\n(true {class_names[y_test[idx]]})", fontsize=8)
plt.show()""")

    add("tune", "모델 구조 그림 (plot_model)", "plot_model 모델 구조 그림 시각화 graphviz show_shapes",
"""keras.utils.plot_model(best_model, "model.png", show_shapes=True)   # Colab: 그림이 바로 표시됨
# 그림이 안 되면 (pydot/graphviz 없음): best_model.summary() 로 대신""")
