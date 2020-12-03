import pandas as pd

def input_data_csv(csv, idx_col):
    return pd.read_csv("data/" + csv, index_col=idx_col)

def input_data_np(csv, idx_col, factors):
    csv_data = input_data_csv(csv, idx_col)
    data = pd.DataFrame(csv_data[factors].copy()).to_numpy()
    data = list(filter(lambda col: not "?" in col, data))
    return (data, csv_data.index.copy());