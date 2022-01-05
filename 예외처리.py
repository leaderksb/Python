try:
    print("[ 나누기 전용 계산기 ]")

    nums = []
    nums.append(int(input("첫번째 수 >> ")))
    nums.append(int(input("두번째 수 >> ")))
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print("에러!", err)
except Exception as err:  # 위에 해당하는 에러가 없을 경우 모든 에러를 출력
    print("알 수 없는 에러가 발생하였습니다!")
    print(err)