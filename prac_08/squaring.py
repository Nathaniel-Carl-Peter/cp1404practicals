"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lindsay Ward'


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (800, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass


SquareNumberApp().run()

# Change the output Label text colour to pink (color is an RGBA tuple).
# Change the orientation so the widgets display left-to-right instead of top-to-bottom.
# Add a label at the bottom with the text: Enter a number and press "Square".
# To do this you will need to use nested layouts.
# There are two 'sections', made with BoxLayout, arranged vertically:
# In the top section (BoxLayout), there are three widgets, arranged horizontally.
# In the bottom section, there is just one label.
# A good way to think about organising BoxLayouts is to draw boxes to represent them. You can have multiple widgets and/or BoxLayouts arranged within a BoxLayout.