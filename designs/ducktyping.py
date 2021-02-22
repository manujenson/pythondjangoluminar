class swift:
    def drive(self):
        print("driving swift car")


class sonet:
    def drive(self):
        print("driving sonet car")
class person:
    def start(self,car):
        car.drive()
sw=sonet()
p=person()
p.start(sw)
