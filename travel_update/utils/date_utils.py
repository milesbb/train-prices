from datetime import datetime, timedelta

MONDAY_DAY_ORDER = 0
FRIDAY_DAY_ORDER = 4

DEFAULT_DAYS_IN_OFFICE = [MONDAY_DAY_ORDER, FRIDAY_DAY_ORDER]


def get_days_in_office_settings() -> list[int]:
    return DEFAULT_DAYS_IN_OFFICE


def get_next_dates_in_office() -> list[str]:
    days_in_office = get_days_in_office_settings()

    next_dates_in_office = []
    for day in days_in_office:
        next_dates_in_office.append(get_next_earliest_occuring_day(day))

    return next_dates_in_office
    

def get_next_earliest_occuring_day(target_weekday) -> str:
    today = datetime.now()
    days_ahead = target_weekday - today.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    next_date = today + timedelta(days=days_ahead+14)
    return next_date.strftime('%Y-%m-%d')