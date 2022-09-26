import json


class ImdbObject:
    def __init__(self):
        pass

    def to_json(self):
        return self.__dict__
