# 실제 과제(Week3 Pandas, Week4 심층신경망, 6주차 사용자 정의 모델) 형식 정리와 변형 연습
# Week4 변형 10문제는 snippets_practice.py

PANDAS = [
 [
  "1. experience_level(경력)별로 몇 명의 데이터가 있는지 확인하시오.",
  "df['experience_level'].value_counts()",
  "experience_level\nSenior-level       4105\nMid-level          1675\nEntry-level         565\nExecutive-level     254\nName: count, dtype: int64"
 ],
 [
  "2. 2024년 데이터만 골라 job_title별 평균 salary_in_usd 상위 5개를 구하시오.",
  "df_2024 = df[df['work_year'] == 2024]\ndf_2024.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False).head(5)",
  "job_title\nMachine Learning Scientist        282916.666667\nManaging Director Data Science    260000.000000\nAI Architect                      229662.500000\nResearch Engineer                 227896.782609\nApplied Scientist                 222618.875000\nName: salary_in_usd, dtype: float64"
 ],
 [
  "3. company_size별 salary_in_usd 평균을 높은 순으로 정렬하시오.",
  "df.groupby('company_size')['salary_in_usd'].mean().sort_values(ascending=False)",
  "company_size\nMedium    149659.386689\nLarge     120638.404218\nSmall      87687.458824\nName: salary_in_usd, dtype: float64"
 ],
 [
  "4. work_models별 salary_in_usd의 최소, 최대, 평균, 인원수를 구하시오.",
  "df.groupby('work_models')['salary_in_usd'].agg(['min', 'max', 'mean', 'count'])",
  "               min     max           mean  count\nwork_models                                     \nHybrid       15680  423000   83293.502222    225\nOn-site      15000  750000  152600.100970   3813\nRemote       15000  700000  140550.137837   2561"
 ],
 [
  "5. Data Scientist만 골라 experience_level별 평균 salary_in_usd를 구하시오.",
  "ds = df[df['job_title'] == 'Data Scientist']\nds.groupby('experience_level')['salary_in_usd'].mean().round(1)",
  "experience_level\nEntry-level         83387.1\nExecutive-level    189050.5\nMid-level          115501.1\nSenior-level       169793.4\nName: salary_in_usd, dtype: float64"
 ],
 [
  "6. employee_residence가 United States가 아닌 데이터는 몇 개이고 전체의 몇 %인지 구하시오.",
  "not_us = df[df['employee_residence'] != 'United States']\nprint(len(not_us), round(len(not_us) / len(df) * 100, 2), '%')",
  "1294 19.61 %"
 ],
 [
  "7. 연도(work_year)별·경력(experience_level)별 평균 salary_in_usd를 표(피벗)로 만드시오.",
  "df.pivot_table(index='work_year', columns='experience_level', values='salary_in_usd', aggfunc='mean').round(0)",
  "experience_level  Entry-level  Executive-level  Mid-level  Senior-level\nwork_year                                                              \n2020                  69841.0         179958.0    91871.0      138649.0\n2021                  63463.0         186128.0    85441.0      125990.0\n2022                  72823.0         183838.0   101354.0      150241.0\n2023                  90706.0         191130.0   124172.0      164814.0\n2024                  90308.0         191874.0   135578.0      171646.0"
 ],
 [
  "8. salary_in_usd가 200,000 이상인 데이터 수와, 그중 가장 많은 job_title 3개를 구하시오.",
  "high = df[df['salary_in_usd'] >= 200000]\nprint(len(high))\nhigh['job_title'].value_counts().head(3)",
  "1316\njob_title\nData Scientist               258\nData Engineer                245\nMachine Learning Engineer    221\nName: count, dtype: int64"
 ]
]


def _tbl(rows):
    return "<table><tr><th>이름</th><th>한 줄 설명</th></tr>" + "".join(
        f"<tr><td><code>{a}</code></td><td>{b}</td></tr>" for a, b in rows) + "</table>"


