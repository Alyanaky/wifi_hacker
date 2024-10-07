from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from core.scanner import scan_networks
from core.auto_connect import auto_connect

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.scan_button = Button(text='Scan and Connect', on_release=self.scan_and_connect)
        self.result_label = Label(text='')
        layout.add_widget(self.scan_button)
        layout.add_widget(self.result_label)
        self.add_widget(layout)

    def scan_and_connect(self, instance):
        networks = scan_networks()
        if networks:
            result = auto_connect(networks)
            self.result_label.text = f"Auto Connect Result: {result}"
        else:
            self.result_label.text = "No networks found"
