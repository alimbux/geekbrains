class Road:
    def __init__(self, width, length):
        self.__width = width
        self.__length = length

    def get_asphalt_mass(self, thick, mass_to_meter):
        return self.__width * self.__length * thick * mass_to_meter


w = input("Enter road length(m):")
l = input("Enter road width(m):")
road = Road(int(w), int(l))
t = input("Enter road thickness(cm):")
m = input("Enter mass of 1 square meter of road with 1cm thickness(kg):")
print(f"Road asphalt mass is {road.get_asphalt_mass(int(t), int(m))} kg")
