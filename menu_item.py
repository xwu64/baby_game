class MenuItem():
    def __init__(self, type, name) -> None:
        self.type = type
        self.name = name
    def __str__(self) -> str:
        return self.name