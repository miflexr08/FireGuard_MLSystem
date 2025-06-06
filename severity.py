
from enum import Enum

class Severity(Enum):
    Normal = 0
    Ok = "ok",
    Attention = "attention",
    Critical = "critical"