import re
import wx
import time
from sys import exit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


RELEASE = "发布"

g_platform = {"国内测试平台":"aoduo.test.edaoduo.com",
              "国内生产平台":"tbox.prod.edaoduo.com",
              "哥伦比亚测试平台":"tbox.test.edaoduo.com",
              "哥伦比亚生产平台":"tbox.prod.edaoduo.com"
             }

g_searchDriverType = ["ID", "SN", "名称"]
g_smsSendType = {"网络":"0", "短信":"1"}
g_funtionList = ["获取日志", "删除日志", "同步蓝牙", "复位设备"] #操作列表
g_searchFunction = {    # 操作 对应后台下发的 命令
"获取日志":"SHELL tar cjvf /data/logs.tar.bz2 /data/logs && \
ftpput -u xls -p Aoduo168 www.edaoduo.com  logs/logs.tar.bz2  /data/logs.tar.bz2 && \
rm /data/logs.tar.bz2",
"删除日志":"SHELL rm /data/logs/*" ,
"同步蓝牙":"sync_bt_code_post",
"复位设备":"RESET"
}

class PlatformDriver():
    def __init__(self):
        try:
            self.driver = webdriver.Edge()
            self.driver.set_page_load_timeout(10)
            self.driver.set_script_timeout(10)
        except:
            self.__msgDia("浏览器驱动打开失败", "错误", "退出", wx.OK, wx.ID_OK)

    def login(self, host, username, password):
        self.__host = host
        print(self.__host)
        self.driver.get(self.__host)

        try:
            self.driver.find_element_by_id("device_info") 
            print("已登陆\n")
            return 
        except:
            self.__time_out(5, "id", "index_from", "网络超时", "退出")
            # 登陆
            self.driver.find_element_by_id("username").send_keys(username)
            self.driver.find_element_by_id("password").send_keys(password)
            self.driver.find_element_by_id("loginBtn").click()
            print("正在登陆\n")
            self.__time_out(5,"id", "device_info", "网络超时或用户名和密码有错", "退出")
            print("登陆成功\n")

    def searchDriver(self, type, value):
        self.driver.get(self.__host+"/pages/device/list/list.html")
        Select(self.driver.find_element_by_id("beam_search")).select_by_visible_text(type)
        self.driver.find_element_by_id("keyword").send_keys(value+"\r\n")
        
        time.sleep(1)

        lise = self.driver.find_element_by_id("list_table_info")
        numStr = re.finditer(r'\d+', lise.text)
        num = []
        for n in numStr :
            num.append(int(n.group()))
        print("搜索到的设备个数="+str(num[2]))
        if num[2] == 1:
            return True
        elif num[2] == 0:
            self.__msgDia("搜索的设备不存在", "提示", "不处理", wx.OK, wx.ID_OK)
            return False
        else:
            self.__msgDia("搜索的设备不唯一", "提示", "不处理", wx.OK, wx.ID_OK)
            return False
        


    def searchFunction(self, fun, smsSendType):
        actionMenu = self.driver.find_element_by_class_name("actionMenu")
        ActionChains(self.driver).move_to_element(actionMenu).perform()
        #========================================== 添加操作在此添加
        try:
            if fun == "获取日志":
                self.__sendSms(fun, smsSendType)
            if fun == "删除日志":
                self.__sendSms(fun, smsSendType)
            elif fun == "同步蓝牙":
                self.driver.find_element_by_class_name("sync_bt_code_post").click()
                if RELEASE == "发布" :
                    self.driver.find_element_by_id("btCode_saveBtn").click()   #确认按键
            elif fun == "复位设备":
                self.__sendSms(fun, smsSendType)
        except:
               print("选择操作失败")

    def __logOff(self):
        self.driver.get(self.__host+"/pages/device/list/list.html")
        self.driver.implicitly_wait(3) 
        self.driver.find_element_by_id("admin").click()
        self.driver.find_element_by_id("exit").click()


    def __sendSms(self, fun, smsSendType):
        self.driver.find_element_by_class_name("send_sms_to_device_post").click()
        Select(self.driver.find_element_by_id("send_type")).select_by_value(smsSendType)
        self.driver.find_element_by_id("sendSms_cmd").send_keys(g_searchFunction.get(fun))
        if RELEASE == "发布" :
            self.__time_out(2, "id", "sendSms_saveBtn", "没找到发送按键", "不处理")
            self.driver.find_element_by_id("sendSms_saveBtn").click() #发送按键

    def __time_out(self, time, type, name, msg, action):
        if type == "class":
            locator = (By.CLASS_NAME, name)
        elif type == "id":
            locator = (By.ID , name)
        try:
            print("等待网页加载")
            WebDriverWait(self.driver, time, 0.5).until(EC.presence_of_element_located(locator))
            print("加载完成")
            return True
        except:
            self.__msgDia(msg, "错误", action, wx.OK, wx.ID_OK)
        return False

    def __msgDia(self, msg, cap, action, style, clickId):   #弹框提示
            msg = wx.MessageDialog(None, msg, cap, style) 
            if msg.ShowModal() == clickId:
                if action == "不处理":
                    pass
                if action == "退出":
                    self.driver.close()
                    sys.exit(1)
                msg.Destroy()

    def exit(self):
        print("driver exit")
        self.driver.close()
        print("driver exit")
        return


