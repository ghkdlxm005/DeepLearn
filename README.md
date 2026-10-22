# DL Notes

딥러닝(TensorFlow/Keras) 수업용 코드 예제 모음. 사이트 안 검색창으로 예제를 찾아 복사해 쓰는 용도.

## 파일

| 파일 | 역할 |
|---|---|
| `snippets.py` | 내용 원본 (제목, 검색 키워드, 코드, 설명) |
| `template.html` | 화면 틀 (검색, 분류 버튼, 복사 버튼) |
| `build.py` | `snippets.py` + `template.html` → `index.html` 생성 |
| `test.py` | `snippets.py`의 코드를 실제로 실행해 오류 확인 |
| `index.html` | 게시되는 페이지 (직접 수정하지 않음) |

## 내용 추가·수정 절차

1. `snippets.py`에 `add(분류, 제목, 키워드, 코드, 설명)` 추가 또는 수정
   - 키워드에는 검색할 때 칠 만한 다른 표현(한글·영문·줄임말)을 넣는다
2. `python test.py` → 마지막 줄이 `fails 0`인지 확인 (TensorFlow, pandas 필요. `Salary2024.csv`가 같은 폴더에 있어야 함)
3. `python build.py` → `index.html` 다시 생성
4. 커밋·푸시하면 1~2분 뒤 GitHub Pages에 반영

## 검색 규칙

- 띄어쓰기·가운뎃점·하이픈 무시 (`배치정규화` = `배치 정규화`)
- 여러 단어를 치면 모두 포함된 항목만 표시
- `/` 키로 검색창 이동, `Esc`로 지우기
- 주소 끝에 `#q=검색어`를 붙이면 그 검색어로 열림
