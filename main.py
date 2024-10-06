# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 11:15:01 2018
Description:tkinter界面切换
Version:

@author:
"""
'''导入库'''
import os
import sys
from pyaudio import PyAudio, paInt16
import numpy as np
import wave
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time
import webbrowser


try:
    import Tkinter as tk
    from tkinter import messagebox
    from tkinter.filedialog import *
except ImportError:
    import tkinter as tk
    from tkinter import messagebox
    from tkinter.filedialog import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import page0_support
### 录音——变量初始化
global framerate, num_sample, channels, sampwidth
framerate = 16000   # 采样率
num_samples = 2000  # 采样点
channels = 1        # 声道
sampwidth = 2       # 采样宽度2bytes


'''桌面'''
class basedesk():
    def __init__(self, master):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        self.root = master
        self.root.config()
        self.root.title('Base page')
        self.root.geometry('1200x601+153+152')
        self.root.minsize(180,1)
        self.root.maxsize(1284,701)
        self.root.resizable(1,1)
        self.root.configure(background="#ffffff")
        self.root.configure(highlightbackground='#d9d9d9')
        self.root.configure(highlightcolor="black")

        FrameLeft(self.root)
        FrameRight1(self.root)

'''左边的桌布'''
class FrameLeft():
    def __init__(self, master):
        '''基准界面设置'''
        self.master = master
        self.FrameLeft = tk.Frame(self.master, )
        self.FrameLeft.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=1.001)
        self.FrameLeft.configure(relief='groove')
        self.FrameLeft.configure(borderwidth="5")
        self.FrameLeft.configure(relief="groove")
        self.FrameLeft.configure(background="#f1ede6")
        self.FrameLeft.configure(highlightbackground="#ffffff")
        self.FrameLeft.configure(highlightcolor="black")

        self.TSeparator1 = ttk.Separator(self.FrameLeft)
        self.TSeparator1.place(relx=0.391, rely=0.007, relheight=0.98)
        self.TSeparator1.configure(orient="vertical")

        self.title = tk.Message(self.FrameLeft)
        self.title.place(relx=0.008, rely=0.014, relheight=0.066, relwidth=0.376)
        self.title.configure(background="#f1ede6")
        self.title.configure(font="-family {微软雅黑} -size 18 -weight bold")
        self.title.configure(foreground="#453735")
        self.title.configure(highlightbackground="#d9d9d9")
        self.title.configure(highlightcolor="black")
        self.title.configure(text='''语音识别垃圾分类系统''')
        self.title.configure(width=483)

        self.message1 = tk.Message(self.FrameLeft)
        self.message1.place(relx=0.016, rely=0.099, relheight=0.085,relwidth=0.367)
        self.message1.configure(background="#f1ede6")
        self.message1.configure(font="-family {微软雅黑} -size 12 -weight bold")
        self.message1.configure(foreground="#99682d")
        self.message1.configure(highlightbackground="#d9d9d9")
        self.message1.configure(highlightcolor="black")
        self.message1.configure(justify='center')
        self.message1.configure(text='''请告诉小海你想投放的垃圾名称，例如香蕉皮、啤酒瓶……''')
        self.message1.configure(width=473)

        self.TSeparator2 = ttk.Separator(self.FrameLeft)
        self.TSeparator2.place(relx=0.018, rely=0.917, relwidth=0.352)

        self.statement1 = tk.Message(self.FrameLeft)
        self.statement1.place(relx=0.007, rely=0.922, relheight=0.047,relwidth=0.377)
        self.statement1.configure(background="#f1ede6")
        self.statement1.configure(font="-family {微软雅黑} -size 8")
        self.statement1.configure(foreground="#a5a2a5")
        self.statement1.configure(highlightbackground="#d9d9d9")
        self.statement1.configure(highlightcolor="black")
        self.statement1.configure(text='''声明：上传音频除作识别外无其他用途，请无需担心您的隐私泄露。''')
        self.statement1.configure(width=484)


        '''STEP1. 语音类型选择'''
        self.language = tk.Message(self.FrameLeft)
        self.language.place(relx=0.039, rely=0.205, relheight=0.048
                            , relwidth=0.126)
        self.language.configure(background="#f1ede6")
        self.language.configure(font="-family {微软雅黑} -size 12")
        self.language.configure(foreground="#000000")
        self.language.configure(highlightbackground="#d9d9d9")
        self.language.configure(highlightcolor="black")
        self.language.configure(text='''语言选择类型''')
        self.language.configure(width=162)

        global v1
        v1 = tk.StringVar()
        v1.set("普通话（默认）")
        self.languagechoose = tk.OptionMenu(self.FrameLeft, v1, "普通话（默认）", "普通话（带标点）", "英语", "粤语", "四川话")
        self.languagechoose.place(relx=0.187, rely=0.212, relheight=0.041
                                  , relwidth=0.144)
        self.languagechoose.configure(background="#000000")
        self.languagechoose.configure(foreground="white")

        global devpid
        devpid = 1536

        def optionClick2(event):
            global devpid
            v = v1.get()
            p = FrameRight2(self.master)
            p.show_done_steps([1,0,0,0],v1=v1.get(),v2=None)
            devpid = page0_support.get_devpid(v)

        self.languagechoose.bind('<Button-1>', optionClick2)

        '''STEP2.1 音频选择'''
        def choose():
            global audio_path
            audio_path = askopenfilename()
            p = FrameRight2(self.master)
            p.show_done_steps([1,1,0,0],v1=v1.get(),v2=audio_path)
            sys.stdout.flush()
        self.audiochoose = tk.Button(self.FrameLeft)
        self.audiochoose.place(relx=0.078, rely=0.296, height=115, width=309)
        self.audiochoose.configure(activebackground="#f1ede6")
        self.audiochoose.configure(activeforeground="#f1ede6")
        self.audiochoose.configure(anchor='e')
        self.audiochoose.configure(background="#f1ede6")
        self.audiochoose.configure(borderwidth="3")
        self.audiochoose.configure(command=choose)
        self.audiochoose.configure(disabledforeground="#f1ede6")
        self.audiochoose.configure(font="-family {微软雅黑} -size 13 -weight bold")
        self.audiochoose.configure(foreground="#000000")
        self.audiochoose.configure(highlightbackground="#f1ede6")
        self.audiochoose.configure(highlightcolor="black")
        self.audiochoose.configure(highlightthickness="0")
        self.audiochoose.configure(pady="0")
        self.audiochoose.configure(text='''音频选择   ''')

        '''实时录音'''
        def save_wave_file(filepath, data):
            wf = wave.open(filepath, 'wb')
            wf.setnchannels(channels)
            wf.setsampwidth(sampwidth)
            wf.setframerate(framerate)
            wf.writeframes(b''.join(data))
            wf.close()

        def record():
            global result,audio_path
            pa = PyAudio()
            audio_path = os.path.join('speech',str(time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))) + '.wav')
            # 打开一个新的音频stream
            stream = pa.open(format=paInt16, channels=channels,
                             rate=framerate, input=True, frames_per_buffer=num_samples)
            my_buf = []  # 存放录音数据
            # count = 0
            t = time.time()
            while time.time() < t + 2:  # 设置录音时间（秒）
                # 循环read, 每次read 2000frames
                string_audio_data = stream.read(num_samples)
                my_buf.append(string_audio_data)
            save_wave_file(audio_path, my_buf)
            stream.close()
            p = FrameRight2(self.master)
            p.show_done_steps([1,1,0,0],v1=v1.get(),v2=audio_path)
            sys.stdout.flush()

        self.audiorecord = tk.Button(self.FrameLeft)
        self.audiorecord.place(relx=0.078, rely=0.536, height=115, width=309)
        self.audiorecord.configure(activebackground="#f1ede6")
        self.audiorecord.configure(activeforeground="#f1ede6")
        self.audiorecord.configure(anchor='e')
        self.audiorecord.configure(borderwidth="3")
        self.audiorecord.configure(background="#f1ede6")
        self.audiorecord.configure(disabledforeground="#f1ede6")
        self.audiorecord.configure(font="-family {微软雅黑} -size 13 -weight bold")
        self.audiorecord.configure(foreground="#000000")
        self.audiorecord.configure(highlightbackground="#f1ede6")
        self.audiorecord.configure(highlightcolor="black")
        self.audiorecord.configure(pady="0")
        self.audiorecord.configure(command=record)
        self.audiorecord.configure(text='''实时录音   ''')

        #文件夹和麦克风的小图标
        global icon1
        icon1 = tk.PhotoImage(file="./img/ICON1.png")
        self.folder = tk.Canvas(self.FrameLeft)
        self.folder.place(relx=0.086, rely=0.310, relheight=0.159
                          , relwidth=0.096)
        self.folder.configure(background="#f1ede6")
        self.folder.configure(borderwidth="0")
        self.folder.configure(highlightbackground="#f1ede6")
        self.folder.configure(highlightcolor="#f1ede6")
        self.folder.configure(insertbackground="#f1ede6")
        self.folder.configure(relief="ridge")
        self.folder.configure(selectbackground="#f1ede6")
        self.folder.configure(selectforeground="#f1ede6")
        self.folder.create_image(20, 15, anchor='nw', image=icon1)

        global icon2
        icon2 = tk.PhotoImage(file="./img/ICON2.png")
        self.microphone = tk.Canvas(self.FrameLeft)
        self.microphone.place(relx=0.086, rely=0.545, relheight=0.159
                              , relwidth=0.096)
        self.microphone.configure(background="#f1ede6")
        self.microphone.configure(borderwidth="0")
        self.microphone.configure(highlightbackground="#f1ede6")
        self.microphone.configure(highlightcolor="#646464")
        self.microphone.configure(insertbackground="#f1ede6")
        self.microphone.configure(relief="ridge")
        self.microphone.configure(selectbackground="#00ffff")
        self.microphone.configure(selectforeground="white")
        self.microphone.create_image(32, 15, anchor='nw', image=icon2)

        '''开始识别'''
        def jia():
            result, per = page0_support.prediction(audio_path)
            #result = page0_support.baidu_api(devpid, audio_path)
            p = FrameRight3(self.master)
            p.show_result(result)
        self.begin = tk.Button(self.FrameLeft)
        self.begin.place(relx=0.132, rely=0.762, height=71, width=159)
        self.begin.configure(activebackground="#000000")
        self.begin.configure(activeforeground="white")
        self.begin.configure(activeforeground="#000000")
        self.begin.configure(background="#000000")
        self.begin.configure(disabledforeground="#a3a3a3")
        self.begin.configure(font="-family {微软雅黑} -size 11 -weight bold")
        self.begin.configure(foreground="#ffffff")
        self.begin.configure(highlightbackground="#d9d9d9")
        self.begin.configure(highlightcolor="#ffffff")
        self.begin.configure(pady="0")
        self.begin.configure(command=jia)
        self.begin.configure(text='''开始识别''')


'''右边的第一张桌布————排行榜'''
class FrameRight1():
    def __init__(self, master):
        self.master = master
        self.FrameRight1 = tk.Frame(self.master, )
        self.FrameRight1.place(relx=0.405, rely=0.028, relheight=0.952
                , relwidth=0.578)
        self.FrameRight1.configure(relief='groove')
        self.FrameRight1.configure(borderwidth="2")
        self.FrameRight1.configure(relief="groove")
        self.FrameRight1.configure(background="#f1ede6")
        self.FrameRight1.configure(highlightbackground="#d9d9d9")
        self.FrameRight1.configure(highlightcolor="black")

        self.listtitle = tk.Message(self.FrameRight1)
        self.listtitle.place(relx=0.205, rely=0.013, relheight=0.068
                             , relwidth=0.615)
        self.listtitle.configure(background="#f1ede6")
        self.listtitle.configure(font="-family {微软雅黑} -size 16 -weight bold")
        self.listtitle.configure(foreground="#453735")
        self.listtitle.configure(highlightbackground="#d9d9d9")
        self.listtitle.configure(highlightcolor="black")
        self.listtitle.configure(text='''垃圾分类排行榜''')
        self.listtitle.configure(width=483)

        # self.Listbox1 = tk.Listbox(self.FrameRight1)
        # self.Listbox1.place(relx=0.179, rely=0.099, relheight=0.773
        #                     , relwidth=0.681)
        # self.Listbox1.configure(background="#e7dfd3")
        # self.Listbox1.configure(disabledforeground="#a3a3a3")
        # self.Listbox1.configure(font="TkFixedFont")
        # self.Listbox1.configure(foreground="#000000")
        # self.Listbox1.configure(highlightbackground="#d9d9d9")
        # self.Listbox1.configure(highlightcolor="black")
        # self.Listbox1.configure(selectbackground="blue")
        # self.Listbox1.configure(selectforeground="white")

        Colors={"可回收物":"#d0dde4","厨余垃圾":"#4dd1e6","有害垃圾":"#6ebddb","其他垃圾":"#32a5d7","干垃圾":"#0192b3"}
        r=0
        # conn=sqlite3.connect('laji.db')
        # c=conn.cursor()
        # c.execute("SELECT  * FROM contacts ORDER BY phone DESC LIMIT 6")
        # items=c.fetchall()
        pseudo_items=[["猫砂", "其他垃圾", "", 8],
                      ["牛奶盒", "可回收物", "", 7],
                      ["过期药品", "有害垃圾", "", 6],
                      ["旧衣服", "可回收物", "", 6],
                      ["瓜子壳", "厨余垃圾", "", 5],
                      ["塑料袋", "其他垃圾", "", 5]]
        for item in pseudo_items:
            tk.Label(self.FrameRight1,text=item[0],font="-family {微软雅黑} -size 13 ",relief="groove",width=3).place(relx=0.163, 
                                                                                                                  rely=0.099+float(r*0.11), 
                                                                                                                  relheight=0.103,
                                                                                                                  relwidth=0.211)
            tk.Label(self.FrameRight1,bg=Colors[item[1]], text=str(item[3])+"次",fg="white",relief="ridge",width=3).place(relx=0.403, 
                                                                                                                  rely=0.099+float(r*0.11), 
                                                                                                                  relheight=0.103,                                                                                                     
                                                                                                                  relwidth=0.211+0.04*float(item[3]))
            r+=1
        tk.Label(self.FrameRight1,bg="#f1ede6", text="可回收物",font="-family {微软雅黑} -size 13 ").place(relx=0.13, 
                                                                                          rely=0.1+float(r*0.11), 
                                                                                          relheight=0.08,
                                                                                          relwidth=0.211)
        tk.Label(self.FrameRight1,bg="#d0dde4").place(relx=0.13+0.16, 
                                                  rely=0.1+float(r*0.11)+0.02, 
                                                  relheight=0.04,
                                                  relwidth=0.04)
        tk.Label(self.FrameRight1,bg="#f1ede6", text="其他垃圾",font="-family {微软雅黑} -size 13 ").place(relx=0.13+0.2, 
                                                                                          rely=0.1+float(r*0.11), 
                                                                                          relheight=0.08,
                                                                                          relwidth=0.211)
        tk.Label(self.FrameRight1,bg="#32a5d7").place(relx=0.13+0.2+0.16, 
                                                  rely=0.1+float(r*0.11)+0.02, 
                                                  relheight=0.04,
                                                  relwidth=0.04)
        tk.Label(self.FrameRight1,bg="#f1ede6", text="厨余垃圾",font="-family {微软雅黑} -size 13 ").place(relx=0.13+0.2+0.2, 
                                                                                          rely=0.1+float(r*0.11), 
                                                                                          relheight=0.08,
                                                                                          relwidth=0.211)
        tk.Label(self.FrameRight1,bg="#4dd1e6").place(relx=0.13+0.2+0.2+0.16, 
                                                  rely=0.1+float(r*0.11)+0.02, 
                                                  relheight=0.04,
                                                  relwidth=0.04)
        tk.Label(self.FrameRight1,bg="#f1ede6", text="有害垃圾",font="-family {微软雅黑} -size 13 ").place(relx=0.13, 
                                                                                          rely=0.1+float((r+0.5)*0.11), 
                                                                                          relheight=0.08,
                                                                                          relwidth=0.211)
        tk.Label(self.FrameRight1,bg="#6ebddb").place(relx=0.13+0.16, 
                                                  rely=0.1+float((r+0.5)*0.11)+0.02, 
                                                  relheight=0.04,
                                                  relwidth=0.04)
        
        tk.Label(self.FrameRight1,bg="#f1ede6", text="干垃圾",font="-family {微软雅黑} -size 13 ").place(relx=0.13+0.2, 
                                                                                          rely=0.1+float((r+0.5)*0.11), 
                                                                                          relheight=0.08,
                                                                                          relwidth=0.211)
        tk.Label(self.FrameRight1,bg="#0192b3").place(relx=0.13+0.16+0.2, 
                                                  rely=0.1+float((r+0.5)*0.11)+0.02, 
                                                  relheight=0.04,
                                                  relwidth=0.04)
        


        self.TSeparator3 = ttk.Separator(self.FrameRight1)
        self.TSeparator3.place(relx=0.013, rely=0.947,  relwidth=0.51)

        self.statement2 = tk.Message(self.FrameRight1)
        self.statement2.place(relx=0.013, rely=0.963, relheight=0.036
                , relwidth=0.587)
        self.statement2.configure(anchor='w')
        self.statement2.configure(background="#f1ede6")
        self.statement2.configure(font="-family {微软雅黑} -size 8")
        self.statement2.configure(foreground="#a5a2a5")
        self.statement2.configure(highlightbackground="#d9d9d9")
        self.statement2.configure(highlightcolor="black")
        self.statement2.configure(text='''相关内容由人工智能技术生成。''')
        self.statement2.configure(width=436)

        btn_back = tk.Button(self.FrameRight1, text='下一步', command=self.goon)
        btn_back.place(relx=0.0, rely=0.0)

    def goon(self):
        self.FrameRight1.destroy()
        FrameRight2(self.master)

'''右边的第二张桌布————中间过程'''
class FrameRight2():
    def __init__(self, master):
        self.master = master
        self.FrameRight2 = tk.Frame(self.master, )
        self.FrameRight2.place(relx=0.405, rely=0.028, relheight=0.952, relwidth=0.578)
        self.FrameRight2.configure(relief="groove")
        self.FrameRight2.configure(background="#f1ede6")
        self.FrameRight2.configure(highlightbackground="#d9d9d9")
        self.FrameRight2.configure(highlightcolor="black")

        self.fenleizhong = tk.Message(self.FrameRight2)
        self.fenleizhong.place(relx=0.205, rely=0.013, relheight=0.068, relwidth=0.615)
        self.fenleizhong.configure(background="#f1ede6")
        self.fenleizhong.configure(font="-family {微软雅黑} -size 16 -weight bold")
        self.fenleizhong.configure(foreground="#453735")
        self.fenleizhong.configure(highlightbackground="#d9d9d9")
        self.fenleizhong.configure(highlightcolor="black")
        self.fenleizhong.configure(text='''为你分类中''')
        self.fenleizhong.configure(width=483)

        self.TSeparator3 = ttk.Separator(self.FrameRight2)
        self.TSeparator3.place(relx=0.013, rely=0.947,  relwidth=0.51)

        self.statement2 = tk.Message(self.FrameRight2)
        self.statement2.place(relx=0.013, rely=0.963, relheight=0.036, relwidth=0.587)
        self.statement2.configure(anchor='w')
        self.statement2.configure(background="#f1ede6")
        self.statement2.configure(font="-family {微软雅黑} -size 8")
        self.statement2.configure(foreground="#a5a2a5")
        self.statement2.configure(highlightbackground="#d9d9d9")
        self.statement2.configure(highlightcolor="black")
        self.statement2.configure(text='''相关内容由人工智能技术生成。''')
        self.statement2.configure(width=436)


        # 画布
        self.process = tk.Canvas(self.FrameRight2)
        self.process.place(relx=0.046, rely=0.11, relheight=0.415, relwidth=0.914)
        self.process.configure(background="#ffffff")
        self.process.configure(borderwidth="2")
        self.process.configure(highlightbackground="#d9d9d9")
        self.process.configure(highlightcolor="black")
        self.process.configure(insertbackground="black")
        self.process.configure(relief="ridge")
        self.process.configure(selectbackground="blue")
        self.process.configure(selectforeground="white")
        # 文本框
        self.processmessage = tk.Text(self.FrameRight2)
        self.processmessage.place(relx=0.09, rely=0.554, relheight=0.356, relwidth=0.826)
        self.processmessage.configure(background="#f1ede6")
        self.processmessage.configure(font="-family {宋体} -size 10")
        self.processmessage.configure(foreground="black")
        self.processmessage.configure(highlightbackground="#d9d9d9")
        self.processmessage.configure(highlightcolor="black")
        self.processmessage.configure(insertbackground="black")
        self.processmessage.configure(relief="flat")
        self.processmessage.configure(selectbackground="blue")
        self.processmessage.configure(selectforeground="#ffffffffffff")
        self.processmessage.configure(wrap="word")

        btn_back = tk.Button(self.FrameRight2, text='下一步', command=self.goahead)
        btn_back.place(relx=0.0, rely=0.0)
    def goahead(self):
        self.FrameRight2.destroy()
        FrameRight3(self.master)
    def draw(self,audiopath):
        f = Figure(figsize=(5, 4), dpi=100,
                   facecolor="#f1ede6",edgecolor="#f1ede6")
        a = f.add_subplot(111)
        b = wave.open(audiopath)
        nf = b.getnframes()
        data = b.readframes(nf) # data还不是数的列表，而是一个bytes格式的数据
        w = np.frombuffer(data, dtype=np.int16) #把data转化为数组
        t = np.arange(len(w))/float(nf)
        w = w * 1.0 / (max(abs(w)))#除以最大值，使得所有的数字介于-1到1之间
        a.plot(t,w, linewidth=0.1, c='g',alpha=0.7)
        canvas = FigureCanvasTkAgg(f,self.FrameRight2)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.046, rely=0.11, relheight=0.415, relwidth=0.914)
    def show_done_steps(self,steps,v1,v2,):
        if steps[0] == 1:
            self.processmessage.insert(END, "您选择的语音种类是：")
            words2 = [v1]
            words = ["done!"]
            self.processmessage.insert(END, "".join("{k:.<{m}}".format(k=k,m=40) for k in words2))
            self.processmessage.insert(END, "".join("{k:.>{m}}".format(k=k,m=15) for k in words))
            if steps[1] == 1:
                self.draw(v2)
                self.processmessage.insert(END, "\n您已经输入好音频，地址为：")
                words2 = [v2]
                words = ["done!"]
                self.processmessage.insert(END, "".join("{k:.<{m}}".format(k=k, m=40) for k in words2))
                self.processmessage.insert(END, "".join("{k:.>{m}}".format(k=k, m=15) for k in words))
                self.processmessage.insert(END, "\n您确认无误后，可点击“开始识别")
                words = ["Wait!"]
                self.processmessage.insert(END, "".join("{k:.>{m}}".format(k=k, m=52) for k in words))
                if steps[2] == 1:
                    self.processmessage.insert(END,"\n已传入识别系统...")
                    words = ["done!"]
                    self.processmessage.insert(END, "".join("{k:.>{m}}".format(k=k, m=40) for k in words))
                    if steps[3] == 1:
                        self.processmessage.insert(END,"\n完成识别！")
                        words = ["done!"]
                        self.processmessage.insert(END, "".join("{k:.>{m}}".format(k=k, m=15) for k in words))
            else:
                self.processmessage.insert(END, "\n您还未输入音频")
                words = ["Wait!"]
                self.processmessage.insert(END, "".join("{k:.>{m}}".format(k=k, m=67) for k in words))


'''右边的第三张桌布————显示结果'''
class FrameRight3():
    def __init__(self, master):
        self.master = master
        self.FrameRight3 = tk.Frame(self.master, )
        self.FrameRight3.place(relx=0.405, rely=0.028, relheight=0.952
                , relwidth=0.578)
        self.FrameRight3.configure(relief="ridge")
        self.FrameRight3.configure(background="#f1ede6")
        self.FrameRight3.configure(highlightbackground="#d9d9d9")
        self.FrameRight3.configure(highlightcolor="black")

        self.Resulttitle = tk.Message(self.FrameRight3)
        self.Resulttitle.place(relx=0.205, rely=0.013, relheight=0.068, relwidth=0.615)
        self.Resulttitle.configure(background="#f1ede6")
        self.Resulttitle.configure(font="-family {微软雅黑} -size 16 -weight bold")
        self.Resulttitle.configure(foreground="#453735")
        self.Resulttitle.configure(highlightbackground="#d9d9d9")
        self.Resulttitle.configure(highlightcolor="black")
        self.Resulttitle.configure(text='''识别结果''')
        self.Resulttitle.configure(width=483)

        global icon3
        icon3 = tk.PhotoImage(file="./img/man.png")
        self.trashcan = tk.Canvas(self.FrameRight3)
        self.trashcan.place(relx=0.013, rely=0.281, relheight=0.609, relwidth=0.502)
        self.trashcan.configure(background="#f1ede6")
        self.trashcan.configure(borderwidth="0")
        self.trashcan.configure(highlightbackground="#f1ede6")
        self.trashcan.configure(insertbackground="#f1ede6")
        self.trashcan.configure(relief="ridge")
        self.trashcan.create_image(100, 10, anchor='n', image=icon3)

        self.TSeparator3 = ttk.Separator(self.FrameRight3)
        self.TSeparator3.place(relx=0.013, rely=0.947,  relwidth=0.51)

        self.statement2 = tk.Message(self.FrameRight3)
        self.statement2.place(relx=0.013, rely=0.963, relheight=0.036, relwidth=0.587)
        self.statement2.configure(anchor='w')
        self.statement2.configure(background="#f1ede6")
        self.statement2.configure(font="-family {微软雅黑} -size 8")
        self.statement2.configure(foreground="#a5a2a5")
        self.statement2.configure(highlightbackground="#d9d9d9")
        self.statement2.configure(highlightcolor="black")
        self.statement2.configure(text='''相关内容由人工智能技术生成。''')
        self.statement2.configure(width=436)
        # 结果
        self.result = tk.Message(self.FrameRight3)
        self.result.place(relx=0.463, rely=0.076, relheight=0.228, relwidth=0.261)
        self.result.configure(background="#f1ede6")
        self.result.configure(font="-family {Microsoft YaHei UI} -size 23 -weight bold")
        self.result.configure(foreground="#000000")
        self.result.configure(highlightbackground="#d9d9d9")
        self.result.configure(highlightcolor="#000000")
        # self.result.configure(text='''……属于可回收物''')
        self.result.configure(width=194)
        # 介绍该种垃圾
        self.introduction = tk.Text(self.FrameRight3)
        self.introduction.place(relx=0.592, rely=0.295, relheight=0.446, relwidth=0.396)
        self.introduction.configure(background="#eedcc6")
        self.introduction.configure(font="TkTextFont")
        self.introduction.configure(foreground="black")
        self.introduction.configure(highlightbackground="#d9d9d9")
        self.introduction.configure(font="-family {微软雅黑} -size 13 ")
        self.introduction.configure(highlightcolor="black")
        self.introduction.configure(insertbackground="black")
        self.introduction.configure(selectbackground="blue")
        self.introduction.configure(selectforeground="white")
        self.introduction.configure(wrap="word")
        # 提示框提供搜索
        self.search = tk.Text(self.FrameRight3)
        self.search.place(relx=0.538, rely=0.796, relheight=0.161
                , relwidth=0.448)
        self.search.configure(background="#f1ede6")
        self.search.configure(font="TkTextFont")
        self.search.configure(font="-family {微软雅黑} -size 10 ")
        self.search.configure(foreground="black")
        self.search.configure(highlightbackground="#d9d9d9")
        self.search.configure(highlightcolor="black")
        self.search.configure(insertbackground="black")
        self.search.configure(selectbackground="blue")
        self.search.configure(selectforeground="white")
        self.search.configure(wrap="word")

        btn_back = tk.Button(self.FrameRight3, text='返回', command=self.back)
        btn_back.place(relx=0.0, rely=0.0)

    def back(self):
        self.FrameRight3.destroy()
        FrameRight1(self.master)

    def show_result(self,result):
        lei,kepu = page0_support.find(result)
        myText = "{}属于{}".format(result,lei)
        self.result.configure(text=myText)
        self.introduction.insert(END,kepu)
        #6c61ff
        self.search.insert(END,"百度，搜一下就知道！\n请帮助我们完善数据库,\n查询并选择您所说的垃圾对应的类别")
        self.search.tag_add("百度，搜一下就知道！",1.0,2.0)
        self.search.tag_config("百度，搜一下就知道！",underline=True)
        def webshow(event):
            webbrowser.open("http://www.baidu.com")
        self.search.tag_bind("百度，搜一下就知道！","<Button-1>",webshow)

if __name__ == '__main__':
    root = tk.Tk()
    basedesk(root)
    root.title("语音识别垃圾分类小程序")
    root.iconbitmap('./img/favicon.ico')
    root.mainloop()