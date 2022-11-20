class Singleton:
    class __Singleton:
        def __init__(self):
            self.val = None

        def __str__(self):
            return f"{self.val}"

    # the rest of the class definition will follow here, as per the previous logging script

    instance = None

    def __new__(cls):
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton()
        return Singleton.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)
