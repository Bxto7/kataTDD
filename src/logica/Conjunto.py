class Conjunto:
    def __init__(self, conjunto):
        self.__conjunto = conjunto

    def promedio(self):
        if not self.__conjunto:  # Si la lista está vacía
            return None
        elif len(self.__conjunto) == 1:
            return self.__conjunto[0]
        else:
            return sum(self.__conjunto) / len(self.__conjunto)