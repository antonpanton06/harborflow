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


def main():
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

        elif option == 7:
            weekly_dispatch_report()


if __name__ == "__main__":
    main()