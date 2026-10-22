# DL Notes

딥러닝(TensorFlow/Keras) 수업용 코드 예제 모음. 사이트 안 검색창으로 예제를 찾아 복사해 쓰는 용도.

## 파일

| 파일 | 역할 |
|---|---|
| `snippets.py` | 내용 원본 (제목, 검색 키워드, 코드, 설명) — 2·3·4장 범위 |
| `snippets_tf.py` | 5·6장(텐서플로 저수준·사용자 정의), 7장(CNN) 예제 |
| `snippets_eval.py` | 하이퍼파라미터 탐색(그리드·Keras Tuner·GridSearchCV), 혼동 행렬·F1·ROC/AUC |
| `mock_cards.py` | 모의시험 답안 노트북 → 문항별 카드 |
| `concepts.py` | 개념 사전 (뜻·비유·코드 위치·바꾸면) + 개념별 예제·노트북·실험 연결(`LINK`) |
| `experiments.py` | "바꾸면 이렇게 된다" 실험 그룹 정의와 결과 해석(`EXPL`) |
| `results.json` | 실험 결과 (Fashion MNIST, 기준 모델에서 하나씩 바꿔 10 epoch) |
| `run_experiments.py` | `results.json`을 다시 만드는 실험 스크립트 (CPU 약 30분) |
| `results_cnn.json`, `run_experiments_cnn.py` | CNN 실험 결과와 스크립트 (교수님 7-1 구조 기준, 5 epoch) |
| `nb_src/` | 교수님 노트북 원본 (.ipynb) |
| `nb/` | `make_nb.py`가 만든 노트북 웹페이지 |
| `pandas_out.json` | Pandas 예제 실제 출력 (Salary2024.csv) |
| `make_nb.py` | `nb_src/*.ipynb` → `nb/*.html` (교수님 노트북 보기용) |
| `template.html` | 화면 틀 (검색, 분류 버튼, 복사 버튼) |
| `build.py` | `snippets.py` + `template.html` → `index.html` 생성 |
| `test.py` | `snippets.py`의 코드를 실제로 실행해 오류 확인 |
| `index.html` | 게시되는 페이지 (직접 수정하지 않음) |

## 내용 추가·수정 절차

1. `snippets.py`에 `add(분류, 제목, 키워드, 코드, 설명)` 추가 또는 수정
   - 키워드에는 검색할 때 칠 만한 다른 표현(한글·영문·줄임말)을 넣는다
2. `python test.py` → 마지막 줄이 `fails 0`인지 확인 (TensorFlow, pandas 필요. `Salary2024.csv`가 같은 폴더에 있어야 함)
   - `snippets_tf.py`를 고쳤으면 그 예제들도 같은 방식으로 실행 확인
3. (노트북을 바꿨으면) `python make_nb.py` → `nb/*.html` 다시 생성
4. `python build.py` → `index.html` 다시 생성 (노트북 링크 위치도 이때 다시 찾음)
5. 커밋·푸시하면 1~2분 뒤 GitHub Pages에 반영

## 검색 규칙

- 띄어쓰기·가운뎃점·하이픈 무시 (`배치정규화` = `배치 정규화`)
- 여러 단어를 치면 모두 포함된 항목만 표시
- `/` 키로 검색창 이동, `Esc`로 지우기
- 주소 끝에 `#q=검색어`를 붙이면 그 검색어로 열림
