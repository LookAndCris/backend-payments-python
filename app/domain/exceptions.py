class DomainError(Exception):
    pass


class InvalidAmount(DomainError):
    pass


class PaymentNotFound(DomainError):
    pass


class DuplicatePayment(DomainError):
    pass