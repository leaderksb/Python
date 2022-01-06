import travel.thailand

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

# travel 패키지에 있는 thailand 모듈에서 ThailandPackage 클래스 불러오기
from travel.thailand import ThailandPackage

trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam

trip_to = vietnam.VietnamPackage()
trip_to.detail()