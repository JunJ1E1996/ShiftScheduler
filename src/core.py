from collections import defaultdict
from typing import List, Optional

from .type import Day, Worker, Availability, Shift, PriorityMap

class Scheduler:
    def __init__(
            self,
            availability: Availability,
            days: List[Day],
            priorities: Optional[PriorityMap] = None,
            max_days: int = 2
                 ):
        self.availability = availability # record available days of each worker 
        self.days = days # record the days needed to been assign
        self.max_days = max_days
        self.assignment: Shift = {} # day -> worker
        self.workload = defaultdict(int)
        self.priorities = priorities or {}

    # Check the worker weather overload
    def _can_assign(self, worker: Worker) -> bool: 
            return self.workload[worker] < self.max_days
        
    # execute assignment
    def _assign(self, day: Day, worker: Worker):
        self.assignment[day] = worker
        self.workload[worker] += 1

    # delete assignment
    def _unassign(self, day: Day, worker: Worker):
        del self.assignment[day]
        self.workload[worker] -= 1

    # main scheduler function
    def _find_daily_shift(self, day_idx: int) -> bool:
        if day_idx == len(self.days):
            return True
        
        day = self.days[day_idx]

        candidates = [
            c for c in self.availability
            if day in self.availability[c] and self._can_assign(c)
        ]

        # 優先級排序 worker
        candidates.sort(
            key = lambda w: (
                -self.priorities.get(w, 0), # 優先級先排
                self.workload[w]            # loading 低先排
            )
        )

        for c in candidates:
            self._assign(day, c)

            if self._find_daily_shift(day_idx + 1):
                return True
            
            self._unassign(day, c)

        return False
    
    # action function
    def Action(self) -> Optional[Shift]:
        result = self._find_daily_shift(0)
        if result:
            return dict(self.assignment) # return the shift
        else:
            return None
                

                


    

