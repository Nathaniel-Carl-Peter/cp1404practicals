FILENAME = 'projects.txt'


class Projects:
    def __init__(self, name="", start_date=0, priority=0, cost=0.0, completion=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        """Output as str"""
        return f"{self.name}, {self.start_date}, {self.priority}, {self.cost}, {self.completion}"
