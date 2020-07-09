#다음 조건을 만족하는 Point 클래스 작성
#Point class는 생성자를 통해 (x,y)좌표를 입력받음
#setx(x), sety(y) 메서들를 통해 x좌표와 y좌표를 따로 입력받을 수 있음
#get() 메서도 호출시 튜플로 구성된 (x,y)좌표를 반환
#movexy(dx,dy) 메서드는 현재 좌표를 dx,dy만큼 이동
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def setx(self,x):
        self.x = x
    def sety(self,y):
        self.y = y
    def getxy(self):
        return(self.x,self.y)
    def movexy(self,dx,dy):
        self.x += dx
        self.y += dy
        return(self.x,self.y)

if __name__ == '__main__':
    mypoint = Point(0,0)
    print(mypoint.getxy())
    mypoint.setx(10)
    mypoint.sety(30)
    print(mypoint.getxy())
    mypoint.movexy(10,-5)
    print(mypoint.getxy())


print('')


#네임스페이스 예제
class Country:
    local = "Seoul"
    def addr(self,*others):
        self.local,self.gu,self.load = others

if __name__ == "__main__":
    me = Country()
    print(Country.__dict__)
    print(me.__dict__)
    print(me.local)
    me.addr('부산','해운대','해운대로')
    print(me.__dict__)
    print(f'{me.local}{me.gu}{me.load}')


print('')


class Country:
    local = "인천"
    print(f'id of local: {id(local)}')                # ㄱ
    def addr(self,*others):
        self.local,self.gu,self.load = others
        print(f'id of self.local: {id(self.local)}')  # ㄴ

if __name__ == "__main__":
    me = Country()
    you = Country()
    me.addr('서울','해운대','해운대로')
    print(f'id of me.local: {id(me.local)}')          # ㄷ
    print(f'id of you.local: {id(you.local)}')        # ㄹ

#ㄴ,ㄷ이 같은 값이 나오고 ㄱ,ㄹ이 같은 값이 나온다.


print('')


class Country:
    local = "서울"
    def addr(self,*others):
        self.gu,self.load = others

if __name__ == "__main__":
    me = Country()
    you = Country()
    me.addr('영등포구','선유로')
    you.addr('종로구','인사동길')
    print(me.local,me.gu,me.load)
    print(you.local,you.gu,you.load)
    print(f'{id(me.gu),id(you.gu)}')


print('')


class Car:
    count = 0
    def __init__(self,colorV,speedV):
        self.color = colorV
        self.speed = speedV
        Car.count += 1 #self.count로 한다면 계속해서 1이 나올것

greenCar,redCar = None, None
greenCar = Car("green",60)
print("greenCar의 색상은 {}, 속도는 {}, 생산 댓수는 {}".format(greenCar.color,greenCar.speed,greenCar.count))
redCar = Car("red",80)
print("redCar의 색상은 {}, 속도는 {}, 생산 댓수는 {}".format(redCar.color,redCar.speed,redCar.count))


print('')


#상속
#class 부모클래스:
#class 자식클래스(부모클래스명):
class Car:
    def __init__(self, colorV,speedV):
        self.color = colorV
        self.speed = speedV

class Sedan(Car):
    def carNum(self,num):
        self.number = num
        #__init__은 부모클래스로부터 상속받을것이므로 안써도ㅇㅋ
        #부모클래스에 있는 것들은 그대로 물려받으므로 쓰지않아도 발현됨

myCar = Sedan('yellow',150)
print(myCar.color,myCar.speed)
myCar.carNum(5)
print(myCar.number)


print('')


class Car:
    count = 0
    def __init__(self,colorV,speedV):
        self.color = colorV
        self.speed = speedV
        Car.count += 1

class Sedan(Car):
    def __init__(self,colorV,speedV,numV): #부모클래스에서 일부 수정ㅇ
        super().__init__(colorV,speedV) #부모클래스=슈퍼클래스
        self.number = numV

myCar = Sedan('red',120,5)
print("myCar 색상은 {}, 속도는 {}, 승차인원은 {}, 차의 생산댓수는 {}".
      format(myCar.color,myCar.speed,myCar.number,myCar.count))


print('')


#메서드 오버라이딩
class Car:
    def __init__(self, colorV, speedV):
        self.color = colorV
        self.speed = speedV
    def upSpeed(self,plus):
        self.speed += plus

class Sedan(Car):
    def __init__(self,colorV,speedV,doorV):
        super().__init__(colorV,speedV)
        self.door = doorV
    def upSpeed(self,plus):
        self.speed += plus     #super().upSpeed(plus)라고 쓰는 것과 같다
        if self.speed >= 150:  #자식클래스에서 일부함수 재정의(메서드오버라이딩)
            self.speed = 150

me = Sedan('green',80,4)
print("초기 속도: %d" % me.speed)
me.upSpeed(100)
print("업 속도: %d" % me.speed) #80+100=180이지만 if문으로인해 150 출력


print('')


#Car->Sedan->Sona의 클래스를 생성하고, Sona는 추가 메서드는 없고
#회사명의 인스턴스변수 추가하는 코드 작성
class Car:
    count = 0
    def __init__(self,colorV,speedV):
        self.color = colorV
        self.speed = speedV
        Car.count += 1

class Sedan(Car):
    def __init__(self,colorV,speedV,doorV):
        super().__init__(colorV,speedV)
        self.door = doorV
    def upSpeed(self,plus):
        self.speed += plus     
        if self.speed >= 150:  
            self.speed = 150

class Sona(Sedan):
    def __init__(self,colorV,speedV,doorV,coV):
        super().__init__(colorV,speedV,doorV)
        self.company = coV

me = Sona("green",50,2,"Hyun")
print("초기속도 : %d, 도어 수 : %d" % (me.speed,me.door))
print("생산회사: %s" % me.company)
me.upSpeed(200)
print("업 속도: %d" % me.speed)


print('')


#property 적용하여 __변수 값 알아내기
class InfoClass:
    def __init__(self):
        self.__name = "Python"
        self.__weekday = "수요일"
    @property
    def getName(self):        # ㄱ
	return self.__name
    @getName.setter           # ㄴ
    def setName(self,name):
	self.__name = name
    @property
    def getweekday(self):
	return self.__weekday
    @getweekday.setter
    def setweekday(self,weekday):
	self.__weekday = weekday
#ㄱ과 ㄴ의 함수명을 똑같게 해도 된다.

if __name__ == "__main__":
    class1 = InfoClass()
    class1.setName = "Data Design"
    print(class1.getName)
    class1.setweekday = "금요일"
    print(class1.getweekday)
