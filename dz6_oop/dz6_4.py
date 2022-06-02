class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.speed_driving = 0
        self.is_police = is_police

    def go(self):
        print(f"{self.name} started the ride")
        self.speed_driving = self.speed

    def stop(self):
        print(f"{self.name} stopped the ride")
        self.speed_driving = 0

    def turn(self, direction):
        if direction in ("left", "right"):
            print(f"{self.name} turned to {direction}")
        else:
            print(f"Wrong direction")

    def show_speed(self):
        if self.speed_driving > 0:
            print(f"{self.name} is driving with speed {self.speed_driving} km/h")
        if self.speed_driving <= 0:
            print(f"{self.name} is stopped")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed_driving > 60:
            print(f"{self.name} has exceed speed limit")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"{self.name} has exceed speed limit")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


ferrari = SportCar(150, "Red", "Ferrari")
ferrari.go()
ferrari.show_speed()
ferrari.turn("left")
ferrari.stop()
hyundai = TownCar(80, "Grey", "Hyundai")
hyundai.show_speed()
hyundai.go()
hyundai.show_speed()
print(f"{hyundai.name} is {'' if hyundai.is_police else 'not'} police")
man = WorkCar(30, "Blue", "MAN")
man.go()
man.turn("right")
man.show_speed()
police = PoliceCar("100", "Black and whit", "Ford")
print(f"{police.name} is {'' if police.is_police else 'not '}police")