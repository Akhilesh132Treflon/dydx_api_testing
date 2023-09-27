from  dydx_service import  DydxPClient
from dydx3 import constants
from tests.constants import SEVEN_DAYS_S
import time
from datetime import datetime, timedelta
"""
This class is used  to manage The order's on dydx .
This class have   functions create_order() and cancel_orders() that are used to open and close position on dydx.
"""

ORDER_STATUS_PENDING = 'PENDING'
ORDER_STATUS_OPEN = 'OPEN'
ORDER_STATUS_FILLED = 'FILLED'
ORDER_STATUS_CANCELED = 'CANCELED'
ORDER_STATUS_UNTRIGGERED = 'UNTRIGGERED'
MARKET_BTC_USD = 'BTC-USD'
MARKET_ETH_USD = 'ETH-USD'
MARKET_LINK_USD = 'LINK-USD'
class DydxOrder:

    def __init__(self):
        self.dydx_client = DydxPClient()
        self.dydx_p_client = self.dydx_client.client() 

    def create_order(self, order_params):
        placed_order_details = self.dydx_p_client.private.create_order(**order_params)
        print(vars(placed_order_details))
        return placed_order_details

    """ function is responsible for deleting the order on dydx.
        @param orderId orderId to be deleted.
        @return deleted order information.
    """

    def cancel_order(self, id):
        deleted_order = self.dydx_p_client.private.cancel_order(order_id=id)
        return deleted_order

    """ function get_market_orders is responsible for getting all the market order according to the order_params.
        @param Order_params are the parameters that pass to dydx3  API.
        @return Orders information.
    """

    # def get_market_orders(self, order_params):
    #      all_orders = self.dydx_p_client.private.get_orders(
    #         market=order_params["market"],
    #         status=order_params["status"])
    #     return all_orders

    def get_market_orders(self):
        all_orders = self.dydx_p_client.private.get_orders(
    market=MARKET_BTC_USD,
    status=ORDER_STATUS_OPEN,
    side="BUY",
      limit=5
                )
        return all_orders
    def get_order_book(self, market="ETH-USD"):
        order_book = self.dydx_p_client.public.get_orderbook(
            market=market,
        )
        if order_book is not None:
            order_book = vars(order_book)
        return order_book["data"]

    def get_account(self):
        account_info = self.dydx_p_client.private.get_account(
        ethereum_address="0xD5255Ac600d440F445607BABeb2Be5Fa320ce9a6"
        )
        return account_info

    def get_positions(self):
        positions = self.dydx_p_client.private.get_positions(
        market=MARKET_BTC_USD,
        status=ORDER_STATUS_OPEN,
        limit=5)
        return positions
    # return dydx_user dydx position_id.
    def get_position_id(self):
        user = self.get_account()
        user = vars(user)
        position_id = user["data"]["account"]["positionId"]
        return position_id
    def create_order_params(self, side, market, size, market_price, position_id):
        if side == "BUY":
            market_price = int(market_price) + 1350 
        else:
            market_price = int(market_price) - 1313
        order_params = {
            "position_id": position_id,
            "side": side,
            "order_type": constants.ORDER_TYPE_MARKET,
            "market": market,
            "size": size,
            "price": str(market_price),
            "post_only": "false",
            "limit_fee": "0.000500",
            "expiration_epoch_seconds": time.time() + SEVEN_DAYS_S + 60,
            "time_in_force": "FOK"
        }
        return order_params
if __name__ == "__main__":
    obj = DydxOrder()
    position_id = obj.get_position_id()
    print(position_id)
    # order_params = obj.create_order_params("SELL","BTC-USD","0.1200","26392",position_id)
    # obj.create_order(order_params)

    # order = obj.get_market_orders()
    # print(vars(order)['data']['orders'])
    account = obj.get_account();
    print(vars(account)['data']['account'])

    print("--------------------")

    print(vars(obj.get_positions()))
    # obj.cancel_order("4ea98a5983a777f6802156a689088d8386b156ef65daa9c4e4fdfb50b14b8c7")

