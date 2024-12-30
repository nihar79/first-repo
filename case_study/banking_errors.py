class InsufficientBalanceException(Exception):
    def __init__(self):
        super().__init__("You cannot withdraw more than your current balance.")

class NotACustomerException(Exception):
    def __init__(self):
        super().__init__("Please consider becoming a customer to avail our services. Thankyou!")

class ZeroOrNegativeDepositException(Exception):
    def __init__(self):
        super().__init__("Cannot deposit zero/negative values. Please enter a valid digit.")