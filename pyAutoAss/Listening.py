from ctypes import *
from ctypes import wintypes
from .utils.VKCODE import vk_code
from .utils.MCODE import m_code
from win32con import *
import win32api
class KBDLLHOOKSTRUCT(Structure):
    _fields_ = [
        ('vkCode', c_int),
        ('scanCode', c_int),
        ('flags', c_int),
        ('time', c_int),
        ('dwExtraInfo', c_uint),
        ('', c_void_p)
    ]
class POINT(Structure):
    _fields_ = [
        ('x', c_long),
        ('y', c_long)
    ]
class MSLLHOOKSTRUCT(Structure):
    _fields_ = [
        ('pt',POINT),
        ('hwnd',c_int),
        ('wHitTestCode',c_uint),
        ('dwExtraInfo',c_uint),
    ]
class BaseListening:
    def __init__(self):
        self._SetWindowsHookEx = windll.user32.SetWindowsHookExA
        self._UnhookWindowsHookEx = windll.user32.UnhookWindowsHookEx
        self._CallNextHookEx = windll.user32.CallNextHookEx
        self._GetMessage = windll.user32.GetMessageW
        self._GetModuleHandle = windll.kernel32.GetModuleHandleW
        self._PeekMessage = windll.user32.PeekMessageA
        self._PostThreadMessage = windll.user32.PostThreadMessageW
        self._GetCurrentThreadId = windll.kernel32.GetCurrentThreadId
        self._GetCurrentThreadId.restype = wintypes.DWORD

        self._t_id = self._GetCurrentThreadId()

        # 监听类型 键盘 win32con.WH_KEYBOARD_LL /鼠标  win32con.WH_KEYBOARD_LL/WH_MOUSE_LL
        self._idHook =  None
        # 保存钩子函数句柄
        self._hwnd = None

    def __enter__(self):
        ...

    def __exit__(self,type,value,trace):
        self.stop()

    def listening(self,onPress,onRelease):
        """listening
        这个方法定义了监听触发时执行的事件并开启监听。

        Keyword arguments:
        onPress -- 当按键按下时将要执行的函数
        onRelease -- 当按键松开时将要执行的函数

        Return: None
        """
        
        self.onPress = onPress
        self.onRelease = onRelease

        # 开始监听
        self.start()

    def func(self,wParam,lParam):
        ...

    def _hookPro(self,nCode=None, wParam=None, lParam=None):
        try:
            if nCode == HC_ACTION:
                msg = self.func(wParam,lParam)

            if msg == False:
                raise Exception("KeyboardInterrupt")
            return self._CallNextHookEx(self._hwnd,nCode, wParam, lParam)
        except Exception:
            self.stop()
            return self._CallNextHookEx(self._hwnd,nCode, wParam, lParam)            

    def waitForMsg(self):

        msg = wintypes.MSG()
        lpmsg = byref(msg)
        self._GetMessage(lpmsg, None, 0, 0)
        return msg

    def start(self):
        """
        函数功能：启动监听
        """
        HOOKPROTYPE = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
        pointer = HOOKPROTYPE(self._hookPro)
        self._hwnd = self._SetWindowsHookEx(
            self._idHook,
            pointer,
            None,
            0)
        self.waitForMsg()

    def kbInterrupt(self,*keys):
        """
        键盘中断，用于检测是否按下组合键，以便中止监听
        """
        status = True
        for key in keys:
            code = vk_code[key]
            state = win32api.GetKeyState(code)
            status = state
        
        return status
        

    def stop(self):
        """
        函数功能：停止监听
        """
        self._UnhookWindowsHookEx(self._hwnd) # 卸载钩子
        self._PostThreadMessage(self._t_id, 0x0401, 0, 0) # 销毁线程

class KeyboardListening(BaseListening):
    """KeyboardListening
    键盘监听类 通过对该类的实例化，可以实现对键盘按键的监听。通过设置onPress和onRelease这两个方法，可以实现对按键事件的挂钩。
    调用star方法运行该监听。
    
    示例：
        from Listening import *
        def onPress(vkcode):
            if vkcode == "esc":
                print("是执行了这里了吗？")
                return False

        def onRelease(key):
            print(f"当前松开了{key}")
            if key == "esc":
                print("是执行了这里了吗？2")
                return False


        if __name__ == '__main__':
            kl = KeyboardListening()
            with kl: 
                kl.listening(onPress,onRelease) 
    """
    
    def __init__(self):
        super().__init__()
        self._idHook =  WH_KEYBOARD_LL
    
    def func(self,wParam,lParam):
        # 获取消息
        KBDLLHOOKSTRUCT_p = POINTER(KBDLLHOOKSTRUCT)
        param = cast(lParam, KBDLLHOOKSTRUCT_p)
        
        # 获取按键码
        vkCode = param.contents.vkCode

        # 转换vk_code获取vkCode对应字符
        key = {value:key for key,value in vk_code.items()}[vkCode]
        
        # 执行键盘按下行为
        if wParam == WM_KEYDOWN or wParam == WM_SYSKEYDOWN:
            msg = self.onPress(key)
        # 执行键盘松开行为
        elif wParam == WM_KEYUP or wParam == WM_SYSKEYUP:
            msg = self.onRelease(key)
        else:
            msg = False

        if self.kbInterrupt("ctrl","c"):  # 检查是否按下Ctrl+C
            msg = False
            
        return msg

class MouseListening(BaseListening):
    def __init__(self):
        super().__init__()
        self._idHook =  WH_MOUSE_LL
    
    def func(self,wParam,lParam):
        # 获取消息
        MSLLHOOKSTRUCT_p = POINTER(MSLLHOOKSTRUCT)
        param = cast(lParam, MSLLHOOKSTRUCT_p)

        # 转换vk_code获取vkCode对应字符
        xy = (param.contents.pt.x,param.contents.pt.y)
        key = {value:key for key,value in m_code.items()}[wParam]

        # 执行鼠标按下行为
        if wParam in [WM_LBUTTONDOWN, WM_RBUTTONDOWN, WM_MBUTTONDOWN,WM_MOUSEMOVE,WM_MOUSEWHEEL]:
            msg = self.onPress(key,xy)
        # 执行鼠标松开行为
        elif wParam in [WM_LBUTTONUP, WM_RBUTTONUP, WM_MBUTTONUP]:
            msg = self.onRelease(key,xy)
        else:
            msg = False

        if self.kbInterrupt("ctrl","c"):  # 检查是否按下Ctrl+C
            msg = False
        return msg

