
# =======================
# 弹框
# 
# import wx
# class MyFrame(wx.Frame):
    
#     def __init__(self, parent, id):
#         wx.Frame.__init__(self, parent, id, u'测试面板Panel', size = (600, 300))
        
#         #创建面板
#         panel = wx.Panel(self) 
        
#         #在Panel上添加Button
#         button = wx.Button(panel, label = u'关闭', pos = (150, 60), size = (100, 60))
        
#         #绑定单击事件
#         self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        
#     def OnCloseMe(self, event):
#         dlg = wx.MessageDialog(None, u"消息对话框测试", u"标题信息", wx.OK)
#         if dlg.ShowModal() == wx.ID_OK:
#             print("点击确定")
#             self.Close(True)
#         dlg.Destroy()
#         # dlg = wx.MessageDialog(None, u"消息对话框测试", u"标题信息", wx.YES_NO | wx.ICON_QUESTION)
#         # if dlg.ShowModal() == wx.ID_YES:
#         #     self.Close(True)
#         # dlg.Destroy()
 

        
# if __name__ == '__main__':
#     app = wx.PySimpleApp()
#     frame = MyFrame(parent = None, id = -1)
#     frame.Show()
#     app.MainLoop()


# # ================================
# # 隐式等待
# # 
# from selenium import webdriver
# driver = webdriver.Edge()
# driver.implicitly_wait(30)  # 隐性等待，最长等30秒
# driver.get("https://huilansame.github.io")

# print(driver.current_url)
# driver.quit()


# ================================
# 显式等待
# 
# -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

# driver = webdriver.Edge()
# driver.implicitly_wait(10)  # 隐性等待和显性等待可以同时用，但要注意：等待的最长时间取两者之中的大者
# driver.get('https://huilansame.github.io')
# locator = (By.LINK_TEXT, 'CSDN')

# try:
#     WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
#     print("out="+driver.find_element_by_link_text('CSDN').get_attribute('href'))
# finally:
#     # driver.close()
#     print("finally")


# ================================
# BoxSizer 例程
# 
# import wx
# class MyApp(wx.App):
# 	def OnInit(self):
# 		frame = MyFrame(parent=None, id=-1, title='ExampleBoxSizer')
# 		frame.Show(True)
# 		return True
 
# class MyFrame(wx.Frame):
# 	def __init__(self, parent, id, title):
# 		wx.Frame.__init__(self, parent, id, title, size=(778, 494),
# 		                  style=wx.DEFAULT_FRAME_STYLE | wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
# 		self.panel = wx.Panel(self, -1)
 
# 		h_box_sizer = wx.BoxSizer(wx.HORIZONTAL)
 
# 		self.file_path = wx.TextCtrl(self.panel, -1)
# 		self.open_button = wx.Button(self.panel, -1, label=u'打开')
# 		self.save_button = wx.Button(self.panel, -1, label= u'保存')
 
# 		h_box_sizer.Add(self.file_path, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
# 		h_box_sizer.Add(self.open_button, proportion=0, flag= wx.ALL, border=5)
# 		h_box_sizer.Add(self.save_button, proportion=0, flag= wx.ALL, border=5)
 
# 		self.edit_text = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE|wx.TE_RICH2|wx.HSCROLL)
 
# 		v_box_sizer = wx.BoxSizer(wx.VERTICAL)
# 		v_box_sizer.Add(h_box_sizer, proportion=0, flag=wx.EXPAND)
# 		v_box_sizer.Add(self.edit_text, proportion=1, flag=wx.EXPAND, border=5)
 
# 		self.panel.SetSizer(v_box_sizer)
 
# def main():
#     app = MyApp()
#     app.MainLoop()
 
# if __name__ == '__main__':
# 	main()


# ================================
# logs 例程
# 
# import re
# import logging 
# #logging模块
# def logs_show():
#     print("wechat running...") 
#     return "wechat" 

# def logs_test1(): 
#     logging.basicConfig(filename='myapp.log', level=logging.INFO) 
#     tag=logs_show() 
#     logging.info('Started %s'%tag) 
#     logging.info('Finished %s'%tag) 

# def logs_test2(): 
#     logging.basicConfig(filename='myapp.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.INFO) 
#     tag=logs_show() 
#     logging.info('%s start in', tag) 
#     logging.info('%s Finished',tag) 

