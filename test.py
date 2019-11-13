import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('agg_distinct_transaction.csv')
agg_df = df.groupby(['fiscal_year']).agg({'total_obligation': np.sum})
print(agg_df)
