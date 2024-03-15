import win32con,win32api
from time import sleep
from .utils.VKCODE import vk_code as VKC

class PyAutoMouse:
    # 鼠标点击
    def click(self, about:str="left",n:int=1):
        """鼠标点击
        :param about -- 鼠标左键或右键 选项为 left right -1 1
        :param n -- 点击次数
        :return: None
        """
        if about == "left" or about == "-1":
            self.clickL(n)
        elif about == "right" or about == "1":
            self.clickR(n)
        else:
            raise "参数有错误，请检查一下是否符合要求！"

    # 鼠标左击按下
    def clickDownL(self):
        """
        按下鼠标左键
        :return: None
        """
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0, 0,0)

    
    # 鼠标右击按下
    def clickDownR(self):
        """
        按下鼠标右键
        :return: None
        """
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0, 0,0)

    # 鼠标左击松开
    def clickUpL(self):
        """
        松开鼠标左键
        :return: None
        """
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0, 0,0)
    
    # 鼠标右击松开
    def clickUpR(self):
        """
        松开鼠标右键
        :return: None
        """
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0, 0,0)

    # 鼠标左击
    def clickL(self,n:int=1):
        """鼠标左击
        
        :param n -- 点击次数
        :return: None
        """
        for i in range(n):
            self.clickDownL()
            self.clickUpL()
        
    # 鼠标右击
    def clickR(self,n:int=1):
        """鼠标右击
        
        :param n -- 点击次数
        :return: None
        """
        for i in range (n):
            self.clickDownR()
            self.clickUpR()

    # 鼠标移动
    def move(self,x,y,relative:bool=False):
        """鼠标移动
        
        :param relative -- 是否相对移动
        :param x -- 横向移动距离/横坐标
        :param y-- 纵向移动距离/纵坐标
        :return: None
        """
        if relative:
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,x,y,0,0)
        else:
            win32api.SetCursorPos((x,y))

    # 鼠标移动点击
    def moveClick(self,x,y,relative:bool=False,about:str="left",n:int=1):
        """鼠标点击
        :param relative -- 是否相对移动
        :param x -- 横向移动距离/横坐标
        :param y -- 纵向移动距离/纵坐标
        :param about -- 鼠标左键或右键 选项为 left right -1 1
        :param n -- 点击次数
        :return: None
        """
        self.move(x,y,relative)
        self.click(about,n)

    # 鼠标拖动
    def drag(self,ex,ey,*c,about:str="left"):
        """鼠标拖动
        :param cx -- 横坐标起点
        :param cy -- 纵坐标起点
        :param ex -- 横坐标终点
        :param ey -- 纵坐标终点
        :param about -- 鼠标左键或右键 选项为 left right -1 1
        :return: None
        """
        cx,cy = self.isAutoMouseXY(*c)

        if about == "left" or about == "-1":
            self.dragL(ex,ey,cx,cy)
        elif about == "right" or about == "1":
            self.dragR(ex,ey,cx,cy)
        else:
            raise "参数有错误，请检查一下是否符合要求！"


    # 鼠标左击拖动
    def dragL(self,ex,ey,*c):
        """鼠标左击拖动
        :param cx -- 横坐标起点
        :param cy -- 纵坐标起点
        :param ex -- 横坐标终点
        :param ey -- 纵坐标终点
        :return: None
        """
        cx,cy = self.isAutoMouseXY(*c)

        self.move(cx,cy)
        self.clickDownL()
        sleep(0.3)
        self.move(ex,ey,False)
        sleep(0.3)
        self.clickUpL()

    # 鼠标右击拖动
    def dragR(self,ex,ey,*c):
        """鼠标右击拖动
        :param cx -- 横坐标起点
        :param cy -- 纵坐标起点
        :param ex -- 横坐标终点
        :param ey -- 纵坐标终点
        :return: None
        """
        cx,cy = self.isAutoMouseXY(*c)

        self.move(cx,cy)
        self.clickDownL()
        sleep(0.3)
        self.move(ex,ey,False)
        sleep(0.3)
        self.clickUpL()

    # 鼠标判断是否使用自动获取本地坐标
    def isAutoMouseXY(self,x=None,y=None):
        cx,cy = win32api.GetCursorPos()
        cx,cy = (cx if x is None else x, cy if y is None else y)
        return cx,cy
    
    # 鼠标滚动
    def scroll(self,num:int):
        """鼠标滚动
        :param num -- 滚动范围 为正向上滚动 页面向下 为负向下滚动 页面向上
        :return: None
        """
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0, 0,num)

    # 鼠标向上滚动
    def scrollUp(self,num:int=20):
        """鼠标向上滚动 页面会向下
        :param num -- 滚动范围
        :return: None
        """
        self.scroll(num)

    # 鼠标向下滚动
    def scrollDown(self,num:int=20):
        """鼠标向下滚动 页面会向上
        :param num -- 滚动范围
        :return: None
        """
        self.scroll(-num)