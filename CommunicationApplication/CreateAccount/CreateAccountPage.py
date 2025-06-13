from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.factory import Factory
from kivy.uix.screenmanager import ScreenManager, Screen,SlideTransition


# 创建用户类
class Page(RelativeLayout, MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # # 创建屏幕管理器
        # self.sr = ScreenManager(current='create_account_page',# 屏幕名称
        #                         transition=SlideTransition(),  # 切换动画一个屏幕划出，一个屏幕划入
        #                         duration=0.8,  # 切换动画持续时间
        #                         direction='down',  # 切换方向
        #                         )
        # # 当前实例添加进入屏幕管理器
        # self.self.sr.add_widget(self)

    # 添加账户操作
    def add_account_action(self):
        # 判断是否存在
        if "create_account_card" in self.ids and "login_account_card" in self.ids:
            # 隐藏按钮
            self.ids.login_button.opacity = 0
            self.ids.create_account_button.opacity = 0
            # 隐藏卡片
            self.ids.create_account_card.opacity = 0
            self.ids.login_account_card.opacity = 0

        else:
            pass
        
