import pyautogui
import time

print(pyautogui.position())

pyautogui.moveTo(1848, 34, 1)

pyautogui.doubleClick()

time.sleep(1)

pyautogui.typewrite(['enter'])  # 자판 키 사용
pyautogui.typewrite("Hello")  # 타이핑 사용

# i = pyautogui.locateOnScreen('7.png')
# q = pyautogui.center(i)
# i = pyautogui.locateCenterOnScreen('7.png')

# pyautogui.screenshot('1.png', region=(5, 525, 95, 70))
q = pyautogui.locateCenterOnScreen('1.png')

pyautogui.click(q)

btn_1 = pyautogui.alert(text='경고', title='title', button='버튼버튼')
print(btn_1)
print(type(btn_1))

btn_2 = pyautogui.confirm(text='테스트', title='TITLE', buttons=['1', '2', '3', '4'])
print(btn_2)
if btn_2 == '2':
    print("2입니다.")

btn_3 = pyautogui.prompt(title='TITLE', default='여기에 쓰세요.', text='텍스트')
print(btn_3)

btn_4 = pyautogui.password('password', '비밀번호를 입력하세요.', mask='$')
print(btn_4)
# 패스워드가 단순히 안보이게 해줄뿐이지, 보안이 뛰어나지는 것은 아니다. 문자 타입이다.
