from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class SavingsCalculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=10, **kwargs)

        # Inputs
        self.contribution = TextInput(hint_text="Monthly Contribution", multiline=False)
        self.current_age = TextInput(hint_text="Current Age", multiline=False)
        self.retirement_age = TextInput(hint_text="Retirement Age", multiline=False)
        self.interest = TextInput(hint_text="Yearly Interest (%)", multiline=False)

        # Add inputs to layout
        for field in [self.contribution, self.current_age, self.retirement_age, self.interest]:
            self.add_widget(field)

        # Button
        calc_button = Button(text="Calculate", size_hint=(1, None), height=50)
        calc_button.bind(on_press=self.calculate_savings)
        self.add_widget(calc_button)

        # Result label
        self.result_label = Label(text="", halign="left", valign="middle")
        self.add_widget(self.result_label)

    def calculate_savings(self, instance):
        try:
            monthly_contribution = float(self.contribution.text)
            current_age = int(self.current_age.text)
            retirement_age = int(self.retirement_age.text)
            yearly_interest = float(self.interest.text) / 100.0

            if retirement_age <= current_age:
                self.result_label.text = "Retirement age must be greater than current age."
                return
            if monthly_contribution < 0 or yearly_interest < 0:
                self.result_label.text = "Please enter non-negative numbers."
                return

            years = retirement_age - current_age
            months = years * 12
            monthly_rate = yearly_interest / 12.0

            if monthly_rate != 0:
                future_value = monthly_contribution * ((1 + monthly_rate)**months - 1) / monthly_rate
            else:
                future_value = monthly_contribution * months

            total_contrib = monthly_contribution * months
            interest_earned = future_value - total_contrib

            self.result_label.text = (
                f"Future value: {future_value:,.2f}\n"
                f"Total contributions: {total_contrib:,.2f}\n"
                f"Interest earned: {interest_earned:,.2f}"
            )
        except ValueError:
            self.result_label.text = "Please enter valid numbers."


class SavingsApp(App):
    def build(self):
        return SavingsCalculator()


if __name__ == "__main__":
    SavingsApp().run()
