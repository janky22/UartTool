# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # author:洪卫
 
# import tkinter as tk  # 使用Tkinter前需要先导入
 
# # 第1步，实例化object，建立窗口window
# window = tk.Tk()
 
# # 第2步，给窗口的可视化起名字
# window.title('My Window')
 
# # 第3步，设定窗口的大小(长 * 宽)
# window.geometry('500x300')  # 这里的乘是小x
 
# # 第4步，在图形界面上创建一个标签label用以显示并放置
# var1 = tk.StringVar()  # 创建变量，用var1用来接收鼠标点击具体选项的内容
# l = tk.Label(window, bg='green', fg='yellow',font=('Arial', 12), width=10, textvariable=var1)
# l.pack()
 
# # 第6步，创建一个方法用于按钮的点击事件
# def print_selection():
#     value = lb.get(lb.curselection())   # 获取当前选中的文本
#     var1.set(value)  # 为label设置值
 
# # 第5步，创建一个按钮并放置，点击按钮调用print_selection函数
# b1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
# b1.pack()
 
# # 第7步，创建Listbox并为其添加内容
# var2 = tk.StringVar()
# var2.set((1,2,3,4)) # 为变量var2设置值
# # 创建Listbox
# lb = tk.Listbox(window, listvariable=var2)  #将var2的值赋给Listbox
# # 创建一个list并将值循环添加到Listbox控件中
# list_items = [11,22,33,44]
# for item in list_items:
#     lb.insert('end', item)  # 从最后一个位置开始加入值
# lb.insert(1, 'first')       # 在第一个位置加入'first'字符
# lb.insert(2, 'second')      # 在第二个位置加入'second'字符
# lb.delete(2)                # 删除第二个位置的字符
# lb.pack()
 
# # 第8步，主窗口循环显示
# window.mainloop()




#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:洪卫
 
# import tkinter as tk  # 使用Tkinter前需要先导入
 
# # 第1步，实例化object，建立窗口window
# window = tk.Tk()
 
# # 第2步，给窗口的可视化起名字
# window.title('My Window')
 
# # 第3步，设定窗口的大小(长 * 宽)
# window.geometry('500x300')  # 这里的乘是小x
 
# # 第4步，在图形界面上创建一个标签label用以显示并放置
# var = tk.StringVar()    # 定义一个var用来将radiobutton的值和Label的值联系在一起.
# l = tk.Label(window, bg='yellow', width=20, text='empty')
# l.pack()
 
# # 第6步，定义选项触发函数功能
# def print_selection():
#     l.config(text='you have selected ' + var.get())
 
# # 第5步，创建三个radiobutton选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
# r1 = tk.Radiobutton(window, text='Option A', variable=var, value='A', command=print_selection)
# r1.pack()
# r2 = tk.Radiobutton(window, text='Option B', variable=var, value='B', command=print_selection)
# r2.pack()
# r3 = tk.Radiobutton(window, text='Option C', variable=var, value='C', command=print_selection)
# r3.pack()
 
# # 第7步，主窗口循环显示
# window.mainloop()





#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:洪卫
 
# import tkinter as tk  # 使用Tkinter前需要先导入
 
# # 第1步，实例化object，建立窗口window
# window = tk.Tk()
 
# # 第2步，给窗口的可视化起名字
# window.title('My Window')
 
# # 第3步，设定窗口的大小(长 * 宽)
# window.geometry('500x300')  # 这里的乘是小x
 
# # 第4步，在图形界面上创建一个标签label用以显示并放置
# l = tk.Label(window, bg='green', fg='white', width=20, text='empty')
# l.pack()
 
# # 第6步，定义一个触发函数功能
# def print_selection(v):
#     l.config(text='you have selected ' + v)

# # 第5步，创建一个尺度滑条，长度200字符，从0开始10结束，以2为刻度，精度为0.01，触发调用print_selection函数
# s = tk.Scale(window, label='try me', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=2, resolution=0.01, command=print_selection)
# s.pack()
 
# # 第7步，主窗口循环显示
# window.mainloop()





#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:洪卫
 
# import tkinter as tk  # 使用Tkinter前需要先导入
 
# # 第1步，实例化object，建立窗口window
# window = tk.Tk()
 
# # 第2步，给窗口的可视化起名字
# window.title('My Window')
 
# # 第3步，设定窗口的大小(长 * 宽)
# window.geometry('500x300')  # 这里的乘是小x
 
# # 第4步，在图形界面上创建一个标签用以显示内容并放置
# l = tk.Label(window, text='      ', bg='green')
# l.pack()
 
# # 第10步，定义一个函数功能，用来代表菜单选项的功能，这里为了操作简单，定义的功能比较简单
# counter = 0
# def do_job():
#     global counter
#     l.config(text='do '+ str(counter))
#     counter += 1
 
# # 第5步，创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
# menubar = tk.Menu(window)
 
# # 第6步，创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，Exit功能项）
# filemenu = tk.Menu(menubar, tearoff=0)
# # 将上面定义的空菜单命名为File，放在菜单栏中，就是装入那个容器中
# menubar.add_cascade(label='File', menu=filemenu)
 
# # 在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
# filemenu.add_command(label='New', command=do_job)
# filemenu.add_command(label='Open', command=do_job)
# filemenu.add_command(label='Save', command=do_job)
# filemenu.add_separator()    # 添加一条分隔线
# filemenu.add_command(label='Exit', command=window.quit) # 用tkinter里面自带的quit()函数
 
