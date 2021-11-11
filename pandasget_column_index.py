# %%
#######################################
def pandasget_column_index(data_frame: pandas.DataFrame, column_name: str):
    """For a given pandas.DataFrame object and column name, returns the index location of that column.

    References:
        https://sparkbyexamples.com/pandas/pandas-change-position-of-a-column/\n

    Args:
        data_frame (pandas.DataFrame): Reference an existing pandas.DataFrame object
        column_name (str): Reference a valid column name.

    Returns:
        int: Returns an integer.
    """
    import pandas
    col_index = data_frame.columns.get_loc(column_name)
    return col_index

