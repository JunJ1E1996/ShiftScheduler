from typing import Dict, Set

Day = str
Worker = str
Priority = int

Availability = Dict[Worker, Set[Day]]
Shift = Dict[Day, Worker]
PriorityMap = Dict[Worker, Priority]