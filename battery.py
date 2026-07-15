import psutil


def get_battery():
    """
    Returns the current battery object.
    """
    return psutil.sensors_battery()