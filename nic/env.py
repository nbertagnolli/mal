class Env:

    def __init__(self, outer=None, binds=None, exprs=None):
        self.data = {}
        self.outer = outer
        if binds:
            for i in range(0, len(binds)):
                self.set(binds[i], exprs[i])

    def set(self, key, value):
        """Takes symbol key and adds to datastructure"""
        self.data[key] = value
        return value

    def find(self, key):
        """Takes a key and if the current environment contains that key then returns the environment
        if no key is found and outer is not none recurse until we find something."""
        if key in self.data:
            return self
        elif self.outer is None:
            return None
        else:
            return self.outer.find(key)

    def get(self, key):
        """
        Calls find and returns the value if not value is found raises error
        """
        environment = self.find(key)

        if environment:
            return environment.data[key]
        else:
            raise Exception("'" + key + "' not found")