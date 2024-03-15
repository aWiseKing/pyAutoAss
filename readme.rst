
---

更新
----
- 1.0.5.5
    1. 修改getXY等获取图片坐在左边方法位置到pyAutoGui模块下。
    #. 修改getXY方法逻辑。删除方法中的截屏方法，删除screenshot_img_path参数，新增contrast_img_path参数。
    #. 新增screencut方法，用于全屏截图。
    #. 新增getXYByScreencut方法，用于获取图片在屏幕上的坐标位置。
    #. 新增getXYByList方法，用于获取列表最后一个图片在列表第一个图片的上的坐标位置。
    #. 新增getXYByList方法，用于获取列表最后一个图片在屏幕的上的坐标位置。
    #. 新增getAutoXY方法，用于自动选择通过列表或是通过值来获取图片在屏幕上的坐标。 

- 1.0.6.1
    1. 修改AutoOperation类方法wait，提供等待任意键按下效果。
    #. 新增AutoOperation类属性kl,ml。实例化KeyboardListening,MouseListening对象。。
    #. 新增AutoOperation类方法listening，支持对键盘鼠标的监听。
    #. 新增MCODE工具类，用于映射鼠标事件。
    #. 新增Listening类，用于监听硬件事件。
    #. 新增KeyboardListening类，用于监听键盘事件。
    #. 新增MouseListening类，用于监听鼠标事件。
