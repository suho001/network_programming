from tkinter import *
root = Tk() # TK instance 생성

root.title("opt window")#창 이름 설정
root.geometry("300x200+300+300")#창 크기+창좌표 설정
root.resizable(False,False)#창 크기 변경 가능여부

root.mainloop() # TK 화면 호출