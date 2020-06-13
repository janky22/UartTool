 # -*- coding:utf-8 -*- 
import wx
import numpy as np
from multiprocessing import Process
import serial.tools.list_ports
import threading, time

# My
# import MyFile
def get_time_stamp():
    t = time.time()
    d = (t - int(t)) * 100
    string = "%02d:%02d:%02d.%02d"%(time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec, d)
    return string

def str2hexstr(string):
    hex_ = []
    for c in string :
        hex_.append(ord(c))
    text = ""
    for h in hex_ :
        if h != 0x20 :
            text += str("0x%02x "%h)
    return text

def hexstr2hex(hexstr):
    hexhex = []
    hh = bytes(bytearray.fromhex(hexstr))
    for h in hh :
        if h != 0x20 :
            hexhex.append(h)
    return hexhex

def hex2str(hex_):
    string = ""
    for h in hex_ :
        string += str("0x%02x "%h)
    return string


class UartDrive():
    __readTHr_exit = 0
    def __init__(self, com, baudr, onRx):
        self.__uart = serial.Serial(com, baudr, timeout=0.5)
        self.__uartReadThr = threading.Thread( target=self.__uartRead, args=(onRx,))
        self.__readTHr_exit = 0
        self.__uartReadThr.start()

    def __uartRead(self, onRx):
        while(1):
            if self.__readTHr_exit == 1 :
                break
            text = ""
            text = self.__uart.readall().decode('gb2312')
            if text != "" :
                print(text)
                onRx(text)

                # if text.find("next") >= 0 :
                #     data = upfile.get_data()
                #     print("send")
                #     if data != None :
                #         self._uartSend(data)

    def _uartSend(self, data, code=''):
        if code == "" : 
            print("data=" + str(data))
            self.__uart.write(data)
        else :
            self.__uart.write( (data + "\r\n").encode('gb2312') )
 
    def _uartClos(self):
        try:
            self.__readTHr_exit = 1
            self.__uartReadThr.join()
            print("接收线程已退出")
            self.__uart.close()
        except:
            print('串口关闭失败')

#1 定义事件
class wx_MyEvent(wx.PyCommandEvent):
    def __init__(self, evtType, id):
        wx.PyCommandEvent.__init__(self, evtType, id)
        self.__eventArgs = ""

    def GetEventArgs(self):
        return self.__eventArgs

    def SetEventArgs(self, args):
        self.__eventArgs = args

