from dataclasses import dataclass

@dataclass
class Tarifstufe:
    single_online: float
    single_offline: float
    day: float


TARIFSTUFEN = {
    "A":    Tarifstufe( 3.65,  3.90, 10.60),
    "B":    Tarifstufe( 2.91,  3.30,  7.10),
    "C":    Tarifstufe( 2.65,  3.10,  6.20),
    "D":    Tarifstufe( 2.27,  2.60,  5.60),
    "E":    Tarifstufe( 1.87,  2.10,  4.50),
    "F":    Tarifstufe( 1.51,  1.70,  3.70),

    "1":    Tarifstufe( 2.21,  2.60,  5.60),
    "2":    Tarifstufe( 3.06,  3.30,  7.20),
    "2+T":  Tarifstufe( 4.46,  4.80, 16.70),
    "3":    Tarifstufe( 4.46,  4.80, 16.70),
    "3+T":  Tarifstufe( 6.04,  6.50, 16.70),
    "4":    Tarifstufe( 6.04,  6.50, 16.70),
    "4+T":  Tarifstufe( 6.04,  6.50, 16.70),
    "5":    Tarifstufe( 7.44,  8.00, 21.90),
    "5+T":  Tarifstufe( 7.44,  8.00, 21.90),
    "6":    Tarifstufe( 9.02,  9.70, 21.90),
    "6+T":  Tarifstufe( 9.02,  9.70, 21.90),
    "7":    Tarifstufe(10.50, 11.30, 21.90),
    "7+T":  Tarifstufe(10.50, 11.30, 21.90),
    "8":    Tarifstufe(11.99, 12.90, 26.50),
    "8+T":  Tarifstufe(11.99, 12.90, 26.50),
    "9":    Tarifstufe(13.48, 14.50, 26.50),
    "9+T":  Tarifstufe(13.48, 14.50, 26.50),
    "10":   Tarifstufe(14.88, 16.00, 26.50),
    "10+T": Tarifstufe(14.88, 16.00, 26.50)
}

def single_online(days: float, tarifstufe, rides_per_day) -> float:
    return TARIFSTUFEN[tarifstufe].single_online * rides_per_day * days

def single_offline(days: float, tarifstufe, rides_per_day) -> float:
    return TARIFSTUFEN[tarifstufe].single_offline * rides_per_day * days

def day(days: float, tarifstufe) -> float:
    return TARIFSTUFEN[tarifstufe].day * days