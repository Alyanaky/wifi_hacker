from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from ui.main_screen import MainScreen

class WiFiHackerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == '__main__':
    WiFiHackerApp().run()
