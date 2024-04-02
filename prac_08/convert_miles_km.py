"""
Kivy example for CP1404/CP5632, IT@JCU
This shows the use of a StringProperty object to store the "model" of MVC
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

FACTOR_MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """Kivy App for converting miles to kilometres."""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handle calculation (could be button press or other call)."""
        print("handle calculate")
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_increment(self, text, change):
        """Handle up/down button press, update the text input with new value, call calculation function."""
        print("handle increment")
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)
        # Since the InputText.text has changed, its on_text event will fire and handle_calculate will be called

    def update_result(self, miles):
        print("update")
        self.output_km = str(miles * FACTOR_MILES_TO_KM)

    @staticmethod
    def convert_to_number(text):
        """Convert text to float or 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesConverterApp().run()

# Use a StringProperty for the text on the output (km) label.
# Then in the app you can set this property variable without having to manually update the text of the label. It will automatically update.
# See the mvc_demo.py and associated kv file in the demos for an example of this.
# You should be able to type a number in the text entry field.
# Pressing the "Convert" button should calculate the conversion from miles to kilometres.
# Pressing the Up or Down buttons should make the miles number go up or down by 1.
