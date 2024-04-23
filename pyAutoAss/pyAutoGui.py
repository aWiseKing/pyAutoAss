import win32gui,win32api,win32con,win32ui
import cv2 as cv

class PyAutoGui:
    
    # 获取显示器在虚拟屏幕左上定位
    def getMonitorRect(self):
        display_infos = win32api.EnumDisplayMonitors(None, None)
        x = 0
        y = 0
        for info in display_infos:
            if info[2][0] < x:
                x = info[2][0]
            if info[2][1] < y:
                y = info[2][1]
        return (x,y)

    # 截屏并保存到文件
    def screenShotSaveFile(self,file_path:str="./screenshot.png"):
        """截屏
        :param file_path -- 截图保存位置

        :var hdesktop -- 虚拟桌面
        :var hd_width -- 虚拟屏幕宽度
        :var hd_height -- 虚拟屏幕高度
        :var desktop_dc -- 设备描述表
        :var img_dc -- 设备描述表
        :var mem_dc -- 创建内存描述表
        :var screentshot -- 位图对象

        :return: None
        """
        # 获取桌面
        hdesktop = win32gui.GetDesktopWindow()
        # 获取屏幕参数
        hd_width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        hd_height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        # 创建设备描述表
        desktop_dc = win32gui.GetWindowDC(hdesktop)
        img_dc = win32ui.CreateDCFromHandle(desktop_dc)
        # 创建内存设备描述表
        mem_dc = img_dc.CreateCompatibleDC()
        # 创建位图
        screenshot = win32ui.CreateBitmap()
        screenshot.CreateCompatibleBitmap(img_dc,hd_width,hd_height)
        mem_dc.SelectObject(screenshot)
        # 截图保存到内存设备描述表
        mem_dc.BitBlt((0,0),(hd_width,hd_height),img_dc,getMonitorRect(),win32con.SRCCOPY)
        # 保存位图到文件
        screenshot.SaveBitmapFile(mem_dc,file_path)
        # 释放内存
        mem_dc.DeleteDC()
        win32gui.DeleteObject(screenshot.GetHandle())
    
    # 全屏截图
    def screencut(self,screenshot_img_path="./input/pic/screenshot.png"):
        """
        全屏截图
        :param img_path: 图片路径
        :return avg: 全屏截图
        """
        self.screenShotSaveFile(screenshot_img_path)
        return screenshot_img_path

    # 用于获取图片在另一上的坐标位置
    def getXY(self,contrast_img_path, img_path:str="./input/pic/template.png"):
        """
        图片中心在屏幕坐标
        :param img_path: 图片路径
        :param contrast_img_path: 对比获取坐标的图片路径
        :return avg: 图片中心在屏幕坐标
        """
        template_img = cv.imread(img_path)
        contrast_img = cv.imread(contrast_img_path)

        # 获取图片宽高
        height, width, channel = template_img.shape

        # 使用matchTemplate进行模板匹配（标准平方差匹配）
        result = cv.matchTemplate(
            contrast_img, template_img, cv.TM_SQDIFF_NORMED)
        # 解析出匹配区域的左上角图标
        upper_left = cv.minMaxLoc(result)[2]
        # 计算出匹配区域右下角图标（左上角坐标加上模板的长宽即可得到）
        lower_right = (upper_left[0] + width, upper_left[1] + height)
        # 计算坐标的平均值并将其返回
        avg = (int((upper_left[0] + lower_right[0]) / 2),
               int((upper_left[1] + lower_right[1]) / 2),upper_left, width,height)
        return avg
    
    # 用于获取图片在屏幕上的坐标位置
    def getXYByScreencut(self,img_path:str="./input/pic/template.png", screenshot_img_path="./input/pic/screenshot.png"):
        """
        获取图片在屏幕坐标位置
        :param img_path: 图片路径
        :param screenshot_img_path: 全屏截图存储路径
        :return avg: 图片中心在屏幕坐标
        """
        contrast_img_path = self.screencut(screenshot_img_path)
        return self.getXY(contrast_img_path,img_path)

    # 用于获取列表最后一个图片在列表第一个图片的上的坐标位置
    def getXYByList(self, img_paths:list):
        """
        用于获取列表最后一个图片在列表第一个图片的上的坐标位置
        :param img_paths: 图片路径列表
        :return avg: 图片中心在屏幕坐标
        """ 
        upper = [[0,0],img_paths[0]]
        del img_paths[0]
        for img_path in img_paths:
            avg = self.getXY(contrast_img_path=upper[1],img_path=img_path)
            upper[0][0]+=avg[2][0]
            upper[0][1]+=avg[2][1]
            upper[1] = img_path
        # 计算坐标的平均值并将其返回
        avg = (int(upper[0][0] + avg[3]/2),
               int(upper[0][1] + avg[4]/ 2),avg[2],avg[3],avg[4])
        return avg

    # 用于获取列表最后一个图片在屏幕的上的坐标位置
    def getXYByListAndScreencut(self, img_paths:list,screenshot_img_path="./input/pic/screenshot.png"):
        """
        获取图片在屏幕所在坐标
        :param img_paths: 图片路径列表
        :param screenshot_img_path: 全屏截图存储路径
        :return avg: 图片中心在屏幕坐标
        """ 
        contrast_img_path = self.screencut(screenshot_img_path)
        img_paths.insert(0,contrast_img_path)
        return self.getXYByList(img_paths)

    # 自动选择通过列表或是通过值来获取图片在屏幕坐标
    def getAutoXY(self,img_path_info,screenshot_img_path="./input/pic/screenshot.png"):
        if type(img_path_info) == list:
            avg = self.getXYByListAndScreencut(img_path_info,screenshot_img_path)    
        elif type(img_path_info) == str:
            avg = self.getXYByScreencut(img_path_info, screenshot_img_path)
        else:
            avg = (0,0)
        return avg
