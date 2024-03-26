class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, pointer_arithmetic, year):
        """Initialise languages"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.pointer_arithmetic = pointer_arithmetic
        self.year = year

    def __str__(self):
        """Output to string"""
        return f"{self.name}, {self.typing}, {self.reflection},{self.pointer_arithmetic}, {self.year}"

    def is_dynamic(self):
        """Check if typing is dynamic"""
        return self.typing == "Dynamic"


def test():
    """Testing"""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, False, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, False, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, False, 1991)
    java = ProgrammingLanguage('Java', 'Static', False, False, 1995)
    # print(python)
    languages = [python, ruby, visual_basic, java]
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    test()