# def logs_test3():
#     logger = logging.getLogger("WeChat") #获取logger对象 
#     logger.setLevel(logging.DEBUG) #设置日志等级 
#     #创建绑定
#     handler = logging.FileHandler('wechat.log') 
#     logger.addHandler(handler) 
#     formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s') # 创建绑定formatter 
#     formatter.datefmt = '%m/%d/%Y %I:%M:%S %p' #可选的 handler.setFormatter(formatter) 
#     #尝试输出错误信息 
#     logger.debug("debug message") 
#     logger.info("info message") 
#     logger.warning("warining message") 
#     logger.error("error message") 
#     logger.critical("critical message")

# def test4(): #format
#     info = ('janky', '18')
#     print("1: {data}".format(data=','.join(info)))
#     print("2: {name} {age}".format(name='janky', age='18'))

# def test5(): #正则表达式 re
#     line = "Cats are smarter than dogs"
    
#     # match
#     matchObj = re.match( r'(.*) are (.*?) (.*) .*', line, re.M|re.I)
#     if matchObj:
#         print ("matchObj.group() : ", matchObj.group())
#         print ("matchObj.group(1) : ", matchObj.group(1))
#         print ("matchObj.group(2) : ", matchObj.group(2))
#         print ("matchObj.group(3) : ", matchObj.group(3))

#     matchObj = re.match( r'smarter', line, re.M|re.I)
#     if matchObj:
#         print("match --> matchObj.group() : ", matchObj.group())
#     else:
#         print("No match!!")

#     # search
#     matchObj = re.search( r'smarter', line, re.M|re.I)
#     if matchObj:
#         print("search --> matchObj.group() : ", matchObj.group())
#     else:
#         print("No match!!")

#     # finditer
#     string = 'abc666efg222ijk3.14'

#     numS = re.finditer( r'\d+', string)
#     num = []
#     for n in numS :
#         #print(num.group())
#         num.append(int(n.group()))
#     for i in range(2) :
#         print(str(num[i]))

# if __name__ == '__main__':
#     logs_test2()
    
# ================================
# http 例程
# 
# import os
# import requests
# # 以下为GET请求
# if __name__ == '__main__':
#     # url = "http://www.baidu.com"
#     url = "http://www.aod.edaoduo.com:5000/bin/xjz/test.txt"
#     res = requests.get(url)
#     print(res.text)
    
#     # with open(os.path.join(os.path.dirname(os.path.abspath("__file__")),"test.exe"),"wb") as f:
#     #     f.write(res.content)



# import wx
# import shutil
# import os

# class Create_Frame( wx.Frame ):
#     def __init__( self, parent, ID, title ):
#         wx.Frame.__init__( self, parent, ID, title, size = ( 380, 250) ,
#                            style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP )
#         panel = wx.Panel( self, -1 )
#         self.icon = wx.Icon('lihf.ico', wx.BITMAP_TYPE_ICO)
#         self.SetIcon(self.icon)  
#         self.list0 = ["中国", "美国", "俄罗斯", "日本", "韩国", "英国", "澳大利亚"]
#         rb = wx.RadioBox(
#                 panel, -1, "北京奥运", wx.DefaultPosition, wx.DefaultSize,
#                 self.list0, 1, wx.RA_SPECIFY_COLS | wx.NO_BORDER )
#         rb.SetToolTip(wx.ToolTip("北京加油!"))
#         rb.Bind(wx.EVT_RADIOBOX, self.Print, rb)
#     def Print( self, event ):
#         ID =  event.GetInt()
#         print(self.list0[ID])
        
# if __name__ == '__main__':
#     app = wx.App()
#     frame = Create_Frame(None, -1, "new frame")
#     frame.Show( True )
#     app.MainLoop()

# def anagram_solution1(s1,s2):
#     a_list = list(s2)
#     pos1 = 0
#     still_ok = True
#     while pos1 < len(s1) and still_ok:
#         pos2 = 0
#         found = False
#         while pos2 < len(a_list) and not found:
#             if s1[pos1] == a_list[pos2]:
#                 found = True
#             else:
#                 pos2 = pos2 + 1
#     if found:
#         a_list[pos2] = None
#     else:
#         still_ok = False
#     pos1 =pos1 + 1
    
#     return still_ok
# if __name__ == '__main__':
#     print(anagram_solution1('abcd','dcba'))
