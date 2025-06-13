from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.factory import Factory
from kivy.animation import Animation
from kivy.clock import Clock

# 确保版本
kivy_version = "2.1.0"


# 主页面类
class MainWidget(FloatLayout, MDApp):
    def __init__(self):
        super().__init__()
        # 联系人数量计数器
        self.number_of_contcat = 0
        # 判断联系人是否为零
        if self.number_of_contcat == 0:
            self.empty_contact()
       

    # 空联系人显示页面
    def empty_contact(self):
        global Label1
        # 无联系人文本
        Label1 = Label(
            text="None contcat",
            font_size="14sp",
            color=(0, 0, 0, 1),
            # 加粗
            bold=True,
            halign="center",
            valign="middle",
            # font_name="/Users/jean/Desktop/python/CommunicationApplication/Font/Body.otf",
            size=(100, 100),
            pos_hint={"center_x": 0.483, "center_y": 0.52},
            text_size=self.size,
        )
        # 添加进入布局
        self.add_widget(Label1)

    # 点击添加按钮后操作
    def click_the_Add_button(self):
        global examples_add_account
        """
        点击加号按钮添加联系人功能
        """

        self.remove_widget(Label1)

        # 实例化AddAccount控件
        examples_add_account = Factory.AddAccount()
        # 添加
        self.add_widget(examples_add_account)
        # 允许运行一次
        self.ids.add_button.disabled = True

        # 重新发送验证码文本后续实现

    # 邮件验证
    def email_verify(self, code):
        if code == "zyh0192837465@outlook.com":
            print("OK,Please log in")
        else:
            print("密码错误")

    # 验证码验证
    def code_verify(self, code):
        if code == "147369":
            # 删除输入框
            self.remove_widget(examples_add_account)
            # 动画
            am = Animation(opacity=1, duration=2)
            # 添加成功提示
            correct_text = Label(
                text="Add Account Success!",
                size=(100, 100),
                pos_hint={"center_x": 0.483, "center_y": 0.52},
                font_size="14sp",
                color=(0, 0, 0, 1),
                # 加粗
                bold=True,
                halign="center",
                valign="middle",
                # 透明度
                opacity=0,
            )

            # 添加进入布局
            self.add_widget(correct_text)
            # 运行动画
            am.start(correct_text)

        else:
            # 动画
            start_am = Animation(opacity=1, duration=1)
            # 添加成功提示
            mistake_text = Label(
                text="Code mistake",
                size=(100, 100),
                pos_hint={"center_x": 0.483, "center_y": 0.66},
                font_size="14sp",
                color=(0, 0, 0, 1),
                # 加粗
                bold=True,
                halign="center",
                valign="middle",
                # 透明度
                opacity=0,
            )

            # 添加进入布局
            self.add_widget(mistake_text)
            # 运行动画
            start_am.start(mistake_text)

            # 消失动画
            def remove_correct_text(*args):
                def callbacks(dt):
                    if mistake_text.opacity > 0:
                        mistake_text.opacity -= 0.1  # 实时修改透明度
                    else:
                        mistake_text.opacity = 0
                        # 删除控件
                        self.remove_widget(mistake_text)
                        return False

                # 每隔 1/70 秒调用一次
                Clock.schedule_interval(callbacks, 1 / 70)

            start_am.bind(on_complete=remove_correct_text)
    # 发送验证码
    def sent_code(self):
        pass
