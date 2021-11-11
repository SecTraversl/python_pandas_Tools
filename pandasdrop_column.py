# %%
#######################################
def pandasdrop_column(data_frame: pandas.DataFrame, column_name: str):
    import pandas
    if isinstance(data_frame, pandas.DataFrame):
        return data_frame.drop(column_name, axis=1)

