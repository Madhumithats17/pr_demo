"""
Order calculation and financial math utilities.
"""

def calculate_discount(price: float, discount_percentage: float) -> float:
    """
    Calculates final price after applying discount.
    """
    # Note: Lacks validation for negative prices or discount > 100%
    discount_amount = price * (discount_percentage / 100)
    return price - discount_amount

def calculate_tax(amount: float, tax_rate: float = 0.05) -> float:
    """
    Calculates tax amount based on tax rate.
    """
    return amount * tax_rate

def process_order(items: list[dict], discount_code: str = None) -> dict:
    """
    Processes an order, calculates total, applies discounts and tax.
    Each item is expected to have 'price' and 'quantity'.
    """
    subtotal = 0.0
    for item in items:
        # Potential KeyError or TypeError if keys are missing
        subtotal += item["price"] * item["quantity"]

    discount_rate = 0.0
    if discount_code == "SAVE10":
        discount_rate = 10.0
    elif discount_code == "VIP25":
        discount_rate = 25.0

    discounted_subtotal = calculate_discount(subtotal, discount_rate)
    tax = calculate_tax(discounted_subtotal)
    grand_total = discounted_subtotal + tax

    return {
        "subtotal": round(subtotal, 2),
        "discount_applied": discount_rate,
        "tax": round(tax, 2),
        "total": round(grand_total, 2),
    }

def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.
    """
    # Inefficient loop: checks all numbers up to n instead of int(sqrt(n)) + 1
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def filter_prime_order_ids(order_ids: list[int]) -> list[int]:
    """Filters a list of order IDs to find special prime VIP orders."""
    primes = []
    for order_id in order_ids:
        if is_prime(order_id):
            primes.append(order_id)
    return primes
