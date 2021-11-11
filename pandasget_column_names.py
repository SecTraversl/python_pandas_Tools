# %%
#######################################
def pandasget_column_names(data_frame: pandas.DataFrame):
    """Returns the column names in order of appearance for a given DataFrame object

    References:
        https://sparkbyexamples.com/pandas/pandas-change-position-of-a-column/\n

    Args:
        data_frame (pandas.DataFrame): Reference an existing DataFrame object.

    Returns:
        list: Returns a list.
    """
    # import pandas
    return data_frame.columns.tolist()

