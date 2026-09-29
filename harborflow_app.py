"""HarborFlow Assignment 1 starter file.

Replace the TODO sections with your team's implementation. Keep the program
entry point so the file can be run with: python harborflow_app.py
"""


def main():
    """Run the HarborFlow Dispatch Console."""
    running = True

    while running:
        print("HARBORFLOW DISPATCH CONSOLE")
        print("1. Close console")
        print("2. Validate booking reference")
        print("3. Calculate delivery quote")
        print("4. Consolidate parcel labels")
        print("5. Check van capacity")
        print("6. Classify service performance")
        print("7. Produce weekly dispatch report")

        option = int(input("Select service: "))

        if option == 1:
            print("Console closed. Dispatch data remains safe.")
            running = False

        elif option == 2:
            oldRef = input("Reference: ")
            validate_reference(oldRef)

        elif option == 7:
            weekly_dispatch_report()


#Option 2, 
def validate_reference(reference):
    
    oldRef = reference      # copy of old reference
    reference = reference.upper().strip().replace(" ", "")
    
    # Literally checking everything (i think), and if someting is wrong make reference an empty string
    # Maybe should make a if-block to print what is wrong with reference (only if needed or i feel like it)
    if reference[0:3] != "HFL" or reference[3] != "-" or reference[7] != "-" or reference[4:7].isalpha() == False or reference[9:12].isdigit() == False:
        reference = ""

    if len(reference) != 0:                         # If string isnt empty by this point it is valid
        print(f"Valid reference: {reference}")      #
    else:                                           # If ir is empty it is invalid
        print(f"Invalid reference: {oldRef}")       #
    return reference

if __name__ == "__main__":
    TestReference = "    hfl-no r-2048 "
    

#Option 7,
def weekly_dispatch_report():
    deliveries_input = input("Completed deliveries: ")
    delivery_values = deliveries_input.split(",")

    deliveries = []

    for value in delivery_values:
        deliveries.append(int(value.strip()))

    target = int(input("Daily target: "))

    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    total = 0
    highest = deliveries[0]
    lowest = deliveries[0]
    highest_day = 0
    lowest_day = 0
    days_meeting_target = 0

    for i in range(7):
        total = total + deliveries[i]

        if deliveries[i] >= target:
            days_meeting_target = days_meeting_target + 1

        if deliveries[i] >= highest:
            highest = deliveries[i]
            highest_day = i

        if deliveries[i] <= lowest:
            lowest = deliveries[i]
            lowest_day = i

    average = total / 7

    print("Weekly dispatch report")
    print(f"Total deliveries: {total}")
    print(f"Average per day: {average:.2f}")
    print(f"Highest day: {weekdays[highest_day]} ({highest})")
    print(f"Lowest day: {weekdays[lowest_day]} ({lowest})")
    print(f"Days meeting target: {days_meeting_target}")

if __name__ == "__main__":
    main()
