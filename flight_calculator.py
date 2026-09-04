def calculate_flight_time(weight_grams):
    if weight_grams < 0:
        raise ValueError("Weight cannot be negative")

    flight_time_minutes = 180 - (weight_grams * 0.1)

    if flight_time_minutes < 0:
        return 0

    return flight_time_minutes


def flight_time_table(max_weight_grams, step_grams):
    if max_weight_grams < 0 or step_grams <= 0:
        # Rejected Copilot's initial suggestion because it carried over
        # a spelling mistake from my original code. I corrected the variable,
        # reviewed the updated suggestion, and accepted the corrected version.
        raise ValueError(
            "Maximum weight can't be negative and step needs to be a positive number"
        )

    table = []

    for weight in range(0, max_weight_grams + 1, step_grams):
        flight_time = calculate_flight_time(weight)
        table.append((weight, flight_time))
    return table
