import setuptools
with open("README.rst", "r",encoding="utf-8") as f:
  long_description = f.read()
setuptools.setup(
    name='pyautoass',
    version='1.0.6.2',
    description='基于键鼠、图片定位的自动化gui工作套件。',
    author='awise',
    long_description=long_description,
    packages=["pyAutoAss","pyAutoAss.utils","pyAutoAss.dependent"],
    install_requires=['pyautogui','opencv-python',"pywin32"],
    # 指定项目依赖的 Python 版本。
    python_requires='>=3',
    # 是否使用静态文件，为true时静态文件生效，否则不起作用
    include_package_data=True,
    zip_safe=True,
   )