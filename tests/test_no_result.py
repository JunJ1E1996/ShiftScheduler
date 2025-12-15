from src import Scheduler


def test_no_solution():
    availability = {
        "A": {"Mon"},
        "B": {"Mon"},
    }

    days = ["Mon", "Tue"]

    scheduler = Scheduler(availability, days)
    result = scheduler.Action()

    assert result is None