import tkinter as tk


# textラベル更新
def updateText():
    global text
    global count
    global after_id
    
    count += 1

    text.config(
        text="CONNECTING" + "." * (count % 4)
    )
    
    # 250ms * 10まで"CONNECTING..."を表示
    if count > 10:
        text.config(
            text="SUCCESS! 524kHz",
            width=15
        )
        root.after_cancel(after_id)
    else:    
        after_id = root.after(250, updateText)


# ウィンドウ画面設定
root = tk.Tk()
root.update_idletasks()
width = 720
height = 480
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
root.geometry(str(width)+"x"+str(height)+"+"+str(int(sw/2-width/2))+"+"+str(int(sh/2-height/2)))
root.title("Connector")

frame = tk.Frame(root, width=500, height=480, padx=50, pady=200)
frame.pack()


# ラベルウィジェット作成
text = tk.Label(
    frame,
    text="CONNECTING",
    font=("Consolas", 30, "bold"),
    width=13,
    anchor=tk.W
)
text.pack(anchor="center", expand=1)

# 更新フェーズカウンター
count = 0

# textラベル更新フェーズに移行
root.after(10, updateText)

root.mainloop()