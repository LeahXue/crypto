from docplex.mp.model import Model
from .info import fiat, trading_fee, tokens
from .utils import get_crypto_prices, get_withdrawal_fees

class Optimizer(Model): 
    def __init__(self, exchanges, **params): 
        # init_currency_info 
        self.currency_set = set()
        for 

    def update_price_mtx(df): 
        transit_price_mtx = dict()
        for i in range(len(df)): 
            tiker = df["symbol"].iloc[i]
            base = ticker.split("_")[0]
            quote = ticker.split("_")[1]
            if base in currency_set and quote in currency_set: 
                transit_price_mtx[base, quote] = df["bid"].iloc[i]
                transit_price_mtx[quote, base] = 1 / df["ask"].iloc[i]
            
    



            

        