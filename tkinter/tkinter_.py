from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.simpledialog import *
#window = Tk()
#이 부분에 화면을 구성하고 처리하는 코드 작성
#window.mainloop() #file.close()의 close = tkinter의 mainloop
#1
win01 = Tk()
win01.title("윈도우 연습")
win01.geometry('400x100')
win01.resizable(width=FALSE,height=FALSE) #true하면 커서 이용해서 크기변경 가능
win01.mainloop()

#2
window = Tk()
window.title("label 연습")
window.geometry('400x100')
window.resizable(width=TRUE,height=TRUE)
label1 = Label(window,text='Python을')
label2 = Label(window,text='한달동안')
label3 = Label(window,text='배웠습니다')
label1.pack();label2.pack();label3.pack() #label 가시화
window.mainloop()
#Label
#font(폰트,크기),fg(글자색),bg(배경색),anchor(위치.N/NE/E/../CENTER등) 지정가능

#3
window = Tk()
window.title("연습용")
window.geometry('500x500')
window.resizable(width=TRUE,height=TRUE)
photo = PhotoImage(file='../tkinter/tumblr_m7hs1aZU5c1rt3fn2540.gif') #jpg,png는 불가능. 오직 gif만 가능하다
label1 = Label(window,image=photo)
label1.pack()
window.mainloop()

#4
#pyglet 모듈 사용 안하면 gif 안 움직임.
#움직이는 gif 띄우기
import pyglet
ag_file = "C:/Users/cjdfi/Desktop/20200710/giphy.gif"
animation = pyglet.resource.animation(ag_file)
sprite = pyglet.sprite.Sprite(animation)
win = pyglet.window.Window(width=sprite.width,height=sprite.height)
@win.event 
def on_draw():
    win.clear()
    sprite.draw()
pyglet.app.run()

window = Tk()
button1 = Button(window,text="Quit",fg='red',command=quit)
button1.pack()
window.mainloop()
#button: 마우스의 클릭이벤트를 이용해 특정작업이 실행되도록 하는 위젯. command에 입력한 작업이 마우스 클릭시 실행.

#button 기능 확장
#5
def messageFunc():
    messagebox.showinfo("fun","완전 신난다")
win01 = Tk()
photo = PhotoImage(file="C:/Users/cjdfi/Desktop/20200710/giphy.gif")
button1 = Button(win01,image=photo,command=messageFunc)
button1.pack()
win01.mainloop()

def checkFunc():
    if chk.get() == 0: #체크버튼에 체크가 안 된 상태. get()메소드로 값을 읽어온다
        messagebox.showinfo("check button","Check Button Off")
    else:
        messagebox.showinfo("check button","Check Button On")
window = Tk()
chk = IntVar() #정수형 타입의 변수를 생성하는 클래스(위젯에 사용되는 값을 객체로) StrVar(),DoubleVar()도 있다.더블=float
cb1 = Checkbutton(window,text="Please Click",variable=chk,command=checkFunc)
cb1.pack()
window.mainloop()

#6
def checkFunc():
    if chk1.get() == 1:
        messagebox.showinfo("check button", "Python Check")
    elif chk2.get() == 1:
        messagebox.showinfo("check button","visual C++ Check")
    elif chk3.get() == 1:
        messagebox.showinfo("check button","Ruby Check")
    else:
        messagebox.showinfo("check button","Check Button Off")
window = Tk()
chk1 = IntVar();chk2 = IntVar();chk3 = IntVar()
cb1 = Checkbutton(window,text="Python",variable=chk1,command=checkFunc)
cb2 = Checkbutton(window,text="visual C++",variable=chk2,command=checkFunc)
cb3 = Checkbutton(window,text="Ruby",variable=chk3,command=checkFunc)
cb1.pack(side=TOP);cb2.pack(side=TOP);cb3.pack(side=BOTTOM)
window.mainloop()

#7
def radioFunc():
    if rbk.get() == 1:
        label1.configure(text='python')  
        #configure: "기존에 출력된"(한번 함수가 돌아가서 아래 라벨이 바뀌었을 때) 라벨위젯의 모양을 다시 변경하는 함수
    elif rbk.get() == 2:
        label1.configure(text='C++')
    else:
        label1.configure(text='Java')

window = Tk()
rbk = IntVar()
rb1 = Radiobutton(window,text="파이썬",variable=rbk,value=1,width=10,height=1,anchor=W,command=radioFunc)
rb2 = Radiobutton(window,text="씨뿔뿔",variable=rbk,value=2,width=10,height=1,anchor=W,command=radioFunc)
rb3 = Radiobutton(window,text="자바",variable=rbk,value=3,width=10,height=1,anchor=W,command=radioFunc)
label1 = Label(window,text="선택한 언어",fg="red")
rb1.pack();rb2.pack();rb3.pack();label1.pack()
window.mainloop()

#8
def buttonClick():
    text1.delete(0,END)
    text1.insert(0,'click') #값 추가/삽입(추가할 위치,추가할 내용)
