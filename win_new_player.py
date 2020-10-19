import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from win_collect_data import CollectDataWindow

class NewPlayerWindow():
    def __init__(self, match_name, match_type, set_number, decide_set, top):
        self.m_name = match_name
        self.m_type = 1 if match_type == 'single' else 2
        self.s_no = set_number
        self.d_set = decide_set

        self.top = top
        self.window = tk.Toplevel(top)
        self.window.title('新建比赛')
        if self.m_type == 1:
            self.window.geometry('300x250')
        elif self.m_type == 2:
            self.window.geometry('600x250')
        self.window.iconbitmap('tennis.ico')
        self.window.resizable(0,0)
        self.body()

    def body(self):
        # ====================================================================
        # command
        # ====================================================================
        def button_collect():
            if self.m_type == 1:
                p1 = entry_p1_name.get()
                p2 = entry_p2_name.get()
                p1_h = p1_hand.get()
                p2_h = p2_hand.get()
                if p1 == '' or p2 == '':
                    msg.showerror(title='错误', message='请输入球员姓名！')
                elif p1 == p2:
                    msg.showerror(title='错误', message='双方球员姓名相同！')
                elif p1_h == '' or p2_h == '':
                    msg.showerror(title='错误', message='请选择球员惯用手')
                else:
                    self.window.destroy()
                    CollectDataWindow(match_name=self.m_name,
                                      player1_name=p1,
                                      player2_name=p2,
                                      player1_hand=p1_h,
                                      player2_hand=p2_h,
                                      set_number=self.s_no,
                                      decide_set=self.d_set,
                                      top=self.top,
                                      is_read=False).window.mainloop()
            elif self.m_type == 2:
                p1 = entry_p1_name.get()
                p2 = entry_p2_name.get()
                p3 = entry_p3_name.get()
                p4 = entry_p4_name.get()
                p1_h = p1_hand.get()
                p2_h = p2_hand.get()
                p3_h = p3_hand.get()
                p4_h = p4_hand.get()
                if p1 == '' or p2 == '' or p3 == '' or p4 == '':
                    msg.showerror(title='错误', message='请输入球员姓名！')
                elif p1 + p2 == p3 + p4:
                    msg.showerror(title='错误', message='双方球员姓名相同！')
                elif p1_h == '' or p2_h == '' or p3_h == '' or p4_h == '':
                    msg.showerror(title='错误', message='请选择球员惯用手')
                else:
                    self.window.destroy()
                    CollectDataWindow(match_name=self.m_name,
                                      player1_name=p1 + '+' + p2,
                                      player2_name=p3 + '+' + p4,
                                      player1_hand=p1_h + '+' + p2_h,
                                      player2_hand=p3_h + '+' + p4_h,
                                      set_number=self.s_no,
                                      decide_set=self.d_set,
                                      top=self.top,
                                      is_read=False).window.mainloop()

        # ====================================================================
        # widget
        # ====================================================================
        ttk.Label(self.window, text='比赛名称：' + self.m_name)\
            .pack(side='top', expand=1, anchor='center', pady=5)
        if self.m_type == 1:
            # ----------------------------------------
            # player1
            # ----------------------------------------
            group_p1 = ttk.LabelFrame(self.window, text='球员1')
            group_p1.pack(side='top', expand=1, anchor='center', pady=5)
            # ~~~~~~~~~~~~~
            # player1 name
            # ~~~~~~~~~~~~~
            group_p1_name = ttk.Frame(group_p1)
            group_p1_name.pack(side='top', expand=1, anchor='center')
            ttk.Label(group_p1_name, text='姓名：')\
                .pack(side='left', expand=1, anchor='center', padx=5)
            entry_p1_name = ttk.Entry(group_p1_name, show=None)
            entry_p1_name.pack(side='right', expand=1, anchor='center', padx=5)
            # ~~~~~~~~~~~~~
            # player1 hand
            # ~~~~~~~~~~~~~
            group_p1_hand = ttk.Frame(group_p1)
            group_p1_hand.pack(side='top', expand=1, anchor='center')
            p1_hand = tk.StringVar()
            ttk.Radiobutton(group_p1_hand, text='左手', variable=p1_hand, value='left')\
                .pack(side='left', expand=1, anchor='center', padx=5)
            ttk.Radiobutton(group_p1_hand, text='右手', variable=p1_hand, value='right')\
                .pack(side='right', expand=1, anchor='center', padx=5)

            # ----------------------------------------
            # player2
            # ----------------------------------------
            group_p2 = ttk.LabelFrame(self.window, text='球员2')
            group_p2.pack(side='top', expand=1, anchor='center', pady=5)
            # ~~~~~~~~~~~~~
            # player2 name
            # ~~~~~~~~~~~~~
            group_p2_name = ttk.Frame(group_p2)
            group_p2_name.pack(side='top', expand=1, anchor='center')
            ttk.Label(group_p2_name, text='姓名：')\
                .pack(side='left', expand=1, anchor='center', padx=5)
            entry_p2_name = ttk.Entry(group_p2_name, show=None)
            entry_p2_name.pack(side='right', expand=1, anchor='center', padx=5)
            # ~~~~~~~~~~~~~
            # player2 hand
            # ~~~~~~~~~~~~~
            group_p2_hand = ttk.Frame(group_p2)
            group_p2_hand.pack(side='top', expand=1, anchor='center')
            p2_hand = tk.StringVar()
            ttk.Radiobutton(group_p2_hand, text='左手', variable=p2_hand, value='left')\
                .pack(side='left', expand=1, anchor='center', padx=5)
            ttk.Radiobutton(group_p2_hand, text='右手', variable=p2_hand, value='right')\
                .pack(side='right', expand=1, anchor='center', padx=5)
        elif self.m_type == 2:
            # ---------------------------------------- #
            # team A                                   #  
            # ---------------------------------------- #
            group_ta = ttk.LabelFrame(self.window, text='A队')
            group_ta.pack(side='left', expand=1, anchor='center', pady=5)
            # ----------------------------------------
            # player1
            # ----------------------------------------
            group_p1 = ttk.LabelFrame(group_ta, text='球员1')
            group_p1.pack(side='top', expand=1, anchor='center', pady=5)
            # ~~~~~~~~~~~~~
            # player1 name
            # ~~~~~~~~~~~~~
            group_p1_name = ttk.Frame(group_p1)
            group_p1_name.pack(side='top', expand=1, anchor='center')
            ttk.Label(group_p1_name, text='姓名：')\
                .pack(side='left', expand=1, anchor='center', padx=5)
            entry_p1_name = ttk.Entry(group_p1_name, show=None)
            entry_p1_name.pack(side='right', expand=1, anchor='center', padx=5)
            # ~~~~~~~~~~~~~
            # player1 hand
            # ~~~~~~~~~~~~~
            group_p1_hand = ttk.Frame(group_p1)
            group_p1_hand.pack(side='top', expand=1, anchor='center')
            p1_hand = tk.StringVar()
            ttk.Radiobutton(group_p1_hand, text='左手', variable=p1_hand, value='left')\
                .pack(side='left', expand=1, anchor='center', padx=5)
            ttk.Radiobutton(group_p1_hand, text='右手', variable=p1_hand, value='right')\
                .pack(side='right', expand=1, anchor='center', padx=5)

            # ----------------------------------------
            # player2
            # ----------------------------------------
            group_p2 = ttk.LabelFrame(group_ta, text='球员2')
            group_p2.pack(side='top', expand=1, anchor='center', pady=5)
            # ~~~~~~~~~~~~~
            # player2 name
            # ~~~~~~~~~~~~~
            group_p2_name = ttk.Frame(group_p2)
            group_p2_name.pack(side='top', expand=1, anchor='center')
            ttk.Label(group_p2_name, text='姓名：')\
                .pack(side='left', expand=1, anchor='center', padx=5)
            entry_p2_name = ttk.Entry(group_p2_name, show=None)
            entry_p2_name.pack(side='right', expand=1, anchor='center', padx=5)
            # ~~~~~~~~~~~~~
            # player2 hand
            # ~~~~~~~~~~~~~
            group_p2_hand = ttk.Frame(group_p2)
            group_p2_hand.pack(side='top', expand=1, anchor='center')
            p2_hand = tk.StringVar()
            ttk.Radiobutton(group_p2_hand, text='左手', variable=p2_hand, value='left')\
                .pack(side='left', expand=1, anchor='center', padx=5)
            ttk.Radiobutton(group_p2_hand, text='右手', variable=p2_hand, value='right')\
                .pack(side='right', expand=1, anchor='center', padx=5)
            # ---------------------------------------- #
            # team B                                   # 
            # ---------------------------------------- #
            group_tb = ttk.LabelFrame(self.window, text='B队')
            group_tb.pack(side='right', expand=1, anchor='center', pady=5)
            # ----------------------------------------
            # player3
            # ----------------------------------------
            group_p3 = ttk.LabelFrame(group_tb, text='球员3')
            group_p3.pack(side='top', expand=1, anchor='center', pady=5)
            # ~~~~~~~~~~~~~
            # player3 name
            # ~~~~~~~~~~~~~
            group_p3_name = ttk.Frame(group_p3)
            group_p3_name.pack(side='top', expand=1, anchor='center')
            ttk.Label(group_p3_name, text='姓名：')\
                .pack(side='left', expand=1, anchor='center', padx=5)
            entry_p3_name = ttk.Entry(group_p3_name, show=None)
            entry_p3_name.pack(side='right', expand=1, anchor='center', padx=5)
            # ~~~~~~~~~~~~~
            # player3 hand
            # ~~~~~~~~~~~~~
            group_p3_hand = ttk.Frame(group_p3)
            group_p3_hand.pack(side='top', expand=1, anchor='center')
            p3_hand = tk.StringVar()
            ttk.Radiobutton(group_p3_hand, text='左手', variable=p3_hand, value='left')\
                .pack(side='left', expand=1, anchor='center', padx=5)
            ttk.Radiobutton(group_p3_hand, text='右手', variable=p3_hand, value='right')\
                .pack(side='right', expand=1, anchor='center', padx=5)

            # ----------------------------------------
            # player4
            # ----------------------------------------
            group_p4 = ttk.LabelFrame(group_tb, text='球员2')
            group_p4.pack(side='top', expand=1, anchor='center', pady=5)
            # ~~~~~~~~~~~~~
            # player4 name
            # ~~~~~~~~~~~~~
            group_p4_name = ttk.Frame(group_p4)
            group_p4_name.pack(side='top', expand=1, anchor='center')
            ttk.Label(group_p4_name, text='姓名：')\
                .pack(side='left', expand=1, anchor='center', padx=5)
            entry_p4_name = ttk.Entry(group_p4_name, show=None)
            entry_p4_name.pack(side='right', expand=1, anchor='center', padx=5)
            # ~~~~~~~~~~~~~
            # player4 hand
            # ~~~~~~~~~~~~~
            group_p4_hand = ttk.Frame(group_p4)
            group_p4_hand.pack(side='top', expand=1, anchor='center')
            p4_hand = tk.StringVar()
            ttk.Radiobutton(group_p4_hand, text='左手', variable=p4_hand, value='left')\
                .pack(side='left', expand=1, anchor='center', padx=5)
            ttk.Radiobutton(group_p4_hand, text='右手', variable=p4_hand, value='right')\
                .pack(side='right', expand=1, anchor='center', padx=5)

        # ----------------------------------------
        # collect data
        # ----------------------------------------
        ttk.Button(self.window, text='开始采集', command=button_collect, width=10)\
            .pack(side='top', expand=1, anchor='center', pady=5)
