"""A tiny module for the ci-failure-explainer demo."""


def total(prices: list[float], discount: float = 0.0) -> float:
    """Sum of prices after a fractional discount, rounded to cents."""
    if not 0 <= discount < 1:
        raise ValueError("discount must be in [0, 1)")
    return round(sum(prices) * (1 - discount), 2)


def bulk_total(carts: list[list[float]], discount: float = 0.0) -> float:
    """Total of several carts with the same discount."""
    import math
    return round(sum(total(cart, discount) for cart in carts), 2)
