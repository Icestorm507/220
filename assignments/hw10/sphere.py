class Sphere:
    def __init__(self, radius):
        self.radius = radius

    # to get the radius
    def get_radius(self):
        return self.radius

    # to get the surface area
    def surface_area(self):
        return 4 * (22 / 7) * self.radius * self.radius

    # to get the volume volume
    def volume(self):
        return (4 / 3) * (22 / 7) * self.radius * self.radius * self.radius
