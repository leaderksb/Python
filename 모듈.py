import theater_module  # 모듈 불러오기

theater_module.price(3)  # 3인 가격
theater_module.price_morning(4)  # 4인 조조 할인 가격
theater_module.price_soldier(5)  # 5인 군인 할인 가격

import theater_module as mv  # 모듈 별명 부여
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import *  # 모듈 전체를 사용
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning  # 모듈 내 필요한 부분만 사용
price(5)
price_morning(4)