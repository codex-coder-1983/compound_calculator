from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, RoundedRectangle
import math

KV = """
BoxLayout:
    orientation: "vertical"
    padding: dp(20)
    spacing: dp(15)

    # Top section with blue background
    BoxLayout:
        size_hint_y: None
        height: dp(70)
        padding: dp(10)
        canvas.before:
            Color:
                rgba: 0.2, 0.4, 0.8, 1              # blue background
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            text: "Retirement Savings Calculator"
            font_size: "22sp"
            bold: True
            color: (1, 1, 1, 1)                     # white text
            halign: "center"
            valign: "middle"
            text_size: self.size

    LabeledInput:
        id: contribution
        label_text: "Monthly Contribution"

    LabeledInput:
        id: age_now
        label_text: "Current Age"

    LabeledInput:
        id: age_retire
        label_text: "Retirement Age"

    LabeledInput:
        id: rate
        label_text: "Yearly Interest (%)"

    RoundedButton:
        text: "Calculate"
        size_hint_y: None
        height: dp(50)
        on_press: app.calculate(contribution.text, age_now.text, age_retire.text, rate.text)

    RoundedLabel:
        id: result
        text: "Result will appear here"
"""

# 🔹 Custom Widgets
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
        self.height = dp(120)   # increased height
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

    def calculate(self, contrib, age_now, age_retire, rate):
        try:
            PMT = float(contrib)              # monthly contribution
            age_now = int(age_now)
            age_retire = int(age_retire)
            R = float(rate) / 100.0           # annual interest in decimal

            years = age_retire - age_now
            if years <= 0:
                self.root.ids.result.text = "⚠️ Retirement age must be greater than current age"
                return

            n = 12  # compounding monthly
            FV = PMT * (((1 + R/n)**(n*years) - 1) / (R/n))

            total_contributions = PMT * n * years
            interest_earned = FV - total_contributions

            result_text = (f"Total Contributions: {total_contributions:,.2f}\\n"
                           f"Interest Earned: {interest_earned:,.2f}\\n"
                           f"Final Amount: {FV:,.2f}")
        except Exception:
            result_text = "⚠️ Please enter valid numbers"

        self.root.ids.result.text = result_text

class LabeledInput(BoxLayout):
    def __init__(self, label_text="", **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint_y = None
        self.height = dp(70)
        self.padding = [dp(8), dp(4), dp(8), dp(4)]
        self.spacing = dp(2)

        # Rounded background
        with self.canvas.before:
            Color(0.95, 0.95, 0.95, 1)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[10])
        self.bind(pos=self.update_rect, size=self.update_rect)

        # Label (small, always visible)
        self.label = Label(
            text=label_text,
            font_size="12sp",
            size_hint_y=None,
            height=dp(16),
            halign="left",
            valign="middle",
            color=(0.3, 0.3, 0.3, 1)
        )
        self.label.bind(size=self.label.setter("text_size"))

        # Input field
        self.input = TextInput(
            multiline=False,
            size_hint_y=1,
            font_size="16sp",
            background_normal="",
            background_active="",
            background_color=(0, 0, 0, 0),
            padding=[dp(4), dp(4), dp(4), dp(4)]
        )

        self.add_widget(self.label)
        self.add_widget(self.input)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        

if __name__ == "__main__":
    CompoundApp().run()
