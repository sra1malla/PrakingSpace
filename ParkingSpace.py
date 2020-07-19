import pandas as pd
import argparse

class VehicleType:                                      ## to make our code handle parking for multiple vehicles
    def __init__(self,reg_no,colour):
        self.colour =  colour
        self.reg_no = reg_no

class Car(VehicleType):                                 ## currently sticked to CAR

    def __init__(self,reg_no,colour):
        VehicleType.__init__(self,reg_no,colour)

    def getType(self):
        return "Car"
    
class ParkingSpace:
    def __init__(self):
        self.slts = 0
        self.slot_id = 0
        self.SlotsOccupied = 0

    def createParking(self,slts):                       ## Create parking Lot with given slots
        try:
            self.slots = [-1] * slts
            self.slts = slts
            print('Parking lot with '+str(self.slts)+' slots is created')
        except Exception as ex:
            print("An exception occurred ", ex)
        return self.slts
            
    def getNextAvailableSlot(self):                     ## Get Empty slots to fill in Greedy Approch
        try:
            for i in range(len(self.slots)):
                if self.slots[i] == -1:
                    return i
        except Exception as ex:
            print("An exception occurred ", ex)
    
    def checkRegNoExistence(self,reg_no):               ## Check if reg_no already exists
        try:
            reg_nos = []
            for i in self.slots:
                if i == -1:
                    continue
                else:
                    reg_nos.append(i.reg_no)
            if reg_no in reg_nos:
                return True
            else:
                return False
        except Exception as ex:
            print("An exception occurred ", ex)
            

    def parkCar(self,reg_no,colour):                    ## Park the car with give reg_no and color
        try:
            if self.SlotsOccupied < self.slts:
                exists = self.checkRegNoExistence(reg_no)
                if exists:
                    print('Registration Number already exists, Please re-check')
                    return -2
                else:
                    slot_id = self.getNextAvailableSlot()
                    self.slots[slot_id] = Car(reg_no,colour)
                    self.slot_id = self.slot_id+1
                    self.SlotsOccupied = self.SlotsOccupied + 1
                    print('Allocated slot number: '+str(slot_id+1))
                    return slot_id+1
            else:
                print("Sorry, parking lot is full")
                return -1
        except Exception as ex:
            print("An exception occurred ", ex)

    def leaveSlot(self,slot_id):                        ## Leave the slot/un-park the car from give slot id
        try:
            if self.SlotsOccupied > 0 and self.slots[slot_id-1] != -1:
                self.slots[slot_id-1] = -1
                self.SlotsOccupied = self.SlotsOccupied - 1
                print('Vehicle Left from Slot number '+str(slot_id))
                return True
            else:
                print('No Vehicle found at Slot number '+str(slot_id))
                return False
        except Exception as ex:
            print("An exception occurred ", ex)

    def getStatus(self):                                ## get status of slots filled currently
        try:
            columns = ["Slot No.", "Registration No.", "Colour"]
            slt_no = []; reg_no = []; colours = []
            for i in range(len(self.slots)):
                if self.slots[i] != -1:
                    slt_no.append(i+1)
                    reg_no.append(self.slots[i].reg_no)
                    colours.append(self.slots[i].colour)
                else:
                    continue
            vehicle_df = pd.DataFrame(list(zip(slt_no, reg_no, colours)), columns=columns)
            print(vehicle_df)
            return vehicle_df
        except Exception as ex:
            print("An exception Occured ", ex)

    def getRegNoFromcolour(self,colour):                ## get Registration Number from give color
        try:
            reg_nos = []
            for i in self.slots:
                if i == -1:
                    continue
                if i.colour == colour:
                    reg_nos.append(i.reg_no)
            if len(reg_nos) > 0:
                print('Registration Numbers belonging to colour '+ str(colour) + ' are ' + ', '.join(reg_nos))
                return reg_nos
            else:
                print('colour Not found')
                return -1
        except Exception as ex:
            print("An exception Occured ", ex)
            
            
    def getSlotNoFromRegNo(self,reg_no):                ## Get Slot ID from give registration number
        try:
            for i in range(len(self.slots)):
                slt = 0
                if (self.slots[i] != -1):
                    if (self.slots[i].reg_no) == reg_no:
                        slt += 1
                        break
            if slt > 0:
                print('Car with Registration Number '+ str(reg_no) + ' is in slot ' + str(i+1))
                return i+1
            else:
                print('Registration Number Not Found')
                return -1
        except Exception as ex:
            print("An exception Occured ", ex)
            
def main():
    parkingspace = ParkingSpace()
    parkingspace.createParking(5)
    parkingspace.getNextAvailableSlot()
    parkingspace.parkCar("OR-07-AB-6677", "White")
    parkingspace.parkCar("OR-07-AB-6666", "Blue")
    parkingspace.parkCar("OR-07-AB-6666", "Blue")
    parkingspace.parkCar("AP-07-AB-7689", "Red")
    parkingspace.parkCar("TS-07-AB-4365", "Red")
    parkingspace.parkCar("AP-07-AB-1299", "Black")
    parkingspace.leaveSlot(4)
    parkingspace.leaveSlot(2)
    parkingspace.getStatus()
    parkingspace.getRegNoFromcolour("Red")
    parkingspace.getRegNoFromcolour("Green")
    parkingspace.getSlotNoFromRegNo("OR-07-AB-6677")
    parkingspace.getSlotNoFromRegNo("AP-07-AB-7687")
    
if __name__ == '__main__':
    main()