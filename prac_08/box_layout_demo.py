from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def input_name(self):
        """Handle input name"""
        self.message = self.root.ids.user_input.text

    def handle_greet(self):
        # self.root.ids.output_label.text = "Hello "
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear_all(self):
        """Clear all widgets that are children of the "entries_box" layout widget."""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
