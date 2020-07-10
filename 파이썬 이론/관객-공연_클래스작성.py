#관객과 공연정보의 클래스 구성
#관객: 이름, 회원id 정보와 공연예약,공연평점주기 메소드로 구성
#관객클래스는 공연클래스와 연관
#공연클래스는 관객클래스와는 별도로 실행될 수 있음
#공연정보는 공연명,공연장소 정보와 공연평점보기로 구성
#공연정보 클래스에서 관객이 준 공연평점은 동일 공연일 경우, 평점을 평균해서 보여줌

#관객클래스
class Customer:
    def __init__(self,name,num):
        self.name = name
        self.num = num
    def book(self,play,place):
        self.play = Play(play,place)
    def classPoint(self,point,name):
        self.play.p_point(point)

#일 때 공연클래스를 작성하여 아래 결과문이 정상적으로 작동되게 하라.
class Play:
    points = {}
    def __init__(self,name,place):
        self.play_name = name
        self.place = place
    def p_point(self,point):
        count = 1
        if self.play_name in Play.points:
            count += 1
            Play.points[self.play_name] = (Play.points[self.play_name] + point)/count
        else:
            Play.points[self.play_name] = point
    def point_print(self):
        print(f'{self.play_name}의 평점은 {Play.points[self.play_name]}입니다.')

#결과문
if __name__ == "__main__":
    c1 = Customer('Gildong','123')
    c1.book('Rent','ArtCenter')
    c1.classPoint(5,'Rent')
    c2 = Customer('Jane','124')
    c2.book('Rent','ArtCenter')
    c2.classPoint(3,'Rent')
    c3 = Customer('Yuna','125')
    c3.book('Dracula','Sejong')
    c3.classPoint(4,'Dracula')

    p1 = Play('Rent','ArtCenter')
    p1.point_print()
    p2 = Play('Dracula','Sejong')
    p2.point_print()