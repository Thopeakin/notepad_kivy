from kivy.app import App
import os.path
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class Frame(BoxLayout):
    theText = 'Notepad'

    def save(self, *args):
        getter = self.ids['text']
        save = self.ids['save']
        filename = save.text
        DataList = getter.text
        if os.path.isfile(filename):
            Clock.schedule_once(self.exist, 0.111111111)
            Clock.schedule_once(self.clear, 1)

        elif len(filename) == 0:
            Clock.schedule_once(self.none, 0.111111111)
            Clock.schedule_once(self.clear, 1)

        else:
            try:
                saveFile = open(filename, 'w')
                saveFile.write(DataList)
                saveFile.close()
                Clock.schedule_once(self.success, 0.111111111)
                Clock.schedule_once(self.clear, 1)
            except:
                Clock.schedule_once(self.name, 0.11111111111)
                Clock.schedule_once(self.clear, 1)
    def exist(self, *args):
        error = self.ids['error']
        error.color = 1, 0, 0, 1
        error.text = 'A file with that name exists'

    def none(self, *args):
        error = self.ids['error']
        error.color = 1, 0, 0, 1
        error.text = 'Filename must a character or more'

    def name(self, *args):
        error = self.ids['error']
        error.color = 1, 0, 0, 1
        error.text = 'Invalid file name'

    def success(self, *args):
        error = self.ids['error']
        error.color = 0, 1, 0, 1
        error.text = 'File successfully submitted'

    def clear(self, *args):
        error = self.ids['error']
        error.text = ''

Builder.load_file('notepad.kv')

class Notepad(App):
    def build(self):
        return Frame()

if __name__ == '__main__':
    Notepad().run()
