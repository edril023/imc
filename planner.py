from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window

def resize_window(*args):
    Window.size = (400, 550)

Window.clearcolor = (0.87, 0.63, 0.87)

class WhiteSquare(Widget):
    pass

class Planner(App):
    def build(self):
        # Layout principal
        layout = FloatLayout()

        # Quadrado branco centralizado na janela
        white_square = WhiteSquare(size_hint=(None, None), size=(200, 200))
        white_square.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        # Adicionando o quadrado branco ao layout principal
        layout.add_widget(white_square)

        return layout
    
if __name__ == '__main__':
    Window.size = (400, 550)
    Window.bind(on_resize=resize_window)
    Planner().run()
