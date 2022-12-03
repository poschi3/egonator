class Tarifstufe:
    def __init__(self, single_online: float, single_offline: float, day: float, solo_31: float) -> None:
        self.single_online = single_online
        self.single_offline = single_offline
        self.day = day
        self.solo_31 = solo_31

TARIFSTUFEN = {
    "A":    Tarifstufe( 2.75,  3.20,  8.30,  80.10),
    "B":    Tarifstufe( 2.40,  2.70,  5.70,  71.90),
    "C":    Tarifstufe( 2.17,  2.50,  5.10,  57.70),
    "D":    Tarifstufe( 1.80,  2.10,  4.70,  46.50),
    "E":    Tarifstufe( 1.57,  1.70,  3.70,  39.80),
    "F":    Tarifstufe( 1.30,  1.40,  2.90,  31.80),
    #"K":    Tarifstufe( 1.45,  1.70,  9999, 9999), # There is no day ticket for K

    "1":    Tarifstufe( 1.80,  2.10,  4.70,  46.50),
    "2":    Tarifstufe( 2.51,  2.70,  5.70,  75.90),
    "2+T":  Tarifstufe( 3.62,  3.90, 13.60,  90.80),
    "3":    Tarifstufe( 3.62,  3.90, 13.60, 100.90),
    "3+T":  Tarifstufe( 4.92,  5.30, 13.60, 119.50),
    "4":    Tarifstufe( 4.92,  5.30, 13.60, 130.70),
    "4+T":  Tarifstufe( 4.92,  5.30, 13.60, 140.40),
    "5":    Tarifstufe( 6.04,  6.50, 17.80, 152.60),
    "5+T":  Tarifstufe( 6.04,  6.50, 17.80, 163.10),
    "6":    Tarifstufe( 7.25,  7.80, 17.80, 171.00),
    "6+T":  Tarifstufe( 7.25,  7.80, 17.80, 186.30),
    "7":    Tarifstufe( 8.55,  9.20, 17.80, 200.00),
    "7+T":  Tarifstufe( 8.55,  9.20, 17.80, 214.40),
    "8":    Tarifstufe( 9.67, 10.40, 21.50, 228.20),
    "8+T":  Tarifstufe( 9.67, 10.40, 21.50, 240.80),
    "9":    Tarifstufe(10.88, 11.70, 21.50, 254.60),
    "9+T":  Tarifstufe(10.88, 11.70, 21.50, 266.70),
    "10":   Tarifstufe(12.09, 13.00, 21.50, 282.10),
    "10+T": Tarifstufe(12.09, 13.00, 21.50, 303.40)
}

def single_online(days: float, tarifstufe) -> float:
    return TARIFSTUFEN[tarifstufe].single_online * 2 * days

def single_offline(days: float, tarifstufe) -> float:
    return TARIFSTUFEN[tarifstufe].single_offline * 2 * days

def day(days: float, tarifstufe) -> float:
    return TARIFSTUFEN[tarifstufe].day * days