def register_head(add):
    add("practice", "과제 목록과 형식 (시험도 같은 형식)", "과제 목록 형식 week3 week4 6주차 pandas 마크다운 제출 에러 텍스트 박스",
html="""<table>
<tr><th>과제</th><th>내용</th><th>형식 · 제출물에서 한 것</th></tr>
<tr><td><b>Week3 (Pandas)</b></td><td>Salary2024.csv로 job_title별 개수, 종류 수, 최소·최대·평균</td><td>문제를 마크다운 제목으로, 코드 셀 첫 줄에 <code>#1. 문제</code> 주석, 한 줄 코드로 답</td></tr>
<tr><td><b>Week4 (심층신경망 기초)</b></td><td>사양(200·100, ELU, He, NAG 0.9, BN, Softmax)대로 MNIST 모델 만들고 정확도 확인</td><td>셀을 Import → Data → Model → Compile → Learning → Evaluation로 나누고, 끝에 마크다운 "정리"(구조·설정·결과·기법 한 줄씩)</td></tr>
<tr><td><b>6주차 (10/10)</b></td><td>6장 노트북(사용자 정의 층·모델, GradientTape, 훈련 반복, tf.function)을 돌리고 에러 고치기</td><td>함수·클래스마다 <code>`이름` : 한 줄 설명</code> 마크다운, 에러 셀 아래 <b>에러 원인 / 수정</b> 마크다운</td></tr>
</table>
<p><b>녹음에서 나온 다른 과제·실습</b>: 9/12 실습 후 마크다운 설명 정리, 9/19 데이터 증강으로 손글씨 인식 개선, 9/26 옵티마이저 실험 각자 실행</p>
<p>교수님: 시험은 "저번이랑 같은 방식", "과제 할 때 실력을…" → 위 세 형식(<b>집계 한 줄 코드</b>, <b>사양대로 모델 만들기 + 정리</b>, <b>코드 설명·에러 원인 쓰기</b>)이 그대로 나올 가능성이 큼</p>""")


def register_pandas(add):
    for i, (q, code, out) in enumerate(PANDAS, 1):
        add("practice", f"[Week3] Pandas 연습 {q}", "pandas week3 연습 salary2024 groupby value_counts 집계 판다스 문제",
            code="#" + q + "\n" + code, out=out)


