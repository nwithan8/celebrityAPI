from datetime import datetime, timedelta


def today() -> datetime:
    return datetime.today()


def yesterday() -> datetime:
    return datetime.today() - timedelta(days=1)


def tomorrow() -> datetime:
    return datetime.today() + timedelta(days=1)


def start_of_week(date: datetime) -> datetime:
    return date - timedelta(days=date.weekday())


def end_of_week(date: datetime) -> datetime:
    return date + timedelta(days=6 - date.weekday())


def start_of_month(date: datetime) -> datetime:
    return date.replace(day=1)


def end_of_month(date: datetime) -> datetime:
    addition = timedelta(days=30)
    if date.month in [1, 3, 5, 7, 8, 10, 12]:
        addition = timedelta(days=31)
    elif date.month == 2:
        addition = timedelta(days=28)
    return date.replace(day=1) + addition


def start_of_year(date: datetime) -> datetime:
    return date.replace(month=1, day=1)


def end_of_year(date: datetime) -> datetime:
    return date.replace(month=12, day=31)


def start_of_this_week() -> datetime:
    return start_of_week(today())


def start_of_week_offset(offset: int) -> datetime:
    x_weeks_ago = weeks_from_now(weeks=offset)
    return start_of_week(x_weeks_ago)


def end_of_week_offset(offset: int) -> datetime:
    x_weeks_ago = weeks_from_now(weeks=offset)
    return end_of_week(x_weeks_ago)


def start_of_month_offset(offset: int) -> datetime:
    x_months_ago = months_from_now(months=offset)
    return start_of_month(x_months_ago)


def end_of_month_offset(offset: int) -> datetime:
    x_months_ago = months_from_now(months=offset)
    return end_of_month(x_months_ago)


def start_of_year_offset(offset: int) -> datetime:
    x_years_ago = years_from_now(years=offset)
    return start_of_year(x_years_ago)


def end_of_year_offset(offset: int) -> datetime:
    x_years_ago = years_from_now(years=offset)
    return end_of_year(x_years_ago)


def end_of_this_week() -> datetime:
    return end_of_week(today())


def start_of_this_month() -> datetime:
    return start_of_month(today())


def end_of_this_month() -> datetime:
    return end_of_month(today())


def start_of_this_year() -> datetime:
    return start_of_year(today())


def end_of_this_year() -> datetime:
    return end_of_year(today())


def days_ago(days: int) -> datetime:
    return datetime.today() - timedelta(days=days)


def days_from_now(days: int) -> datetime:
    return days_ago(days=days * -1)


def weeks_ago(weeks: int) -> datetime:
    return datetime.today() - timedelta(weeks=weeks)


def weeks_from_now(weeks: int) -> datetime:
    return weeks_ago(weeks=weeks * -1)


def months_ago(months: int) -> datetime:
    return datetime.today() - timedelta(days=months * 30)


def months_from_now(months: int) -> datetime:
    return months_ago(months=months * -1)


def years_ago(years: int) -> datetime:
    return datetime.today() - timedelta(days=years * 365)


def years_from_now(years: int) -> datetime:
    return years_ago(years=years * -1)


def yyyy_mm_dd(date: datetime) -> str:
    return date.strftime("%Y-%m-%d")


def clean_date_string(date_string: str, date_format: str = "%Y-%m-%d") -> str:
    datetime_date = datetime.strptime(date_string, date_format)
    return yyyy_mm_dd(datetime_date)
