class Task:
    def __init__(self, id, title, description=None, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else " "
        desc = f" ({self.description})" if self.description else ""
        return f"[{status}] {self.id}: {self.title}{desc}"
