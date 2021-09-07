class ParkingSlot:
    def __init__(self):
        self.slots = 3
        self.booked = 0
        self.parking_data = [0 for i in range(self.slots)]

    def park(self):
        if self.booked < self.slots:
            idx = self.parking_data.index(0)
            self.parking_data[idx] = 1
            print(idx)
            print(f"vehical is parked at {idx}")
            self.booked += 1
        else:
            print("parking not available")

    def unpark(self):
        idx = self.parking_data.index(1)
        self.parking_data[idx] = 0
        print(idx)
        print(f"vehical is out at {idx}")
        self.booked -= 1


x = ParkingSlot()
while True:
    cmd = input("enter a command: ")

    if (cmd == "park"):
        x.park()

    elif (cmd == "unpark"):
        x.unpark()

    else:
        print("enter a valid command! ")