def register_explain(add):
    add("practice", "[6주차 형식] 함수 한 줄 설명 + 에러 원인 쓰는 법", "6주차 과제 형식 한 줄 설명 에러 원인 수정 마크다운 쓰는 법 예시",
html="""<p>6주차 제출본에서 쓴 형식 그대로:</p>
<pre class="out"><code>`MyDense` : Dense 층을 직접 구현한 것.
- `__init__` : 뉴런 수와 활성화 함수를 저장
- `build` : 입력 크기를 처음 알게 될 때 가중치(kernel)와 편향(bias)을 생성
- `call` : 입력 @ 가중치 + 편향 후 활성화 함수 적용
- `get_config` : 모델 저장 시 units, activation 값도 함께 저장되도록 반환</code></pre>
<pre class="out"><code>**에러 원인**
`TypeError: hi2() takes 1 positional argument but 2 were given`
`hi2`는 인자를 하나(`Names`)만 받도록 정의되어 있는데 '이순신', '안중근' 두 개를 넣어서 에러가 발생했다.
**수정** : 두 이름을 리스트 하나로 묶어서 전달했다.</code></pre>
<ul><li>순서: <b>무엇을 하는지</b>(한 줄) → 메서드별로 <b>언제·무엇을</b></li>
<li>에러: <b>에러 메시지 그대로</b> → <b>왜</b>(정의와 사용이 어떻게 안 맞는지) → <b>어떻게 고쳤는지</b></li>
<li>다른 노트북의 에러는 "노트북 에러 수정" 분류에 같은 형식의 문장이 있음</li></ul>""")

    add("practice", "[6주차 형식] 5장 함수·클래스 한 줄 설명", "5장 한 줄 설명 huber_fn create_huber HuberLoss my_softplus MyGlorotInitializer MyL1Regularizer MyPositiveWeights HuberMetric",
html=_tbl([
 ("huber_fn", "오차가 1보다 작으면 제곱/2, 크면 |오차|−0.5를 tf.where로 골라 반환하는 손실 함수"),
 ("create_huber", "threshold를 받아 그 값을 기준으로 하는 huber_fn을 만들어 반환하는 함수(함수를 만드는 함수)"),
 ("HuberLoss", "keras.losses.Loss를 상속한 후버 손실 클래스. get_config로 threshold도 모델에 저장됨"),
 ("my_softplus", "사용자 정의 활성화 함수 log(1 + e^z)"),
 ("MyGlorotInitializer", "표준편차 √(2/(fan_in+fan_out))인 정규분포로 가중치를 초기화하는 사용자 정의 초기화"),
 ("MyL1Regularizer", "가중치 절댓값 합 × 계수(0.01 또는 factor)를 손실에 더하는 L1 규제. factor 버전은 get_config로 계수도 저장"),
 ("MyPositiveWeights", "음수 가중치를 0으로 바꾸는 제약(constraint)"),
 ("HuberMetric", "배치마다 후버 값의 합(total)과 개수(count)를 누적해 평균을 내는 스트리밍 지표"),
 ("update_state", "새 배치의 값을 total·count에 더하는 메서드"),
 ("result", "지금까지 누적한 total / count를 반환하는 메서드"),
 ("@register_keras_serializable()", "사용자 정의 클래스를 저장·로드할 때 케라스가 이름으로 찾을 수 있게 등록"),
]))

    add("practice", "[6주차 형식] 6장 함수·클래스 한 줄 설명", "6장 한 줄 설명 Lambda MyDense MyMultiLayer AddGaussianNoise ResidualBlock ResidualRegressor GradientTape random_batch print_status_bar tf.function",
html=_tbl([
 ("keras.layers.Lambda", "가중치 없이 정해진 계산만 하는 층(예: 입력에 e^x)"),
 ("MyDense", "Dense 층을 직접 구현. build에서 가중치·편향 생성, call에서 입력@가중치+편향 후 활성화"),
 ("MyMultiLayer", "입력 두 개를 받아 더하기·곱하기·나누기 세 결과를 반환하는 층(가중치 없음)"),
 ("AddGaussianNoise", "훈련할 때(training=True)만 입력에 가우시안 노이즈를 더하는 층"),
 ("compute_output_shape", "층의 출력 크기를 알려 주는 메서드(노이즈 층은 입력과 같음)"),
 ("ResidualBlock", "Dense 여러 개를 통과한 결과에 원래 입력을 더하는(스킵 연결) 블록"),
 ("ResidualRegressor", "keras.Model을 상속한 사용자 정의 모델: Dense → ResidualBlock 반복 → 출력"),
 ("tf.GradientTape", "with 블록 안의 계산을 기록했다가 tape.gradient로 미분값을 자동 계산"),
 ("tape.watch", "상수(tf.constant)도 미분 대상으로 기록하게 강제"),
 ("random_batch", "훈련 데이터에서 batch_size개를 무작위로 뽑아 미니배치를 만듦"),
 ("print_status_bar", "현재 진행 수와 손실·지표 값을 한 줄로 출력"),
 ("optimizer.apply_gradients", "구한 기울기로 가중치를 갱신"),
 ("tf.function", "파이썬 함수를 텐서플로 그래프로 바꿔 빠르게 실행"),
 ("get_concrete_function", "특정 입력 타입에 맞춰 만들어진 실제 그래프 함수를 가져옴"),
]))

    add("practice", "[6주차 형식] 7장 함수·클래스 한 줄 설명", "7장 cnn 한 줄 설명 plot_image crop feature_map_size manual_same_padding DepthMaxPool tf.nn.conv2d Conv2D MaxPool2D",
html=_tbl([
 ("load_sample_image", "사이킷런 예제 사진(china.jpg, flower.jpg)을 불러옴 (427×640×3)"),
 ("plot_image / plot_color_image", "흑백/컬러 이미지를 축 없이 그려 주는 함수"),
 ("inspectFilters", "필터 배열(7×7×3×2)의 값을 행·채널별로 출력해 보는 함수"),
 ("tf.nn.conv2d", "직접 만든 필터로 합성곱을 계산 (strides: 몇 칸씩, padding: SAME/VALID)"),
 ("crop", "이미지의 일부 영역(150:220, 130:250)만 잘라 반환"),
 ("feature_map_size", "입력 크기·커널·스트라이드·패딩으로 출력(특성 맵) 크기를 계산"),
 ("pad_before_and_padded_size", "SAME 패딩에 필요한 앞쪽 패딩 수와 패딩 후 크기를 계산"),
 ("manual_same_padding", "이미지 둘레에 0을 채워 SAME 패딩을 직접 구현"),
 ("keras.layers.Conv2D", "합성곱 층. 필터 값은 학습되는 가중치"),
 ("keras.layers.MaxPool2D", "칸 안의 최댓값만 남겨 크기를 줄이는 층(파라미터 0)"),
 ("DepthMaxPool", "채널(깊이) 방향으로 최댓값 풀링하는 사용자 정의 층"),
]))


