from Media import Media


class Game(Media):
    # TODO
    # change *args to explicitly stated arguments or kwargs
    def __init__(self, *args):
        super().__init__(*args[:-2])
        platform, has_multiplayer = args[-2:]
        self.platform = platform
        self.has_multiplayer = has_multiplayer

    @property
    def platforms(self):
        return self.platforms

    @platform.setter
    def platform(self, new_platform: str):
        if not isinstance(new_platform, str):
            raise TypeError("Platforms must be a list of strings.")
        self._platform = new_platform

    @property
    def has_multiplayer(self):
        return self.has_multiplayer

    @has_multiplayer.setter
    def has_multiplayer(self, new_has_multiplayer: bool):
        if not isinstance(new_has_multiplayer, bool):
            raise TypeError("Has_multiplayer must be of boolean type.")
        self._has_multiplayer = new_has_multiplayer