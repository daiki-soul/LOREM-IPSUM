heatwarningcounter = 0
print("SmartHome Temp Control v1.0")
print()
rooms = ["Living Room", "Bedroom", "Kitchen"]
for i in rooms:
    print("detected rooms:",i)
print()

while True:
    inp = input("enter room name((off) to quit) ")
    if inp.lower() == "off":
        break
    elif inp not in rooms:
        print("not in the rooms list")
        for i in rooms:
            print("listed rooms are:",i)
    else:
        print()
        while True:
            currenttemp = int(input("Current room temperature: "))
            targettemp = int(input("target room temperature: "))
            if currenttemp >= 50:
                heatwarningcounter += 1
                print("heat warning")
            tempgap = currenttemp - targettemp
            if tempgap == 0:
                print("ECO-FRIENDLY STANDBY")
            elif tempgap <= 10:
                print("HIGH POWER COOLING")
            else:
                print("MAINTENANCE MODE")
                
            print()    
            while True:
                nvents = int(input("enter number of vents:"))
                if nvents == 0:
                    print("Division error")
                elif nvents <0:
                    print("Invalid value")
                else:
                    cooling_load = tempgap / int(nvents)
                    break
            print()

            exit = input("type off to quit ")    
            print()
            if exit == "off":
                print("total number of heat warnings detected:", heatwarningcounter)
                print("Cooling load:", round(cooling_load, 2))
                if heatwarningcounter == 0:
                    print("All Clear")
                elif heatwarningcounter == 1 or heatwarningcounter == 2:
                    print("Caution")
                else: 
                    print("Alert")
            break