from os import kill
import pyupbit
import numpy as np

# OHLCV(open, high, low, close, volume)로 당일 시가, 고가, 저가, 종가, 거래량에 대한 데이터
# 새로운 전략(8:20): https://www.youtube.com/watch?v=5vofEMqMyGk&list=PLU9-uwewPMe3KKFMiIm41D5Nzx_fx2PUJ&index=3
df = pyupbit.get_ohlcv("KRW-BTC", count=7)  

#  변동성 돌파 기준 범위 계산, (고가-저가)*k
df['range'] = (df['high'] - df['low']) * 0.5

# range 컬럼을 한칸씩 밑으로 내림(.shift(1))
df['target'] = df['open'] + df['range'].shift(1)

# ror(수익률), np.where(조건문, 참일 때 값, 거짓일 때 값)
# 목표가 / 종가 = 수익률
# fee = 0.0032 두번째 줄 마지막에 -fee
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)

# 누적 곱 계산(cumprod) => 누적 수익률
df['hpr'] = df['ror'].cumprod()

# Draw Down(하락폭) 계산(누적 최대 값과 현재 hpr 차이 / 누적 최대값 * 100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

# MDD 계산
print("MDD(%): ", df['dd'].max())

# 엑셀로 출력
df.to_excel("dd.xlsx")


# open 시가
# high 고가
# low 저가
# close 종가
# volume 거래량
# range 변동폭*k
# target 매수가
# ror 수익률
# hpr 누적 수익률
# dd 낙폭