import requests
import io
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler


class Data:
    def __init__(self):
        self.path = 'https://drive.google.com/uc?export=download&id=1mQr7hY6yO88nv5SmLbYBRk14cJJ_FQnP'

    def load_data(self):
        s = requests.get(self.path).content
        dateparse = lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
        df = pd.read_csv(io.StringIO(s.decode('utf-8')),
                         header='infer',
                         delimiter=',',
                         parse_dates=['Date'],
                         date_parser=dateparse)
        df = df.sort_values('Date')
        return df
