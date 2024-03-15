"""
    name: pyautoAss
    author: awiseking
    version: 1.0.5.5
    des: 基于键鼠、图片定位的自动化gui工作套件。
        
"""
from .utils.Utils import *
from .pyclipboard import PyClipboard
from .pyAutoKeyboard import PyAutoKeyboard
from .pyAutoMouse import PyAutoMouse
from .pyAutoGui import PyAutoGui
from .Listening import KeyboardListening,MouseListening

__version__ = "1.0.6.1"

class AutoOperation(PyAutoKeyboard,PyAutoMouse,PyAutoGui):

    def __init__(self,app_name:str="app") -> None:
        """自动化套件
        初始化自动化套件所需组件，自动进行数据处理等工作。
        :param app_name -- 应用名

        :var self.app_name -- 应用名
        :var self.pclip -- 剪贴板控件

        :return: None
        """
        super().__init__()

        self.app_name = app_name
        self.pclip = PyClipboard()
        self.kl = KeyboardListening()
        self.ml = MouseListening()
    
    
    def wait(self):
        """暂停
        在当前位置停下

        Keyword arguments:
        Return: None
        """
        def onPress(key):
            return False
        def onRelease(key):...

        self.listening("k",onPress,onRelease)

    def listening(self, device, onPress, onRelease):
        """暂停
        在当前位置停下

        Keyword arguments:
        Return: None
        """
        if device == "m":
            return self.ml.listening(onPress, onRelease)
        elif device == "k":
            return self.kl.listening(onPress, onRelease)
        else:
            return self.kl.listening(onPress, onRelease)

    # 识别图片左击
    def autoORCLeftClick(self, img_path):
        """
        识别图片后进行左击单击
        :param img_path: 图片路径
        :return: None
        """
        avg = self.getAutoXY(img_path)
        xy = (avg[0],avg[1])
        self.moveClick(*xy)

    # 识别图片右击
    def autoORCRightClick(self, img_path):
        """
        识别图片后进行右击单击
        :param img_path: 图片路径
        :return: None
        """
        avg = self.getAutoXY(img_path)
        xy = (avg[0],avg[1])
        self.moveClick(*xy,about="right")

    # 记录当前数据
    def recordData(self):
        self.record_data = self.paste()

    #  取出当前记录数据
    def getRecordData(self):
        self.pclip.copy(self.record_data)

    # 记录当前备注
    def recordNote(self):
        self.note = self.paste()

    #  取出当前记录备注
    def getRecordNote(self):
        self.pclip.copy(self.note)