# 시험 준비 키트

시험 볼 컴퓨터(노트북·PC)마다 한 번씩 해 두기.

## 1. 가상환경 만들기 (처음 한 번, 10분 정도)
1. 시작 메뉴 → **Anaconda Prompt** 실행
2. 이 폴더로 이동: `cd /d "E:\user\개인 프로젝트\DeepLearn\exam_kit"` (컴퓨터마다 경로 맞게)
3. `setup_dl_env.bat` 입력 → 마지막에 `OK  tensorflow 2.x` 가 나오면 성공
   - Python 3.11 가상환경 `dl`에 tensorflow, pandas, scikit-learn, scipy, seaborn, scikit-image, jupyter 설치
   - 주피터 커널 이름: **Python (dl)**

## 2. 점검 (시험 전날)
1. Anaconda Prompt → `conda activate dl` → `jupyter notebook`
2. `00_환경점검.ipynb` 열기 → 커널 **Python (dl)** 선택 → Kernel → Restart & Run All
3. 모두 ✅이면 끝. 데이터셋(MNIST, Fashion MNIST, 캘리포니아 주택)도 이때 미리 받아짐
4. 마지막 셀에 이 컴퓨터의 학습 속도(10 epoch 몇 분)가 나옴 → 시험 때 epoch 정할 때 참고

## 3. 시험 당일
1. `01_시험시작_템플릿.ipynb`를 복사해서 시험용 파일 이름으로 바꿔 시작
2. 문제 사양대로 고치고, 사이트(https://ghkdlxm005.github.io/DeepLearn/)에서 검색
3. 제출하면 시험 종료 → 제출 전 템플릿 맨 아래 체크리스트 확인

## 이미 가상환경이 있으면
`conda activate 환경이름` 후 `pip install tensorflow pandas matplotlib scikit-learn scipy seaborn scikit-image pillow notebook ipykernel`
→ `python -m ipykernel install --user --name 환경이름`
