# %%
#######################################
def pandasget_dataframe_headers(data_frame: pandas.DataFrame):
    import pandas
    if isinstance(data_frame, pandas.DataFrame):
        column_headers = [name for name in data_frame.columns]
        return column_headers

