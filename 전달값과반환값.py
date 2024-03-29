def open_account():
    print("새로운 계좌가 생성되었습니다")

def deposit(balance, money):
    print("입금이 완료되었습니다.\n잔액 : {0}원".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:  # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다.\n잔액 : {0}원".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다.\n잔액 : {0}원".format(balance))
        return balance

def withdraw_end(balance, money):  # 영업시간 종료 이후 출금
    commission = 100  # 수수료 100원
    return  commission, balance - money - commission

balance = 0  # 잔액
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commisson, balance = withdraw_end(balance, 500)
print("출금이 완료되었습니다.\n수수료 : {0}원\n잔액 : {1}".format(commisson, balance))
