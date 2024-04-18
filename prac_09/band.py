"""Cp1404 Band class"""


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
            musician_info = "\n".join(f"{muscian.name}: {muscian.play()}" for muscian in self.musicians)
            return f"{self.name} musicians:\n{musician_info}"

    def __str__(self):
        """Output as string representation for band"""
        return f'{self.name} ({len(self.musicians)} musicians)'
