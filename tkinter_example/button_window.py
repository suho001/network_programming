from tkinter import *

count = 0

def count_plus():
    global count
    count += 1
    label.config(text=str(count))

def count_minus():
    global count
    count -=1
    label.config(text=str(count))


root = Tk() # TK instance 생성

label = Label(root, text="0") # label 생성
label.pack() # 레이블을 화면에 배치

button1 = Button(root, width=10, text="plus", overrelief="solid", command=count_plus)
#count_plus 이벤트를 가지는 버튼 생성
button1.pack() # 버튼을 화면에 배치

button2 = Button(root, width=10, text="plus", overrelief="solid", command=count_minus)
#count_minus 이벤트를 가지는 버튼 생성
button2.pack() # 버튼을 화면에 배치

root.mainloop() # TK 화면 호출