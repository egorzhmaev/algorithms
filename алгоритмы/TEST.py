class JSON(dict):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, args, kwargs)

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]


some_dict = {
    1: 'a',
    2: 'b',
    3: 'c'
}

test = JSON(some_dict)

print(test[1,2])