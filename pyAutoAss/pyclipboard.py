import win32clipboard as w32cb,win32con
from .dependent.DataType import Queue

class PyClipboard:
    def __init__(self) -> None:
        """剪贴板控件初始化
        @param
        self.memory_mode = 0
        self.contents = ()
        Return: return_description
        """

        self.memory_mode = 0
        self.contents = ()
        self.queue = Queue()
    
    # 读取剪贴板
    def paste(self) -> object:
        """读取剪贴板
        通过win32clipboard读取剪贴板
        Keyword arguments:
        Return: 剪贴板的内容
        """

        w32cb.OpenClipboard()
        content = w32cb.GetClipboardData(win32con.CF_UNICODETEXT)
        w32cb.CloseClipboard()
        return content
    
    # 写入剪贴板
    def copy(self,value:object) -> object:
        """写入剪贴板
        通过win32clipboard写入剪贴板
        Keyword arguments:
        value -- 剪贴板
        Return: None
        """

        w32cb.OpenClipboard()
        w32cb.EmptyClipboard()
        w32cb.SetClipboardData(win32con.CF_UNICODETEXT,value)
        w32cb.CloseClipboard()
        self.queue.enqueue(value)