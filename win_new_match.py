import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from win_new_player import NewPlayerWindow

class NewMatchWindow():
    def __init__(self, top):
        self.top = top
        self.window = tk.Toplevel(top)
        self.window.title('新建比赛')
        self.window.geometry('360x200')
        self.window.iconbitmap('tennis.ico')
        self.window.resizable(0,0)
        self.body()

    def body(self):
        # ====================================================================
        # command
        # ====================================================================
        def button_collect():
            m = entry_match_name.get()
            mt = match_type.get()
            sn = set_number.get()
            ds = decide_set.get()
            if m == '':
                msg.showerror(title='错误', message='请输入比赛名称！')
            elif mt == '':
                msg.showerror(title='错误', message='请选择比赛类型！')
            elif sn == '':
                msg.showerror(title='错误', message='请选择比赛盘数！')
            elif ds == '':
                msg.showerror(title='错误', message='请选择决胜盘类型！')
            else:
                self.window.destroy()
                NewPlayerWindow(match_name=m, 
                                match_type=mt, 
                                set_number=int(sn),
                                decide_set=ds,
                                top=self.top).window.mainloop()

        # ====================================================================
        # widget
        # ====================================================================
        # ----------------------------------------
        # match name
        # ----------------------------------------
        group_match_name = ttk.Frame(self.window)
        group_match_name.pack(side='top', expand=1, anchor='w', pady=5, padx=5)
        ttk.Label(group_match_name, text='比赛名称：')\
            .pack(side='left', expand=1, anchor='center', padx=5)
        entry_match_name = ttk.Entry(group_match_name, show=None)
        entry_match_name.pack(side='right', expand=1, anchor='center', padx=5)

        # ----------------------------------------
        # match type
        # ----------------------------------------
        group_match_type = ttk.Frame(self.window)
        group_match_type.pack(side='top', expand=1, anchor='w', pady=5, padx=5)
        ttk.Label(group_match_type, text='比赛类型：')\
            .pack(side='left', expand=1, anchor='center', padx=5)
        match_type = tk.StringVar()
        ttk.Radiobutton(group_match_type, text='单打', variable=match_type, value='single')\
            .pack(side='left', expand=1, anchor='center', padx=5)
        ttk.Radiobutton(group_match_type, text='双打', variable=match_type, value='double')\
            .pack(side='right', expand=1, anchor='center', padx=5)

        # ----------------------------------------
        # set number
        # ----------------------------------------
        group_set_number = ttk.Frame(self.window)
        group_set_number.pack(side='top', expand=1, anchor='w', pady=5, padx=5)
        ttk.Label(group_set_number, text='比赛盘数：')\
            .pack(side='left', expand=1, anchor='center', padx=5)
        set_number = tk.StringVar()
        ttk.Radiobutton(group_set_number, text='三盘两胜', variable=set_number, value='2')\
            .pack(side='left', expand=1, anchor='center', padx=5)
        ttk.Radiobutton(group_set_number, text='五盘三胜', variable=set_number, value='3')\
            .pack(side='right', expand=1, anchor='center', padx=5)

        # ----------------------------------------
        # deciding set
        # ----------------------------------------
        group_decide_set = ttk.Frame(self.window)
        group_decide_set.pack(side='top', expand=1, anchor='w', pady=5, padx=5)
        ttk.Label(group_decide_set, text='决胜盘类型：')\
            .pack(side='left', expand=1, anchor='center', padx=5)

        group_set_comb = ttk.Frame(group_decide_set)
        group_set_comb.pack(side='right', expand=1, anchor='center')
        group_set_comb_1 = ttk.Frame(group_set_comb)
        group_set_comb_1.pack(side='top', expand=1, anchor='center')
        group_set_comb_2 = ttk.Frame(group_set_comb)
        group_set_comb_2.pack(side='bottom', expand=1, anchor='center')

        decide_set = tk.StringVar()
        # ~~~~~~~~~~~~~
        # line 1
        # ~~~~~~~~~~~~~
        ttk.Radiobutton(group_set_comb_1, text='直接抢七  ', variable=decide_set, value='tie7')\
            .pack(side='left', expand=1, anchor='center', padx=5)
        ttk.Radiobutton(group_set_comb_1, text='直接抢十  ', variable=decide_set, value='tie10')\
            .pack(side='left', expand=1, anchor='center', padx=5)
        ttk.Radiobutton(group_set_comb_1, text='六局抢七  ', variable=decide_set, value='6tie7')\
            .pack(side='left', expand=1, anchor='center', padx=5)
        # ~~~~~~~~~~~~~
        # line 2
        # ~~~~~~~~~~~~~
        ttk.Radiobutton(group_set_comb_2, text='六局抢十  ', variable=decide_set, value='6tie10')\
            .pack(side='left', expand=1, anchor='center', padx=5)
        ttk.Radiobutton(group_set_comb_2, text='十二局抢七', variable=decide_set, value='12tie7')\
            .pack(side='left', expand=1, anchor='center', padx=5)
        ttk.Radiobutton(group_set_comb_2, text='长盘      ', variable=decide_set, value='long')\
            .pack(side='right', expand=1, anchor='center', padx=5)

        # ----------------------------------------
        # next step
        # ----------------------------------------
        ttk.Button(self.window, text='下一步', command=button_collect, width=10)\
            .pack(side='top', expand=1, anchor='center', pady=5)
