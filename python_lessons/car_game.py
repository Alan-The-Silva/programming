command = ""
started = False

while command.lower() != "quit":
    command = str(input(">"))

    if command.lower() == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started...Ready to Go!")

    elif command.lower() == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("car stopped.")

    elif command.lower() == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")

    elif command.lower() == "quit":
        break

    else:
        print("I don't understand that...")
