available_rooms = ["Living room", "Bedroom", "Kitchen"]

heat_warning_count = 0



print("SmartHome Temp Control v1.0")

print("Room detected: Living Room")
print("Room detected: Bedroom")
print("Room detected: Kitchen")

#MAIN LOPO
while True:
    real_input = input("Enter room to check (or 'off' to exit): ")
    room = real_input.strip()

    if room == "off":
        break
    try:
        if room not in available_rooms:
            raise ValueError("'{}' is not recognized. Please try again..".format(room))
    except ValueError as e:
        print("  Room Error:", e)
        print("  Available rooms:", ", ".join(available_rooms))
        continue
#temp
    try:
        current_temp = int(input("  Enter current room temperature (°C): "))
        target_temp  = int(input("  Enter target temperature (°C): "))

    except ValueError:
        print(f"Input error: could not convert string to float: 'Warm'")
        print("Please try again using numerical values.")
        continue

    temp_gap = current_temp - target_temp


    if current_temp > 50:
        print("!!HEAT WARNING!! Current temp %.1f°C exceeds safe limit (50°C)!" % current_temp)  # Ch1: %
        heat_warning_count += 1  # Ch3: counter increment

#systtem action logic

        (temp_gap, current_temp, target_temp)

    if temp_gap > 10:
        action = "ACTION: HIGH POWER COOLING"
    elif 1 <= temp_gap <= 10:
        action = "ACTION: MAINTENANCE MODE"
    else:
        action = "ACTION: ECO-FRIENDLY STANDBY"

    print("  {}".format(action))

 #vents
    while True:
        try:
            vents_input = input("\n  Enter number of AC vents in {}: ".format(room))
            num_vents   = int(vents_input)

            if num_vents == 0:
                raise ZeroDivisionError("Error: Cannot calculate load for zero vents. Restarting check...")


            if num_vents < 0:
                raise ValueError("Number of vents cannot be negative!")


            cooling_load = round(temp_gap / num_vents, 2)

            print("\n  Vents          : {}".format(num_vents))
            print("  Cooling Load   : {:.2f}°C per vent".format(cooling_load))  # Ch1: {}
            break

        except ZeroDivisionError as e:
            print("  ZeroDivisionError:", e, "— Please enter at least 1 vent.")

        except ValueError:
            print("  Error: Number of vents must be a whole number. Try again.")

    print()

#ENDING
print("\n" + "=" * 50)
shutdown_message = "system shutting down. goodbye, homeowner!"
print("  " + shutdown_message)
print("=" * 50)
print("  Session Summary:")
print("  Total Heat Warnings Detected : %d" % heat_warning_count)

#rating
if heat_warning_count == 0:
    rating = "All Clear — No heat issues detected."
elif heat_warning_count <= 2:
    rating = "Caution — A few heat warnings were triggered."
else:
    rating = "Alert — Multiple heat warnings! Check your home insulation."

print("  Session Health Rating        : {}".format(rating))
print("=" * 50)
