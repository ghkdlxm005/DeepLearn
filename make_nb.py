# nb_src/*.ipynb → nb/*.html (교수님 노트북을 사이트 안에서 보기)
import os, re, nbformat
from nbconvert import HTMLExporter
SRC = {"ch2": "2. 케라스를 사용한 인공 신경망 소개.ipynb",
       "ch3": "3. 필기숫자 인식.ipynb",
       "ch4": "4. 신경망 요소.ipynb",
       "opt": "4. 신경망요소-Optimizer.ipynb",
       "ch5": "5.사용자_정의_모델.ipynb",
       "ch6": "6. 사용자 정의 모델 2.ipynb",
       "ch7a": "7-1. 합성곱 신경망을 사용한 컴퓨터 비전.ipynb",
       "ch7b": "7-2. 합성곱 신경망-숫자.ipynb",
       "mock": "모의중간고사_답안.ipynb", "mock_q": "모의중간고사_문제.ipynb"}
os.makedirs("nb", exist_ok=True)
ex = HTMLExporter(template_name="lab")
ex.exclude_input_prompt = True; ex.exclude_output_prompt = True
for key, fn in SRC.items():
    p = os.path.join("nb_src", fn)
    if not os.path.exists(p): print("없음:", fn); continue
    nb = nbformat.read(p, 4)
    body, _ = ex.from_notebook_node(nb)
    bar = ('<div style="position:sticky;top:0;z-index:9;background:#0b6670;color:#fff;padding:8px 16px;font:14px sans-serif">'
           f'<a href="../index.html" style="color:#fff;text-decoration:none">← DL Notes</a> &nbsp;·&nbsp; 교수님 노트북: {fn}</div>')
    body = re.sub(r"(<body[^>]*>)", r"\1" + bar, body, count=1)
    body = body.replace("</head>", "<style>html{scroll-padding-top:56px}</style></head>", 1)
    open(f"nb/{key}.html", "w", encoding="utf-8").write(body)
    print("ok", key, len(body))
