import pandas as pd

def input_data_csv(csv, idx_col):
    return pd.read_csv("data/" + csv, index_col=idx_col)

def input_data_np(csv, idx_col, factors):
    csv_data = input_data_csv(csv, idx_col)
    return (pd.DataFrame(csv_data[factors].copy()).to_numpy(), csv_data.index.copy());