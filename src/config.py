import json
from pathlib import Path
from typing import Dict, Set, List
from .type import Availability, Day, PriorityMap


# src/config.py
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Availability of each worker loaded by config file
def input_availability(path: str) -> Availability:
    file_path = PROJECT_ROOT / path

    if not file_path.exists():
        raise FileNotFoundError(f"Config file not found: {file_path}")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data: Dict[str: Set(str)] = json.load(f)
    
    return {
        worker: set(days)
        for worker, days in data.items()
    }

# days needed to schedule loaded by config file
def input_days(path: str) -> List[Day]:
    file_path = PROJECT_ROOT / path

    if not file_path.exists():
        raise FileNotFoundError(f"Config file not found: {file_path}")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data: List[Day] = json.load(f)
    
    return data

# priorities loaded by config file
def input_availability(path: str) -> PriorityMap:
    file_path = PROJECT_ROOT / path

    if not file_path.exists():
        raise FileNotFoundError(f"Config file not found: {file_path}")
    
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
    