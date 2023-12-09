from dataclasses import dataclass

@dataclass
class Tarifstufe:
    single_online: float
    single_offline: float
    day: float
    solo_31: float # Outdated
    abo_3: float # Outdated
    abo_6: float # Outdated
    abo_12: float # Outdated
    abo_12_9: float # Outdated
    mobi_9: float # Outdated
    mobi_31: float # Outdated


TARIFSTUFEN = {
    "A":    Tarifstufe( 3.25,  3.70,  9.70,  80.10,  73.90,  68.90,  61.60, 37.90,  73.40,  90.90),
    "B":    Tarifstufe( 2.69,  3.00,  6.40,  71.90,  66.30,  62.50,  53.30, 27.90,  63.70,  79.00),
    "C":    Tarifstufe( 2.42,  2.80,  5.70,  57.70,  54.20,  51.10,  43.80, 26.90,  52.50,  64.30),
    "D":    Tarifstufe( 1.97,  2.40,  5.10,  46.50,  44.20,  41.70,  36.30, 22.30,  41.20,  51.30),
    "E":    Tarifstufe( 1.75,  1.90,  4.10,  39.80,  37.70,  35.60,  31.30, 19.30,  35.60,  44.20),
    "F":    Tarifstufe( 1.39,  1.500, 3.30,  31.80,  30.10,  28.50,  25.10, 15.50,  28.60,  35.60),
    #"K":    Tarifstufe( 1.67,  2.00,  9999, 9999), # There is no day ticket for K

    "1":    Tarifstufe( 1.97,  2.40,  5.10,  46.50,  44.20,  41.70,  36.30, 22.30,  41.20,  51.30),
    "2":    Tarifstufe( 2.79,  3.00,  6.40,  75.90,  71.90,  67.90,  59.70, 36.70,  68.80,  84.40),
    "2+T":  Tarifstufe( 4.02,  4.40, 15.10,  90.80,  86.00,  81.30,  71.40, 52.10,  81.70, 101.00),
    "3":    Tarifstufe( 4.02,  4.40, 13.60, 100.90,  95.60,  90.30,  79.60, 52.10,  81.70, 112.30),
    "3+T":  Tarifstufe( 5.46,  5.90, 15.10, 119.50, 113.20, 107.00,  94.00, 52.10,  81.70, 132.90),
    "4":    Tarifstufe( 5.46,  5.90, 15.10, 130.70, 123.80, 117.00, 102.60, 52.10,  81.70, 145.70),
    "4+T":  Tarifstufe( 5.46,  5.90, 15.10, 140.40, 133.00, 125.70, 110.40, 52.10,  81.70, 156.50),
    "5":    Tarifstufe( 6.70,  7.30, 19.80, 152.60, 144.60, 136.60, 120.10, 82.90, 101.90, 169.90),
    "5+T":  Tarifstufe( 6.70,  7.30, 19.80, 163.10, 154.50, 146.00, 128.40, 82.90, 101.90, 181.40),
    "6":    Tarifstufe( 8.05,  8.80, 19.80, 171.00, 162.00, 153.00, 134.70, 82.90, 101.90, 190.20),
    "6+T":  Tarifstufe( 8.05,  8.80, 19.80, 186.30, 176.50, 166.70, 147.10, 82.90, 101.90, 207.20),
    "7":    Tarifstufe( 9.49, 10.30, 19.80, 200.00, 189.50, 179.00, 157.70, 82.90, 101.90, 222.40),
    "7+T":  Tarifstufe( 9.49, 10.30, 19.80, 214.40, 203.10, 191.90, 168.90, 82.90, 101.90, 238.20),
    "8":    Tarifstufe(10.73, 11.70, 23.90, 228.20, 216.20, 204.20, 180.20, 99.90, 111.50, 253.80),
    "8+T":  Tarifstufe(10.73, 11.70, 23.90, 240.80, 228.20, 215.50, 189.60, 99.90, 111.50, 267.80),
    "9":    Tarifstufe(12.08, 13.10, 23.90, 254.60, 241.20, 227.90, 200.70, 99.90, 111.50, 283.10),
    "9+T":  Tarifstufe(12.08, 13.10, 23.90, 266.70, 252.70, 238.70, 210.30, 99.90, 111.50, 296.60),
    "10":   Tarifstufe(13.42, 14.50, 23.90, 282.10, 267.30, 252.50, 222.20, 99.90, 111.50, 313.60),
    "10+T": Tarifstufe(13.42, 14.50, 23.90, 303.40, 287.50, 271.50, 238.70, 99.90, 111.50, 337.30)
}

def single_online(days: float, tarifstufe, rides_per_day) -> float:
    return TARIFSTUFEN[tarifstufe].single_online * rides_per_day * days

def single_offline(days: float, tarifstufe, rides_per_day) -> float:
    return TARIFSTUFEN[tarifstufe].single_offline * rides_per_day * days

def day(days: float, tarifstufe) -> float:
    return TARIFSTUFEN[tarifstufe].day * days