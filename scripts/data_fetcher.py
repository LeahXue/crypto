import ccxt
import pandas as pd

def is_feasible( exchange: str | ccxt.Exchange, func: str) -> bool:
    try:
        if isinstance(exchange, str):
            exchange = getattr(ccxt, exchange)()
        if exchange.has[ func ]:
            return True
    except Exception as e:
        # Handle exceptions (e.g., API errors, unsupported methods)
        return False
    return False

def get_time(start, end):
    return pd.date_range(start, end, freq='D').strftime('%Y-%m-%d').tolist()

# Get transaction fee for a list of exchanges
# Taker and maker seems same for different pairs
def get_transaction_fees( exchange_names: list[str] ): 
    fees = {}
    for exchange_id in exchange_names:
        assert is_feasible(exchange_id, 'FetchTradingFees')
        exchange = getattr(ccxt, exchange_id)()
        trading_fees = exchange.fetch_trading_fees()
        fees[exchange_id] = {}
        for k in trading_fees:
            fees[exchange_id][k] = {'maker': trading_fees[k]['maker'], 'taker': trading_fees[k]['taker']}
    return fees


# Get data from exchanges
def get_tick(exchange, symbol, date, timeframe = '1m', bars = 100000): 
    # since = exchange.parse8601(f'{date}T00:00:00Z')
    since = exchange.parse8601(date)
    assert is_feasible(exchange, 'fetchOHLCV')
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since, bars)
    
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df

def get_data(exchange, symbol, start, end, timeframe = '1m'):
    time = get_time(start, end)
    dfs = []
    for t in time:
        try:
        	dfs.append( get_tick(exchange, symbol, t, timeframe) )
        except Exception as e:
            print(f'Error: {e} when running {exchange} {symbol} {t}')
    df = pd.concat(dfs)
    df['symbol'] = symbol
    return df		





