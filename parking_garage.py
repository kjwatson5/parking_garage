class parking_garage():
    def __init__(self, parking_spaces, tickets, currentTicket = {
        'paid' : False
        }):
        self.parking_spaces = parking_spaces
        self.tickets = tickets
        self.currentTicket = currentTicket

    def takeTicket(self):
        self.parking_spaces - 1
        self.tickets -1

    def payForParking(self):
        price = input("How much would you like to pay towards your ticket? Enter only number of dollars. Example: '5' = $5: ")
        if not price:
            print('You must pay before you leave.')
        else:
            print('Your ticket has been paid. You have 15 minutes to leave.')
            self.currentTicket['paid'] = True

    def leaveGarage(self):
        if self.currentTicket['paid'] == True:
            print("Thank you, have a nice day")
        else:
            pay_now = input("Your ticket is $5. Do you accept these charges? Enter 'yes' or 'no'")
            if pay_now.lower() == 'yes':
                print('Thank you, have a nice day')
                self.parking_spaces + 1
                self.tickets + 1
            elif pay_now.lower() == 'no':
                print('You must pay your ticket before leaving.')


my_garage = parking_garage(15, 15)

def run():
    while True:
        prompt = input("Would you like to enter/leave or neither?")
        if prompt.lower() == 'enter':
            my_garage.payForParking()
            my_garage.takeTicket()
        elif prompt == 'leave':
            my_garage.leaveGarage()
        elif prompt == 'neither':
            print('Have a nice day!')
            break
        else:
            print('Try entering something else.')

run()
