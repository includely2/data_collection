import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import pandas as pd

class MainWindow():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("网球数据采集工具")
        self.window.geometry("275x50")
        self.window.iconbitmap("tennis.ico")
        self.window.resizable(0,0)
        self.body()

    def body(self):
        # ====================================================================
        # command
        # ====================================================================
        def button_new():
            NewMatchWindow(self.window)

        # ====================================================================
        # widget
        # ====================================================================
        # ----------------------------------------
        # new match
        # ----------------------------------------
        ttk.Button(self.window, text="新建比赛", command=button_new, width=10)\
            .pack(side="left", expand=1, anchor="center", padx=5)

        # ----------------------------------------
        # exit
        # ----------------------------------------
        ttk.Button(self.window, text="退出", command=self.window.destroy, width=10)\
            .pack(side="right", expand=1, anchor="center", padx=5)


class NewMatchWindow():
    def __init__(self, top):
        self.top = top
        self.window = tk.Toplevel(top)
        self.window.title("新建比赛")
        self.window.geometry("300x200")
        self.window.iconbitmap("tennis.ico")
        self.window.resizable(0,0)
        self.body()

    def body(self):
        # ====================================================================
        # command
        # ====================================================================
        def button_collect():
            m = entry_match_name.get()
            p1 = entry_p1_name.get()
            p2 = entry_p2_name.get()
            p1_h = p1_hand.get()
            p2_h = p2_hand.get()
            if m == "":
                msg.showerror(title="错误", message="请输入比赛名称！")
            elif p1 == "" or p2 == "":
                msg.showerror(title="错误", message="请输入球员姓名！")
            elif p1_h == "" or p2_h == "":
                msg.showerror(title="错误", message="请选择球员惯用手")
            else:
                self.window.destroy()
                CollectDataWindow(m, p1, p2, p1_h, p2_h, self.top).window.mainloop()
                # CollectDataWindow(m, p1, p2, p1_h, p2_h).window.mainloop()

        # ====================================================================
        # widget
        # ====================================================================
        # ----------------------------------------
        # match name
        # ----------------------------------------
        group_match_name = ttk.Frame(self.window)
        group_match_name.pack(side="top", expand=1, anchor="center")
        ttk.Label(group_match_name, text="比赛名称：")\
            .pack(side="left", expand=1, anchor="center", padx=5)
        entry_match_name = ttk.Entry(group_match_name, show=None)
        entry_match_name.pack(side="right", expand=1, anchor="center", padx=5)

        # ----------------------------------------
        # player1
        # ----------------------------------------
        group_p1 = ttk.LabelFrame(self.window, text="球员1")
        group_p1.pack(side="top", expand=1, anchor="center")
        # ~~~~~~~~~~~~~
        # player1 name
        # ~~~~~~~~~~~~~
        group_p1_name = ttk.Frame(group_p1)
        group_p1_name.pack(side="top", expand=1, anchor="center")
        ttk.Label(group_p1_name, text="姓名：")\
            .pack(side="left", expand=1, anchor="center", padx=5)
        entry_p1_name = ttk.Entry(group_p1_name, show=None)
        entry_p1_name.pack(side="right", expand=1, anchor="center", padx=5)
        # ~~~~~~~~~~~~~
        # player1 hand
        # ~~~~~~~~~~~~~
        group_p1_hand = ttk.Frame(group_p1)
        group_p1_hand.pack(side="top", expand=1, anchor="center")
        p1_hand = tk.StringVar()
        ttk.Radiobutton(group_p1_hand, text="左手", variable=p1_hand, value="left")\
            .pack(side="left", expand=1, anchor="center", padx=5)
        ttk.Radiobutton(group_p1_hand, text="右手", variable=p1_hand, value="right")\
            .pack(side="right", expand=1, anchor="center", padx=5)

        # ----------------------------------------
        # player2
        # ----------------------------------------
        group_p2 = ttk.LabelFrame(self.window, text="球员2")
        group_p2.pack(side="top", expand=1, anchor="center")
        # ~~~~~~~~~~~~~
        # player2 name
        # ~~~~~~~~~~~~~
        group_p2_name = ttk.Frame(group_p2)
        group_p2_name.pack(side="top", expand=1, anchor="center")
        ttk.Label(group_p2_name, text="姓名：")\
            .pack(side="left", expand=1, anchor="center", padx=5)
        entry_p2_name = ttk.Entry(group_p2_name, show=None)
        entry_p2_name.pack(side="right", expand=1, anchor="center", padx=5)
        # ~~~~~~~~~~~~~
        # player2 hand
        # ~~~~~~~~~~~~~
        group_p2_hand = ttk.Frame(group_p2)
        group_p2_hand.pack(side="top", expand=1, anchor="center")
        p2_hand = tk.StringVar()
        ttk.Radiobutton(group_p2_hand, text="左手", variable=p2_hand, value="left")\
            .pack(side="left", expand=1, anchor="center", padx=5)
        ttk.Radiobutton(group_p2_hand, text="右手", variable=p2_hand, value="right")\
            .pack(side="right", expand=1, anchor="center", padx=5)

        # ----------------------------------------
        # collect data
        # ----------------------------------------
        ttk.Button(self.window, text="开始采集", command=button_collect, width=10)\
            .pack(side="top", expand=1, anchor="center")


