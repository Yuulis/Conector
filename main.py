import tkinter as tk
import tkinter.ttk as ttk


# 画面遷移
def change_window(window):
    window.tkraise()
    
    # textラベル更新フェーズに移行
    root.after(10, update_text)


# textラベル更新
def update_text():
    global text
    global count
    global after_id
    
    count += 1

    text.config(
        text="CONNECTING" + "." * (count % 4)
    )
    
    # 250ms*10まで"CONNECTING..."を表示
    if count > 10:
        text.config(
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
frame_input = ttk.Frame(root)
frame_input.grid(row=0, column=0, sticky=tk.NSEW, pady=20)
frame_connection = ttk.Frame(root)
frame_connection.grid(row=0, column=0, sticky=tk.NSEW, pady=20)

"""
ウィジェットリスト
# frame_input
    - pos_input : 位置情報入力用
    - button : 画面遷移用

# frame_connection
    - text : 接続表示用
"""
pos_input = ttk.Entry(
    frame_input,
    width=30,
    font=("BIZ UDゴシック", 20),
    justify=tk.CENTER,
)
pos_input.pack()

style = ttk.Style().configure("pos_input.TButton", font=("Consolas", 20, "bold"))
button = ttk.Button(
    frame_input,
    command=lambda: change_window(frame_connection),
    width=10,
    padding=[10],
    style="pos_input.TButton",
    text="Connect",
)
button.pack()

text = ttk.Label(
    frame_connection,
    width=13,
    anchor=tk.W,
    font=("Consolas", 30, "bold"),
    text="CONNECTING",
)
text.pack(anchor="center", expand=1)

# 更新フェーズカウンター
count = 0

frame_input.tkraise()

root.mainloop()