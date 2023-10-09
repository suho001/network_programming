from tkinter import *

def calc(event):
    label.config(text="계산결과 : " + str(eval(entry.get())))

root = Tk() # TK instance 생성

label = Label(root, text="0") # label 생성
label.pack() # 레이블을 화면에 배치

entry = Entry(root, width=30) # Entry 생성
entry.bind("<Return>", calc) # Entry 이벤트 부여
entry.pack() # 엔트리 화면에 배치

root.mainloop() # TK 화면 호출