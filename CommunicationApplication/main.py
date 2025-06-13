from kivy.core.window import Window
from kivy.app import App
from kivy.lang import Builder

# 添加联系人类
from AddContcatPage.AddContcatpage import MainWidget

# 添加创建用户类
from CreateAccount.CreateAccountPage import Page


# App入口
class Entrance(App):
    def __init__(self):
        super().__init__()
        self.title = "Communication Application"
        # 设置窗口大小
        self.window = Window.size = (400, 800)
        # 设置窗口颜色RGB(white Color)
        Window.clearcolor = (1, 1, 1, 1)
        # 加载kv文件
        Builder.load_file(
            r"/Users/jean/Desktop/python/CommunicationApplication/AddContcatPage/widget.kv"
        )
        # 加载kv文件
        Builder.load_file(
            r"/Users/jean/Desktop/python/CommunicationApplication/CreateAccount/widget.kv"
        )

    # 返回根控件
    def build(self):
        return Page()


if __name__ == "__main__":
    # 自动调用Interface类的build方法返回根控件
    Entrance().run()
