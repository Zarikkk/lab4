from models.Building import Building
from models.Country import Country
from models import Purpose


class Rink(Building):
    def __init__(self, name: str = "",
                 price: int = 0,
                 country: Country = Country,
                 year: int = 0,
                 capasity: int = 0,
                 purpose: Purpose = Purpose,
                 size_in_sq_m: int = 0,
                 open_air: bool = True,
                 material: str = ""):
        super().__init__()
        self.name = name
        self.price = price
        self.country = country
        self.year = year
        self.capasity = capasity
        self.purpose = purpose
        self.size_in_sq_m = size_in_sq_m
        self.material = material
        self.open_air = open_air

    def __str__(self):
        return f"name: {self.name} \n" \
               f"price : {self.price} \n" \
               f"country : {self.country} \n" \
               f"capasity: {self.capasity} \n" \
               f"purpose: {self.purpose} \n" \
               f"size_in_sq_m: {self.size_in_sq_m} \n" \
               f"material: {self.material} \n" \
               f"open_air: {self.open_air} \n"
