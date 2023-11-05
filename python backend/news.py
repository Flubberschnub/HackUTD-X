import random

def generateNewsEvent(sources):
    event = NewsEvent("Test", "A thing happened!", -0.1, sources, random.randint(1, 3))
    return event

class NewsEvent:
    def __init__(self, title, description, effect, sources, duration):
        self.title = title
        self.description = description
        self.effect = effect
        self.sources = sources
        self.duration = duration
        self.age = 0
        self.over = False

    def update(self):
        self.age += 1
        if self.age >= self.duration:
            self.over = True