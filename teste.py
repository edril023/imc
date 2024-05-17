from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

# Set initial window size and prevent resizing
Window.size = (400, 550)
Window.clearcolor = (0.87, 0.63, 0.87)

class WhiteSquare(Widget):
    pass

class PlannerApp(App):
    def build(self):
        layout = FloatLayout()

        white_square = WhiteSquare(size_hint=(None, None), size=(350, 300))
        white_square.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        layout.add_widget(white_square)

        # FloatLayout to hold TextInput fields inside WhiteSquare
        input_layout = FloatLayout(size_hint=(None, None), size=(350, 300))

        # Create TextInput fields
        self.altura_input = TextInput(hint_text="email ou nome de usuario", font_size=16, multiline=False, size_hint=(None, None), size=(300, 40))
        self.altura_input.pos_hint = {'center_x': 0.7, 'center_y': 1.3}
        
        self.peso_input = TextInput(hint_text="senha", font_size=16, multiline=False, password=True, size_hint=(None, None), size=(300, 40))
        self.peso_input.pos_hint = {'center_x': 0.7, 'center_y': 1}

        # Add TextInput fields to the layout
        input_layout.add_widget(self.altura_input)
        input_layout.add_widget(self.peso_input)

        # Add input_layout to white_square
        white_square.add_widget(input_layout)

        return layout

if __name__ == '__main__':
    PlannerApp().run()

