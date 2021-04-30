from models import *
from manager import *


def main():

    rink = Rink(purpose=Purpose.ICESCATING, name="Ice arena", price=200000, country=Country.BRAZIL, year=1999,
                size_in_sq_m=3000, capasity=200, material="plastic", open_air=True)

    stadium = Stadium(purpose=Purpose.FOOTBALL, name="Ali arena", price=350000, country=Country.CHINA, year=2020,
                      size_in_sq_m=7000, capasity=999, real_grass=True, open_air=True)

    spring_road = Spring_road(purpose=Purpose.SKIING, name="Springer", price=1200000, country=Country.ENGLAND,
                              year=2007, size_in_sq_m=23000, capasity=500, height_in_m=25.5, steepness_in_degrees=60)
    item = [rink, stadium, spring_road]
    object_manager = Olympics_manager(item)

    def sort_by_name_main():
        out = object_manager.sort_by_name()
        for i in out:
            print(i)

    def search_by_capasity_main():
        out = object_manager.search_by_capasity()
        for i in out:
            print(i)

    search_by_capasity_main()

    print("---------------------------------")

    sort_by_name_main()


if __name__ == '__main__':
    main()
