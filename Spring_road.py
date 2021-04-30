from models.Building import Building
from models.Country import Country
from models import Purpose


class Spring_road(Building):
    def __init__(self, name: str = "",
                 price: int = 0,
                 country: Country = Country,
                 year: int = 0,
                 capasity: int = 0,
                 purpose: Purpose = Purpose,
                 size_in_sq_m: int = 0,
                 height_in_m: float = 0,
                 steepness_in_degrees: int = 0):
        super().__init__()
        self.name = name
        self.price = price
        self.country = country
        self.year = year
        self.capasity = capasity
        self.purpose = purpose
        self.size_in_sq_m = size_in_sq_m
        self.height_in_m = height_in_m
        self.steepness_in_degrees = steepness_in_degrees

    def __str__(self):
        return f"name: {self.name} \n" \
               f"price : {self.price} \n" \
               f"country : {self.country} \n" \
               f"capasity: {self.capasity} \n" \
               f"purpose: {self.purpose} \n" \
               f"size_in_sq_m: {self.size_in_sq_m} \n" \
               f"height_in_m: {self.height_in_m} \n" \
               f"steepness_in_degrees: {self.steepness_in_degrees} \n"
