from prac_06.programming_language import ProgrammingLanguage


def main():
    """Programming language client program"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    languages = [python, ruby, visual_basic]
    for language in languages:
        if language.is_dynamic() == True:
            # prints only dynamic typing languages
            print(language.name)
        else:
            print("")
