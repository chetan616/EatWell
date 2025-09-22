from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class HomeScreen(Screen):
    pass

class FarmerScreen(Screen):
    pass

class ConsumerScreen(Screen):
    pass

class EatWellApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(FarmerScreen(name='farmer'))
        sm.add_widget(ConsumerScreen(name='consumer'))
        return sm

if __name__ == '__main__':
    EatWellApp().run()