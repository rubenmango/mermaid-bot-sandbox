# Inventory restock flow (new source — no diagram exists yet)

def restock(item):
    level = check_stock(item)
    if level < threshold(item):
        order = create_purchase_order(item)
        await_delivery(order)
        update_stock(item, order)
    return level


def check_stock(item):
    """Return the current on-hand quantity for an item."""
    ...


def threshold(item):
    """Reorder point for the item."""
    ...


def create_purchase_order(item):
    """Raise a PO with the supplier."""
    ...


def await_delivery(order):
    """Block until the supplier delivery is received."""
    ...


def update_stock(item, order):
    """Add the delivered quantity back into stock."""
    ...
