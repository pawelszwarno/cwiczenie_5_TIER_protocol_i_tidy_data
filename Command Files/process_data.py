import pandas as pd

df = pd.read_csv(r'D:\uczelnia\semestr_5\AiBD\cw\lab_5\Original Data\tb.csv')
# Converting NaN to zeros for easier processing.
df = df.fillna(0.0)
# Removing years and countries with zero tuberculosis cases.
df.drop(df[df.new_sp == 0].index, inplace=True)

df.to_csv(r'D:\uczelnia\semestr_5\AiBD\cw\lab_5\Analysis Data\tb_processed.csv')
