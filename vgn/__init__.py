class Tarifstufe:
    def __init__(self, single_online: float, single_offline: float, day: float) -> None:
        self.single_online = single_online
        self.single_offline = single_offline
        self.day = day

TARIFSTUFEN = {
    "A": Tarifstufe(2.75, 3.20, 8.30),
    # "B": Tarifstufe(,,),
    # "C": Tarifstufe(,,),
    # "D": Tarifstufe(,,),
    # "E": Tarifstufe(,,),
    # "F": Tarifstufe(,,),
    # "1": Tarifstufe(,,),
    # "1+T": Tarifstufe(,,),
    # "2": Tarifstufe(,,),
    # "2+T": Tarifstufe(,,),
    # "3": Tarifstufe(,,),
    # "3+T": Tarifstufe(,,),
    # "4": Tarifstufe(,,),
    # "4+T": Tarifstufe(,,),
    # "5": Tarifstufe(,,),
    # "5+T": Tarifstufe(,,),
    # "6": Tarifstufe(,,),
    # "6+T": Tarifstufe(,,),
    # "7": Tarifstufe(,,),
    # "7+T": Tarifstufe(,,),
    # "8": Tarifstufe(,,),
    # "8+T": Tarifstufe(,,),
    # "9": Tarifstufe(,,),
    # "9+T": Tarifstufe(,,),
    # "10": Tarifstufe(,,),
    "10+T": Tarifstufe(12.09, 13.00, 21.50),
}
