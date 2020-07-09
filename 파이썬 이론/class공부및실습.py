#Class
class Car:
    def color(self, car_color):
        self.c_color=car_color

yellowCar = Car()
yellowCar.color("yellow")
print(yellowCar.c_color)


print('')


class Tar:
    def color(self, tar_color):
        self.t_color = tar_color
    def tarPrint(self):
        print("class Tar")

yellowTar = Tar()
yellowTar.tarPrint()


print('')


class Car:
    def color(self, car_color):
        self.c_color = car_color
        self.carPrint() #그냥 carPrint()라고만 쓰면 오류

    def carPrint(self):
        print("class Car")

yellowCar = Car()
yellowCar.color('yellow') #>> class Car 출력
print(yellowCar.c_color)  #>> yellow 출력


print('')


class EC:
    def f1():
        print("first function")
    def f2(self):
        print(id(self))
        print("second function")

if __name__=="__main__":
    me = EC()
    print(id(me))
    me.f2()
    you = EC()
    print(id(you))
    you.f2()
#EC.f1() 은 first function 잘 나온다
#me.f1() 은 에러 뜬다. me는 instancef라서 self(instance를 받아줄 정보)가 필요


#최대 속도가 150이 되도록 설정
class Car:
    def __init__(self,speed): #인스턴스 생성시 자.동.생.성
        #초기화할 코드 작성
        self.speed = speed
    def upSpeed(self,up_value):
        self.speed += up_value
        if self.speed >= 150:
            self.speed = 150
    def color(self, car_color):
        self.c_color = car_color

if __name__ == "__main__":
    yellowcar = Car(30) #인스턴스 생성, __init__ 자동 호출. speed초기값=30
    yellowcar.upSpeed(200)
    yellowcar.color = "yellow"
    print(yellowcar.speed,yellowcar.color)


print('')


class Car:
    def __init__(self):
        self.c_color = 'white'
    def color(self, car_color):
        self.c_color = car_color

if __name__ == "__main__":
    yellowcar = Car()
    bluecar = Car()
    print(yellowcar.c_color)
    print(bluecar.c_color)
    #>> white white 출력

class Car:
    def __init__(self,color):
        self.c_color=color
    def color(self, car_color):
        self.c_color = car_color

if __name__ == "__main__":
    yellowcar = Car('yellow')
    bluecar = Car('blue')
    print(yellowcar.c_color, bluecar.c_color)
    #>> yellow blue 출력


print('')


class Car:
    def __init__(self,colorV,speedV):
        self.c_color = colorV
        self.speed = speedV
    def upSpeed(self, up_value):
        self.speed = up_value
    def downSpeed(self,down_value):
        self.speed = down_value
    def color(self, car_color):
        self.c_color = car_color

redcar = Car('red',10)
bluecar = Car('blue',20)
print(redcar.c_color,redcar.speed)
print(bluecar.c_color,bluecar.speed)
