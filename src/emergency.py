from .type import Availability, Worker, Day

def apply_emergency(availability: Availability, worker: Worker, day: Day) -> Availability:
    new_availability = {k:set(v) for k, v in availability.items()}
    if day in new_availability[worker]:
        new_availability[worker].remove(day)
    return new_availability
