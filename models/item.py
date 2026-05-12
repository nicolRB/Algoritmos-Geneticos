class Item:
    def __init__(self, name, weight, score):
        self.name = name
        self.weight = weight
        self.score = score

    def __repr__(self):
        return f"{self.name} (Peso={self.weight}, Pontos={self.score})"