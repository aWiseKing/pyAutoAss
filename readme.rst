pyAutoAss
=========

.. contents:: 目录 / Contents
   :depth: 2

中文介绍
--------

项目介绍
~~~~~~~~
pyAutoAss 是一个基于 Python 的 GUI 自动化工具包，集成了键盘模拟、鼠标控制、图像识别定位及剪贴板管理等功能。旨在通过简单的 API 调用，帮助开发者快速构建自动化脚本，处理重复性工作，提升效率。无论是简单的点击操作，还是基于图像匹配的复杂交互，pyAutoAss 都能轻松胜任。

功能特性
~~~~~~~~
- **键盘控制**：支持按键模拟、快捷键组合（如 Ctrl+C/V）、文本输入等。
- **鼠标控制**：支持移动、点击、拖拽、滚动及坐标获取。
- **图像识别**：基于 OpenCV 的模板匹配，支持屏幕截图、图片定位、相对坐标定位。
- **事件监听**：内置键盘鼠标监听器，支持录制操作或等待特定事件。
- **剪贴板管理**：便捷的剪贴板读写操作。

安装
~~~~
.. code:: shell

   pip install pyAutoAss

使用示例
~~~~~~~~

1. 初始化
^^^^^^^^^
.. code:: python

    from pyAutoAss import AutoOperation

    # 初始化自动化对象
    ao = AutoOperation()

2. 基础键鼠操作
^^^^^^^^^^^^^^^
.. code:: python

    # 鼠标移动到坐标 (100, 200) 并点击
    ao.moveClick(100, 200)

    # 键盘输入文本
    ao.keyInput("Hello World")

    # 使用快捷键
    ao.kCopy()   # 复制 (Ctrl+C)
    ao.kPaste()  # 粘贴 (Ctrl+V)
    ao.kEnter()  # 回车
    ao.kSelecAll() # 全选 (Ctrl+A)

3. 图像识别自动化
^^^^^^^^^^^^^^^^^
.. code:: python

    # 识别屏幕上的目标图片并自动点击
    # 需要传入目标图片的路径
    ao.autoORCLeftClick("./target_icon.png")

    # 右键点击识别到的图片
    ao.autoORCRightClick("./target_icon.png")

4. 监听与等待
^^^^^^^^^^^^^
.. code:: python

    # 暂停程序，等待用户按键（默认监听 'k' 即键盘事件）
    ao.wait()

English Introduction
--------------------

Project Overview
~~~~~~~~~~~~~~~~
pyAutoAss is a comprehensive GUI automation toolkit for Python that integrates keyboard simulation, mouse control, image recognition positioning, and clipboard management. It is designed to help developers quickly build automation scripts and handle repetitive tasks with simple API calls. From simple clicks to complex interactions based on image matching, pyAutoAss handles it all with ease.

Features
~~~~~~~~
- **Keyboard Control**: Simulates key presses, shortcuts (e.g., Ctrl+C/V), and text input.
- **Mouse Control**: Supports moving, clicking, dragging, scrolling, and retrieving coordinates.
- **Image Recognition**: OpenCV-based template matching for screen capture, image positioning, and relative coordinate location.
- **Event Listening**: Built-in keyboard and mouse listeners for recording actions or waiting for events.
- **Clipboard Management**: Easy read/write access to the system clipboard.

Installation
~~~~~~~~~~~~
.. code:: shell

   pip install pyAutoAss

Usage Examples
~~~~~~~~~~~~~~

1. Initialization
^^^^^^^^^^^^^^^^^
.. code:: python

    from pyAutoAss import AutoOperation

    # Initialize the automation object
    ao = AutoOperation()

2. Basic Keyboard & Mouse
^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    # Move mouse to (100, 200) and click
    ao.moveClick(100, 200)

    # Input text
    ao.keyInput("Hello World")

    # Use shortcuts
    ao.kCopy()   # Copy (Ctrl+C)
    ao.kPaste()  # Paste (Ctrl+V)
    ao.kEnter()  # Enter
    ao.kSelecAll() # Select All (Ctrl+A)

3. Image Recognition Automation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    # Recognize target image on screen and left-click it
    # Requires the path to the target image
    ao.autoORCLeftClick("./target_icon.png")

    # Right-click the recognized image
    ao.autoORCRightClick("./target_icon.png")

4. Listening & Waiting
^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    # Pause program and wait for user input
    ao.wait()

更新日志 / Update Log
---------------------
- 1.0.6.3
    1. 修复pyAutoGui截图错误。
- 1.0.6.2
    1. 优化屏幕截图位图创建逻辑，修复当副显示器在主显示器左上时无法截取到的问题。
- 1.0.6.1
    1. 修改AutoOperation类方法wait，提供等待任意键按下效果。
    #. 新增AutoOperation类属性kl,ml。实例化KeyboardListening,MouseListening对象。。
    #. 新增AutoOperation类方法listening，支持对键盘鼠标的监听。
    #. 新增MCODE工具类，用于映射鼠标事件。
    #. 新增Listening类，用于监听硬件事件。
    #. 新增KeyboardListening类，用于监听键盘事件。
    #. 新增MouseListening类，用于监听鼠标事件。
- 1.0.5.5
    1. 修改getXY等获取图片坐在左边方法位置到pyAutoGui模块下。
    #. 修改getXY方法逻辑。删除方法中的截屏方法，删除screenshot_img_path参数，新增contrast_img_path参数。
    #. 新增screencut方法，用于全屏截图。
    #. 新增getXYByScreencut方法，用于获取图片在屏幕上的坐标位置。
    #. 新增getXYByList方法，用于获取列表最后一个图片在列表第一个图片的上的坐标位置。
    #. 新增getXYByList方法，用于获取列表最后一个图片在屏幕的上的坐标位置。
    #. 新增getAutoXY方法，用于自动选择通过列表或是通过值来获取图片在屏幕上的坐标。
