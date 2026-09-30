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

        elif option == 3:
            distance = float(input("Distance (km):"))
            weight = float(input("Total parcel weight (kg): "))
            service_code = input("Service code (S for Standard), (X for Express) or (P for priority): ")
            calculate_quote(distance, weight, service_code)

        elif option == 4:
            scanned_labels = (input("Scanned labels:"))
            ConsolidateParcelLabels(scanned_labels)

        elif option == 7:
            deliveries_input = input("Completed deliveries: ")
            target = int(input("Daily target: "))
            weekly_dispatch_report(deliveries_input, target)


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
    
#Option 3,
def calculate_quote(distance, weight, service_code):

    multipliers = {"S": 1.00,
                   "X": 1.25,
                   "P": 1.60}
    
    multiplier = multipliers[service_code]
    subtotal = 45 + distance * 6.50 + weight * 4.00
    quote = subtotal * multiplier


    print(f"Delivery quote: {quote:.2f} SEK")     
#Option 4,
def ConsolidateParcelLabels(scanned_labels):
    labels = scanned_labels.split(",")
    unique_labels =[]
    #User Input could be: gb-104, GB-220, gb-104, se-011, GB-220
    print(f"Scanned labels: {scanned_labels}")

    for label in labels:
        label = label.strip().upper()

        if label not in unique_labels:
            unique_labels.append(label)

    print("Unique load list:")
    #Create a loop for printing all unique labels.
    for i in range(len(unique_labels)):
        print(f"{i + 1}. {unique_labels[i]}")
    print(f"Total unique parcels: {len(unique_labels)}")


#Option 5,

#Option 6,

#Option 7,
def weekly_dispatch_report(deliveries_input, target):
    
    delivery_values = deliveries_input.split(",")

    deliveries = []

    for value in delivery_values:
        deliveries.append(int(value.strip()))


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

#Option 8, 