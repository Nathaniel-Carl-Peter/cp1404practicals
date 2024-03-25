class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=False, pointer_arithmatic=False, year=0):
        """Initialise languages"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.pointer_arithmatic = pointer_arithmatic
        self.year = year

    def __str__(self):
        """Output to string"""
        return f"{self.name}, {self.typing}, {self.reflection},{self.pointer_arithmatic}, {self.year}"

    def is_dynamic(self):
        """Check if typing is dynamic"""
        return self.typing == "Dynamic"

    def pointer_arithmatic_yes(self):
        """Check if PA == yes"""
        return self.pointer_arithmatic == "Yes"


def test():
    """Testing"""
    python = ProgrammingLanguage("Python", "Dynamic", True, False, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, False, 1991)
    java = ProgrammingLanguage('Java', 'Static', False, False, 1995)
    # print(python)
    languages = [python, ruby, visual_basic, java]
    # Using comprehensions
    # dynamic_language = [language for language in languages if language.is_dynamic() == True]
    # print(dynamic_language)
    # No comprehensions
    for language in languages:
        if language.pointer_arithmatic():
            print(language.name)


test()
