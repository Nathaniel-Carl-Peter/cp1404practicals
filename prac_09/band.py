from muscian import Musician
from guitar import Guitar


class Band:
    def __init__(self, name):
        """Initialize a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string indicating which instruments each musician is playing."""
        if not self.musicians:
            return f"{self.name} has no musicians."
        else:
            musician_info = "\n".join(f"{m.name}: {m.play()}" for m in self.musicians)
            return f"{self.name} musicians:\n{musician_info}"
