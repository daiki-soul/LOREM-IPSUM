current_temp = 0
target_temp = 0

rooms = ["Livingroom", "Bedroom", "Kitchen"]

print("Available rooms:")
print("Living room, Bedroom, Kitchen")

input("Enter room: ")

print(f"Your room is: {rooms}")


print("SmartHome Temp Control v1.0")
print("=" * 50)


print("\nAvailable Rooms:")
for i, room in enumerate(available_rooms, start=1):
    print("  {}. {}".format(i, room))  # Ch1: {} formatting

print("\nType 'off' at the room prompt to shut down.")



