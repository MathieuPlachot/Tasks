from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.app import App

class taskWidget(Widget):
    pass

    def __init__(self,taskInfo):
        super().__init__()
        print("hello")
        # self.height = 10
        # self.add_widget(Label(text="this"))
        self.ids.taskWidgetLabel.text = str(taskInfo[1])        





