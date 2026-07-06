class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        """
        Initializes Pet instance
        """
        self.name = name
        self.power = power
        self.health = health

    def output_attributes(self):
        print(f"{self.name}")
        print(f"{self.power}")
        print(f"{self.health}")
# TODO: Create Superhero instances
batman = SuperHero("Batman","Intelligence",100)
superman = SuperHero("Superman","Strength",150)
# TODO: Print out the attributes of each superhero
batman.output_attributes()
superman.output_attributes()