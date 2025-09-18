from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import StringProperty


class CalculatorLayout(BoxLayout):
    result_text = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 16
        self.spacing = 10

        # Monthly contribution
        self.add_widget(Label(text="Monthly Contribution:"))
        self.entry_contribution = TextInput(text="1000", multiline=False, input_filter="float")
        self.add_widget(self.entry_contribution)

        # Current age
        self.add_widget(Label(text="Current Age:"))
        self.entry_current_age = TextInput(text="30", multiline=False, input_filter="int")
        self.add_widget(self.entry_current_age)

        # Retirement age
        self.add_widget(Label(text="Retirement Age:"))
        self.entry_retirement_age = TextInput(text="60", multiline=False, input_filter="int")
        self.add_widget(self.entry_retirement_age)

        # Yearly interest
        self.add_widget(Label(text="Yearly Interest (%):"))
        self.entry_interest = TextInput(text="6.0", multiline=False, input_filter="float")
        self.add_widget(self.entry_interest)

        # Buttons row
        button_row = BoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=50)
        calc_btn = Button(text="Calculate", on_press=self.calculate_savings)
        clear_btn = Button(text="Clear", on_press=self.clear_fields)
        button_row.add_widget(calc_btn)
        button_row.add_widget(clear_btn)
        self.add_widget(button_row)

        # Result area
        self.result_label = Label(text=self.result_text, halign="left", valign="top")
        self.result_label.bind(size=self.result_label.setter("text_size"))  # wrap text
        self.add_widget(self.result_label)

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
                f"Future value:          {future_value:,.2f}\n"
                f"Total contributions:   {total_contrib:,.2f}\n"
                f"Interest earned:       {interest_earned:,.2f}"
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
