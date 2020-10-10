import tkinter as tk
import tkinter.ttk as ttk

from win_new_match import NewMatchWindow
from win_open_match import OpenMatchWindow

class MainWindow():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('网球数据采集工具')
        self.window.geometry('275x50')
        self.window.iconbitmap('tennis.ico')
        self.window.resizable(0,0)
        self.body()

    def body(self):
        # ====================================================================
        # command
        # ====================================================================
        def button_new():
            NewMatchWindow(self.window)

        def button_open():
            OpenMatchWindow(self.window)

        # ====================================================================
        # widget
        # ====================================================================
        # ----------------------------------------
        # new match
        # ----------------------------------------
        ttk.Button(self.window, text='新建比赛', command=button_new, width=10)\
            .pack(side='left', expand=1, anchor='center', padx=5)

        # ----------------------------------------
        # read match
        # ----------------------------------------
        ttk.Button(self.window, text='打开文件', command=button_open, width=10)\
            .pack(side='left', expand=1, anchor='center', padx=5)

        # ----------------------------------------
        # exit
        # ----------------------------------------
        ttk.Button(self.window, text='退出', command=self.window.destroy, width=10)\
            .pack(side='right', expand=1, anchor='center', padx=5)

if __name__ == "__main__":
    win = MainWindow()
    win.window.mainloop()