class Car:
    def __init__(self, register_number, max_speed):
        self.register_number = register_number
        self.odometer = 2000
        self.speed = 60
        self.max_speed = max_speed


    def print_info(self):
        print(f"Auton {self.register_number} huippunopeus on {self.max_speed} km/h, "
              f"matkamittari: {self.odometer}, "
              f"tämänhetkinen nopeus: {self.speed}")

    def accelerate(self, speed_change):
        self.speed = speed_change + self.speed
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0

    def drive(self, trip_change):
        self.odometer = self.odometer + trip_change * self.speed


someCar = Car("ABC-123", 142)
someCar.drive(1.5)
someCar.print_info()