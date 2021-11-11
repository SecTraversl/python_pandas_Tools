# %%
#######################################
def pandasget_column_dtypes(data_frame: pandas.DataFrame):
    import pandas
    if isinstance(data_frame, pandas.DataFrame):
        return data_frame.dtypes

