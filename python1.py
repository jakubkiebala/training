class Shape:
    def __init__(self, x, y, color):
        self.color = color
        self.center = (x, y)
        self.description = ''

    
    def describe(self, description):
        self.description = description

    def __str__(self):
        return f'Shape with color {self.color} o środku w punktach {self.center}'
    