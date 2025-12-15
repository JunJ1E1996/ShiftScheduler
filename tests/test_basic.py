from src import Scheduler

def test_basic_scheduler():
    availability = {
        "A": {"Mon", "Tue", "Wed"},
        "B": {"Mon", "Thu", "Fri"},
        "C": {"Tue", "Wed", "Thu"},
        "D": {"Tue", "Fri"},
    }
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

    shift_scheduler = Scheduler(availability, days)
    shift_schedule = shift_scheduler.Action()

    assert shift_schedule is not None
    assert len(shift_schedule) == len(days)

