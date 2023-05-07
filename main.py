import tkinter as tk
import tkinter.ttk as ttk
import random
import datetime
import threading
import time

# 更新フェーズカウンター
count = 0

# 終了判定
quitting_flag = False

# 時刻表示
def get_datetime():
    global quitting_flag
    
    while not quitting_flag:
        now_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        datetime_label.config(
            text=now_time
        )
        
        time.sleep(1)

# 画面遷移
def change_window(window):
    window.tkraise()

# textラベル更新
def update_text():
    global label
    global count
    global connection_progress
    global after_id
    
    count += 1
    connection_progress.set(connection_progress.get() + random.uniform(5.0, 10.0))

    label.config(
        text="CONNECTING" + "." * (count % 4)
    )
    
    # progressbarが100%になるまで"CONNECTING..."を表示
    if connection_progress.get() >= 100:
        label.config(
            text="SUCCESS! 524kHz",
            width=15
        )
        root.after_cancel(after_id)
        frame_input.tkraise()
    else:    
        after_id = root.after(250, update_text)

# アプリケーション終了時
def quit_app():
    global quitting_flag
    global root
    global thread

    quitting_flag = True
    thread.join()
    root.destroy()


# rootメインウィンドウ設定
root = tk.Tk()
root.update_idletasks()
width = 720
height = 480
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
root.geometry(str(width)+"x"+str(height)+"+"+str(int(sw/2-width/2))+"+"+str(int(sh/2-height/2)))
root.title("Connector")

# rootメインウィンドウのグリッドを1x1にする
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# フレーム配置
frame_input = tk.Frame(root, padx=50, pady=100)
frame_input.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW)
frame_connection = tk.Frame(root, padx=50, pady=100)
frame_connection.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW)
frame_time = tk.Frame(root)
frame_time.grid(row=1, column=1, sticky=tk.NSEW)

"""
ウィジェットリスト
# frame_input
    - pos_input : 位置情報入力用
    - button : 画面遷移用

# frame_connection
    - text : 接続表示用
    - progress_bar : 装飾用
"""
entry = tk.Entry(
    frame_input,
    width=30,
    font=("BIZ UDゴシック", 20),
    justify=tk.CENTER,
)
entry.pack(padx=5, pady=45)

button = tk.Button(
    frame_input,
    command=lambda: change_window(frame_connection),
    width=10,
    padx=10,
    pady=10,
    font=("Consolas", 20, "bold"),
    text="Submit",
)
button.pack(padx=5, pady=5)

label = tk.Label(
    frame_connection,
    width=13,
    anchor=tk.W,
    font=("Consolas", 30, "bold"),
    text="CONNECTING",
)
label.pack(anchor="center", expand=1)

datetime_label = tk.Label(
    frame_time,
    anchor=tk.E,
    font=("Consolas", 15),
    text="0000/00/00 00:00:00",
)
datetime_label.pack(side="right")

connection_progress = tk.IntVar()

progressbar = ttk.Progressbar(
    frame_connection,
    orient="horizontal",
    variable=connection_progress,
    maximum=100,
    length=500,
    mode="determinate",
)
progressbar.pack(expand=1)

root.protocol("WM_DELETE_WINDOW", quit_app)

frame_connection.tkraise()
root.after(500, update_text)

thread = threading.Thread(target=get_datetime)
thread.start()

root.mainloop()