from src import Scheduler, apply_emergency

def main():
    availability = {
        "A": {"Mon", "Tue", "Wed"},
        "B": {"Mon", "Thu", "Fri"},
        "C": {"Tue", "Wed", "Thu"},
        "D": {"Tue", "Fri"},
    }
    
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

    scheduler = Scheduler(availability, days)
    shift_schedule = scheduler.Action()

    print("Initial shift schedule:")
    print(shift_schedule)

    print("\nEmergency: A cannot work on Mon")
    new_av = apply_emergency(availability, "A", "Mon")
    scheduler2 = Scheduler(new_av, days)
    schedule2 = scheduler2.Action()

    print("Rescheduled:")
    print(schedule2)

if __name__ == "__main__":
    main()