CA_CODE = '''from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt

housing = fetch_california_housing(as_frame=True)
df = housing.frame                    # 표(DataFrame)로 받기
print(df.shape)                       # (20640, 9)
print(df.head())
# 열: MedInc(중간 소득, 만 달러) HouseAge(주택 연식) AveRooms(평균 방 수) AveBedrms(평균 침실 수)
#     Population(인구) AveOccup(평균 거주 인원) Latitude(위도) Longitude(경도) MedHouseVal(집값, 10만 달러)

#1. HouseAge(주택 연식)별로 몇 개의 데이터가 있는지 상위 5개
print(df['HouseAge'].value_counts().head())

#2. HouseAge 종류 수
print(df['HouseAge'].nunique())

#3. HouseAge별 집값(MedHouseVal)의 최소, 최대, 평균
print(df.groupby('HouseAge')['MedHouseVal'].agg(['min', 'max', 'mean']).head())

#4. 소득(MedInc)이 8 이상인 지역의 평균 집값
print(df[df['MedInc'] >= 8]['MedHouseVal'].mean())

#5. 집값이 가장 비싼 10개 지역
print(df.sort_values('MedHouseVal', ascending=False).head(10))

#6. 소득을 구간으로 나눠 구간별 평균 집값 (pd.cut)
df['income_cat'] = pd.cut(df['MedInc'], bins=[0, 1.5, 3, 4.5, 6, float('inf')], labels=[1, 2, 3, 4, 5])
print(df.groupby('income_cat', observed=True)['MedHouseVal'].mean())

#7. 열 사이의 상관관계: 집값과 가장 관련 있는 열
print(df.drop(columns='income_cat').corr()['MedHouseVal'].sort_values(ascending=False))

#8. 교수님이 그린 캘리포니아 지도 (색 = 집값). c='MedInc'로 바꾸면 소득 지도
df.plot(kind="scatter", x="Longitude", y="Latitude", alpha=0.4,
        s=df["Population"] / 100, c="MedHouseVal", cmap="jet", colorbar=True, figsize=(10, 7))
plt.show()'''


def register_pandas_ca(add):
    add("pandas", "캘리포니아 집값 데이터를 Pandas 표로 (Salary2024 말고 나올 만한 표 데이터)",
        "캘리포니아 집값 california housing fetch_california_housing as_frame dataframe pandas 부동산 지도 scatter latitude longitude MedInc MedHouseVal corr 상관관계 pd.cut",
        code=CA_CODE,
        note="2·5·6장에서 쓴 캘리포니아 데이터. as_frame=True로 받으면 Salary2024와 같은 함수로 집계 가능. 10/10 교수님: '평균 소득 말고 다른 걸로 플로팅해 보세요'. 처음 보는 CSV도 순서는 같음: head()·info()로 열 이름 확인 → '~별로'=groupby, '몇 개'=value_counts, '종류 수'=nunique, '~인 것만'=df[조건], '높은 순'=sort_values.")
