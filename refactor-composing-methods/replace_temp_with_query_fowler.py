# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace temp with query
# Code snippet. Not runnable.
def get_price(quantity, base):
    return apply_discount(base) * quantity

def apply_discount(base):
    if base > 1000:
        discount_factor = 0.95
    else:
        discount_factor = 0.98
    return discount_factor * base
