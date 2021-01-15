import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import tkinter.filedialog as tf
import pandas as pd
from os.path import abspath, dirname

from win_collect_data import CollectDataWindow

class OpenMatchWindow():
    def __init__(self, top):
        self.top = top
        self.window = tk.Toplevel(top)
        self.window.title('打开文件')
        self.window.geometry('450x75')
        self.window.iconbitmap('tennis.ico')
        self.window.resizable(0,0)

        self.file = ''
        self.body()

    def body(self):
        # ====================================================================
        # command
        # ====================================================================
        def button_browse():
            default_dir = abspath(dirname(__file__))
            self.file = tf.askopenfilename(title='选择文件', initialdir=(default_dir))
            file_path.set(self.file)

        def button_collect():
            if self.file == '':
                msg.showerror(title='错误', message='请选择文件!')
            else:
                self.window.destroy()
                pd_data = pd.read_csv(self.file, sep=',', encoding='utf_8_sig')
                [m, p1, p2, sn, ds] = self.file.split('/')[-1].split('.')[0].split('-')
                [temp, p1_name, p1_hand] = p1.split('_')
                [temp, p2_name, p2_hand] = p2.split('_')
                CollectDataWindow(match_name=m,
                                  player1_name=p1_name,
                                  player2_name=p2_name,
                                  player1_hand=p1_hand,
                                  player2_hand=p2_hand,
                                  set_number=int(sn),
                                  decide_set=ds,
                                  top=self.top,
                                  is_read=True,
                                  dataframe=pd_data).window.mainloop()
            
        # ====================================================================
        # widget
        # ====================================================================
        # ----------------------------------------
        # choose file
        # ----------------------------------------
        group_file = ttk.Frame(self.window)
        group_file.pack(side='top', expand=1, anchor='center', pady=5)
        # ~~~~~~~~~~~~~
        # file path
        # ~~~~~~~~~~~~~
        file_path = tk.StringVar()
        entry_file = ttk.Entry(group_file, textvariable=file_path, show=None, width=50)
        entry_file.pack(side='left', expand=1, anchor='center', padx=5)
        # ~~~~~~~~~~~~~
        # browse
        # ~~~~~~~~~~~~~
        ttk.Button(group_file, text='浏览文件', command=button_browse, width=10)\
            .pack(side='right', expand=1, anchor='center', padx=5)

        # ----------------------------------------
        # collect data
        # ----------------------------------------
        ttk.Button(self.window, text='开始采集', command=button_collect, width=10)\
            .pack(side='bottom', expand=1, anchor='center', pady=5)
