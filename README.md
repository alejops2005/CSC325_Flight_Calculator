# Flight Time Calculator

Flight Time Calculator is a Python program that calculates a drone's estimated flight time based on payload weight. It can also generate a table of sampled payload weights and their corresponding flight times.

## Features

- Calculates flight time based on payload weight
- Prevents negative payload values
- Prevents calculated flight time from going below zero
- Generates a table of payload weights and corresponding flight times
- Includes automated tests using `pytest`

## AI-Use Disclosure

- Used GitHub Copilot inline suggestions to help build the `flight_time_table()` function. Rejected an incorrect suggestion that carried over a typo from my original code. I corrected the variable name from `step_gram` to `step_grams`, reviewed the revised suggestion, and accepted the corrected function body. Verified the function correctly calls `calculate_flight_time()` and tested its output with multiple payload values using temporary `print()` statements that were later deleted.

- Used GitHub Copilot to generate the initial `pytest` tests for `calculate_flight_time()`. Reviewed the generated tests to confirm they covered zero weight, normal weight, heavy weight, and negative weight. Verified all 4 tests pass with `py -m pytest`.

- Used ChatGPT to help reason through the condition that prevents calculated flight time from going below zero and to explain why the calculation function should return a numeric value instead of printing a message such as `"Too heavy, can't fly."` Verified the final function returns `0` when appropriate and manually tested the expected outputs.