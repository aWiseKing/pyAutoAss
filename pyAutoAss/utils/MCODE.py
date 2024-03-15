"""
映射鼠标事件
"""
from win32con import *
m_code = {
    "LMD": WM_LBUTTONDOWN, # 鼠标左键按下
    "LMU": WM_LBUTTONUP, # 鼠标左键抬起
    "RMD": WM_RBUTTONDOWN, # 鼠标右键按下
    "RMU": WM_RBUTTONUP, # 鼠标右键抬起
    "MMD":WM_MBUTTONDOWN, # 鼠标中键按下
    "MMU":WM_MBUTTONUP, # 鼠标中键抬起
    "MM":WM_MOUSEMOVE, # 鼠标移动
    "MW":WM_MOUSEWHEEL # 鼠标中键滚动
}
