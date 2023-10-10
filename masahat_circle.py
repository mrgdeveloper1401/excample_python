class Circle:
    def __init__(self, r) -> None:
        self.r = r
    
    @staticmethod
    def mashaht(r):
        return r ** 2 * 3.14
    
    @staticmethod
    def mohit(r):
        return r * 3.14 * 2
    
    
c1 = 5
print(Circle.mashaht(c1))
print(round(Circle.mohit(c1), 2))
 