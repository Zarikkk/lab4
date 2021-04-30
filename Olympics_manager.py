class Olympics_manager:
    def __init__(self, buildings):
        self.building = buildings


    def search_by_capasity(self):
        out = list()
        for capasity in self.building:
            if 100 <= capasity.capasity <= 1000:
                out.append(capasity)
        self.building = out
        return out

    def sort_by_name(self):
        self.building.sort(key=lambda x: x.name)
        out = self.building
        return out


