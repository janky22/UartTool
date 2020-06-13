import os

def FileRead(path, offet, len):
    try:
        file = open(path, "rb") # 二进制只读
        file.seek(offet, 0)
        data = file.read(len)
        file.close()
        return data
    except :
        print("文件操作失败")
        return None

def FileGetSize(path):
    try :
        return os.path.getsize(path)
    except :
        return 0

class Upgrade:
    __offet = 101
    __path = "G:\\nxp_kw36\mcuxIDE_workpace\\frdmkw36_wireless_examples_bluetooth_otac_att_freertos\\Debug\\otac_att.s19"
    def get_data(self):
        data = FileRead(self.__path, self.__offet, 35)
        if data != None :
            self.__offet = self.__offet + 35 + 11
            return data

    def get_size(self):
        fsize = FileGetSize(self.__path)
        # print("fsize=%d"%fsize)
        # return fsize
        return 514048
        
