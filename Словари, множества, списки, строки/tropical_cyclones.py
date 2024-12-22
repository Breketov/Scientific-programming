def parse_date(date_string : str):
    DAYS_IN_MONTH = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 
                     7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    YEAR_RANGE = (1982, 2022)

    date_parts = date_string.strip().replace(" ", "").split("/")
    
    if len(date_parts) != 3:
        return 0, 0, 0, False
    else:
        day, month, year = map(int, date_parts)
    
    if not (1 <= day <= 31 and 1 <= month <= 12 and YEAR_RANGE[0] <= year <= YEAR_RANGE[1]):
        return day, month, year, False
    
    if day > DAYS_IN_MONTH[month]:
        return day, month, year, False

    return day, month, year, True


def common_tc_dates(cyclone_dates_1 : list[str], 
                    cyclone_dates_2 : list[str]) -> dict:
    results = {"any_year": 0,
               "both_years": 0,
               "only_one_year": 0,
               "only_first_year": 0,
               "only_second_year": 0,
               "none_of_years": 365}

    days1 = set()
    days2 = set()

    for date in cyclone_dates_1:
        day, month, year, is_valid = parse_date(date)
        if is_valid:
            date_tuple = (day, month)
            if date_tuple not in days1:
                days1.add(date_tuple)
                results["any_year"] += 1
                results["only_first_year"] += 1

    for date in cyclone_dates_2:
        day, month, year, is_valid = parse_date(date)
        if is_valid:
            date_tuple = (day, month)
            if date_tuple not in days2:
                days2.add(date_tuple)
                if date_tuple not in days1:
                    results["any_year"] += 1
                    results["only_second_year"] += 1
                else:
                    results["only_first_year"] -= 1

    results["only_one_year"] = results["only_first_year"] + results["only_second_year"]
    results["none_of_years"] = 365 - results["any_year"]
    results["both_years"] = results["any_year"] - results["only_one_year"]

    return results