import Data
from fbprophet import Prophet
from matplotlib import pyplot as plt
from matplotlib.dates import MonthLocator, num2date
from matplotlib.ticker import FuncFormatter

if __name__ == "__main__":
    df = Data.Data().load_data()
    df_prophet = df[["Date", "CHSB"]]
    df_prophet.columns = ['ds', 'y']
    m = Prophet(yearly_seasonality=False)
    m.fit(df_prophet)
    future = m.make_future_dataframe(periods=480, freq='H')
    forecast = m.predict(future)
    print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())
    fig1 = m.plot(forecast)
    print("Hello")