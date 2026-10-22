@echo off
chcp 65001 > nul
REM 딥러닝 시험용 가상환경(dl) 만들기 - Anaconda Prompt에서 실행
REM 사용법: Anaconda Prompt를 열고 이 파일이 있는 폴더로 이동한 뒤  setup_dl_env.bat  입력
call conda create -n dl python=3.11 -y
if errorlevel 1 goto fail
call conda activate dl
python -m pip install --upgrade pip
pip install tensorflow pandas matplotlib scikit-learn scipy seaborn scikit-image pillow notebook ipykernel
if errorlevel 1 goto fail
python -m ipykernel install --user --name dl --display-name "Python (dl)"
python -c "import tensorflow as tf, pandas, sklearn, scipy, skimage, seaborn; print(\"OK  tensorflow\", tf.__version__)"
echo.
echo 완료: Jupyter에서 커널을 "Python (dl)"로 선택하세요.  실행: conda activate dl  후  jupyter notebook
goto end
:fail
echo 설치 중 오류가 났습니다. 위 메시지를 확인하세요.
:end
pause
