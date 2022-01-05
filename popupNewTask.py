from kivy.uix.popup import Popup
from kivy.app import App

class popupNewTask(Popup):

    def addButton(self, instance):
        app = App.get_running_app()
        taskTitle = self.ids.titleInput.text
        app.addTaskToDB()

    def cancelButton(self, instance):
        print("cancel")






