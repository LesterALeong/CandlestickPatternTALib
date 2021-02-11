import talib
import yfinance as yf 

ticker = 'SPY'

data = yf.download(ticker, start='2020-01-01', end='2020-12-31')

# More examples from: https://mrjbq7.github.io/ta-lib/func_groups/pattern_recognition.html
morning_star = talib.CDLMORNINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])

# # Example of looking at morning star candle pattern
# print(morning_star[morning_star != 0])

engulfing = talib.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])

# # Exampling of looking at engulfing pattern
# print(engulfing[engulfing != 0])

data['morning_star'] = morning_star
data['engulfing'] = engulfing

print(data)