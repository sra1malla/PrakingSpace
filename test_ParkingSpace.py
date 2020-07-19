import unittest
from ParkingSpace import ParkingSpace
class TestParkingSpace(unittest.TestCase):

    def test_create_parking_lot_1(self):                      ## Testcase to check creation of parking slot +ve case
        parkingspace = ParkingSpace()
        res = parkingspace.createParking(4)
        self.assertEqual(4,res)
    
    def test_create_parking_lot_2(self):                      ## Testcase to check creation of parking slot -ve case
        parkingspace = ParkingSpace()
        res = parkingspace.createParking("a")
        self.assertEqual(0,res)

    def test_park_1(self):                                    ## Testcase to park a vehicle with reg_no and color
        parkingspace = ParkingSpace()
        res = parkingspace.createParking(4)
        res = parkingspace.parkCar("TS-07-AB-4365","White")
        self.assertNotEqual(-1,res)
    
    def test_park_2(self):                             
               ## Testcase to check if duplicate registration number
        parkingspace = ParkingSpace()
        res = parkingspace.createParking(4)
        res = parkingspace.parkCar("TS-07-AB-4365","White")
        res = parkingspace.parkCar("TS-07-AB-4365","White")
        self.assertEqual(-2,res)

    def test_leaveSlot_1(self):                               ## Testcase to check leave slot which is occupied (+ve case)
        parkingspace = ParkingSpace()
        res = parkingspace.createParking(4)
        res = parkingspace.parkCar("TS-07-AB-4365","White")
        res = parkingspace.leaveSlot(1)
        self.assertEqual(True,res)
    
    def test_leaveSlot_2(self):                               ## Testcase to check leave slot which is already free (-ve case)
        parkingspace = ParkingSpace()
        res = parkingspace.createParking(4)
        res = parkingspace.parkCar("TS-07-AB-4365","White")
        res = parkingspace.leaveSlot(2)
        self.assertEqual(False,res)

    def test_getRegNoFromcolour_1(self):                      ## Testcase to check get reg_no from color (+ve case)
        parkingspace = ParkingSpace()
        res = parkingspace.createParking(4)
        res = parkingspace.parkCar("TS-07-AB-4365","White")
        res = parkingspace.parkCar("OR-07-AB-6767","White")
        res = parkingspace.getRegNoFromcolour("White")
        self.assertIn("TS-07-AB-4365",res)
        self.assertIn("OR-07-AB-6767",res)
        
    def test_getRegNoFromcolour_2(self):                      ## Testcase to check get reg_no from color which is not available (-ve case)
        parkingspace = ParkingSpace()
        res = parkingspace.createParking(4)
        res = parkingspace.parkCar("TS-07-AB-4365","Red")
        res = parkingspace.getRegNoFromcolour("White")
        self.assertEqual(-1,res)

    def test_getSlotNoFromRegNo_1(self):                      ## Testcase to check get slot from reg_no (+ve case)
        parkingspace = ParkingSpace()
        res = parkingspace.createParking(4)
        res = parkingspace.parkCar("TS-07-AB-4365","White")
        res = parkingspace.parkCar("OR-07-AB-6767","White")
        res = parkingspace.getSlotNoFromRegNo("OR-07-AB-6767")
        self.assertEqual(2,res)
    
    def test_getSlotNoFromRegNo_2(self):                      ## Testcase to check get slot from invalid reg_no (-ve case)
        parkingspace = ParkingSpace()
        res = parkingspace.createParking(4)
        res = parkingspace.parkCar("TS-07-AB-4365","White")
        res = parkingspace.getSlotNoFromRegNo("TS-07-AB-4366")
        self.assertEqual(-1,res)


if __name__ == '__main__':
	#unittest.main()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)