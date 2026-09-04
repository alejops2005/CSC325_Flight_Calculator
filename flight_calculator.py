def calculate_flight_time(weight_grams):
    if weight_grams < 0:
        raise ValueError("Negative weight is not allowed.")

    flight_time_minutes = 180 - (weight_grams * 0.1)

    if flight_time_minutes < 0:
        return 0

    return flight_time_minutes
