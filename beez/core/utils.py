from datetime import datetime

colors = ['blue', 'white', 'yellow', 'red', 'green']


def current_color():
    """Return the color of the current year."""
    return color_for_year(datetime.now().year)


def color_for_year(year: int):
    """Return the color of the given year.

    2016 - white, 2017 - yellow, 2018 - red, 2019 - green, 2020 - blue
    2021 - white etc."""
    return colors[year % 5]