#buttonClick으로 인해 text1에는 뭘 쓰든 click을 누른 순간 'click'으로 변하고 아래 배너글자(라벨글자)도 바뀌지 않는다.
def buttonVar():
    label1.configure(text=string.get())
    string.set('오늘은 금요일!')
#buttonVar로 인해 text2에 쓴 글자는 var를 누른 순간 '오늘은 금요일!'로 변하고 쓴 글자는 배너글자(라벨글자)가 된다.

win = Tk()
string = StringVar()
text1 = Entry(win,textvariable=string,width=15)
btn1 = Button(win,text='Click',command=buttonClick)
btn2 = Button(win,text='var',command=buttonVar)
label1 = Label(win,text="value of text1")
text1.pack();btn1.pack();btn2.pack()
label1.pack()
win.mainloop()

#9
#pack:상대적 위치(side=LEFT/RIGHT/..)
#place:고정 위치(x=X좌표, y=Y좌표)
window = Tk()
button1 = Button(window,text='Button A')
button2 = Button(window,text='Button B')
button3 = Button(window,text='Button C')
button1.place(x=0,y=0)
button2.place(x=50,y=50)
button3.place(x=100,y=100)
window.mainloop()
#위젯 만들 때에도 반복문 쓸 수 있다.

#10
window = Tk()
btnList = [None]*3
for i in range(len(btnList)):
    btnList[i] = Button(window,text='Button'+chr(65+i))
for btn in btnList:
    btn.pack(side=TOP,fill=X,ipadx=10,ipady=10)  #ipadx,ipady : 여백조절
window.mainloop()

#곱셈계산 윈도우프로그램 실습
def buttonClick():
    text1.delete(0,END)
    text2.delete(0,END)
    num1.set(0);num2.set(0) #위젯변수 num1,num2를 0으로 셋팅
    label1.configure(text='operator result')
def buttonCal():
    var1 = num1.get()  #변수.get():앞에 쓰인 그 변수를 가져온다
    var2 = num2.get()
    label1.configure(text=var1*var2)
    
window = Tk()
window.geometry("300x150")
window.title("multiple cal")
num1 = IntVar(value=0)
num2 = IntVar(value=0) #초기값=0이고, 정수인 위젯변수 생성
text1 = Entry(window,textveriable=num1,width=20)
text2 = Entry(window,textveriable=num2,width=20)
btn1 = Button(window,text='clear',width=8,height=1,command=buttonClick)
btn2 = Button(window,text='multi_cal',width=8,height=1,command=buttonCal)
label1 = Label(window,text="operator result")
text1.pack();text2.pack();btn1.pack();btn2.pack()
label1.pack()
window.mainloop()

#11
def clickLeft(event):
    messagebox.showinfo("Mouse","Click Left Button")

window = Tk()
window.bind("<Button-1>",clickLeft)
window.mainloop()

#12
def clickLeft(event):
    messagebox.showinfo("Mouse","Click Left Button")
def clickImage(event):
    messagebox.showinfo("Mouse","Mouse clicked on Friday")

window = Tk()
window.geometry("500x500")
photo = PhotoImage(file='C:/Users/cjdfi/Desktop/20200710/giphy.gif')
label1 = Label(window,image=photo)
label1.bind("<Button>",clickImage)
window.bind("<Button-1>",clickLeft)
label1.pack(expand=1,anchor=CENTER)
window.mainloop()

#13
window = Tk()
mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label='Open')
fileMenu.add_separator()
fileMenu.add_command(label='Exit') #exit 누르면 실제로 exit되길 원한다면 command=로 실행값 추가

window.mainloop()

#14
def func_open():
    messagebox.showinfo("Open","Select Open")
def func_exit():
    window.quit()
    window.destroy()

window = Tk()
mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='File',menu=fileMenu)
fileMenu.add_command(label='Open',command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=func_exit)

window.mainloop()

#15
def func_open():
    name = filedialog.askopenfilename(initialdir="/",title="Select file")
    print(name)
def func_exit():
    window.quit()
    window.destroy()
def func_edit():
    messagebox.showinfo("Editor","This program was coded by Yujin at 07/10")
def func_version():
    yes = messagebox.askquestion("Ask Ok/Cancel","Version 1.0 and Quit?")
    if yes == 'yes':
        window.quit()
        window.destroy()

window = Tk()
mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label='Open',command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=func_exit)

infoMenu = Menu(mainMenu)
mainMenu.add_cascade(label="Info",menu=infoMenu)
infoMenu.add_command(label='Editor',command=func_edit)
infoMenu.add_command(label='Version',command=func_version)

window.mainloop()

#16
window = Tk()
window.geometry("500x500")
label1 = Label(window,text="Input Value")
label1.pack()
value = askinteger("Number","input from 1 to 6",minvalue=1,maxvalue=6)
label1.configure(text=str(value))
window.mainloop()
