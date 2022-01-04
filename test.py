import pyupbit

access = "2r0YSd5SjfLfCgxIW6aRd36Ct6a8uNwvm8f9OgEx"          # 본인 값으로 변경
secret = "jVY82C8vIxHgto8YXvcAoasyvXJzl9BeiKlezjgC"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회

