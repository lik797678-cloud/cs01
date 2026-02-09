class TradingEngine:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)
        self.match_orders()  

    def match_orders(self):
        # Logic for matching buy and sell orders
        buy_orders = sorted([o for o in self.orders if o['type'] == 'buy'], key=lambda x: x['price'], reverse=True)
        sell_orders = sorted([o for o in self.orders if o['type'] == 'sell'], key=lambda x: x['price'])

        while buy_orders and sell_orders:
            buy_order = buy_orders[0]
            sell_order = sell_orders[0]

            if buy_order['price'] >= sell_order['price']:
                trade_quantity = min(buy_order['quantity'], sell_order['quantity'])
                print(f'Trade executed: {trade_quantity} units at price {sell_order['price']}')
                buy_order['quantity'] -= trade_quantity
                sell_order['quantity'] -= trade_quantity

                if buy_order['quantity'] == 0:
                    buy_orders.pop(0)
                if sell_order['quantity'] == 0:
                    sell_orders.pop(0)
            else:
                break

# Example use:
# trading_engine = TradingEngine()
# trading_engine.add_order({'type': 'buy', 'quantity': 5, 'price': 10})
# trading_engine.add_order({'type': 'sell', 'quantity': 5, 'price': 8})