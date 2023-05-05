import tkinter as tk
import tkinter.ttk as ttk
import random


# 画面遷移
def change_window(window):
    window.tkraise()
    
    # frame_connectionに移行
    root.after(10, update_text)


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
    else:    
        after_id = root.after(250, update_text)


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
frame_input = tk.Frame(root, padx=50, pady=50)
frame_input.grid(row=0, column=0, sticky=tk.NSEW)
frame_connection = tk.Frame(root, padx=50, pady=50)
frame_connection.grid(row=0, column=0, sticky=tk.NSEW)

"""
ウィジェットリスト
# frame_input
    - pos_input : 位置情報入力用
    - button : 画面遷移用

# frame_connection
    - text : 接続表示用
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
    text="Connect",
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

connection_progress = tk.IntVar()

progressbar = ttk.Progressbar(
    frame_connection,
    orient="horizontal",
    variable=connection_progress,
    maximum=100,
    length=300,
    mode="determinate"
)
progressbar.pack(expand=1)

# 更新フェーズカウンター
count = 0

frame_input.tkraise()

root.mainloop()