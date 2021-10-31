# %%
#######################################
def pandaswrite_csv(data_frame: pandas.core.frame.DataFrame, output_file: str):
    """Writes an existing pandas DataFrame object as a .csv file.

    Reference:
        https://stackoverflow.com/questions/16923281/writing-a-pandas-dataframe-to-csv-file

    Args:
        data_frame (pandas.core.frame.DataFrame): Reference an existing pandas DataFrame.
        output_file (str): Reference a name for the .csv file you are creating.
    """
    import pandas as pd
    
    if isinstance(data_frame, pd.DataFrame):
        data_frame.to_csv(output_file, index=False)

