def metric_to_metric(val, metric_from, metric_to):
    """converts metric inputs and returns metric answer"""
    conversions = {"mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000}
    return val * (conversions[metric_from] / conversions[metric_to])


def metric_to_meter(val, metric_value):
    """converts metric inputs into meter standard"""
    conversions = {"mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000}
    new_meter = val * conversions[metric_value] / conversions["m"]
    return new_meter


def meter_to_imperial(meter, imperial_to):
    """converts meter input into imperial equivalent"""
    meter_conversions = {"in": 39.3701, "ft": 3.28084, "yd": 1.09361, "mi": 0.000621371}
    return meter * meter_conversions[imperial_to]


def metric_to_imperial(val, metric_from, imperial_to):
    """takes metric_from value and converts it to meter to call imperial equivalent function"""
    meter_equivalent = metric_to_meter(val, metric_from)
    # takes meter value and returns imperial equivalent
    meter_converted = meter_to_imperial(meter_equivalent, imperial_to)
    return meter_converted


def imperial_to_metric(val, imperial_from, metric_to):
    """takes imperial value, converts it to meter, then to proper metric measurement"""
    conversions = {"mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000}
    meter_conversions = {"in": 39.3701, "ft": 3.28084, "yd": 1.09361, "mi": 0.000621371}
    meter_equivalent = val / meter_conversions[imperial_from]
    metric_value = meter_equivalent * conversions["m"] / conversions[metric_to]
    return metric_value


def select_unit(metric_or_imperial, to_or_from):
    """takes units and 'to' or 'from' to display appropriate text"""
    metric_units = ["mm", "cm", "m", "km"]
    imperial_units = ["in", "ft", "yd", "mi"]
    # Metric Units
    if metric_or_imperial == "metric":
        # makes sure unit is correct
        while True:
            unit = input(
                f"\nWhat unit are you converting {to_or_from}?\nChoices are: 'mm' 'cm' 'm' or 'km': "
            ).lower()
            if unit in metric_units:
                break
            else:
                print(
                    f"\nNeed to choose units from: {str([unit for unit in metric_units])}"
                )
        return unit
    # Imperial Units
    elif metric_or_imperial == "imperial":
        # makes sure unit is correct
        while True:
            unit = input(
                f"\nWhat unit are you converting {to_or_from}?\nChoices are: 'in', 'ft', 'yd', 'mi': "
            ).lower()
            if unit in imperial_units:
                break
            else:
                print(
                    f"\nNeed to choose units from: {str([unit for unit in imperial_units])}"
                )
        return unit


def get_value(from_unit):
    """asks user amount to convert and returns value of 'from' unit"""
    while True:
        value = input(f"\nHow many {from_unit}? ")
        try:
            value = float(value)
            break
        except ValueError:
            print("Not a valid number")
    return value


# main body that lets users convert until they want to quit
body = True
while body:
    main_choice = input(
        "Which conversion tool do you want to use? Type 'q' to quit.\n1: Metric to Metric\n"
        "2: Metric to Imperial\n3: Imperial to Metric\n"
    )

    # Metric to Metric conversion
    if main_choice == "1":
        # selecting units using functions
        from_unit = select_unit("metric", "from")
        to_unit = select_unit("metric", "to")
        value = get_value(from_unit)
        # calling converting functions to get result
        converted_units = metric_to_metric(value, from_unit, to_unit)
        print(
            f"\n{value:,.2f}{from_unit} is equal to {converted_units:,.2f}{to_unit}.\n"
        )

    # Metric to Imperial conversion
    elif main_choice == "2":
        # selecting units using function
        from_unit = select_unit("metric", "from")
        to_unit = select_unit("imperial", "to")
        value = get_value(from_unit)
        # calling converting functions to get result
        converted_units = metric_to_imperial(value, from_unit, to_unit)
        print(
            f"\n{value:,.2f}{from_unit} is equal to {converted_units:,.2f}{to_unit}.\n"
        )

    # Imperial to Metric conversion
    elif main_choice == "3":
        # selecting units using function
        from_unit = select_unit("imperial", "from")
        to_unit = select_unit("metric", "to")
        value = get_value(from_unit)
        # calling converting functions to get result
        converted_units = imperial_to_metric(value, from_unit, to_unit)
        print(
            f"\n{value:,.2f}{from_unit} is equal to {converted_units:,.2f}{to_unit}.\n"
        )

    # Quits Program
    elif main_choice == "q":
        break

    else:
        print("Not an option.\n")
