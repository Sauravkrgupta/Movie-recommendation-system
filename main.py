import pandas as pd
from ydata_profiling import ProfileReport

DATA_DIR='/Data'

df = pd.read_csv(DATA_DIR + 'housing.csv')
print(df)

