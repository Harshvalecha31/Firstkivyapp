import kivy
from kivy.uix.label import Label
from kivy.app import App

class Hello(App):
    def build(self):
        return Label(text='Hello world!!')
    
Hello().run()