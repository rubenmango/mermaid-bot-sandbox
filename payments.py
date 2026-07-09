# Payment processing flow (source of truth for payments.mmd)

def process_payment(order):
    authenticate(order)
    if fraud_check(order):
        charge_card(order)
        send_receipt(order)      # NEW step — not yet in payments.mmd
    return "done"


def authenticate(order):
    """Verify the customer's identity / token."""
    ...


def fraud_check(order):
    """Run risk rules; return True if the charge may proceed."""
    return True


def charge_card(order):
    """Capture funds on the card."""
    ...


def send_receipt(order):
    """Email the receipt to the customer after a successful charge."""
    ...
