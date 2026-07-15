from winotify import Notification


def show_notification(title, message):

    toast = Notification(
        app_id="Battery Monitor",
        title=title,
        msg=message
    )

    toast.show()