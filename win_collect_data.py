import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import pandas as pd
import numpy as np
import time

class CollectDataWindow():
    def __init__(self, match_name, player1_name, player2_name, player1_hand, player2_hand, set_number, decide_set, top, is_read=False, dataframe=None):
        self.m_name = match_name
        self.p1_name = player1_name
        self.p2_name = player2_name
        self.p1_hand = player1_hand
        self.p2_hand = player2_hand
        self.s_no = set_number
        self.d_set = decide_set
        self.file_name = self.m_name + \
                         '-p1_' + self.p1_name + '_' + self.p1_hand + \
                         '-p2_' + self.p2_name + '_' + self.p2_hand + \
                         '-' + str(self.s_no) + '-' + self.d_set + '.csv'

        self.window = tk.Toplevel(top)
        self.window.title('数据采集')
        self.window.geometry('1050x700')
        self.window.iconbitmap('tennis.ico')
        # self.window.resizable(0,0)

        self.col_name = ['盘', '局', '分', '球', '球员', '站位', '技术', '落点', '状态', '效果', '分1', '分2', '局1', '局2', '盘1', '盘2']
        self.is_read = is_read
        if is_read == False:
            self.data = pd.DataFrame(columns=self.col_name)
        else:
            self.data = dataframe
        self.data_len = len(self.data.columns)
        self.point = np.zeros((1, self.data_len), dtype=int)
        self.is_tiebreak = False

        self.set = 0
        self.game = 0
        self.score = 0
        self.score1 = 0
        self.score2 = 0
        self.game1 = 0
        self.game2 = 0
        self.set1 = 0
        self.set2 = 0

        self.body()

    def body(self):
        data_dict = {'set': 0,  # 盘
                    'game': 1,  # 局
                    'score': 2,  # 分 
                    'rally': 3,  # 球
                    'player': 4,  # 球员
                    'position': 5,  # 站位
                    'tech': 6,  # 技术
                    'place': 7,  # 落点
                    'state': 8,  # 状态
                    'winner': 9,  # 效果
                    'score1': 10,  # 分1
                    'score2': 11,  # 分2
                    'game1': 12,  # 局1
                    'game2': 13,  # 局2
                    'set1': 14,  # 盘1
                    'set2': 15  # 盘2
                    }
        # ====================================================================
        # command
        # ====================================================================
        def button_begin():
            begin.state(['disabled'])
            if self.is_read == False:
                # update score board
                set_p1.set('0')
                set_p2.set('0')
                game_p1.set('0')
                game_p2.set('0')
                score_p1.set('0')
                score_p2.set('0')
                # update self.point
                self.point[0][data_dict['set']] = 1
                self.point[0][data_dict['game']] = 1
                self.point[0][data_dict['score']] = 1
                self.point[0][data_dict['rally']] = 1
            else:
                # update score board
                set_p1.set(str(self.data.iloc[-1][data_dict['set1']]))
                set_p2.set(str(self.data.iloc[-1][data_dict['set2']]))
                game_p1.set(str(self.data.iloc[-1][data_dict['game1']]))
                game_p2.set(str(self.data.iloc[-1][data_dict['game2']]))

                if int(set_p1.get()) != self.s_no - 1 or int(set_p2.get()) != self.s_no - 1 or \
                (int(set_p1.get()) == self.s_no - 1 and int(set_p2.get()) == self.s_no - 1 and self.d_set == '6tie7'):
                    if game_p1.get() == '6' and game_p2.get() == '6':
                        self.is_tiebreak = True
                    else:
                        self.is_tiebreak = False
                elif int(set_p1.get()) == self.s_no - 1 and int(set_p2.get()) == self.s_no - 1 and self.d_set == 'tie7':
                    self.is_tiebreak = True
                elif int(set_p1.get()) == self.s_no - 1 and int(set_p2.get()) == self.s_no - 1 and self.d_set == 'tie10':
                    self.is_tiebreak = True
                elif int(set_p1.get()) == self.s_no - 1 and int(set_p2.get()) == self.s_no - 1 and self.d_set == '6tie10':
                    if game_p1.get() == '6' and game_p2.get() == '6':
                        self.is_tiebreak = True
                    else:
                        self.is_tiebreak = False
                elif int(set_p1.get()) == self.s_no - 1 and int(set_p2.get()) == self.s_no - 1 and self.d_set == '12tie7':
                    if game_p1.get() == '12' and game_p2.get() == '12':
                        self.is_tiebreak = True
                    else:
                        self.is_tiebreak = False
                elif int(set_p1.get()) == self.s_no - 1 and int(set_p2.get()) == self.s_no - 1 and self.d_set == 'long':
                    self.is_tiebreak = False

                if self.is_tiebreak == False:
                    int_score_array = ['0', '15', '30', '40']
                    score_p1_tmp = self.data.iloc[-1][data_dict['score1']]
                    score_p2_tmp = self.data.iloc[-1][data_dict['score2']]
                    if score_p1_tmp <= 3 and score_p2_tmp <= 3:
                        score_p1.set(int_score_array[score_p1_tmp])
                        score_p2.set(int_score_array[score_p2_tmp])
                    elif score_p1_tmp == score_p2_tmp:
                        score_p1.set('40')
                        score_p2.set('40')
                    elif score_p1_tmp > score_p2_tmp:
                        score_p1.set('AD')
                        score_p2.set('-')
                    elif score_p1_tmp < score_p2_tmp:
                        score_p1.set('-')
                        score_p2.set('AD')
                else:
                    score_p1.set(self.data.iloc[-1][data_dict['score1']])
                    score_p2.set(self.data.iloc[-1][data_dict['score2']])
                # update self.point
                if self.data.iloc[-1][data_dict['score1']] == 0 and \
                    self.data.iloc[-1][data_dict['score2']] == 0 and \
                    self.data.iloc[-1][data_dict['game1']] == 0 and \
                    self.data.iloc[-1][data_dict['game2']] == 0 and \
                    (self.data.iloc[-1][data_dict['set1']] != 0 or \
                    self.data.iloc[-1][data_dict['set2']] != 0):
                    self.point[0][data_dict['set']] = self.data.iloc[-1][data_dict['set']] + 1
                else:
                    self.point[0][data_dict['set']] = self.data.iloc[-1][data_dict['set']]
                
                if self.data.iloc[-1][data_dict['score1']] == 0 and \
                    self.data.iloc[-1][data_dict['score2']] == 0:
                    self.point[0][data_dict['game']] = self.data.iloc[-1][data_dict['game']] + 1
                else:
                    self.point[0][data_dict['game']] = self.data.iloc[-1][data_dict['game']]
                
                self.point[0][data_dict['score']] = self.data.iloc[-1][data_dict['score']] + 1
                self.point[0][data_dict['rally']] = 1
                self.point[0][data_dict['score1']] = self.data.iloc[-1][data_dict['score1']]
                self.point[0][data_dict['score2']] = self.data.iloc[-1][data_dict['score2']]
                self.point[0][data_dict['game1']] = self.data.iloc[-1][data_dict['game1']]
                self.point[0][data_dict['game2']] = self.data.iloc[-1][data_dict['game2']]
                self.point[0][data_dict['set1']] = self.data.iloc[-1][data_dict['set1']]
                self.point[0][data_dict['set2']] = self.data.iloc[-1][data_dict['set2']]
                # update memory
                self.set = self.point[0][data_dict['set']] - 1
                self.game = self.point[0][data_dict['game']] - 1
                self.score = self.point[0][data_dict['score']] - 1
                # update data preview table
                for i in range(len(self.data)):
                    row = self.data.iloc[i].values.tolist()
                    table.insert('', 'end', values=row)

        def button_change():
            temp = p_up.get()
            p_up.set(p_down.get())
            p_down.set(temp)

        # ----------------------------------------
        # court
        # ----------------------------------------
        def court(position, i):
            if self.point[-1][data_dict['position']] == 0:
                self.point[-1][data_dict['position']] = i
                if position == 'up':
                    if p_up.get() == self.p1_name:
                        self.point[-1][data_dict['player']] = 1
                    elif p_up.get() == self.p2_name:
                        self.point[-1][data_dict['player']] = 2
                elif position == 'down':
                    if p_down.get() == self.p1_name:
                        self.point[-1][data_dict['player']] = 1
                    elif p_down.get() == self.p2_name:
                        self.point[-1][data_dict['player']] = 2
            elif self.point[-1][data_dict['place']] == 0:
                self.point[-1][data_dict['place']] = i

        # ----------------------------------------
        # technique
        # ----------------------------------------
        def tech(i):
            self.point[-1][data_dict['tech']] = i

        # ----------------------------------------
        # state
        # ----------------------------------------
        def state(i):
            self.point[-1][data_dict['state']] = i

        # ----------------------------------------
        # score board
        # ----------------------------------------
        def set_plus(player):
            # write self.point
            self.set = self.point[-1][data_dict['set']]
            self.point[-1][data_dict['set'+str(player)]] += 1
            self.point[-1][data_dict['game1']] = 0
            self.point[-1][data_dict['game2']] = 0
            # update score board
            set_ = set_p1 if player == 1 else set_p2
            # set_other = set_p2 if player == 1 else set_p1
            set_.set(str(int(set_.get())+1))
            if int(set_.get()) == self.s_no:
                msg.showinfo(title='提示', message='比赛结束！')
        def game_plus(player):
            # write self.point
            self.game = self.point[-1][data_dict['game']]
            self.point[-1][data_dict['game'+str(player)]] += 1
            self.point[-1][data_dict['score1']] = 0
            self.point[-1][data_dict['score2']] = 0
            # update score board
            game = game_p1 if player == 1 else game_p2
            game_other = game_p2 if player == 1 else game_p1
            g_value = int(game.get())
            g_other_value = int(game_other.get())
            # deceding set: long
            if int(set_p1.get()) == self.s_no - 1 and int(set_p2.get()) == self.s_no - 1 and self.d_set == 'long':
                game.set(str(g_value + 1))
                if g_value + 1 >= 6 and g_value + 1 > g_other_value + 1:
                    time.sleep(1)
                    set_plus(player)
                    game.set('0')
                    game_other.set('0')
            elif int(set_p1.get()) == self.s_no - 1 and int(set_p2.get()) == self.s_no - 1 and self.d_set == '12tie7':
                if g_value == 12 and g_other_value == 12:
                    game.set('13')
                    time.sleep(1)
                    set_plus(player)
                    game.set('0')
                    game_other.set('0')
                elif g_other_value == 12:
                    game.set('12')
                elif g_value == 11 and g_other_value < 11:
                    game.set('12')
                    time.sleep(1)
                    set_plus(player)
                    game.set('0')
                    game_other.set('0')
                else:
                    game.set(str(g_value + 1))
            else:
                if g_value == 6 and g_other_value == 6:
                    game.set('7')
                    time.sleep(1)
                    set_plus(player)
                    game.set('0')
                    game_other.set('0')
                elif g_other_value == 6:
                    game.set('6')
                elif g_value == 5 and g_other_value < 5:
                    game.set('6')
                    time.sleep(1)
                    set_plus(player)
                    game.set('0')
                    game_other.set('0')
                else:
                    game.set(str(g_value + 1))

        def score_plus(player):
            # write self.point
            self.score = self.point[-1][data_dict['score']]
            self.point[-1][data_dict['score'+str(player)]] += 1
            # update score board
            score = score_p1 if player == 1 else score_p2
            score_other = score_p2 if player == 1 else score_p1
            if int(set_p1.get()) != self.s_no - 1 or int(set_p2.get()) != self.s_no - 1 or \
                (int(set_p1.get()) == self.s_no - 1 and int(set_p2.get()) == self.s_no - 1 and self.d_set == '6tie7'):
                if game_p1.get() == '6' and game_p2.get() == '6':
                    self.is_tiebreak = True
                    score.set(str(int(score.get()) + 1))
                    s_value = int(score.get())
                    s_other_value = int(score_other.get())
                    if s_value == 7 and s_other_value < 6:
                        time.sleep(1)
                        game_plus(player)
                        score.set('0')
                        score_other.set('0')
                    elif s_value > 7 and s_value > s_other_value + 1:
                        time.sleep(1)
                        game_plus(player)
                        score.set('0')
                        score_other.set('0')
                else:
                    self.is_tiebreak = False
                    if score.get() == '0':
                        score.set('15')
                    elif score.get() == '15':
                        score.set('30')
                    elif score.get() == '30':
                        score.set('40')
                    elif score.get() == '40':
                        if score_other.get() == '40':
                            score.set('AD')
                            score_other.set('-')
                        else:
                            game_plus(player)
                            score.set('0')
                            score_other.set('0')
                    elif score.get() == 'AD':
                        game_plus(player)
                        score.set('0')
                        score_other.set('0')
                    elif score.get() == '-':
                        score.set('40')
                        score_other.set('40')
            elif int(set_p1.get()) == self.s_no - 1 and int(set_p2.get()) == self.s_no - 1 and self.d_set == 'tie7':
                self.is_tiebreak = True
                score.set(str(int(score.get()) + 1))
                s_value = int(score.get())
                s_other_value = int(score_other.get())
                if s_value == 7 and s_other_value < 6:
                    time.sleep(1)
                    set_plus(player)
                    score.set('0')
                    score_other.set('0')
                elif s_value > 7 and s_value > s_other_value + 1:
                    time.sleep(1)
                    set_plus(player)
                    score.set('0')
                    score_other.set('0')
            elif int(set_p1.get()) == self.s_no - 1 and int(set_p2.get()) == self.s_no - 1 and self.d_set == 'tie10':
                self.is_tiebreak = True
                score.set(str(int(score.get()) + 1))
                s_value = int(score.get())
                s_other_value = int(score_other.get())
                if s_value == 10 and s_other_value < 9:
                    time.sleep(1)
                    set_plus(player)
                    score.set('0')
                    score_other.set('0')
                elif s_value > 10 and s_value > s_other_value + 1:
                    time.sleep(1)
                    set_plus(player)
                    score.set('0')
                    score_other.set('0')
            elif int(set_p1.get()) == self.s_no - 1 and int(set_p2.get()) == self.s_no - 1 and self.d_set == '6tie10':
                if game_p1.get() == '6' and game_p2.get() == '6':
                    self.is_tiebreak = True
                    score.set(str(int(score.get()) + 1))
                    s_value = int(score.get())
                    s_other_value = int(score_other.get())
                    if s_value == 10 and s_other_value < 9:
                        time.sleep(1)
                        game_plus(player)
                        score.set('0')
                        score_other.set('0')
                    elif s_value > 10 and s_value > s_other_value + 1:
                        time.sleep(1)
                        game_plus(player)
                        score.set('0')
                        score_other.set('0')
                else:
                    self.is_tiebreak = False
                    if score.get() == '0':
                        score.set('15')
                    elif score.get() == '15':
                        score.set('30')
                    elif score.get() == '30':
                        score.set('40')
                    elif score.get() == '40':
                        if score_other.get() == '40':
                            score.set('AD')
                            score_other.set('-')
                        else:
                            game_plus(player)
                            score.set('0')
                            score_other.set('0')
                    elif score.get() == 'AD':
                        game_plus(player)
                        score.set('0')
                        score_other.set('0')
                    elif score.get() == '-':
                        score.set('40')
                        score_other.set('40')
            elif int(set_p1.get()) == self.s_no - 1 and int(set_p2.get()) == self.s_no - 1 and self.d_set == '12tie7':
                if game_p1.get() == '12' and game_p2.get() == '12':
                    self.is_tiebreak = True
                    score.set(str(int(score.get()) + 1))
                    s_value = int(score.get())
                    s_other_value = int(score_other.get())
                    if s_value == 7 and s_other_value < 6:
                        time.sleep(1)
                        game_plus(player)
                        score.set('0')
                        score_other.set('0')
                    elif s_value > 7 and s_value > s_other_value + 1:
                        time.sleep(1)
                        game_plus(player)
                        score.set('0')
                        score_other.set('0')
                else:
                    self.is_tiebreak = False
                    if score.get() == '0':
                        score.set('15')
                    elif score.get() == '15':
                        score.set('30')
                    elif score.get() == '30':
                        score.set('40')
                    elif score.get() == '40':
                        if score_other.get() == '40':
                            score.set('AD')
                            score_other.set('-')
                        else:
                            game_plus(player)
                            score.set('0')
                            score_other.set('0')
                    elif score.get() == 'AD':
                        game_plus(player)
                        score.set('0')
                        score_other.set('0')
                    elif score.get() == '-':
                        score.set('40')
                        score_other.set('40')
            elif int(set_p1.get()) == self.s_no - 1 and int(set_p2.get()) == self.s_no - 1 and self.d_set == 'long':
                self.is_tiebreak = False
                if score.get() == '0':
                    score.set('15')
                elif score.get() == '15':
                    score.set('30')
                elif score.get() == '30':
                    score.set('40')
                elif score.get() == '40':
                    if score_other.get() == '40':
                        score.set('AD')
                        score_other.set('-')
                    else:
                        game_plus(player)
                        score.set('0')
                        score_other.set('0')
                elif score.get() == 'AD':
                    game_plus(player)
                    score.set('0')
                    score_other.set('0')
                elif score.get() == '-':
                    score.set('40')
                    score_other.set('40')

        def button_next():
            if score_p1.get() == '':
                msg.showerror(title='错误', message='请点击“开始比赛”！')
            elif server.get() == '':
                msg.showerror(title='错误', message='请选择发球方！')
            elif self.point[-1][data_dict['position']] == 0:
                msg.showerror(title='错误', message='请选择站位！')
            elif self.point[-1][data_dict['place']] == 0:
                msg.showerror(title='错误', message='请选择落点！')
            elif self.point[-1][data_dict['state']] == 0:
                msg.showerror(title='错误', message='请选择状态！')
            elif winner.get() == '':
                # update table
                point_value = []
                for j in range(len(self.col_name)):
                    point_value.append(self.point[-1][j])
                table.insert('', 'end', values=point_value)
                # update self.point
                self.point = np.vstack((self.point, np.zeros((1, self.data_len), dtype=int)))
                self.point[-1][data_dict['set']] = self.point[-2][data_dict['set']]
                self.point[-1][data_dict['game']] = self.point[-2][data_dict['game']]
                self.point[-1][data_dict['score']] = self.point[-2][data_dict['score']]
                self.point[-1][data_dict['rally']] = self.point[-2][data_dict['rally']] + 1
                self.point[-1][data_dict['score1']] = self.point[-2][data_dict['score1']]
                self.point[-1][data_dict['score2']] = self.point[-2][data_dict['score2']]
                self.point[-1][data_dict['game1']] = self.point[-2][data_dict['game1']]
                self.point[-1][data_dict['game2']] = self.point[-2][data_dict['game2']]
                self.point[-1][data_dict['set1']] = self.point[-2][data_dict['set1']]
                self.point[-1][data_dict['set2']] = self.point[-2][data_dict['set2']]
            else:
                if winner.get() == self.p1_name:
                    player = 1
                elif winner.get() ==self.p2_name:
                    player = 2
                # update score board
                score_plus(player)
                server.set('')
                winner.set('')
                # write self.point
                self.score1 = self.point[-1][data_dict['score1']]
                self.score2 = self.point[-1][data_dict['score2']]
                self.game1 = self.point[-1][data_dict['game1']]
                self.game2 = self.point[-1][data_dict['game2']]
                self.set1 = self.point[-1][data_dict['set1']]
                self.set2 = self.point[-1][data_dict['set2']]
                # update table
                items = table.get_children()
                for item in items:
                    if table.item(item, 'values')[data_dict['score']] == str(self.point[-1][data_dict['score']]):
                        table.delete(item)
                for i in range(len(self.point)):
                    self.point[i][data_dict['winner']] = player
                    data_value = []
                    for j in range(len(self.col_name)):
                        data_value.append(self.point[i][j])
                    table.insert('', 'end', values=data_value)
                # write csv
                point = pd.DataFrame(self.point, columns=['盘', '局', '分', '球', '球员', '站位', '技术', '落点', '状态', '效果', '分1', '分2', '局1', '局2', '盘1', '盘2'])
                self.data = self.data.append(point, ignore_index=True)
                self.data.to_csv(self.file_name, index=False, sep=',')
                # update self.point
                self.point = np.zeros((1, self.data_len), dtype=int)
                self.point[0][data_dict['set']] = self.set + 1
                self.point[0][data_dict['game']] = self.game + 1
                self.point[0][data_dict['score']] = self.score + 1
                self.point[0][data_dict['rally']] = 1
                self.point[0][data_dict['score1']] = self.score1
                self.point[0][data_dict['score2']] = self.score2
                self.point[0][data_dict['game1']] = self.game1
                self.point[0][data_dict['game2']] = self.game2
                self.point[0][data_dict['set1']] = self.set1
                self.point[0][data_dict['set2']] = self.set2

        # ----------------------------------------
        # withdraw one rally
        # ----------------------------------------
        def button_withdraw_rally():
            if score_p1.get() == '':
                msg.showerror(title='错误', message='请点击“开始比赛”！')
            else:
                if len(self.point) == 1:
                    if len(self.data.index) == 0:
                        msg.showerror(title='错误', message='无可撤回数据！')
                    else:
                        if self.data.iloc[-1][data_dict['rally']] == 1:
                            # update self.data
                            score_no = self.data.iloc[-1][data_dict['score']]
                            self.data = self.data.drop(index=self.data.loc[self.data[self.col_name[data_dict['score']]]==score_no].index)
                            self.data.to_csv(self.file_name, index=False, sep=',')
                            self.point = np.zeros((1, self.data_len), dtype=int)
                            if len(self.data.index) == 0:
                                # update score board
                                set_p1.set('0')
                                set_p2.set('0')
                                game_p1.set('0')
                                game_p2.set('0')
                                score_p1.set('0')
                                score_p2.set('0')
                                # update self.point
                                self.point[0][data_dict['set']] = 1
                                self.point[0][data_dict['game']] = 1
                                self.point[0][data_dict['score']] = 1
                                self.point[0][data_dict['rally']] = 1
                                # update memory
                                self.set = 0
                                self.game = 0
                                self.score = 0
                            else:
                                # update score board
                                set_p1.set(str(self.data.iloc[-1][data_dict['set1']]))
                                set_p2.set(str(self.data.iloc[-1][data_dict['set2']]))
                                game_p1.set(str(self.data.iloc[-1][data_dict['game1']]))
                                game_p2.set(str(self.data.iloc[-1][data_dict['game2']]))

                                if self.is_tiebreak == False:
                                    int_score_array = ['0', '15', '30', '40']
                                    score_p1_tmp = self.data.iloc[-1][data_dict['score1']]
                                    score_p2_tmp = self.data.iloc[-1][data_dict['score2']]
                                    if score_p1_tmp <= 3 and score_p2_tmp <= 3:
                                        score_p1.set(int_score_array[score_p1_tmp])
                                        score_p2.set(int_score_array[score_p2_tmp])
                                    elif score_p1_tmp == score_p2_tmp:
                                        score_p1.set('40')
                                        score_p2.set('40')
                                    elif score_p1_tmp > score_p2_tmp:
                                        score_p1.set('AD')
                                        score_p2.set('-')
                                    elif score_p1_tmp < score_p2_tmp:
                                        score_p1.set('-')
                                        score_p2.set('AD')
                                else:
                                    score_p1.set(self.data.iloc[-1][data_dict['score1']])
                                    score_p2.set(self.data.iloc[-1][data_dict['score2']])
                                # update self.point
                                if self.data.iloc[-1][data_dict['score1']] == 0 and \
                                    self.data.iloc[-1][data_dict['score2']] == 0 and \
                                    self.data.iloc[-1][data_dict['game1']] == 0 and \
                                    self.data.iloc[-1][data_dict['game2']] == 0 and \
                                    (self.data.iloc[-1][data_dict['set1']] != 0 or \
                                    self.data.iloc[-1][data_dict['set2']] != 0):
                                        self.point[0][data_dict['set']] = self.data.iloc[-1][data_dict['set']] + 1
                                else:
                                    self.point[0][data_dict['set']] = self.data.iloc[-1][data_dict['set']]
                
                                if self.data.iloc[-1][data_dict['score1']] == 0 and \
                                    self.data.iloc[-1][data_dict['score2']] == 0:
                                    self.point[0][data_dict['game']] = self.data.iloc[-1][data_dict['game']] + 1
                                else:
                                    self.point[0][data_dict['game']] = self.data.iloc[-1][data_dict['game']]
                
                                self.point[0][data_dict['score']] = self.data.iloc[-1][data_dict['score']] + 1
                                self.point[0][data_dict['rally']] = 1
                                self.point[0][data_dict['score1']] = self.data.iloc[-1][data_dict['score1']]
                                self.point[0][data_dict['score2']] = self.data.iloc[-1][data_dict['score2']]
                                self.point[0][data_dict['game1']] = self.data.iloc[-1][data_dict['game1']]
                                self.point[0][data_dict['game2']] = self.data.iloc[-1][data_dict['game2']]
                                self.point[0][data_dict['set1']] = self.data.iloc[-1][data_dict['set1']]
                                self.point[0][data_dict['set2']] = self.data.iloc[-1][data_dict['set2']]
                                # update memory
                                self.set = self.point[0][data_dict['set']] - 1
                                self.game = self.point[0][data_dict['game']] - 1
                                self.score = self.point[0][data_dict['score']] - 1
                            # update table
                            items = table.get_children()
                            for item in items:
                                if table.item(item, 'values')[data_dict['score']] == str(score_no):
                                    table.delete(item)
                        else:
                            score_no = self.data.iloc[-1][data_dict['score']]
                            rally_no = self.data.iloc[-1][data_dict['rally']]
                            # update self.point
                            self.point = self.data.loc[self.data[self.col_name[data_dict['score']]]==score_no].values
                            self.point[-1] = np.zeros((1, self.data_len), dtype=int)
                            self.point[-1][data_dict['set']] = self.point[-2][data_dict['set']]
                            self.point[-1][data_dict['game']] = self.point[-2][data_dict['game']]
                            self.point[-1][data_dict['score']] = self.point[-2][data_dict['score']]
                            self.point[-1][data_dict['rally']] = self.point[-2][data_dict['rally']] + 1
                            self.point[-1][data_dict['score1']] = self.point[-2][data_dict['score1']]
                            self.point[-1][data_dict['score2']] = self.point[-2][data_dict['score2']]
                            self.point[-1][data_dict['game1']] = self.point[-2][data_dict['game1']]
                            self.point[-1][data_dict['game2']] = self.point[-2][data_dict['game2']]
                            self.point[-1][data_dict['set1']] = self.point[-2][data_dict['set1']]
                            self.point[-1][data_dict['set2']] = self.point[-2][data_dict['set2']]
                            # update self.data
                            self.data = self.data.drop(index=self.data.loc[self.data[self.col_name[data_dict['score']]]==score_no].index)
                            self.data.to_csv(self.file_name, index=False, sep=',')
                            # update score board
                            set_p1.set(str(self.data.iloc[-1][data_dict['set1']]))
                            set_p2.set(str(self.data.iloc[-1][data_dict['set2']]))
                            game_p1.set(str(self.data.iloc[-1][data_dict['game1']]))
                            game_p2.set(str(self.data.iloc[-1][data_dict['game2']]))

                            if self.is_tiebreak == False:
                                int_score_array = ['0', '15', '30', '40']
                                score_p1_tmp = self.data.iloc[-1][data_dict['score1']]
                                score_p2_tmp = self.data.iloc[-1][data_dict['score2']]
                                if score_p1_tmp <= 3 and score_p2_tmp <= 3:
                                    score_p1.set(int_score_array[score_p1_tmp])
                                    score_p2.set(int_score_array[score_p2_tmp])
                                elif score_p1_tmp == score_p2_tmp:
                                    score_p1.set('40')
                                    score_p2.set('40')
                                elif score_p1_tmp > score_p2_tmp:
                                    score_p1.set('AD')
                                    score_p2.set('-')
                                elif score_p1_tmp < score_p2_tmp:
                                    score_p1.set('-')
                                    score_p2.set('AD')
                            else:
                                score_p1.set(self.data.iloc[-1][data_dict['score1']])
                                score_p2.set(self.data.iloc[-1][data_dict['score2']])
                            # update table
                            items = table.get_children()
                            for item in items:
                                if table.item(item, 'values')[data_dict['score']] == str(score_no) and table.item(item, 'values')[data_dict['rally']] == str(rally_no):
                                    table.delete(item)
                else:
                    # update self.point
                    self.point = np.delete(self.point, -2, axis=0)
                    self.point[-1][data_dict['rally']] = self.point[-1][data_dict['rally']] - 1
                    # update table
                    score_no = self.point[-1][data_dict['score']]
                    rally_no = self.point[-1][data_dict['rally']]
                    items = table.get_children()
                    for item in items:
                        if table.item(item, 'values')[data_dict['score']] == str(score_no) and table.item(item, 'values')[data_dict['rally']] == str(rally_no):
                            table.delete(item)
                msg.showinfo(title='提示', message='撤回一拍成功！')

        # ----------------------------------------
        # withdraw one score
        # ----------------------------------------
        def button_withdraw_score():
            if score_p1.get() == '':
                msg.showerror(title='错误', message='请点击“开始比赛”！')
            else:
                if len(self.data.index) == 0:
                    msg.showerror(title='错误', message='无可撤回数据！')
                else:
                    if len(self.point) == 1:
                        # update self.data
                        score_no = self.data.iloc[-1][data_dict['score']]
                        self.data = self.data.drop(index=self.data.loc[self.data[self.col_name[data_dict['score']]]==score_no].index)
                        self.data.to_csv(self.file_name, index=False, sep=',')
                        self.point = np.zeros((1, self.data_len), dtype=int)
                        if len(self.data.index) == 0:
                            # update score board
                            set_p1.set('0')
                            set_p2.set('0')
                            game_p1.set('0')
                            game_p2.set('0')
                            score_p1.set('0')
                            score_p2.set('0')
                            # update self.point
                            self.point[0][data_dict['set']] = 1
                            self.point[0][data_dict['game']] = 1
                            self.point[0][data_dict['score']] = 1
                            self.point[0][data_dict['rally']] = 1
                            # update memory
                            self.set = 0
                            self.game = 0
                            self.score = 0
                        else:
                            # update score board
                            set_p1.set(str(self.data.iloc[-1][data_dict['set1']]))
                            set_p2.set(str(self.data.iloc[-1][data_dict['set2']]))
                            game_p1.set(str(self.data.iloc[-1][data_dict['game1']]))
                            game_p2.set(str(self.data.iloc[-1][data_dict['game2']]))

                            if self.is_tiebreak == False:
                                int_score_array = ['0', '15', '30', '40']
                                score_p1_tmp = self.data.iloc[-1][data_dict['score1']]
                                score_p2_tmp = self.data.iloc[-1][data_dict['score2']]
                                if score_p1_tmp <= 3 and score_p2_tmp <= 3:
                                    score_p1.set(int_score_array[score_p1_tmp])
                                    score_p2.set(int_score_array[score_p2_tmp])
                                elif score_p1_tmp == score_p2_tmp:
                                    score_p1.set('40')
                                    score_p2.set('40')
                                elif score_p1_tmp > score_p2_tmp:
                                    score_p1.set('AD')
                                    score_p2.set('-')
                                elif score_p1_tmp < score_p2_tmp:
                                    score_p1.set('-')
                                    score_p2.set('AD')
                            else:
                                score_p1.set(self.data.iloc[-1][data_dict['score1']])
                                score_p2.set(self.data.iloc[-1][data_dict['score2']])
                            # update self.point
                            if self.data.iloc[-1][data_dict['score1']] == 0 and \
                                self.data.iloc[-1][data_dict['score2']] == 0 and \
                                self.data.iloc[-1][data_dict['game1']] == 0 and \
                                self.data.iloc[-1][data_dict['game2']] == 0 and \
                                (self.data.iloc[-1][data_dict['set1']] != 0 or \
                                self.data.iloc[-1][data_dict['set2']] != 0):
                                    self.point[0][data_dict['set']] = self.data.iloc[-1][data_dict['set']] + 1
                            else:
                                self.point[0][data_dict['set']] = self.data.iloc[-1][data_dict['set']]
                
                            if self.data.iloc[-1][data_dict['score1']] == 0 and \
                                self.data.iloc[-1][data_dict['score2']] == 0:
                                self.point[0][data_dict['game']] = self.data.iloc[-1][data_dict['game']] + 1
                            else:
                                self.point[0][data_dict['game']] = self.data.iloc[-1][data_dict['game']]
                
                            self.point[0][data_dict['score']] = self.data.iloc[-1][data_dict['score']] + 1
                            self.point[0][data_dict['rally']] = 1
                            self.point[0][data_dict['score1']] = self.data.iloc[-1][data_dict['score1']]
                            self.point[0][data_dict['score2']] = self.data.iloc[-1][data_dict['score2']]
                            self.point[0][data_dict['game1']] = self.data.iloc[-1][data_dict['game1']]
                            self.point[0][data_dict['game2']] = self.data.iloc[-1][data_dict['game2']]
                            self.point[0][data_dict['set1']] = self.data.iloc[-1][data_dict['set1']]
                            self.point[0][data_dict['set2']] = self.data.iloc[-1][data_dict['set2']]
                            # update memory
                            self.set = self.point[0][data_dict['set']] - 1
                            self.game = self.point[0][data_dict['game']] - 1
                            self.score = self.point[0][data_dict['score']] - 1
                        # update table
                        items = table.get_children()
                        for item in items:
                            if table.item(item, 'values')[data_dict['score']] == str(score_no):
                                table.delete(item)
                    else:
                        # update self.point
                        self.point = np.zeros((1, self.data_len), dtype=int)
                        if self.data.iloc[-1][data_dict['score1']] == 0 and \
                            self.data.iloc[-1][data_dict['score2']] == 0 and \
                            self.data.iloc[-1][data_dict['game1']] == 0 and \
                            self.data.iloc[-1][data_dict['game2']] == 0 and \
                            (self.data.iloc[-1][data_dict['set1']] != 0 or \
                            self.data.iloc[-1][data_dict['set2']] != 0):
                                self.point[0][data_dict['set']] = self.data.iloc[-1][data_dict['set']] + 1
                        else:
                            self.point[0][data_dict['set']] = self.data.iloc[-1][data_dict['set']]
            
                        if self.data.iloc[-1][data_dict['score1']] == 0 and \
                            self.data.iloc[-1][data_dict['score2']] == 0:
                            self.point[0][data_dict['game']] = self.data.iloc[-1][data_dict['game']] + 1
                        else:
                            self.point[0][data_dict['game']] = self.data.iloc[-1][data_dict['game']]
                
                        self.point[0][data_dict['score']] = self.data.iloc[-1][data_dict['score']] + 1
                        self.point[0][data_dict['rally']] = 1
                        self.point[0][data_dict['score1']] = self.data.iloc[-1][data_dict['score1']]
                        self.point[0][data_dict['score2']] = self.data.iloc[-1][data_dict['score2']]
                        self.point[0][data_dict['game1']] = self.data.iloc[-1][data_dict['game1']]
                        self.point[0][data_dict['game2']] = self.data.iloc[-1][data_dict['game2']]
                        self.point[0][data_dict['set1']] = self.data.iloc[-1][data_dict['set1']]
                        self.point[0][data_dict['set2']] = self.data.iloc[-1][data_dict['set2']]
                        # update table
                        score_no = self.point[-1][data_dict['score']]
                        items = table.get_children()
                        for item in items:
                            if table.item(item, 'values')[data_dict['score']] == str(score_no):
                                table.delete(item)
                    msg.showinfo(title='提示', message='撤回一分成功！')

        # ----------------------------------------
        # export data
        # ----------------------------------------
        def button_export():
            if len(self.point) > 1:
                msg.showerror(title='错误', message='请录完当前一分，或撤回这一分！')
            else:
                self.data.to_csv(self.file_name, index=False, sep=',')
                msg.showinfo(title='提示', message='数据导出成功！')
                self.window.destroy()
        
        # ====================================================================
        # widget
        # ====================================================================
        # ========================================
        # left widget: data collection
        # ========================================
        group_left = ttk.Frame(self.window)
        group_left.pack(side='left', expand=1, anchor='center', fill='y')
        # ----------------------------------------
        # match
        # ----------------------------------------
        ttk.Label(group_left, text='比赛名称：' + self.m_name)\
            .pack(side='top', expand=1, anchor='center', fill='x', padx=5)

        group_up = ttk.Frame(group_left)
        group_up.pack(side='top', expand=1, anchor='center', fill='x')
        # ----------------------------------------
        # info
        # ----------------------------------------
        group_info = ttk.Frame(group_up)
        group_info.pack(side='left', expand=1, anchor='w')
        # ~~~~~~~~~~~~~
        # player info
        # ~~~~~~~~~~~~~
        group_p = ttk.LabelFrame(group_info, text='球员信息')
        group_p.pack(side='top', expand=1, anchor='w', padx=5, pady=5)

        group_p1 = ttk.Frame(group_p)
        group_p1.pack(side='top', expand=1, anchor='center', fill='x')
        ttk.Label(group_p1, text='球员1：' + self.p1_name, width=20)\
            .pack(side='left', expand=1, anchor='center', padx=5)
        hand = self.p1_hand.replace('left', '左手', 2).replace('right', '右手', 2)
        ttk.Label(group_p1, text='持拍手：' + hand)\
            .pack(side='right', expand=1, anchor='center', padx=5)

        group_p2 = ttk.Frame(group_p)
        group_p2.pack(side='top', expand=1, anchor='center', fill='x')
        ttk.Label(group_p2, text='球员2：' + self.p2_name, width=20)\
            .pack(side='left', expand=1, anchor='center', padx=5)
        hand = self.p2_hand.replace('left', '左手', 2).replace('right', '右手', 2)
        ttk.Label(group_p2, text='持拍手：' + hand)\
            .pack(side='right', expand=1, anchor='center', padx=5)
        # ~~~~~~~~~~~~~
        # serve
        # ~~~~~~~~~~~~~
        group_serve = ttk.LabelFrame(group_info, text='发球方：')
        group_serve.pack(side='top', expand=1, anchor='w', padx=5, pady=5)
        server = tk.StringVar()
        ttk.Radiobutton(group_serve, text=self.p1_name, variable=server, value=self.p1_name)\
            .pack(side='left', expand=1, anchor='w', padx=5)
        ttk.Radiobutton(group_serve, text=self.p2_name, variable=server, value=self.p2_name)\
            .pack(side='right', expand=1, anchor='w', padx=5)
        
        # ----------------------------------------
        # score
        # ----------------------------------------
        group_score = ttk.Frame(group_up)
        group_score.pack(side='right', expand=1, anchor='w')
        # ~~~~~~~~~~~~~
        # begin playing
        # ~~~~~~~~~~~~~
        begin = ttk.Button(group_score, text='开始比赛', command=button_begin, width=10)
        begin.pack(side='top', expand=1, anchor='center')
        # ~~~~~~~~~~~~~
        # score board
        # ~~~~~~~~~~~~~
        group_board = ttk.LabelFrame(group_score, text='比分')
        group_board.pack(side='top', expand=1, anchor='center')
        # line 1 ========================
        board_l1 = ttk.Frame(group_board)
        board_l1.pack(side='top', expand=1, anchor='center')
        ttk.Label(board_l1, text=self.p1_name)\
            .pack(side='left', expand=1, anchor='center', padx=5)
        ttk.Label(board_l1, text=':')\
            .pack(side='left', expand=1, anchor='center', padx=5)
        ttk.Label(board_l1, text=self.p2_name)\
            .pack(side='right', expand=1, anchor='center', padx=5)
        # line 2 ========================
        board_l2 = ttk.Frame(group_board)
        board_l2.pack(side='top', expand=1, anchor='w', pady=1)
        ttk.Label(board_l2, text='盘分')\
            .pack(side='left', expand=1, anchor='center', padx=5)
        set_p1 = tk.StringVar()
        tk.Label(board_l2, textvariable=set_p1, width=3, bg='white')\
            .pack(side='left', expand=1, anchor='center')
        ttk.Label(board_l2, text=':')\
            .pack(side='left', expand=1, anchor='center')
        set_p2 = tk.StringVar()
        tk.Label(board_l2, textvariable=set_p2, width=3, bg='white')\
            .pack(side='left', expand=1, anchor='center')
        # line 3 ========================
        board_l3 = ttk.Frame(group_board)
        board_l3.pack(side='top', expand=1, anchor='w', pady=1)
        ttk.Label(board_l3, text='局分')\
            .pack(side='left', expand=1, anchor='center', padx=5)
        game_p1 = tk.StringVar()
        tk.Label(board_l3, textvariable=game_p1, width=3, bg='white')\
            .pack(side='left', expand=1, anchor='center')
        ttk.Label(board_l3, text=':')\
            .pack(side='left', expand=1, anchor='center')
        game_p2 = tk.StringVar()
        tk.Label(board_l3, textvariable=game_p2, width=3, bg='white')\
            .pack(side='left', expand=1, anchor='center')
        # line 4 ========================
        board_l4 = ttk.Frame(group_board)
        board_l4.pack(side='top', expand=1, anchor='w', pady=1)
        ttk.Label(board_l4, text='小分')\
            .pack(side='left', expand=1, anchor='center', padx=5)
        score_p1 = tk.StringVar()
        tk.Label(board_l4, textvariable=score_p1, width=3, bg='white')\
            .pack(side='left', expand=1, anchor='center')
        ttk.Label(board_l4, text=':')\
            .pack(side='left', expand=1, anchor='center')
        score_p2 = tk.StringVar()
        tk.Label(board_l4, textvariable=score_p2, width=3, bg='white')\
            .pack(side='left', expand=1, anchor='center')
        # ----------------------------------------
        # date collection
        # ----------------------------------------
        group_data = ttk.Frame(group_left)
        group_data.pack(side='top', expand=1, anchor='center')
        # ~~~~~~~~~~~~~
        # change court
        # ~~~~~~~~~~~~~
        group_change = ttk.Frame(group_data)
        group_change.pack(side='left', expand=1, anchor='center')
        p_up = tk.StringVar()
        p_up.set(self.p2_name)
        ttk.Label(group_change, textvariable=p_up)\
            .pack(side='top', expand=1, anchor='center')
        ttk.Button(group_change, text='交换场地', command=button_change, width=10)\
            .pack(side='top', expand=1, anchor='center', padx=5)
        p_down = tk.StringVar()
        p_down.set(self.p1_name)
        ttk.Label(group_change, textvariable=p_down)\
            .pack(side='top', expand=1, anchor='center')
        # ~~~~~~~~~~~~~
        # court placement
        # ~~~~~~~~~~~~~
        group_court = ttk.Frame(group_data)
        group_court.pack(side='left', expand=1, anchor='center', padx=5)
        # line 1 ========================
        court_l1 = ttk.Frame(group_court)
        court_l1.pack(side='top', expand=1, anchor='center')
        tk.Button(court_l1, text='31', command=lambda: court('up', 31), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l1, text='27', command=lambda: court('up', 27), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l1, text='28', command=lambda: court('up', 28), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l1, text='29', command=lambda: court('up', 29), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l1, text='30', command=lambda: court('up', 30), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l1, text='32', command=lambda: court('up', 32), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        # line 2 ========================
        court_l2 = ttk.Frame(group_court)
        court_l2.pack(side='top', expand=1, anchor='center')
        tk.Button(court_l2, text='33', command=lambda: court('up', 33), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l2, text='23', command=lambda: court('up', 23), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l2, text='24', command=lambda: court('up', 24), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l2, text='25', command=lambda: court('up', 25), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l2, text='26', command=lambda: court('up', 26), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l2, text='34', command=lambda: court('up', 34), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        # line 3 ========================
        court_l3 = ttk.Frame(group_court)
        court_l3.pack(side='top', expand=1, anchor='center')
        tk.Button(court_l3, text='35', command=lambda: court('up', 35), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l3, text='7', command=lambda: court('up', 7), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l3, text='8', command=lambda: court('up', 8), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l3, text='9', command=lambda: court('up', 9), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l3, text='10', command=lambda: court('up', 10), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l3, text='36', command=lambda: court('up', 36), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        # line 4 ========================
        court_l4 = ttk.Frame(group_court)
        court_l4.pack(side='top', expand=1, anchor='center')
        tk.Button(court_l4, text='37', command=lambda: court('up', 37), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l4, text='11', command=lambda: court('up', 11), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l4, text='12', command=lambda: court('up', 12), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l4, text='13', command=lambda: court('up', 13), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l4, text='14', command=lambda: court('up', 14), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l4, text='38', command=lambda: court('up', 38), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        # line 5 ========================
        court_l5 = ttk.Frame(group_court)
        court_l5.pack(side='top', expand=1, anchor='center')
        tk.Button(court_l5, text='1', command=lambda: court('up', 1), width=3, bg='cadetblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l5, text='2', command=lambda: court('up', 2), width=3, bg='cadetblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l5, text='3', command=lambda: court('up', 3), width=3, bg='cadetblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l5, text='4', command=lambda: court('up', 4), width=3, bg='cadetblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l5, text='5', command=lambda: court('up', 5), width=3, bg='cadetblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l5, text='6', command=lambda: court('up', 6), width=3, bg='cadetblue')\
            .pack(side='left', expand=1, anchor='center')
        # line 6 ========================
        court_l6 = ttk.Frame(group_court)
        court_l6.pack(side='top', expand=1, anchor='center')
        tk.Button(court_l6, text='39', command=lambda: court('up', 39), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l6, text='15', command=lambda: court('up', 15), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l6, text='16', command=lambda: court('up', 16), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l6, text='17', command=lambda: court('up', 17), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l6, text='18', command=lambda: court('up', 18), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l6, text='40', command=lambda: court('up', 40), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        # line 7 ========================
        court_l7 = ttk.Frame(group_court)
        court_l7.pack(side='top', expand=1, anchor='center')
        tk.Button(court_l7, text='41', command=lambda: court('up', 41), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l7, text='19', command=lambda: court('up', 19), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l7, text='20', command=lambda: court('up', 20), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l7, text='21', command=lambda: court('up', 21), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l7, text='22', command=lambda: court('up', 22), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l7, text='42', command=lambda: court('up', 42), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        # line net ========================
        ttk.Label(group_court, text='------球网------------球网------')\
            .pack(side='top', expand=1, anchor='center')
                # line 8 ========================
        court_l8 = ttk.Frame(group_court)
        court_l8.pack(side='top', expand=1, anchor='center')
        tk.Button(court_l8, text='42', command=lambda: court('down', 42), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l8, text='22', command=lambda: court('down', 22), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l8, text='21', command=lambda: court('down', 21), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l8, text='20', command=lambda: court('down', 20), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l8, text='19', command=lambda: court('down', 19), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l8, text='41', command=lambda: court('down', 41), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        # line 9 ========================
        court_l9 = ttk.Frame(group_court)
        court_l9.pack(side='top', expand=1, anchor='center')
        tk.Button(court_l9, text='40', command=lambda: court('down', 40), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l9, text='18', command=lambda: court('down', 18), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l9, text='17', command=lambda: court('down', 17), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l9, text='16', command=lambda: court('down', 16), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l9, text='15', command=lambda: court('down', 15), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l9, text='39', command=lambda: court('down', 39), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        # line 10 ========================
        court_l10 = ttk.Frame(group_court)
        court_l10.pack(side='top', expand=1, anchor='center')
        tk.Button(court_l10, text='6', command=lambda: court('down', 6), width=3, bg='cadetblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l10, text='5', command=lambda: court('down', 5), width=3, bg='cadetblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l10, text='4', command=lambda: court('down', 4), width=3, bg='cadetblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l10, text='3', command=lambda: court('down', 3), width=3, bg='cadetblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l10, text='2', command=lambda: court('down', 2), width=3, bg='cadetblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l10, text='1', command=lambda: court('down', 1), width=3, bg='cadetblue')\
            .pack(side='left', expand=1, anchor='center')
        # line 11 ========================
        court_l11 = ttk.Frame(group_court)
        court_l11.pack(side='top', expand=1, anchor='center')
        tk.Button(court_l11, text='38', command=lambda: court('down', 38), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l11, text='14', command=lambda: court('down', 14), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l11, text='13', command=lambda: court('down', 13), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l11, text='12', command=lambda: court('down', 12), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l11, text='11', command=lambda: court('down', 11), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l11, text='37', command=lambda: court('down', 37), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        # line 12 ========================
        court_l12 = ttk.Frame(group_court)
        court_l12.pack(side='top', expand=1, anchor='center')
        tk.Button(court_l12, text='36', command=lambda: court('down', 36), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l12, text='10', command=lambda: court('down', 10), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l12, text='9', command=lambda: court('down', 9), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l12, text='8', command=lambda: court('down', 8), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l12, text='7', command=lambda: court('down', 7), width=3, bg='deepskyblue')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l12, text='35', command=lambda: court('down', 35), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        # line 13 ========================
        court_l13 = ttk.Frame(group_court)
        court_l13.pack(side='top', expand=1, anchor='center')
        tk.Button(court_l13, text='34', command=lambda: court('down', 34), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l13, text='26', command=lambda: court('down', 26), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l13, text='25', command=lambda: court('down', 25), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l13, text='24', command=lambda: court('down', 24), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l13, text='23', command=lambda: court('down', 23), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l13, text='33', command=lambda: court('down', 33), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        # line 14 ========================
        court_l14 = ttk.Frame(group_court)
        court_l14.pack(side='top', expand=1, anchor='center')
        tk.Button(court_l14, text='32', command=lambda: court('down', 32), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l14, text='30', command=lambda: court('down', 30), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l14, text='29', command=lambda: court('down', 29), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l14, text='28', command=lambda: court('down', 28), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l14, text='27', command=lambda: court('down', 27), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        tk.Button(court_l14, text='31', command=lambda: court('down', 31), width=3, bg='green')\
            .pack(side='left', expand=1, anchor='center')
        # ~~~~~~~~~~~~~
        # technique & state choice
        # ~~~~~~~~~~~~~
        group_choice = ttk.Frame(group_data)
        group_choice.pack(side='right', expand=1, anchor='n')
        # technique choice
        group_tech = ttk.LabelFrame(group_choice, text='技术')
        group_tech.pack(side='top', expand=1, anchor='center', pady=5)
        # line 1 ========================
        tech_l1 = ttk.Frame(group_tech)
        tech_l1.pack(side='top', expand=1, anchor='center')
        ttk.Button(tech_l1, text='1  一区一发', command=lambda: tech(1), width=10)\
            .pack(side='left', expand=1, anchor='center')
        ttk.Button(tech_l1, text='2  一区二发', command=lambda: tech(2), width=10)\
            .pack(side='right', expand=1, anchor='center')
        # line 2 ========================
        tech_l2 = ttk.Frame(group_tech)
        tech_l2.pack(side='top', expand=1, anchor='center')
        ttk.Button(tech_l2, text='3  二区一发', command=lambda: tech(3), width=10)\
            .pack(side='left', expand=1, anchor='center')
        ttk.Button(tech_l2, text='4  二区二发', command=lambda: tech(4), width=10)\
            .pack(side='right', expand=1, anchor='center')
        # line 3 ========================
        tech_l3 = ttk.Frame(group_tech)
        tech_l3.pack(side='top', expand=1, anchor='center')
        ttk.Button(tech_l3, text='5  正手抽击', command=lambda: tech(5), width=10)\
            .pack(side='left', expand=1, anchor='center')
        ttk.Button(tech_l3, text='6  反手抽击', command=lambda: tech(6), width=10)\
            .pack(side='right', expand=1, anchor='center')
        # line 4 ========================
        tech_l4 = ttk.Frame(group_tech)
        tech_l4.pack(side='top', expand=1, anchor='center')
        ttk.Button(tech_l4, text='7  正手截击', command=lambda: tech(7), width=10)\
            .pack(side='left', expand=1, anchor='center')
        ttk.Button(tech_l4, text='8  反手截击', command=lambda: tech(8), width=10)\
            .pack(side='right', expand=1, anchor='center')
        # line 5 ========================
        tech_l5 = ttk.Frame(group_tech)
        tech_l5.pack(side='top', expand=1, anchor='center')
        ttk.Button(tech_l5, text='9  高压球  ', command=lambda: tech(9), width=10)\
            .pack(side='left', expand=1, anchor='center')
        ttk.Button(tech_l5, text='10 削球    ', command=lambda: tech(10), width=10)\
            .pack(side='right', expand=1, anchor='center')
        # line 6 ========================
        tech_l6 = ttk.Frame(group_tech)
        tech_l6.pack(side='top', expand=1, anchor='center')
        ttk.Button(tech_l6, text='11 挑高球  ', command=lambda: tech(11), width=10)\
            .pack(side='left', expand=1, anchor='center')
        ttk.Button(tech_l6, text='12 放小球  ', command=lambda: tech(12), width=10)\
            .pack(side='right', expand=1, anchor='center')
        # line 7 ========================
        tech_l7 = ttk.Frame(group_tech)
        tech_l7.pack(side='top', expand=1, anchor='center')
        ttk.Button(tech_l7, text='13 推挡    ', command=lambda: tech(13), width=10)\
            .pack(side='left', expand=1, anchor='center')
        ttk.Button(tech_l7, text='0  无技术  ', command=lambda: tech(0), width=10)\
            .pack(side='right', expand=1, anchor='center')
        # state choice
        group_state = ttk.LabelFrame(group_choice, text='状态')
        group_state.pack(side='top', expand=1, anchor='center', pady=5)
        # line 1 ========================
        state_l1 = ttk.Frame(group_state)
        state_l1.pack(side='top', expand=1, anchor='center')
        ttk.Button(state_l1, text='1 界内有效', command=lambda: state(1), width=10)\
            .pack(side='left', expand=1, anchor='center')
        ttk.Button(state_l1, text='2 出界球  ', command=lambda: state(2), width=10)\
            .pack(side='right', expand=1, anchor='center')
        # line 2 ========================
        state_l2 = ttk.Frame(group_state)
        state_l2.pack(side='top', expand=1, anchor='center')
        ttk.Button(state_l2, text='3 下网球  ', command=lambda: state(3), width=10)\
            .pack(side='left', expand=1, anchor='center')
        ttk.Button(state_l2, text='4 擦网球  ', command=lambda: state(4), width=10)\
            .pack(side='right', expand=1, anchor='center')
        # line 3 ========================
        state_l3 = ttk.Frame(group_state)
        state_l3.pack(side='top', expand=1, anchor='center')
        ttk.Button(state_l3, text='5 被拦网  ', command=lambda: state(5), width=10)\
            .pack(side='left', expand=1, anchor='center')
        ttk.Button(state_l3, text='6 未过网  ', command=lambda: state(6), width=10)\
            .pack(side='right', expand=1, anchor='center')
        # line 4 ========================
        state_l4 = ttk.Frame(group_state)
        state_l4.pack(side='top', expand=1, anchor='center')
        ttk.Button(state_l4, text='7 被穿越  ', command=lambda: state(7), width=10)\
            .pack(side='left', expand=1, anchor='center')
        ttk.Button(state_l4, text='8 界内无效', command=lambda: state(8), width=10)\
            .pack(side='right', expand=1, anchor='center')
        # ~~~~~~~~~~~~~
        # winner
        # ~~~~~~~~~~~~~
        group_winner = ttk.LabelFrame(group_choice, text='得分方')
        group_winner.pack(side='top', expand=1, anchor='center', pady=5)
        winner = tk.StringVar()
        ttk.Radiobutton(group_winner, text=self.p1_name, variable=winner, value=self.p1_name)\
            .pack(side='left', expand=1, anchor='center', padx=5)
        ttk.Radiobutton(group_winner, text=self.p2_name, variable=winner, value=self.p2_name)\
            .pack(side='right', expand=1, anchor='center', padx=5)
        # ~~~~~~~~~~~~~
        # next ball
        # ~~~~~~~~~~~~~
        ttk.Button(group_choice, text='下一拍/分', command=button_next)\
            .pack(side='top', expand=1, anchor='center', pady=5)
        # ~~~~~~~~~~~~~
        # withdraw
        # ~~~~~~~~~~~~~
        group_withdraw = ttk.Frame(group_choice)
        group_withdraw.pack(side='bottom', expand=1, anchor='center', pady=5)

        ttk.Button(group_withdraw, text='撤回一拍', command=button_withdraw_rally)\
            .pack(side='left', expand=1, anchor='center')
        ttk.Button(group_withdraw, text='撤回一分', command=button_withdraw_score)\
            .pack(side='right', expand=1, anchor='center')

        # ----------------------------------------
        # export data
        # ----------------------------------------
        ttk.Button(group_left, text='导出数据', command=button_export, width=10)\
            .pack(side='bottom', expand=1, anchor='center', pady=5)

        # ========================================
        # right widget: preview table
        # ========================================
        group_right = ttk.LabelFrame(self.window, text='已录入数据预览')
        group_right.pack(side='right', expand=1, anchor='center', padx=5, pady=5)
        table = ttk.Treeview(group_right, columns=self.col_name, show='headings', height=30)
        for i in range(len(self.col_name)):
            table.column(self.col_name[i], width=50, anchor='center')
            table.heading(self.col_name[i], text=self.col_name[i])

        table_y = ttk.Scrollbar(group_right, orient='vertical', command=table.yview)
        table_y.pack(side='right', fill='y')
        table.config(yscrollcommand=table_y.set)
        
        table.pack(side='left', expand=1, anchor='center')
    