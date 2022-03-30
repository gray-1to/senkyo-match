class Option:
    def __init__(self, name, short_name, description, default):
        self.name = name
        self.short_name = short_name
        self.description = description
        self.default = default

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name