class Car:
    def __init__(self, top_speed, current_speed):
        self._top_speed = top_speed
        self.current_speed = current_speed

    def set_accelerate(self, value):
        if self.current_speed > self._top_speed - value:
            self.current_speed == self._top_speed
            print(f"Current speed - {self.current_speed}mph - cannot exceed {self._top_speed}mph")
        else:
            self.current_speed += value

    def set_decrease_current_speed(self, value):
        if self.current_speed < value:
            print("Your car doesn't have a reverse gear")
            self.current_speed == 0
        else:
            self.current_speed -= value


ford = Car(100, 0)

ford.set_accelerate(40)
ford.set_accelerate(40)
ford.set_accelerate(10)
ford.set_accelerate(30)
ford.set_accelerate(10)
print(ford.current_speed)
