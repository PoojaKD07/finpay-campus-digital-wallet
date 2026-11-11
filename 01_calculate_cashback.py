BPS_SCALE = 10000
MULT_SCALE = 10
DIVISOR = BPS_SCALE * MULT_SCALE

RATE_TABLE = {
    "CANTEEN": (200, 5000),
    "STATIONERY": (100, 2000),
    "TRANSPORT": (300, 10000),
    "HOSTEL": (50, 20000),
    "ONLINE": (100, 3000),
    "TOPUP": (0, 0),
}
TIER_TABLE = {
    "BASIC": (10, 10),
    "PRIME": (15, 15),
    "PREMIUM": (20, 20),
}

def calculate_cashback(amount_paise: int, category: str, tier: str) -> int:
    """Pure function: return raw cashback in paise before monthly cap."""
    if not isinstance(amount_paise, int) or isinstance(amount_paise, bool) or amount_paise <= 0:
        raise ValueError("InvalidAmount: amount_paise must be a positive integer")
    if category not in RATE_TABLE:
        raise ValueError("UnknownCategory")
    if tier not in TIER_TABLE:
        raise ValueError("UnknownTier")
    rate_bps, _ = RATE_TABLE[category]
    rate_mult_x10, _ = TIER_TABLE[tier]
    if rate_bps == 0:
        return 0
    return (amount_paise * rate_bps * rate_mult_x10) // DIVISOR

if __name__ == "__main__":
    cases = [
        (10000, "CANTEEN", "BASIC"),
        (10000, "CANTEEN", "PRIME"),
        (10000, "CANTEEN", "PREMIUM"),
        (333, "CANTEEN", "BASIC"),
        (49, "CANTEEN", "BASIC"),
        (50, "CANTEEN", "BASIC"),
        (10300, "HOSTEL", "PRIME"),
        (10000, "TOPUP", "BASIC"),
    ]
    for case in cases:
        print(case, "=>", calculate_cashback(*case), "paise")
