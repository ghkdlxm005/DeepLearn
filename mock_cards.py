# 모의 중간고사 답안 노트북 → 문항별 카드 (sec="mock")
import os, re, nbformat
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "nb_src", "모의중간고사_답안.ipynb")

def items():
    if not os.path.exists(SRC): return []
    nb = nbformat.read(SRC, 4)
    qs, cur = [], None
    for c in nb.cells:
        src = c.source.strip()
        if c.cell_type == "markdown" and re.match(r"^# \d+\.", src):
            rest = "\n".join(src.splitlines()[1:]).strip()
            cur = dict(title=src.splitlines()[0][2:].strip(), q=[rest] if rest else [], code=[], pre=[], out=[])
            qs.append(cur); continue
        if cur is None: continue
        if c.cell_type == "markdown":
            if src.startswith("<pre>"):
                cur["pre"].append(src.replace("<pre>", "").replace("</pre>", "").strip())
            elif not src.startswith("**주의**") and not src.startswith("---"):
                cur["q"].append(src)
        else:
            cur["code"].append(src)
            for o in c.outputs:
                t = o.get("text", "") if o.output_type == "stream" else o.get("data", {}).get("text/plain", "")
                if t and len(t) < 1500 and "Epoch" not in t: cur["out"].append(t.strip())
    import html as H
    out = []
    for q in qs:
        qhtml = "".join(f"<p>{H.escape(x).replace(chr(10), '<br>')}</p>" for x in q["q"])
        ans = "".join(f'<pre style="white-space:pre-wrap">{H.escape(p)}</pre>' for p in q["pre"])
        body = (f'<div><b>문제</b>{qhtml}</div>' if qhtml else '') + (f'<div><b>답안</b>{ans}</div>' if ans else "")
        body += '<p class="note"><a href="nb/mock.html" target="_blank" rel="noopener">실행 결과 포함 답안 노트북 열기 →</a></p>'
        out.append(dict(sec="mock", title="모의 " + q["title"], kw="모의고사 모의시험 중간고사 답안 정답 문제 " + q["title"],
                        code="\n\n".join(q["code"]), note="", html=body,
                        out="\n\n".join(q["out"][-3:]), extra=""))
    intro = dict(sec="mock", title="모의 중간고사 (작년 같은 교수님 형식)", kw="모의고사 모의시험 중간고사 문제 답안 다운로드 colab",
        code="", note="", out="", extra="",
        html=('<p>작년 같은 교수님 시험(받은 Colab 노트북 작성 → .ipynb 제출) 형식으로 만든 1~7장 연습 문제 7개. '
              '이론 서술(<code>&lt;pre&gt;</code> 칸) + Pandas + 단계형 실습.</p>'
              '<p><a href="nb_src/%EB%AA%A8%EC%9D%98%EC%A4%91%EA%B0%84%EA%B3%A0%EC%82%AC_%EB%AC%B8%EC%A0%9C.ipynb" download><b>문제 노트북(.ipynb) 받기</b></a> → Colab에서 파일 → 노트 업로드 · '
              '<a href="nb/mock_q.html" target="_blank" rel="noopener">문제 미리보기</a> · '
              '<a href="nb/mock.html" target="_blank" rel="noopener">답안 노트북(실행 결과 포함)</a></p>'))
    return [intro] + out
