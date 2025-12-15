from src import Scheduler, apply_emergency


def test_emergency_reschedule():
    availability = {
        "A": {"Mon", "Tue", "Wed"},
        "B": {"Mon", "Thu", "Fri"},
        "C": {"Tue", "Wed", "Thu"},
        "D": {"Tue", "Fri"},
    }

    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

    new_av = apply_emergency(availability, "C", "Wed")
    scheduler = Scheduler(new_av, days)
    result = scheduler.Action()

    assert result is not None