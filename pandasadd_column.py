# %%
#######################################
def pandasadd_column(data_frame: pandas.DataFrame, column_name: str, column_content: list):
    import pandas
    data_frame[column_name] = column_content

