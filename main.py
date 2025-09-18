from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.graphics import Color, RoundedRectangle


class Card(BoxLayout):
    """A simple card-style container with rounded corners and background."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = 10
        self.size_hint_y = None
        self.height = 120
        with self.canvas.before:
            Color(0.95, 0.95, 0.95, 1)  # light gray background
            self.bg = RoundedRectangle(radius=[12])
        self.bind(pos=self.update_bg, size=self.update_bg)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size


class CalculatorLayout(BoxLayout):
    result_text = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 20
        self.spacing = 15

        # Helper to create a label + input row
        def make_row(label_text, default="", input_filter=None):
            row = BoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=50)
            label = Label(text=label_text, font_size=18, size_hint_x=0.6, halign="right", valign="middle")
            label.bind(size=label.setter("text_size"))  # align text properly
            entry = TextInput(text=default, multiline=False, input_filter=input_filter,
                              font_size=18, size_hint_x=0.4)
            row.add_widget(label)
            row.add_widget(entry)
            return row, entry

        # Fields
        row1, self.entry_contribution = make_row("Monthly Contribution:", "1000", "float")
        row2, self.entry_current_age = make_row("Current Age:", "30", "int")
        row3, self.entry_retirement_age = make_row("Retirement Age:", "60", "int")
        row4, self.entry_interest = make_row("Yearly Interest (%):", "6.0", "float")

        self.add_widget(row1)
        self.add_widget(row2)
        self.add_widget(row3)
        self.add_widget(row4)

        # Buttons row
        button_row = BoxLayout(orientation="horizontal", spacing=15, size_hint_y=None, height=60)
        calc_btn = Button(text="Calculate", font_size=18, on_press=self.calculate_savings)
        clear_btn = Button(text="Clear", font_size=18, on_press=self.clear_fields)
        button_row.add_widget(calc_btn)
        button_row.add_widget(clear_btn)
        self.add_widget(button_row)

        # Result area inside card
        self.result_card = Card(orientation="vertical")
        self.result_label = Label(text=self.result_text, halign="left", valign="top",
                                  font_size=16, color=(0, 0, 0, 1))
        self.result_label.bind(size=self.result_label.setter("text_size"))  # wrap text
        self.result_card.add_widget(self.result_label)
        self.add_widget(self.result_card)

    def calculate_savings(self, instance):
        try:
            monthly_contribution = float(self.entry_contribution.text or 0)
            current_age = int(self.entry_current_age.text or 0)
            retirement_age = int(self.entry_retirement_age.text or 0)
            yearly_interest = float(self.entry_interest.text or 0) / 100.0

            if retirement_age <= current_age:
                self.result_label.color = (1, 0, 0, 1)  # red
                self.result_label.text = "Retirement age must be greater than current age."
                return
            if monthly_contribution < 0 or yearly_interest < 0:
                self.result_label.color = (1, 0, 0, 1)
                self.result_label.text = "Please enter non-negative numbers."
                return

            years = retirement_age - current_age
            months = years * 12
            monthly_rate = yearly_interest / 12.0

            if monthly_rate != 0:
                future_value = monthly_contribution * ((1 + monthly_rate) ** months - 1) / monthly_rate
            else:
                future_value = monthly_contribution * months

            total_contrib = monthly_contribution * months
            interest_earned = future_value - total_contrib

            self.result_label.color = (0, 0, 0.5, 1)  # dark blue
            self.result_label.text = (
                f"Future value:        {future_value:,.2f}\n"
                f"Total contributions: {total_contrib:,.2f}\n"
                f"Interest earned:     {interest_earned:,.2f}"
            )
        except ValueError:
            self.result_label.color = (1, 0, 0, 1)
            self.result_label.text = "Please enter valid numbers."

    def clear_fields(self, instance):
        self.entry_contribution.text = ""
        self.entry_current_age.text = ""
        self.entry_retirement_age.text = ""
        self.entry_interest.text = ""
        self.result_label.text = ""


class CompoundingApp(App):
    def build(self):
        return CalculatorLayout()


if __name__ == "__main__":
    CompoundingApp().run()
