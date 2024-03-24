class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialise languages"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Output to string"""
        return f"{self.name}, {self.typing}, {self.reflection}, {self.year}"

    def is_dynamic(self):
        """Check if typing is dynamic"""
        return self.typing == "Dynamic"


def test():
    """Testing"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    # print(python)
    languages = [python, ruby, visual_basic]
    # Using comprehensions
    # dynamic_language = [language for language in languages if language.is_dynamic() == True]
    # print(dynamic_language)
    # No comprehensions
    for language in languages:
        if language.is_dynamic():
            print(language.name)


test()
