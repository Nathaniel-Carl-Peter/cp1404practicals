class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialise programing languages"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Output the string"""
        return f"{self.name}, {self.typing}, Reflection: {self.reflection}, {self.year}"

    def is_dynamic(self):
        """Check if typing is dynamic"""
        return self.typing == "Dynamic"


def test():
    """Programming languages testing"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    languages = [python, ruby, visual_basic]
    for language in languages:
        if language.is_dynamic() == True:
            print(language.name)
        else:
            print("")


test()
