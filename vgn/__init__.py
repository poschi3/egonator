class Tarifstufe:
    def __init__(self, single_online: float, single_offline: float, day: float) -> None:
        self.single_online = single_online
        self.single_offline = single_offline
        self.day = day

TARIFSTUFEN = {
    "A":    Tarifstufe( 2.75,  3.20,  8.30),
    "B":    Tarifstufe( 2.40,  2.70,  5.70),
    "C":    Tarifstufe( 2.17,  2.50,  5.10),
    "D":    Tarifstufe( 1.80,  2.10,  4.70),
    "E":    Tarifstufe( 1.57,  1.70,  3.70),
    "F":    Tarifstufe( 1.30,  1.40,  2.90),
    "K":    Tarifstufe( 1.45,  1.70,  9999), # There is no day ticket for K

    "1":    Tarifstufe( 1.80,  2.10,  4.70),
    "2":    Tarifstufe( 2.51,  2.70,  5.70),
    "2+T":  Tarifstufe( 3.62,  3.90, 13.60),
    "3":    Tarifstufe( 3.62,  3.90, 13.60),
    "3+T":  Tarifstufe( 4.92,  5.30, 13.60),
    "4":    Tarifstufe( 4.92,  5.30, 13.60),
    "4+T":  Tarifstufe( 4.92,  5.30, 13.60),
    "5":    Tarifstufe( 6.04,  6.50, 17.80),
    "5+T":  Tarifstufe( 6.04,  6.50, 17.80),
    "6":    Tarifstufe( 7.25,  7.80, 17.80),
    "6+T":  Tarifstufe( 7.25,  7.80, 17.80),
    "7":    Tarifstufe( 8.55,  9.20, 17.80),
    "7+T":  Tarifstufe( 8.55,  9.20, 17.80),
    "8":    Tarifstufe( 9.67, 10.40, 21.50),
    "8+T":  Tarifstufe( 9.67, 10.40, 21.50),
    "9":    Tarifstufe(10.88, 11.70, 21.50),
    "9+T":  Tarifstufe(10.88, 11.70, 21.50),
    "10":   Tarifstufe(12.09, 13.00, 21.50),
    "10+T": Tarifstufe(12.09, 13.00, 21.50)
}
