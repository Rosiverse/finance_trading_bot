class TradingBotException(Exception):
    """Base exception for the Trading Bot."""
    pass

class InvalidInputException(TradingBotException):
    """Raised when user input is invalid."""
    pass

class APIException(TradingBotException):
    """Raised when the API returns an error."""
    pass

def validate_symbol(symbol: str) -> str:
    if not symbol or len(symbol) < 3 or not symbol.isalnum():
        raise InvalidInputException("Symbol must be a valid alphanumeric string (e.g., BTCUSDT).")
    return symbol.upper()

def validate_side(side: str) -> str:
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise InvalidInputException("Side must be either 'BUY' or 'SELL'.")
    return side

def validate_order_type(order_type: str) -> str:
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise InvalidInputException("Order type must be either 'MARKET' or 'LIMIT'.")
    return order_type

def validate_quantity(quantity: float) -> float:
    if quantity <= 0:
        raise InvalidInputException("Quantity must be greater than 0.")
    return quantity

def validate_price(price: float, order_type: str) -> float:
    if order_type == "LIMIT":
        if price is None or price <= 0:
            raise InvalidInputException("Limit orders require a price greater than 0.")
    return price
