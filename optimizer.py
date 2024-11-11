from docplex.mp.model import Model
from .info import fiat, trading_fee, tokens
from .utils import get_crypto_prices, get_withdrawal_fees

class Optimizer(Model): 
    def __init__(self, exchanges, **params): 
        self.exchanges = exchanges 

        # we allow arb w/ fiat currencies by default
        # TODO: fix here 
        self.include_fiat = True 
        self.fiat_set = fiat 
        self.token_set = tokens 

    def init_currency_info(self): 
        self.currency_set = set()
        coin_set = set()
        for exc_name, exchange in self.exchanges.items(): 
            currency_names = ['{}_{}'.format(exc_name, cur) for cur in exchange.currencies.keys()]
            coin_set |= set(exchange.currencies.keys())
            self.currency_set |= set(currency_names) 
            if not self.include_fiat: 
                self.currency_set -= set(['{}_{}'.format(exc_name, fiat) for fiat in self.fiat_set])
       
        # we only consider coins that are stable enough (defined in info.py)
        coin_set = coin_set & (self.token_set | self.fiat_set)
        self.crypto_prices = get_crypto_prices(coin_set) 
        self.currency_set = set([i for i in self.currency_set if i.split('_')[-1] in self.crypto_prices.keys()])

def find_arbitrage(): 
    



            

        