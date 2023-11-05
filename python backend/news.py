import random

def generateNewsEvent(sources):
    # Determine if the event is bad or good
    if random.randint(0, 1) == 0:
        # Generate a good event
        # Determine how good the event is
        effect = random.uniform(0.1, 0.3)
        # Determine the duration of the event
        duration = random.randint(1, 3)
        # Generate the description based on the effect and duration
        description = ""
        if effect < 0.15:
            description += "Slightly "
        elif effect < 0.25:
            description += "Moderately "
        else:
            description += "Extremely "
        description += "good news for "
        if duration == 1:
            description += "one month!"
        elif duration == 2:
            description += "two months!"
        else:
            description += "three months!"
        # Generate description of the sources affected
        description += " "
        for source in sources:
            description += source.name + ", "
        description = description[:-2]
        description += " will be affected."
        # Generate the title based on the effect and duration
        titlePool = [
            # A pool of randomly chosen good titles
            sources[random.randint(0, len(sources)-1)].name + " is booming!",
            "The economy is booming!",
            "The economy is thriving!",
            "The economy is doing well!",
            sources[random.randint(0, len(sources)-1)].name + " is doing well!",
            "The economy is doing great!",
            "The economy is doing fantastic!",
        ]
        event = NewsEvent(titlePool[random.randint(0, len(titlePool)-1)], description, effect, sources, duration)
    else:
        # Generate a bad event
        # Determine how bad the event is
        effect = random.uniform(-0.3, -0.1)
        # Determine the duration of the event
        duration = random.randint(1, 3)
        # Generate the description based on the effect and duration
        description = ""
        if effect > -0.15:
            description += "Slightly "
        elif effect > -0.25:
            description += "Moderately "
        else:
            description += "Extremely "
        description += "bad news for "
        if duration == 1:
            description += "one month!"
        elif duration == 2:
            description += "two months!"
        else:
            description += "three months!"
        # Generate description of the sources affected
        description += " "
        for source in sources:
            description += source.name + ", "
        description = description[:-2]
        description += " will be affected."
        # Generate the title based on the effect and duration
        titlePool = [
            # A pool of randomly chosen bad titles
            sources[random.randint(0, len(sources)-1)].name + " is collapsing!",
            "The economy is collapsing!",
            "The economy is failing!",
            "The economy is doing poorly!",
            sources[random.randint(0, len(sources)-1)].name + " is doing poorly!",
            "The economy is doing terribly!",
            "The economy is doing horribly!",
        ]
        event = NewsEvent(titlePool[random.randint(0, len(titlePool)-1)], description, effect, sources, duration)
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