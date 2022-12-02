PRICE_PER_DISTANCE = 0.24

VOLUME_1 = 12.0
DISCOUNT_1 = 0.5

VOLUME_2 = 72.0
DISCOUNT_2 = 0.5 # 0.75 but is 0.5 to the existing 0.5

VOLUME_3 = 220.0
DISCOUNT_3 = 1


def basic_price(distance: float) -> float:
    price = PRICE_PER_DISTANCE * distance
    return round(price, 2)

def discount(price: float) -> float:
    if price <= VOLUME_1:
        return price
    
    new_price = VOLUME_1 + (price - VOLUME_1) * DISCOUNT_1
    if new_price <= VOLUME_2:
        return new_price

    new_price =  VOLUME_1 + VOLUME_2 + (new_price - VOLUME_1 - VOLUME_2) * DISCOUNT_2 # TODO
    if new_price <= VOLUME_3:
        return new_price

    return VOLUME_3

def price_for_days(days: float, distance: float, nbg: bool) -> float:
    price = basic_price(distance * 2 * days)
    price += (2.0 if nbg else 1.0) * days
    return discount(price)
