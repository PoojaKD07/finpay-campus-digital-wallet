def calculate_monthly_cap(base_cap_paise: int, cap_mult_x10: int) -> int:
    """Tier-adjusted monthly cashback cap in integer paise."""
    if base_cap_paise < 0 or cap_mult_x10 <= 0:
        raise ValueError("Invalid cap or multiplier")
    return (base_cap_paise * cap_mult_x10) // 10

def apply_monthly_cap(raw_cashback_paise: int, cap_paise: int, earned_paise: int) -> int:
    """Return cashback awarded after applying the remaining monthly cap."""
    if min(raw_cashback_paise, cap_paise, earned_paise) < 0:
        raise ValueError("Cashback values cannot be negative")
    remaining = max(0, cap_paise - earned_paise)
    return min(raw_cashback_paise, remaining)

if __name__ == "__main__":
    cap = calculate_monthly_cap(5000, 10)
    print("Cap:", cap, "Remaining:", max(0, cap - 4900))
    print("Awarded:", apply_monthly_cap(200, cap, 4900))
