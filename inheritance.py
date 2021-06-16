class Film:
    def __init__(self, name):
        self.name = name

    def watch(self, player):
        print("Bon visionnage !")


class FilmCassette(Film):
    """Un film en cassette !"""

    def __init__(self, name):
        """Initialise le nom et la bande magnetique."""
        super().__init__(name)
        self.magnetic_tape = True

    def rewind(self):
        """Rembobine le film."""
        print("C'est long à rembobiner !")
        self.magnetic_tape = True

    def watch(self, player):
        """Regarde le film."""
        if player.type != "cassette":
            print(
                "Le lecteur n'est pas un lecteur de cassettes ! ",
                "Vous en trouverez peut être un dans le grenier..?"
            )
        else:
            print("Ca commence ! Allumez votre TV cathodique. :)")
        super().watch(player)

    def __str__(self):
        return "La cassette {} est rembobinée ? {}".format(self.name, self.magnetic_tape)


class Player:
    """Un lecteur."""

    def __init__(self, type):
        """Possède un type."""
        self.type = type


film = Film("2001: l'odyssée de l'espace")
film_cassette = FilmCassette("Blade Runner")

player = Player("DVD")
film_cassette.watch(player)