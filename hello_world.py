from kivy.app import App
from kivy.uix.button import Button

class myApp(App):
    def build(self):
    	return Button(text = 'hello world')

if __name__ ==  '__main__':
    myApp().run()
