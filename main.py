from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, RoundedRectangle


class RoundedBox(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1, 1)  # white background
            self.rect = RoundedRectangle(radius=[15], pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class RoundedTextInput(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = 5
        self.orientation = "vertical"
        self.rounded = RoundedBox()
        self.add_widget(self.rounded)
        self.textinput = TextInput(
            multiline=False,
            background_color=(0, 0, 0, 0),  # transparent background
            foreground_color=(0, 0, 0, 1),
            size_hint=(1, 1)
        )
        self.add_widget(self.textinput)


class RoundedButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_down = ''
        self.background_color = (0.2, 0.6, 0.9, 1)  # blue button
        self.color = (1, 1, 1, 1)  # white text
        self.font_size = 18
        self.bind(size=self.update_canvas, pos=self.update_canvas)

    def update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.background_color)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[15])


class CompoundingCalculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 20
        self.spacing = 15

        # Title
        self.add_widget(Label(text="Compounding Calculator",
                              font_size=24,
                              bold=True,
                              size_hint=(1, None),
                              height=40))

        # Fields
        self.monthly = self.add_field("Monthly Contribution:")
        self.current_age = self.add_field("Current Age:")
        self.retirement_age = self.add_field("Retirement Age:")
        self.interest = self.add_field("Yearly Interest (%):")

        # Buttons
        btn_layout = BoxLayout(size_hint=(1, None), height=50, spacing=20)
        btn_layout.add_widget(RoundedButton(text="Calculate"))
        btn_layout.add_widget(RoundedButton(text="Clear"))
        self.add_widget(btn_layout)

        # Output area
        self.output = Label(text="Future value:\nTotal contributions:\nInterest earned:",
                            halign="left",
                            valign="top",
                            size_hint=(1, None),
                            height=120)
        with self.output.canvas.before:
            Color(1, 1, 1, 1)
            self.bg = RoundedRectangle(radius=[15], pos=self.output.pos, size=self.output.size)
        self.output.bind(pos=self.update_output, size=self.update_output)
        self.add_widget(self.output)

    def add_field(self, label_text):
        self.add_widget(Label(text=label_text,
                              font_size=16,
                              bold=True,
                              size_hint=(1, None),
                              height=30,
                              halign="left"))
        field = RoundedTextInput(size_hint=(1, None), height=50)
        self.add_widget(field)
        return field

    def update_output(self, *args):
        self.bg.pos = self.output.pos
        self.bg.size = self.output.size


class CompoundingApp(App):
    def build(self):
        return CompoundingCalculator()


if __name__ == "__main__":
    CompoundingApp().run()
