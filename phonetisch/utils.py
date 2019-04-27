class Pipeline():

    def __init__(self, steps):
        self.__steps = steps

    def execute(self, data):
        clipboard = data
        for step in self.__steps:
            clipboard = step(clipboard)
        return clipboard
