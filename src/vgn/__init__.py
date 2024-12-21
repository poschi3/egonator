from dataclasses import dataclass

@dataclass
class Tarifstufe:
    single_online: float
    single_offline: float
    day: float


TARIFSTUFEN = {
    "A":    Tarifstufe( 3.47,  3.90, 10.30),
    "B":    Tarifstufe( 2.87,  3.20,  7.00),
    "C":    Tarifstufe( 2.57,  3.00,  6.10),
    "D":    Tarifstufe( 2.15,  2.50,  5.50),
    "E":    Tarifstufe( 1.85,  2.00,  4.40),
    "F":    Tarifstufe( 1.48,  1.60,  3.60),

    "1":    Tarifstufe( 2.15,  2.50,  5.50),
    "2":    Tarifstufe( 2.97,  3.20,  7.00),
    "2+T":  Tarifstufe( 4.34,  4.70, 16.10),
    "3":    Tarifstufe( 4.34,  4.70, 16.10),
    "3+T":  Tarifstufe( 5.85,  6.30, 16.10),
    "4":    Tarifstufe( 5.85,  6.30, 16.10),
    "4+T":  Tarifstufe( 5.85,  6.30, 16.10),
    "5":    Tarifstufe( 7.22,  7.80, 21.10),
    "5+T":  Tarifstufe( 7.22,  7.80, 21.10),
    "6":    Tarifstufe( 8.69,  9.40, 21.10),
    "6+T":  Tarifstufe( 8.69,  9.40, 21.10),
    "7":    Tarifstufe(10.20, 11.00, 21.10),
    "7+T":  Tarifstufe(10.20, 11.00, 21.10),
    "8":    Tarifstufe(11.57, 12.50, 25.50),
    "8+T":  Tarifstufe(11.57, 12.50, 25.50),
    "9":    Tarifstufe(13.04, 14.10, 25.50),
    "9+T":  Tarifstufe(13.04, 14.10, 25.50),
    "10":   Tarifstufe(14.49, 15.60, 25.50),
    "10+T": Tarifstufe(14.49, 15.60, 25.50)
}

def single_online(days: float, tarifstufe, rides_per_day) -> float:
    return TARIFSTUFEN[tarifstufe].single_online * rides_per_day * days

def single_offline(days: float, tarifstufe, rides_per_day) -> float:
    return TARIFSTUFEN[tarifstufe].single_offline * rides_per_day * days

def day(days: float, tarifstufe) -> float:
    return TARIFSTUFEN[tarifstufe].day * days