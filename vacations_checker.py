from vacations_calendar import calendar
def check(date_str):
    data_vac =date_str[0:5]
    if data_vac in calendar:
        return calendar[data_vac]
    else:
        return "None"    