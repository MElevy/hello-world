from kivy.app import App
from kivy.uix.button import Button # import modules

class MyApp(App):
    '''A basic app'''
    def build(self):
        '''Returns a button'''
    	return Button(text = 'Hello, World')

if __name__ ==  '__main__':
    MyApp().run() # runs app
