# 빈자리는 공백으로 표기, 오른쪽 정렬, 총 10자리
print("{0: >10}".format(500))

# 양수와 음수 부호 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 빈자리는 _로 표기, 왼쪽 정렬, 총 10자리
print("{0:_<+10}".format(500))

# 3자리마다 콤마 구분
print("{0:,}".format(100000000))

# 3자리마다 콤마 구분, +- 부호 표시
print("{0:+,}".format(100000000))
print("{0:+,}".format(-100000000))

# 3자리마다 콤마 구분, 부호 표시, 자릿수 확보
print("{0:*<+30,}".format(100000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점을 특정 자리수까지만 표시 (소수점 3번째 자리에서 반올림)
print("{0:.2f}".format(5/3))