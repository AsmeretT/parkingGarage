class ParkingGarage():
    def __init__(self, numberOfSpaces):
        self.tickets =[]
        self.parkingSpaces = []
        self.currentTicket = {'paid': False}
        for x in range(numberOfSpaces):
            self.tickets.append('Ticket')
            self.parkingSpaces.append('Space')

    def takeTicket(self, tickets, parkingSpaces):
        pass

    def payForParking(self, currentTicket):
        pass

    def leaveGarage(self, tickets, parkingSpaces, currentTicket):
        pass

    def run(self):
        while True:
            answer = input("What would you like to do? (Park, Pay, Leave, or Quit): ")
            if answer.lower() == 'park':
                self.takeTicket(self.tickets, self.parkingSpaces)
            elif answer.lower() == 'pay':
                self.payForParking(self.currentTicket)
            elif answer.lower() == 'leave':
                self.leaveGarage(self.tickets, self.parkingSpaces, self.currentTicket)
            elif answer.lower() == 'quit':
                break
            else:
                print("Invalid input, please enter 'Park', 'Pay', 'Leave', or 'Quit'.")

myGarage = ParkingGarage(10)
myGarage.run()

# print(myGarage.tickets)
# print(myGarage.parkingSpaces)