class CollectDataWindow():
    def __init__(self, match_name, player1_name, player2_name, player1_hand, player2_hand, top):
        self.m_name = match_name
        self.p1_name = player1_name
        self.p2_name = player2_name
        self.p1_hand = player1_hand
        self.p2_hand = player2_hand

        self.window = tk.Toplevel(top)
        # self.window = tk.Tk()
        self.window.title("数据采集")
        self.window.geometry("500x700")
        self.window.iconbitmap("tennis.ico")
        self.window.resizable(0,0)
        self.body()

        self.data = pd.DataFrame(columns=["盘", "局", "分", "球", "球员", "站位", "技术", "落点", "状态", "效果", "分1", "分2", "局1", "局2", "盘1", "盘2"])

    def body(self):
        # ====================================================================
        # command
        # ====================================================================
        def button_begin():
            set_p1.set("0")
            set_p2.set("0")
            game_p1.set("0")
            game_p2.set("0")
            score_p1.set("0")
            score_p2.set("0")

        def button_change():
            temp = p_up.get()
            p_up.set(p_down.get())
            p_down.set(temp)

        # ----------------------------------------
        # court
        # ----------------------------------------
        def court_up1():
            return 0
        def court_up2():
            return 0
        def court_up3():
            return 0
        def court_up4():
            return 0
        def court_up5():
            return 0
        def court_up6():
            return 0
        def court_up7():
            return 0
        def court_up8():
            return 0
        def court_up9():
            return 0
        def court_up10():
            return 0
        def court_up11():
            return 0
        def court_up12():
            return 0
        def court_up13():
            return 0
        def court_up14():
            return 0
        def court_up15():
            return 0
        def court_up16():
            return 0
        def court_up17():
            return 0
        def court_up18():
            return 0
        def court_up19():
            return 0
        def court_up20():
            return 0
        def court_up21():
            return 0
        def court_up22():
            return 0
        def court_up23():
            return 0
        def court_up24():
            return 0
        def court_up25():
            return 0
        def court_up26():
            return 0
        def court_up27():
            return 0
        def court_up28():
            return 0
        def court_up29():
            return 0
        def court_up30():
            return 0
        def court_up31():
            return 0
        def court_up32():
            return 0
        def court_up33():
            return 0
        def court_up34():
            return 0
        def court_up35():
            return 0
        def court_up36():
            return 0
        def court_up37():
            return 0
        def court_up38():
            return 0
        def court_up39():
            return 0
        def court_up40():
            return 0
        def court_up41():
            return 0
        def court_up42():
            return 0
        def court_down1():
            return 0
        def court_down2():
            return 0
        def court_down3():
            return 0
        def court_down4():
            return 0
        def court_down5():
            return 0
        def court_down6():
            return 0
        def court_down7():
            return 0
        def court_down8():
            return 0
        def court_down9():
            return 0
        def court_down10():
            return 0
        def court_down11():
            return 0
        def court_down12():
            return 0
        def court_down13():
            return 0
        def court_down14():
            return 0
        def court_down15():
            return 0
        def court_down16():
            return 0
        def court_down17():
            return 0
        def court_down18():
            return 0
        def court_down19():
            return 0
        def court_down20():
            return 0
        def court_down21():
            return 0
        def court_down22():
            return 0
        def court_down23():
            return 0
        def court_down24():
            return 0
        def court_down25():
            return 0
        def court_down26():
            return 0
        def court_down27():
            return 0
        def court_down28():
            return 0
        def court_down29():
            return 0
        def court_down30():
            return 0
        def court_down31():
            return 0
        def court_down32():
            return 0
        def court_down33():
            return 0
        def court_down34():
            return 0
        def court_down35():
            return 0
        def court_down36():
            return 0
        def court_down37():
            return 0
        def court_down38():
            return 0
        def court_down39():
            return 0
        def court_down40():
            return 0
        def court_down41():
            return 0
        def court_down42():
            return 0

        # ----------------------------------------
        # technique
        # ----------------------------------------
        def tech1():
            return 0
        def tech2():
            return 0
        def tech3():
            return 0
        def tech4():
            return 0
        def tech5():
            return 0
        def tech6():
            return 0
        def tech7():
            return 0
        def tech8():
            return 0
        def tech9():
            return 0
        def tech10():
            return 0
        def tech11():
            return 0
        def tech12():
            return 0
        def tech13():
            return 0
        def tech14():
            return 0

        # ----------------------------------------
        # state
        # ----------------------------------------
        def state1():
            return 0
        def state2():
            return 0
        def state3():
            return 0
        def state4():
            return 0
        def state5():
            return 0
        def state6():
            return 0
        def state7():
            return 0
        def state8():
            return 0

        # ----------------------------------------
        # score board
        # ----------------------------------------
        def set_plus(player):
            set_ = set_p1 if player == 1 else set_p2
            set_other = set_p2 if player == 1 else set_p1
        def game_plus(player):
            game = game_p1 if player == 1 else game_p2
            game_other = game_p2 if player == 2 else game_p1
            g_value = int(game.get())
            g_other_value = int(game_other.get())
            if g_value == 6 and g_other_value == 6:
                set_plus(player)
                game.set("0")
                game_other.set("0")
            elif g_other_value == 6:
                game.set("6")
            elif g_value == 5 and g_other_value < 5:
                set_plus(player)
                game.set("0")
                game_other.set("0")
            else:
                game.set(str(g_value + 1))


        def score_plus(player):
            score = score_p1 if player == 1 else score_p2
            score_other = score_p2 if player == 1 else score_p1
            if game_p1.get() == "6" and game_p2.get() == "6":
                pass
            else:
                if score.get() == "0":
                    score.set("15")
                elif score.get() == "15":
                    score.set("30")
                elif score.get() == "30":
                    score.set("40")
                elif score.get() == "40":
                    if score_other.get() == "40":
                        score.set("AD")
                        score_other.set("-")
                    else:
                        game_plus(player)
                        score.set("0")
                        score_other.set("0")
                elif score.get() == "AD":
                    game_plus(player)
                    score.set("0")
                    score_other.set("0")
                elif score.get() == "-":
                    score.set("40")
                    score_other.set("40")
        def button_next():
            if winner.get() == self.p1_name:
                score_plus(1)
            elif winner.get() ==self.p2_name:
                score_plus(2)
            server.set("")
            winner.set("")

        def button_export():
            self.data.to_csv(self.m_name + '-p1_' + self.p1_name + '-p2_' + self.p2_name + '.csv', index=False, sep=',')
            msg.showinfo(title="提示", message="数据导出成功！")
            self.window.destroy()
        
        # ====================================================================
        # widget
        # ====================================================================
        # ----------------------------------------
        # match
        # ----------------------------------------
        ttk.Label(self.window, text="比赛名称：" + self.m_name)\
            .pack(side="top", expand=1, anchor="center", fill="x", padx=5)

        group_up = ttk.Frame(self.window)
        group_up.pack(side="top", expand=1, anchor="center", fill="x")
        # ----------------------------------------
        # info
        # ----------------------------------------
        group_info = ttk.Frame(group_up)
        group_info.pack(side="left", expand=1, anchor="w")
        # ~~~~~~~~~~~~~
        # player info
        # ~~~~~~~~~~~~~
        group_p = ttk.LabelFrame(group_info, text="球员信息")
        group_p.pack(side="top", expand=1, anchor="w", padx=5, pady=5)

        group_p1 = ttk.Frame(group_p)
        group_p1.pack(side="top", expand=1, anchor="center", fill="x")
        ttk.Label(group_p1, text="球员1：" + self.p1_name, width=15)\
            .pack(side="left", expand=1, anchor="center", padx=5)
        hand = "左手" if self.p1_hand == "left" else "右手"
        ttk.Label(group_p1, text="持拍手：" + hand)\
            .pack(side="right", expand=1, anchor="center", padx=5)

        group_p2 = ttk.Frame(group_p)
        group_p2.pack(side="top", expand=1, anchor="center", fill="x")
        ttk.Label(group_p2, text="球员2：" + self.p2_name, width=15)\
            .pack(side="left", expand=1, anchor="center", padx=5)
        hand = "左手" if self.p2_hand == "left" else "右手"
        ttk.Label(group_p2, text="持拍手：" + hand)\
            .pack(side="right", expand=1, anchor="center", padx=5)
        # ~~~~~~~~~~~~~
        # serve
        # ~~~~~~~~~~~~~
        group_serve = ttk.LabelFrame(group_info, text="发球方：")
        group_serve.pack(side="top", expand=1, anchor="w", padx=5, pady=5)
        server = tk.StringVar()
        ttk.Radiobutton(group_serve, text=self.p1_name, variable=server, value=self.p1_name)\
            .pack(side="left", expand=1, anchor="w", padx=5)
        ttk.Radiobutton(group_serve, text=self.p2_name, variable=server, value=self.p2_name)\
            .pack(side="right", expand=1, anchor="w", padx=5)
        
        # ----------------------------------------
        # score
        # ----------------------------------------
        group_score = ttk.Frame(group_up)
        group_score.pack(side="right", expand=1, anchor="w")
        # ~~~~~~~~~~~~~
        # begin playing
        # ~~~~~~~~~~~~~
        ttk.Button(group_score, text="开始比赛", command=button_begin, width=10)\
            .pack(side="top", expand=1, anchor="center")
        # ~~~~~~~~~~~~~
        # score board
        # ~~~~~~~~~~~~~
        group_board = ttk.LabelFrame(group_score, text="比分")
        group_board.pack(side="top", expand=1, anchor="center")
        # line 1 ========================
        board_l1 = ttk.Frame(group_board)
        board_l1.pack(side="top", expand=1, anchor="center")
        ttk.Label(board_l1, text=self.p1_name)\
            .pack(side="left", expand=1, anchor="center", padx=5)
        ttk.Label(board_l1, text=":")\
            .pack(side="left", expand=1, anchor="center", padx=5)
        ttk.Label(board_l1, text=self.p2_name)\
            .pack(side="right", expand=1, anchor="center", padx=5)
        # line 2 ========================
        board_l2 = ttk.Frame(group_board)
        board_l2.pack(side="top", expand=1, anchor="w", pady=1)
        ttk.Label(board_l2, text="盘分")\
            .pack(side="left", expand=1, anchor="center", padx=5)
        set_p1 = tk.StringVar()
        tk.Label(board_l2, textvariable=set_p1, width=3, bg="white")\
            .pack(side="left", expand=1, anchor="center")
        ttk.Label(board_l2, text=":")\
            .pack(side="left", expand=1, anchor="center")
        set_p2 = tk.StringVar()
        tk.Label(board_l2, textvariable=set_p2, width=3, bg="white")\
            .pack(side="left", expand=1, anchor="center")
        # line 3 ========================
        board_l3 = ttk.Frame(group_board)
        board_l3.pack(side="top", expand=1, anchor="w", pady=1)
        ttk.Label(board_l3, text="局分")\
            .pack(side="left", expand=1, anchor="center", padx=5)
        game_p1 = tk.StringVar()
        tk.Label(board_l3, textvariable=game_p1, width=3, bg="white")\
            .pack(side="left", expand=1, anchor="center")
        ttk.Label(board_l3, text=":")\
            .pack(side="left", expand=1, anchor="center")
        game_p2 = tk.StringVar()
        tk.Label(board_l3, textvariable=game_p2, width=3, bg="white")\
            .pack(side="left", expand=1, anchor="center")
        # line 4 ========================
        board_l4 = ttk.Frame(group_board)
        board_l4.pack(side="top", expand=1, anchor="w", pady=1)
        ttk.Label(board_l4, text="小分")\
            .pack(side="left", expand=1, anchor="center", padx=5)
        score_p1 = tk.StringVar()
        tk.Label(board_l4, textvariable=score_p1, width=3, bg="white")\
            .pack(side="left", expand=1, anchor="center")
        ttk.Label(board_l4, text=":")\
            .pack(side="left", expand=1, anchor="center")
        score_p2 = tk.StringVar()
        tk.Label(board_l4, textvariable=score_p2, width=3, bg="white")\
            .pack(side="left", expand=1, anchor="center")
        # ----------------------------------------
        # date collection
        # ----------------------------------------
        group_data = ttk.Frame(self.window)
        group_data.pack(side="top", expand=1, anchor="center")
        # ~~~~~~~~~~~~~
        # change court
        # ~~~~~~~~~~~~~
        group_change = ttk.Frame(group_data)
        group_change.pack(side="left", expand=1, anchor="center")
        p_up = tk.StringVar()
        p_up.set(self.p2_name)
        ttk.Label(group_change, textvariable=p_up)\
            .pack(side="top", expand=1, anchor="center")
        ttk.Button(group_change, text="交换场地", command=button_change, width=10)\
            .pack(side="top", expand=1, anchor="center", padx=5)
        p_down = tk.StringVar()
        p_down.set(self.p1_name)
        ttk.Label(group_change, textvariable=p_down)\
            .pack(side="top", expand=1, anchor="center")
        # ~~~~~~~~~~~~~
        # court placement
        # ~~~~~~~~~~~~~
        group_court = ttk.Frame(group_data)
        group_court.pack(side="left", expand=1, anchor="center", padx=5)
        # line 1 ========================
        court_l1 = ttk.Frame(group_court)
        court_l1.pack(side="top", expand=1, anchor="center")
        tk.Button(court_l1, text="31", command=court_up31, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l1, text="27", command=court_up27, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l1, text="28", command=court_up28, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l1, text="29", command=court_up29, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l1, text="30", command=court_up30, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l1, text="32", command=court_up32, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        # line 2 ========================
        court_l2 = ttk.Frame(group_court)
        court_l2.pack(side="top", expand=1, anchor="center")
        tk.Button(court_l2, text="33", command=court_up33, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l2, text="23", command=court_up23, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l2, text="24", command=court_up24, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l2, text="25", command=court_up25, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l2, text="26", command=court_up26, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l2, text="34", command=court_up34, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        # line 3 ========================
        court_l3 = ttk.Frame(group_court)
        court_l3.pack(side="top", expand=1, anchor="center")
        tk.Button(court_l3, text="35", command=court_up35, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l3, text="7", command=court_up7, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l3, text="8", command=court_up8, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l3, text="9", command=court_up9, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l3, text="10", command=court_up10, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l3, text="36", command=court_up36, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        # line 4 ========================
        court_l4 = ttk.Frame(group_court)
        court_l4.pack(side="top", expand=1, anchor="center")
        tk.Button(court_l4, text="37", command=court_up37, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l4, text="11", command=court_up11, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l4, text="12", command=court_up12, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l4, text="13", command=court_up13, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l4, text="14", command=court_up14, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l4, text="38", command=court_up38, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        # line 5 ========================
        court_l5 = ttk.Frame(group_court)
        court_l5.pack(side="top", expand=1, anchor="center")
        tk.Button(court_l5, text="1", command=court_up1, width=3, bg="cadetblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l5, text="2", command=court_up2, width=3, bg="cadetblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l5, text="3", command=court_up3, width=3, bg="cadetblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l5, text="4", command=court_up4, width=3, bg="cadetblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l5, text="5", command=court_up5, width=3, bg="cadetblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l5, text="6", command=court_up6, width=3, bg="cadetblue")\
            .pack(side="left", expand=1, anchor="center")
        # line 6 ========================
        court_l6 = ttk.Frame(group_court)
        court_l6.pack(side="top", expand=1, anchor="center")
        tk.Button(court_l6, text="39", command=court_up39, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l6, text="15", command=court_up15, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l6, text="16", command=court_up16, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l6, text="17", command=court_up17, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l6, text="18", command=court_up18, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l6, text="40", command=court_up40, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        # line 7 ========================
        court_l7 = ttk.Frame(group_court)
        court_l7.pack(side="top", expand=1, anchor="center")
        tk.Button(court_l7, text="41", command=court_up41, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l7, text="19", command=court_up19, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l7, text="20", command=court_up20, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l7, text="21", command=court_up21, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l7, text="22", command=court_up22, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l7, text="42", command=court_up42, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        # line net ========================
        ttk.Label(group_court, text="------球网------------球网------")\
            .pack(side="top", expand=1, anchor="center")
                # line 8 ========================
        court_l8 = ttk.Frame(group_court)
        court_l8.pack(side="top", expand=1, anchor="center")
        tk.Button(court_l8, text="42", command=court_down42, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l8, text="22", command=court_down22, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l8, text="21", command=court_down21, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l8, text="20", command=court_down20, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l8, text="19", command=court_down19, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l8, text="41", command=court_down41, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        # line 9 ========================
        court_l9 = ttk.Frame(group_court)
        court_l9.pack(side="top", expand=1, anchor="center")
        tk.Button(court_l9, text="40", command=court_down40, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l9, text="18", command=court_down18, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l9, text="17", command=court_down17, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l9, text="16", command=court_down16, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l9, text="15", command=court_down15, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l9, text="39", command=court_down39, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        # line 10 ========================
        court_l10 = ttk.Frame(group_court)
        court_l10.pack(side="top", expand=1, anchor="center")
        tk.Button(court_l10, text="6", command=court_down6, width=3, bg="cadetblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l10, text="5", command=court_down5, width=3, bg="cadetblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l10, text="4", command=court_down4, width=3, bg="cadetblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l10, text="3", command=court_down3, width=3, bg="cadetblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l10, text="2", command=court_down2, width=3, bg="cadetblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l10, text="1", command=court_down1, width=3, bg="cadetblue")\
            .pack(side="left", expand=1, anchor="center")
        # line 11 ========================
        court_l11 = ttk.Frame(group_court)
        court_l11.pack(side="top", expand=1, anchor="center")
        tk.Button(court_l11, text="38", command=court_down38, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l11, text="14", command=court_down14, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l11, text="13", command=court_down13, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l11, text="12", command=court_down12, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l11, text="11", command=court_down11, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l11, text="37", command=court_down37, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        # line 12 ========================
        court_l12 = ttk.Frame(group_court)
        court_l12.pack(side="top", expand=1, anchor="center")
        tk.Button(court_l12, text="36", command=court_down36, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l12, text="10", command=court_down10, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l12, text="9", command=court_down9, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l12, text="8", command=court_down8, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l12, text="7", command=court_down7, width=3, bg="deepskyblue")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l12, text="35", command=court_down35, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        # line 13 ========================
        court_l13 = ttk.Frame(group_court)
        court_l13.pack(side="top", expand=1, anchor="center")
        tk.Button(court_l13, text="34", command=court_down34, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l13, text="26", command=court_down26, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l13, text="25", command=court_down25, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l13, text="24", command=court_down24, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l13, text="23", command=court_down23, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l13, text="33", command=court_down33, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        # line 14 ========================
        court_l14 = ttk.Frame(group_court)
        court_l14.pack(side="top", expand=1, anchor="center")
        tk.Button(court_l14, text="32", command=court_down32, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l14, text="30", command=court_down30, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l14, text="29", command=court_down29, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l14, text="28", command=court_down28, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l14, text="27", command=court_down27, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        tk.Button(court_l14, text="31", command=court_down31, width=3, bg="green")\
            .pack(side="left", expand=1, anchor="center")
        # ~~~~~~~~~~~~~
        # technique & state choice
        # ~~~~~~~~~~~~~
        group_choice = ttk.Frame(group_data)
        group_choice.pack(side="right", expand=1, anchor="n")
        # technique choice
        group_tech = ttk.LabelFrame(group_choice, text="技术")
        group_tech.pack(side="top", expand=1, anchor="center", pady=5)
        # line 1 ========================
        tech_l1 = ttk.Frame(group_tech)
        tech_l1.pack(side="top", expand=1, anchor="center")
        ttk.Button(tech_l1, text="1  一区一发", command=tech1, width=10)\
            .pack(side="left", expand=1, anchor="center")
        ttk.Button(tech_l1, text="2  一区二发", command=tech2, width=10)\
            .pack(side="right", expand=1, anchor="center")
        # line 2 ========================
        tech_l2 = ttk.Frame(group_tech)
        tech_l2.pack(side="top", expand=1, anchor="center")
        ttk.Button(tech_l2, text="3  二区一发", command=tech3, width=10)\
            .pack(side="left", expand=1, anchor="center")
        ttk.Button(tech_l2, text="4  二区二发", command=tech4, width=10)\
            .pack(side="right", expand=1, anchor="center")
        # line 3 ========================
        tech_l3 = ttk.Frame(group_tech)
        tech_l3.pack(side="top", expand=1, anchor="center")
        ttk.Button(tech_l3, text="5  正手抽击", command=tech5, width=10)\
            .pack(side="left", expand=1, anchor="center")
        ttk.Button(tech_l3, text="6  反手抽击", command=tech6, width=10)\
            .pack(side="right", expand=1, anchor="center")
        # line 4 ========================
        tech_l4 = ttk.Frame(group_tech)
        tech_l4.pack(side="top", expand=1, anchor="center")
        ttk.Button(tech_l4, text="7  正手截击", command=tech7, width=10)\
            .pack(side="left", expand=1, anchor="center")
        ttk.Button(tech_l4, text="8  反手截击", command=tech8, width=10)\
            .pack(side="right", expand=1, anchor="center")
        # line 5 ========================
        tech_l5 = ttk.Frame(group_tech)
        tech_l5.pack(side="top", expand=1, anchor="center")
        ttk.Button(tech_l5, text="9  高压球  ", command=tech9, width=10)\
            .pack(side="left", expand=1, anchor="center")
        ttk.Button(tech_l5, text="10 削球    ", command=tech10, width=10)\
            .pack(side="right", expand=1, anchor="center")
        # line 6 ========================
        tech_l6 = ttk.Frame(group_tech)
        tech_l6.pack(side="top", expand=1, anchor="center")
        ttk.Button(tech_l6, text="11 挑高球  ", command=tech11, width=10)\
            .pack(side="left", expand=1, anchor="center")
        ttk.Button(tech_l6, text="12 放小球  ", command=tech12, width=10)\
            .pack(side="right", expand=1, anchor="center")
        # line 7 ========================
        tech_l7 = ttk.Frame(group_tech)
        tech_l7.pack(side="top", expand=1, anchor="center")
        ttk.Button(tech_l7, text="13 推挡    ", command=tech13, width=10)\
            .pack(side="left", expand=1, anchor="center")
        ttk.Button(tech_l7, text="0  无技术  ", command=tech14, width=10)\
            .pack(side="right", expand=1, anchor="center")
        # state choice
        group_state = ttk.LabelFrame(group_choice, text="状态")
        group_state.pack(side="top", expand=1, anchor="center", pady=5)
        # line 1 ========================
        state_l1 = ttk.Frame(group_state)
        state_l1.pack(side="top", expand=1, anchor="center")
        ttk.Button(state_l1, text="1 界内有效", command=state1, width=10)\
            .pack(side="left", expand=1, anchor="center")
        ttk.Button(state_l1, text="2 出界球  ", command=state2, width=10)\
            .pack(side="right", expand=1, anchor="center")
        # line 2 ========================
        state_l2 = ttk.Frame(group_state)
        state_l2.pack(side="top", expand=1, anchor="center")
        ttk.Button(state_l2, text="3 下网球  ", command=state3, width=10)\
            .pack(side="left", expand=1, anchor="center")
        ttk.Button(state_l2, text="4 擦网球  ", command=state4, width=10)\
            .pack(side="right", expand=1, anchor="center")
        # line 3 ========================
        state_l3 = ttk.Frame(group_state)
        state_l3.pack(side="top", expand=1, anchor="center")
        ttk.Button(state_l3, text="5 被拦网  ", command=state5, width=10)\
            .pack(side="left", expand=1, anchor="center")
        ttk.Button(state_l3, text="6 未过网  ", command=state6, width=10)\
            .pack(side="right", expand=1, anchor="center")
        # line 4 ========================
        state_l4 = ttk.Frame(group_state)
        state_l4.pack(side="top", expand=1, anchor="center")
        ttk.Button(state_l4, text="7 被穿越  ", command=state7, width=10)\
            .pack(side="left", expand=1, anchor="center")
        ttk.Button(state_l4, text="8 界内无效", command=state8, width=10)\
            .pack(side="right", expand=1, anchor="center")
        # ~~~~~~~~~~~~~
        # winner
        # ~~~~~~~~~~~~~
        group_winner = ttk.LabelFrame(group_choice, text="得分方")
        group_winner.pack(side="top", expand=1, anchor="center", pady=5)
        winner = tk.StringVar()
        ttk.Radiobutton(group_winner, text=self.p1_name, variable=winner, value=self.p1_name)\
            .pack(side="left", expand=1, anchor="center", padx=5)
        ttk.Radiobutton(group_winner, text=self.p2_name, variable=winner, value=self.p2_name)\
            .pack(side="right", expand=1, anchor="center", padx=5)
        # ~~~~~~~~~~~~~
        # next ball
        # ~~~~~~~~~~~~~
        ttk.Button(group_choice, text="下一分", command=button_next)\
            .pack(side="bottom", expand=1, anchor="center", pady=5)

        # ----------------------------------------
        # export data
        # ----------------------------------------
        ttk.Button(self.window, text="导出数据", command=button_export, width=10)\
            .pack(side="bottom", expand=1, anchor="center")


if __name__ == "__main__":
    win = MainWindow()
    win.window.mainloop()
    # test = CollectDataWindow("ATP1000", "Federer", "Nadal", "right", "left")
    # test.window.mainloop()