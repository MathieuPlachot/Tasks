from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from taskWidget import taskWidget
from taskWidgetCanvas import taskWidgetCanvas


class mainScreen(Screen):

    def on_pre_enter(self):
        nodesToDelete = []
        for n in self.tv.iterate_all_nodes():
            nodesToDelete.append(n)
        for n in nodesToDelete:
            self.tv.remove_node(n)
        data = self.myDBHandler.displayDBEntries("Testreport",["Name","Subsystem"])
        data.sort()
        self.tvPopulate(data, 1)

    def on_touch_up_tree(self, instance, touch):
        # print("node touch")
        node = self.tv.get_selected_node()
        if not node == None :
            if node.level > 1 :
                # print(node.text)
                reportName = node.text
                reportScreen = testReportScreen(reportName, self.myDBHandler, self.screenManager)
                self.screenManager.root.add_widget(reportScreen)
                self.screenManager.root.current = "testReportScreen"
        self.tv.deselect_node()
        return True


    def tvRefresh(self):
        tasks = self.myDBHandler.getAllTasks()
        for node in [i for i in self.tv.iterate_all_nodes()]:
            self.tv.remove_node(node)
        for item in tasks:
            self.tv.add_node(TreeViewLabel(text=str(item), font_size = self.nodeFontSize))

    def svRefresh(self):
        tasks = self.myDBHandler.getAllTasks()
        for task in tasks:
            myTaskWidget = taskWidget(task)
            self.gridLayout.add_widget(myTaskWidget)
            # self.gridLayout.add_widget(Label(text="test"))
            # myFloat = RelativeLayout()
            # myFloat.add_widget(Label(text="coucou"))
            # self.gridLayout.add_widget(myFloat)



    def addTask(self, instance):
        taskTitle = self.newTaskTextInput.text
        self.app.addTaskToDB(taskTitle)
        self.newTaskTextInput.text = ""
        self.tvRefresh()


    def __init__(self, myDBHandler):
        self.app = App.get_running_app()
        self.myDBHandler = myDBHandler
        super().__init__(name = "mainScreen")
        # self.tv = self.ids.tv
        self.newTaskTextInput = self.ids.titleInput
        self.gridLayout = self.ids.gl
        self.gridLayout.bind(minimum_height=self.gridLayout.setter('height'))
        self.svRefresh()


