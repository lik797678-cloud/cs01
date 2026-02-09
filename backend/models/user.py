class User:
    def __init__(self, id, username, email, portfolio=None, balance=0.0, trading_history=None):
        self.id = id
        self.username = username
        self.email = email
        self.portfolio = portfolio if portfolio is not None else []
        self.balance = balance
        self.trading_history = trading_history if trading_history is not None else []

    def __repr__(self):
        return f'User(id={self.id}, username={self.username}, email={self.email}, balance={self.balance})'