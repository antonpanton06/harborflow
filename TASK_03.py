def calculate_quote(distance, weight, service_code):
    multipliers = {"S": 1.00,
                   "X": 1.25,
                   "P": 1.60}
    multiplier = multipliers[service_code]
    subtotal = 45 + distance * 6.50 + weight * 4.00
    quote = subtotal * multiplier
    return quote
distance = float(input("Distance (km):"))
weight = float(input("Total parcel weight (kg): "))
service_code = input("Service code (S for Standard), (X for Express) or (P for priority): ")
quote = calculate_quote(distance, weight, service_code)
print(f"Delivery quote: {quote:.2f} SEK")          