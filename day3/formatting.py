class location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self): #represent
        return f"location(latitude={self.latitude}, logitude={self.longitude})"

    def __str__(self): #string
        return f"({self.latitude}, {self.longitude}"


bham_academy = location(52.488647, -1887249)
print(bham_academy)
# string takes priority

n = 0.004837
print(f"fixed point: {n:f}")
print(f"exponential notation: {n:e}")