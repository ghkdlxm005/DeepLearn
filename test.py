import re, sys, matplotlib; matplotlib.use("Agg")
sys.path.insert(0,'.')
from snippets import S
ns={}
order=["start","data","model","compile","train","pandas","numpy"]
fails=0
for sec in order:
    for s in S:
        if s["sec"]!=sec or not s["code"]: continue
        code=s["code"]
        if code.startswith("# Anaconda"): continue
        code=re.sub(r"epochs=\d+","epochs=1",code)
        if "fetch_california" in code: 
            try: exec(code,ns)
            except Exception as e: print("SKIP(net?)",s["title"],type(e).__name__,str(e)[:80]); continue
            ns["X_train_cal"]=ns["X_train"]; 
            # restore mnist after
            exec('''(X_train_full, y_train_full), (X_test, y_test) = keras.datasets.mnist.load_data()
X_train_full = X_train_full / 255.0; X_test = X_test / 255.0
X_train, X_valid = X_train_full[:-5000], X_train_full[-5000:]
y_train, y_valid = y_train_full[:-5000], y_train_full[-5000:]''',ns); continue
        try:
            exec(code,ns); print("OK ",s["title"])
        except Exception as e:
            fails+=1; print("FAIL",s["title"],type(e).__name__,str(e)[:200])
print("fails",fails)
