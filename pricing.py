"""A tiny module for the ci-failure-explainer demo."""


def total(prices: list[float], discount: float = 0.0) -> float:
    """Sum of prices after a fractional discount, applied per item, rounded to cents."""
    if not 0 <= discount < 1:
        raise ValueError("discount must be in [0, 1)")
    discounted = [price * discount for price in prices]
    return round(sum(discounted), 2)
