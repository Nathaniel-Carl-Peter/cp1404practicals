"""
CP1404 - Prac-5 - Hex Colour
Date: 02/03/2024
Author: Nathaniel Carl Peter
"""

# Use a constant dictionary of about 10 colour names
# write a program that allows a user to enter a name and get the code
# , e.g., entering AliceBlue (or aliceblue - make it case-independent) should show #f0f8ff.

"""
Pseudo:

COLOURS = {"Absolute Zero":	"#0048ba", 
            Acid Green: #b0bf1a,
            AliceBlue:#f0f8ff,
            Alizarin crimson:#e32636,
            Amaranth:#e52b50,
            Amber:#ffbf00,
            Amethyst:#9966cc,
            Purple:#a020f0,
            Cadet Grey:#91a3b0,
            MintCream:#f5fffa}
get colour name
while colour name not = ""
    get colour name
display colour name and hex code
"""

COLOUR_CODES = {"Absolute Zero": "#0048ba",
           "Acid Green": "#b0bf1a",
           "AliceBlue": "#f0f8ff",
           "Alizarin crimson": "#e32636",
           "Amaranth": "#e52b50",
           "Amber": "#ffbf00",
           "Amethyst": "#9966cc",
           "Purple": "#a020f0",
           "Cadet Grey": "#91a3b0",
           "MintCream": "#f5fffa"}
colour_name = input("Enter colour name: ").title()
while colour_name != "":
    if colour_name in COLOUR_CODES:
        print(f"{colour_name}: {COLOUR_CODES[colour_name]}")
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")
