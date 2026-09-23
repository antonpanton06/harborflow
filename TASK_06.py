#Task 6: Classify service performance
#BUSINESS OUTCOME Translate operational numbers into a consistent customerservice status.
#BOUNDARY CASES Test delay values -1, 0, 1, 15 and 16, and repeat a timing case with one damaged parcel.

promised_delivery = int(input("Promised minutes: "))
delivery = int(input("Actual minutes: "))
damaged_parcels = int(input("Damaged parcels: "))
delay = delivery - promised_delivery 

def service_status(damaged_parcels,delay):
    if damaged_parcels > 0:
        return "SERVICE FAILURE"
    elif delay <= 0:
        return "ON TIME"
    elif delay <= 15:
        return "MINOR DELAY"
    else:
        return "MAJOR DELAY"

print(f"Delay: {delay} minutes")
print(f"Service status: {service_status(damaged_parcels,delay)}")