# # 第7步，创建一个Edit菜单项（默认不下拉，下拉内容包括Cut，Copy，Paste功能项）
# editmenu = tk.Menu(menubar, tearoff=0)
# # 将上面定义的空菜单命名为 Edit，放在菜单栏中，就是装入那个容器中
# menubar.add_cascade(label='Edit', menu=editmenu)
 
# # 同样的在 Edit 中加入Cut、Copy、Paste等小命令功能单元，如果点击这些单元, 就会触发do_job的功能
# editmenu.add_command(label='Cut', command=do_job)
# editmenu.add_command(label='Copy', command=do_job)
# editmenu.add_command(label='Paste', command=do_job)
 
# # 第8步，创建第二级菜单，即菜单项里面的菜单
# submenu = tk.Menu(filemenu) # 和上面定义菜单一样，不过此处实在File上创建一个空的菜单
# filemenu.add_cascade(label='Import', menu=submenu, underline=0) # 给放入的菜单submenu命名为Import
 
# # 第9步，创建第三级菜单命令，即菜单项里面的菜单项里面的菜单命令（有点拗口，笑~~~）
# submenu.add_command(label='Submenu_1', command=do_job)   # 这里和上面创建原理也一样，在Import菜单项中加入一个小菜单命令Submenu_1
 
# # 第11步，创建菜单栏完成后，配置让菜单栏menubar显示出来
# window.config(menu=menubar)
 
# # 第12步，主窗口循环显示
# window.mainloop()









#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:洪卫
 
# import tkinter as tk  # 使用Tkinter前需要先导入
 
# # 第1步，实例化object，建立窗口window
# window = tk.Tk()
 
# # 第2步，给窗口的可视化起名字
# window.title('My Window')
 
# # 第3步，设定窗口的大小(长 * 宽)
# window.geometry('500x300')  # 这里的乘是小x
 
# # 第4步，在图形界面上创建一个标签用以显示内容并放置
# tk.Label(window, text='on the window', bg='red', font=('Arial', 16)).pack()   # 和前面部件分开创建和放置不同，其实可以创建和放置一步完成
 
# # 第5步，创建一个主frame，长在主window窗口上
# frame = tk.Frame(window)
# frame.pack()
 
# # 第6步，创建第二层框架frame，长在主框架frame上面
# frame_l = tk.Frame(frame)# 第二层frame，左frame，长在主frame上
# frame_r = tk.Frame(frame)# 第二层frame，右frame，长在主frame上
# frame_l.pack(side='left')
# frame_r.pack(side='right')
 
# # 第7步，创建三组标签，为第二层frame上面的内容，分为左区域和右区域，用不同颜色标识
# tk.Label(frame_l, text='on the frame_l1', bg='green').pack()
# tk.Label(frame_l, text='on the frame_l2', bg='green').pack()
# tk.Label(frame_l, text='on the frame_l3', bg='green').pack()
# tk.Label(frame_r, text='on the frame_r1', bg='yellow').pack()
# tk.Label(frame_r, text='on the frame_r2', bg='yellow').pack()
# tk.Label(frame_r, text='on the frame_r3', bg='yellow').pack()
 
# # 第8步，主窗口循环显示
# window.mainloop()








# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # author:洪卫
 
# # import tkinter as tk  # 使用Tkinter前需要先导入
# # import tkinter.messagebox  # 要使用messagebox先要导入模块
 
# # # 第1步，实例化object，建立窗口window
# # window = tk.Tk()
 
# # # 第2步，给窗口的可视化起名字
# # window.title('My Window')
 
# # # 第3步，设定窗口的大小(长 * 宽)
# # window.geometry('500x300')  # 这里的乘是小x
 
# # # 第5步，定义触发函数功能
# # def hit_me():
# #     tkinter.messagebox.showinfo(title='Hi', message='你好！')              # 提示信息对话窗
# #     # tkinter.messagebox.showwarning(title='Hi', message='有警告！')       # 提出警告对话窗
# #     # tkinter.messagebox.showerror(title='Hi', message='出错了！')         # 提出错误对话窗
# #     # print(tkinter.messagebox.askquestion(title='Hi', message='你好！'))  # 询问选择对话窗return 'yes', 'no'
# #     # print(tkinter.messagebox.askyesno(title='Hi', message='你好！'))     # return 'True', 'False'
# #     # print(tkinter.messagebox.askokcancel(title='Hi', message='你好！'))  # return 'True', 'False'
 
# # # 第4步，在图形界面上创建一个标签用以显示内容并放置
# # tk.Button(window, text='hit me', bg='green', font=('Arial', 14), command=hit_me).pack()
 
# # # 第6步，主窗口循环显示
# # window.mainloop()









# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # author:洪卫
 
# import tkinter as tk  # 使用Tkinter前需要先导入
 
# # 第1步，实例化object，建立窗口window
# window = tk.Tk()
 
# # 第2步，给窗口的可视化起名字
# window.title('My Window')
 
# # 第3步，设定窗口的大小(长 * 宽)
# window.geometry('500x300')  # 这里的乘是小x
 
# # 第4步，grid 放置方法
# for i in range(3):
#     for j in range(3):
#         tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)
 
# # 第5步，主窗口循环显示
# window.mainloop()