class LonginPlatformUi(wx.Frame):
    def __init__(self, name, platform):
        wx.Frame.__init__(self, parent=None, id=-1, title=name, pos=(200,200), size=(400,250))
        self.__platformDri = platform
        panel = wx.Panel(self)

        self.icon = wx.Icon("ioc1.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)  

        platformTxt= wx.StaticText(panel, label='选择平台', style=wx.TE_CENTER)

        platformPort = ["哥伦比亚生产平台", "哥伦比亚测试平台", "国内测试平台", "国内生产平台"]
        platformComb = wx.ComboBox(panel, -1, value=' ', choices=platformPort, style=wx.CB_SORT)
        self.Bind(wx.EVT_COMBOBOX, self.__onGetPlatform, platformComb)

        vbox1 = wx.BoxSizer(wx.HORIZONTAL)  #水平
        vbox1.Add(platformTxt, 0, flag=wx.ALL , border=10)
        vbox1.Add(platformComb, 0, flag=wx.ALL , border=10)

        usernameTxt = wx.StaticText(panel, label='用户名', style=wx.TE_CENTER)
        self.__username = wx.TextCtrl(panel)
        vbox2 = wx.BoxSizer(wx.HORIZONTAL)  #水平
        vbox2.Add(usernameTxt, 0, flag=wx.ALL , border=10)
        vbox2.Add(self.__username, 0, flag=wx.ALL , border=10)

        passwordTxt = wx.StaticText(panel, label='密  码', style=wx.TE_CENTER)
        self.__password = wx.TextCtrl(panel, style = wx.TE_PASSWORD)
        vbox3 = wx.BoxSizer(wx.HORIZONTAL)  #水平
        vbox3.Add(passwordTxt, 0, flag=wx.ALL , border=10)
        vbox3.Add(self.__password, 0, flag=wx.ALL , border=10)

        loginBtn = wx.Button(panel, label='登    录')
        cancel = wx.Button(panel, label='取  消')
        self.Bind(wx.EVT_BUTTON, self.__onLogin, loginBtn)
        self.Bind(wx.EVT_BUTTON, self.__onFunCancel, cancel)
        vbox4 = wx.BoxSizer(wx.HORIZONTAL)  #水平
        vbox4.Add(loginBtn, 0, flag=wx.ALL , border=10)
        vbox4.Add(cancel, 0, flag=wx.ALL , border=10)

        vbox = wx.BoxSizer(wx.VERTICAL)  
        vbox.Add(vbox1,    0, flag=wx.ALIGN_CENTER | wx.LEFT, border=10)
        vbox.Add(vbox2,    0, flag=wx.ALIGN_CENTER | wx.LEFT, border=10)
        vbox.Add(vbox3,    0, flag=wx.ALIGN_CENTER | wx.LEFT, border=10)
        vbox.Add(vbox4,    0, flag=wx.ALIGN_CENTER | wx.LEFT, border=10)
        panel.SetSizer(vbox)

        


    def __onGetPlatform(self, event):
        self.__platform = format(event.GetString())


    def __onLogin(self, even):
        username = self.__username.GetValue()
        password = self.__password.GetValue()
        print(self.__platform)
        print(username)
        # print(password)
        self.__platformDri.login(g_platform.get(self.__platform), username, password)
        self.__quit()

    def __quit(self):
        wx.Exit()

    def __onFunCancel(self, event):
        self.__platformDri.exit()
        sys.exit()



class CtrlPlatformUi(wx.Frame):
    def __init__(self, name, platform):
        wx.Frame.__init__(self, parent=None, id=-1, title=name, pos=(200,200), size=(500,350))
        self.__platform = platform
        panel = wx.Panel(self)

        self.icon = wx.Icon("ioc1.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)  
        
        searchTypeTxt = wx.StaticText(panel, label='搜索类型', style=wx.TE_CENTER)
        searchTypeList = g_searchDriverType
        searchTypeComb = wx.ComboBox(panel, -1, value=' ', size=(100,35), choices=searchTypeList, style=wx.CB_SORT)
        self.Bind(wx.EVT_COMBOBOX, self.__onGetsearchType, searchTypeComb)
        vbox1 = wx.BoxSizer(wx.HORIZONTAL)  #水平
        vbox1.Add(searchTypeTxt, 0, flag=wx.ALL , border=10)
        vbox1.Add(searchTypeComb, 0, flag=wx.ALL , border=10)

        searchValueTxt = wx.StaticText(panel, label='搜 索 值', style=wx.TE_CENTER)
        self.__searchValue = wx.TextCtrl(panel)
        vbox2 = wx.BoxSizer(wx.HORIZONTAL)  #水平
        vbox2.Add(searchValueTxt, 0, flag=wx.ALL , border=10)
        vbox2.Add(self.__searchValue, 0, flag=wx.ALL , border=10)

        selectFunTxt = wx.StaticText(panel, label='操作选择', style=wx.TE_CENTER)
        funtionList = g_funtionList
        funtionComb = wx.ComboBox(panel, -1, value=' ', size=(100,35), choices=funtionList, style=wx.CB_SORT)
        self.Bind(wx.EVT_COMBOBOX, self.__onGetFuntion, funtionComb)

        vbox3 = wx.BoxSizer(wx.HORIZONTAL)  #水平
        vbox3.Add(selectFunTxt, 0, flag=wx.ALL , border=10)
        vbox3.Add(funtionComb, 0, flag=wx.ALL , border=10)

        sendTypeTxt = wx.StaticText(panel, label='发送类型', style=wx.TE_CENTER)
        sendTypeList = ["网络", "短信"]
        self.__SendType = "网络"
        sendTypeComb = wx.ComboBox(panel, -1, value="网络", size=(100,35), choices=sendTypeList, style=wx.CB_SORT)
        self.Bind(wx.EVT_COMBOBOX, self.__onGetSendTypeTxt, sendTypeComb)

        vbox4 = wx.BoxSizer(wx.HORIZONTAL)  #水平
        vbox4.Add(sendTypeTxt, 0, flag=wx.ALL , border=10)
        vbox4.Add(sendTypeComb, 0, flag=wx.ALL , border=10)

        ascertain = wx.Button(panel, label='确    定')
        cancel = wx.Button(panel, label='取  消')
        self.Bind(wx.EVT_BUTTON, self.__onFunAscertain, ascertain)
        self.Bind(wx.EVT_BUTTON, self.__onFunCancel, cancel)

        vbox5 = wx.BoxSizer(wx.HORIZONTAL)  #水平
        vbox5.Add(ascertain, 0, flag=wx.ALL , border=10)
        vbox5.Add(cancel, 0, flag=wx.ALL , border=10)

        vbox = wx.BoxSizer(wx.VERTICAL)  #垂直
        vbox.Add(vbox1,    0, flag=wx.ALIGN_CENTER | wx.LEFT, border=10)
        vbox.Add(vbox2,    0, flag=wx.ALIGN_CENTER | wx.LEFT, border=10)
        vbox.Add(vbox3,    0, flag=wx.ALIGN_CENTER | wx.LEFT, border=10)
        vbox.Add(vbox4,    0, flag=wx.ALIGN_CENTER | wx.LEFT, border=10)
        vbox.Add(vbox5,    0, flag=wx.ALIGN_CENTER | wx.LEFT, border=10)
        panel.SetSizer(vbox)


    def __onGetsearchType(self, event):
        self.__tsearchType = format(event.GetString())

    def __onGetSendTypeTxt(self, event):
        self.__SendType = format(event.GetString())

    def __onGetFuntion(self, event):
        self.__funtion = format(event.GetString())


    def __onFunAscertain(self, event):
        status = self.__platform.searchDriver(self.__tsearchType, self.__searchValue .GetValue())
        if status == True:
            self.__platform.searchFunction(self.__funtion , g_smsSendType.get(self.__SendType))


    def __onFunCancel(self, event):
        self.__platform.exit()
        sys.exit()


def longinPlatform(platformDri):
    wxApp = wx.App()
    longinUi = LonginPlatformUi("登录控车云平台", platformDri)
    longinUi.Show()
    wxApp.MainLoop()
    longinUi.Close()


def ctrlPlatform(platformDri):
    wxApp = wx.App()
    ctrlUi = CtrlPlatformUi("欢迎使用控车云平台小工具", platformDri)
    ctrlUi.Show()
    wxApp.MainLoop()


if __name__ == "__main__":
    platformDri = PlatformDriver()
    longinPlatform(platformDri)
    ctrlPlatform(platformDri)


