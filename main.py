from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle
import math

KV = """
BoxLayout:
    orientation: "vertical"
    padding: dp(20)
    spacing: dp(15)

    # Title
    Label:
        text: "Compounding Calculator"
        font_size: "22sp"
        size_hint_y: None
        height: dp(40)
        bold: True

    # Input fields
    RoundedInput:
        id: principal
        hint_text: "Principal Amount"

    RoundedInput:
        id: rate
        hint_text: "Rate (%)"

    RoundedInput:
        id: years
        hint_text: "Years"

    RoundedInput:
        id: compounds
        hint_text: "Compounds per Year"

    # Calculate button
    RoundedButton:
        text: "Calculate"
        size_hint_y: None
        height: dp(50)
        on_press: app.calculate(principal.text, rate.text, years.text, compounds.text)

    # Output display
    RoundedLabel:
        id: result
        text: "Result will appear here"
"""

# 🔹 Custom Widgets with Rounded Corners
class RoundedInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.height = dp(45)
        self.font_size = "16sp"
        self.background_normal = ""
        self.background_active = ""
        self.background_color = (0, 0, 0, 0)
        self.padding = [dp(12), dp(12), dp(12), dp(12)]
        with self.canvas.before:
            Color(0.95, 0.95, 0.95, 1)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[10])
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class RoundedButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ""
        self.background_down = ""
        self.background_color = (0, 0, 0, 0)
        self.color = (1, 1, 1, 1)
        self.font_size = "16sp"
        with self.canvas.before:
            Color(0.2, 0.6, 1, 1)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[12])
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class RoundedLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.height = dp(60)
        self.color = (0, 0, 0, 1)
        self.valign = "middle"
        self.halign = "center"
        self.bind(size=self.setter("text_size"))
        with self.canvas.before:
            Color(0.9, 0.9, 0.95, 1)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[10])
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


# 🔹 Main App
class CompoundApp(App):
    def build(self):
        return Builder.load_string(KV)

    def calculate(self, p, r, t, n):
        try:
            P = float(p)
            R = float(r) / 100.0
            T = float(t)
            N = float(n)

            A = P * math.pow((1 + R / N), N * T)
            result_text = f"Final Amount: {A:,.2f}"
        except Exception:
            result_text = "⚠️ Please enter valid numbers"

        self.root.ids.result.text = result_text


if __name__ == "__main__":
    CompoundApp().run()