class UartTool(wx.Frame):
    def __init__(self, name):
        wx.Frame.__init__(self, parent=None, id=-1, title=name, pos=(100,100), size=(800,600))
        #放一个面板，用于布局其他控件
        panel = wx.Panel(self)
        #创建静态控件
        pos1 = 5
        pos2 = 10
        #串口基本功能
        #portList = self.__findPort()
        wx.StaticText(panel, label='串  口：',pos=(pos1,pos2) )
        self.__uartCOB = wx.ComboBox(panel,-1,value='', pos=(pos1+50,pos2-5), size=(300,25), style=wx.CB_SORT)
        
        wx.StaticText(panel, label='波特率：',pos=(pos1,pos2+30))
        baudrList = ["19200", "115200", "2400"]
        baudrCOB = wx.ComboBox(panel, -1, value=' ', pos=(pos1+50,pos2+25), choices=baudrList, style=wx.CB_SORT)

        self.__tipsTxt = wx.StaticText(panel, label='提示：请选择串口与波特率', pos=(pos1+140,pos2+30))
        
        self.__open = False
        scanPortBt= wx.Button(panel, -1, label='更新串口', pos=(pos1,pos2+60))
        self.__opBt = wx.Button(panel, -1, label='打开串口', pos=(pos1+90,pos2+60))

        RxClean = wx.Button(panel, -1, label='清除接收', pos=(pos1, pos2+100))

        self.__hexR = wx.CheckBox(panel, -1, label='hex接收', pos=(pos1+90,pos2+100))
        self.__hexS = wx.CheckBox(panel, -1, label='hex发送', pos=(pos1+90,pos2+120))

        self.__RxDisplay = wx.TextCtrl(panel, pos=(pos1,pos2+140), size=(700,300), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.__RxDisplay.SetScrollbar(wx.VERTICAL, 0, 16, 20)

        sendBt = wx.Button(panel, -1, label='发 送', pos=(pos1+610,pos2+450),size=(70,50))
        self.__TxText = wx.TextCtrl(panel, pos=(pos1,pos2+445), size=(600,50), style=wx.TE_MULTILINE)

        #添加事件处理
        self.Bind(wx.EVT_COMBOBOX, self.__on_uartSet,  self.__uartCOB)
        self.Bind(wx.EVT_COMBOBOX, self.__on_baudrSet, baudrCOB)
        self.Bind(wx.EVT_BUTTON,   self.__on_scanPort, scanPortBt)
        self.Bind(wx.EVT_BUTTON,   self.__on_uartCtrl, self.__opBt)
        self.Bind(wx.EVT_BUTTON,   self.__on_uartSend, sendBt)
        self.Bind(wx.EVT_BUTTON,   self.__on_RxClean, RxClean)
        self.Bind(wx.EVT_CLOSE,    self.__on_closeWindow)
 
        #定制事件，Rx显示
        self.Bind(RxDispy_EVT, self.__on_RxDisplay)# 4绑定事件处理函数

        self.__on_scanPort(1)


    def __tips(self, srt):
        self.__tipsTxt.LabelText = '提示：' + srt
        

    def __on_scanPort(self, event):
        portList = []
        for port in serial.tools.list_ports.comports() :
            #print(port.device, port.description)
            portList.append(port.description)
        self.__uartCOB.Clear()
        self.__uartCOB.Append(portList)
        try :
            self.__tips('更新完成')
        except :
            print('更新失败')
        

    def __on_uartSet(self, event):
        uartName = format(event.GetString())
        num1 = uartName.find("(") + 1
        num2 = uartName.find(")")
        self.com = uartName[num1:num2]
        #print("com= " + self.com)

    def __on_baudrSet(self, event):
        self.baudr = int( format(event.GetString()) )
        #print("选择波特率：" + str(self.baudr))

    def __on_RxHandle(self, data):
        evt = wx_MyEvent(RxDispy_EvTy, 1)           #5 创建自定义事件对象
        evt.SetEventArgs(data)                      #6 添加数据到事件
        self.GetEventHandler().ProcessEvent(evt)    #7 处理事件
        

    def __on_RxDisplay(self, even):
        text = even.GetEventArgs()
        if self.__hexR.GetValue() == True :
            text = str2hexstr(text)
        self.__RxDisplay.AppendText("[%s]R: "%get_time_stamp() + text + "\r")

    def __on_RxClean(self, event):
        self.__RxDisplay.SetLabelText("")

    def __on_uartSend(self, event):
        try :
            text = self.__TxText.GetValue()
            if self.__hexS.GetValue() == True :
                try :
                    text = hexstr2hex(text)
                    self.uart._uartSend(text)
                    text = hex2str(text)
                    self.__RxDisplay.AppendText("[%s]S: "%get_time_stamp() + text + "\r")
                except :
                    self.__tips('输入的是非法hex')
                    return
            else :
                self.uart._uartSend(text,'gb2312')
                self.__RxDisplay.AppendText("[%s]S: "%get_time_stamp() + text + "\r")
            self.__tips('发送完成')
        except :
            self.__tips('请打开串口')

    def __on_uartCtrl(self, event):
            try :
                if self.com and self.baudr :
                    if False == self.__open :
                        try :
                            self.uart = UartDrive(self.com,self.baudr, self.__on_RxHandle)
                            self.__tips('打开成功！')
                            self.__opBt.Label = '关闭串口'
                            self.__open = True

                            # self.uart._uartSend("ota-ver:001,size:%d"%upfile.get_size(), 'gb2312')
                        except :
                            __tips('打开失败。该串口可能被占用或松动!')
                    elif True == self.__open :
                        try :
                            self.uart._uartClos()
                            self.__tips('关闭成功')
                            self.__opBt.Label = '打开串口'
                            self.__open = False
                        except :
                            self.__tips('关闭失败')
            except :
                self.__tips('打开失败。请选择正确的串口和波特率!')

    def __on_closeWindow(self, event):
        if True == self.__open :
            self.uart._uartClos()
        self.Destroy()


def main():
    app = wx.App()
    myApp = UartTool("uart tool")
    myApp.Show()
    app.MainLoop()
    


if __name__ == '__main__':
    RxDispy_EvTy = wx.NewEventType() #2 创建一个事件类型
    RxDispy_EVT = wx.PyEventBinder(RxDispy_EvTy, 1) #3 创建一个绑定器对象
    main()

    
    
