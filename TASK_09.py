def compare_services(distance, weight):
    standard = calculate_quote(distance, weight, "S")
    express = calculate_quote(distance, weight, "X")
    priority = calculate_quote(distance, weight, "P")
    print("Service comparison")
    print(f"Standard: {standard:.2f} SEK")
    print(f"Express: {express:.2f} SEK")
    print(f"Priority: {priority:.2f} SEK")
    services = {
    "Standard": standard,
    "Express": express,
    "Priority": priority
}
    cheapest = min(services, key=services.get)
    most_expensive = max(services, key=services.get)

    print(f"Cheapest service: {cheapest}")
    print(f"Most expensive service: {most_expensive}")

    
