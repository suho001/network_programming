import tkinter as tk
import cv2
from PIL import Image, ImageTk
import threading

# 웹캠 캡처를 위한 스레드
class VideoCaptureThread(threading.Thread):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.cap = cv2.VideoCapture(0)
        self.stop_event = threading.Event()

    def run(self):
        while not self.stop_event.is_set():
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                label.config(image=photo)
                label.image = photo
                label.update()
        self.cap.release()

    def stop(self):
        self.stop_event.set()

# 메시지 보내기 함수
def send_message():
    message = entry.get()
    chat_text.config(state=tk.NORMAL)
    chat_text.insert(tk.END, "나: " + message + "\n")
    chat_text.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

# 종료 함수
def on_closing():
    video_thread.stop()
    window.destroy()

# GUI 초기화
window = tk.Tk()
window.title("화상 채팅")

# 웹캠 초기화
video_thread = VideoCaptureThread(window)
video_thread.start()

# 라벨 위젯을 사용하여 영상 표시 (80%)
label = tk.Label(window)
label.grid(row=0, column=0, padx=10, pady=10, rowspan=2, sticky="nsew")

# 채팅 창 (Text 위젯) 추가 (20%)
chat_text = tk.Text(window, wrap=tk.WORD, state=tk.DISABLED)
chat_text.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# 메시지 입력 필드 (20%)
entry = tk.Entry(window)
entry.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# 메시지 보내기 버튼 (20%)
send_button = tk.Button(window, text="보내기", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10, sticky="se")

# 종료 시 이벤트 처리
window.protocol("WM_DELETE_WINDOW", on_closing)

# 행 및 열 가중치 설정
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=4)  # 비디오 화면이 80% 차지
window.grid_columnconfigure(1, weight=1)  # 채팅 창이 20% 차지

# GUI 시작
window.mainloop()
