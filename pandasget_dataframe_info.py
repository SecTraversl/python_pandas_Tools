# %%
#######################################
def pandasget_dataframe_info(data_frame: pandas.DataFrame):
    import pandas
    if isinstance(data_frame, pandas.DataFrame):
        return data_frame.info()

