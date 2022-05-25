class airplane():
    def __init__(self, airplane_ID):
        self.airplane_ID = airplane_ID
        self.plane = ["EasyJet", "Ryanair", "British Airways"]

    def add_plane(self, plane):
        self.plane.append(plane)