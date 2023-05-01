import tkinter as tk


# ウィンドウ画面設定
root = tk.Tk()
root.update_idletasks()
width = 720
height = 480
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
root.geometry(str(width)+"x"+str(height)+"+"+str(int(sw/2-width/2))+"+"+str(int(sh/2-height/2)))
root.title("Application")

frame = tk.Frame(root, width=500, height=480, padx=50, pady=200)
frame.pack()


# ラベルウィジェット作成
text = tk.Label(
    frame,
    text="CONNECTING...",
    font=("Consolas", 30, "bold"),
    anchor=tk.CENTER
)
text.pack()


dict = {
    "text": "SUCCESS! 524kHz"
}

# textラベル更新
def updateText(dict):
    global text

    text.config(
        text=dict["text"]
    )

# 指定時間経過後にtextラベル更新
root.after(5000, updateText, dict)

root.mainloop()