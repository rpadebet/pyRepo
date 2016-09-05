import pandas as pd
from zipline import TradingAlgorithm
from zipline.api import order, sid
from zipline.data.loader import load_bars_from_yahoo

# creating time interval
start = pd.Timestamp('2008-01-01', tz='UTC')
end = pd.Timestamp('2013-01-01', tz='UTC')

# loading the data
input_data = load_bars_from_yahoo(
    stocks=['AAPL', 'MSFT'],
    start=start,
    end=end,
)


def initialize(context):
    context.has_ordered = False


def handle_data(context, data):
    if not context.has_ordered:
        for stock in data:
            order(sid(stock), 100)
        context.has_ordered = True


algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data)
results = algo.run(input_data)