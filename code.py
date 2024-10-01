# Name: Jashanpreet kaur
# This program presents a menu to the user, asking if they want to set the Circuit Playground LEDs to red (1),
# green (2), or blue (3). The program continues running until the user presses 'q' to quit. 
# It handles invalid inputs using a try/except block and ensures the LEDs change color based on the user's choicefrom adafruit_circuitplayground import cp

from adafruit_circuitplayground import cp

# Define color tuples for red, green, and blue
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

while True:
    # Display the menu
    print("\nChoose a color for the LEDs:")
    print("1. Red")
    print("2. Green")
    print("3. Blue")
    print("Press 'q' to quit.")

    # Get user input
    user_input = input("Enter your choice: ").lower()

    # Check if the user wants to quit
    if user_input == 'q':
        print("Exiting the program. Turning off all LEDs.")
        for i in range(10):
            cp.pixels[i] = (0, 0, 0)  # Turn off all LEDs
        cp.pixels.show()  # Update the LEDs
        break

    # Try to cast the input to an integer and handle invalid inputs
    try:
        choice = int(user_input)

        if choice == 1:
            # Set LEDs to red
            for i in range(10):
                cp.pixels[i] = red
            cp.pixels.show()
            print("LEDs set to red.")
        elif choice == 2:
            # Set LEDs to green
            for i in range(10):
                cp.pixels[i] = green
            cp.pixels.show()
            print("LEDs set to green.")
        elif choice == 3:
            # Set LEDs to blue
            for i in range(10):
                cp.pixels[i] = blue
            cp.pixels.show()
            print("LEDs set to blue.")
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    except ValueError:
        print("Invalid input. Please enter a number (1, 2, or 3) or 'q' to quit.")

