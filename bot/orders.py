from bot.client import BinanceClient
from bot.logging_config import logger

class OrderManager:
    def __init__(self):
        self.client = BinanceClient()

    def place_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float = None) -> dict:
        symbol = symbol.upper()
        side = side.upper()
        order_type = order_type.upper()

        if side not in ["BUY", "SELL"]:
            raise ValueError("Side must be BUY or SELL.")
        if order_type not in ["MARKET", "LIMIT"]:
            raise ValueError("Order type must be MARKET or LIMIT.")
        if quantity <= 0:
            raise ValueError("Quantity must be strictly positive.")
        if order_type == "LIMIT" and (price is None or price <= 0):
            raise ValueError("Limit orders require a valid positive price.")

        endpoint = "/fapi/v1/order"
        
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        logger.info(f"Placing order params: {params}")
        
        response = self.client.send_signed_request("POST", endpoint, params=params)
        return response
