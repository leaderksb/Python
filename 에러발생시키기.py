# 사용자 정의 예외 처리
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg  # 에러 메세지 받기

    def __str__(self):
        return self.msg  # 에러 메시지 리턴

# 필요시 특정 에러 발생 시키기
try:
    print("[ 한자리 숫자 나누기 전용 계산기 ]")

    num1 = int(input("첫번째 수 >> "))
    num2 = int(input("두번째 수 >> "))

    if num1 >= 10 or num2 >= 10:
        # raise ValueError  # 에러 발생
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))  # 사용자가 정의한 에러 호출

    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))

except ValueError:
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한자리 숫자만 입력하세요.")
    print(err)  # 리턴된 에러 메시지 출력
finally:  # 에러가 있거나 없거나 항상 실행
    print("계산기를 이용해 주셔서 감사합니다.")

