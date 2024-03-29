class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1  # 홀안에는 현재 만석, 대기번호 1부터 시작

while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇마리를 주문하시겠습니까? "))
        if order < 1 or type(order) != int:
            raise ValueError
        elif chicken == 0:
            raise SoldOutError
        elif order > chicken:  # 남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order

    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break
