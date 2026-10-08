def read_weekly_deliveries():
    """Ask until exactly seven non-negative integers are entered."""
    while True:
        parts = input("Completed deliveries: ").split(",")
        valid = len(parts) == 7
        deliveries = []

        if valid:
            for part in parts:
                part = part.strip()
                if part.isdigit():
                    deliveries.append(int(part))
                else:
                    valid = False

        if valid:
            return deliveries
        print("Error - Weekly report requires 7 delivery counts.")


def read_target():
    """Ask until a non-negative integer target is entered."""
    while True:
        text = input("Daily target: ").strip()
        if text.isdigit():
            return int(text)
        print("Error - Value must be greater than zero.")


def calculate_weekly_stats(deliveries, target):
    """Return total, highest_day, lowest_day, days_meeting_target."""
    total = 0
    highest_day = 0
    lowest_day = 0
    days_meeting_target = 0

    for i in range(len(deliveries)):
        total = total + deliveries[i]

        if deliveries[i] >= target:
            days_meeting_target = days_meeting_target + 1

        if deliveries[i] >= deliveries[highest_day]:
            highest_day = i

        if deliveries[i] <= deliveries[lowest_day]:
            lowest_day = i

    return total, highest_day, lowest_day, days_meeting_target


def print_weekly_report(deliveries, stats):
    """Print the report from already calculated values."""
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]
    total, highest_day, lowest_day, days_meeting_target = stats

    print("Weekly dispatch report")
    print(f"Total deliveries: {total}")
    print(f"Average per day: {total / 7:.2f}")
    print(f"Highest day: {weekdays[highest_day]} ({deliveries[highest_day]})")
    print(f"Lowest day: {weekdays[lowest_day]} ({deliveries[lowest_day]})")
    print(f"Days meeting target: {days_meeting_target}")


def weekly_dispatch_service():
    """Task 7 entry point called from the menu."""
    deliveries = read_weekly_deliveries()
    target = read_target()
    stats = calculate_weekly_stats(deliveries, target)
    print_weekly_report(deliveries, stats)


def print_menu():
    print("HARBORFLOW DISPATCH CONSOLE")
    print("1. Close console")
    print("2. Validate booking reference")
    print("3. Calculate delivery quote")
    print("4. Consolidate parcel labels")
    print("5. Check van capacity")
    print("6. Classify service performance")
    print("7. Produce weekly dispatch report")
    print("8. Compare service scenarios")


def read_menu_option():
    """Ask until an integer from 1 to 8 is entered."""
    while True:
        text = input("Select service: ").strip()
        if text.isdigit():
            option = int(text)
            if 1 <= option <= 8:
                return option
        print("Error - Select a service from 1 to 8.")


def main():
    running = True

    while running:
        print_menu()
        option = read_menu_option()

        if option == 1:
            print("Console closed. Dispatch data remains safe.")
            running = False

        elif option == 7:
            weekly_dispatch_service()

        # elif option == 2, 3, 4, 5, 6, 8: добавят владельцы этих задач


if __name__ == "__main__":
    main()