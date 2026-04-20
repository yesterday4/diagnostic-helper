class Symptom:
    def __init__(self, id, description, categories):
        self.id = id
        self.description = description
        self.categories = categories

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("id must be an integer")
        self._id = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError("description must be a string")
        self._description = value

    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, value):
        if not isinstance(value, list):
            raise TypeError("categories must be a list")
        self._categories = value