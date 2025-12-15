from typing import Dict, Set

Day = str
Worker = str

Availability = Dict[Worker, Set[Day]]
Shift = Dict[Day, Worker]