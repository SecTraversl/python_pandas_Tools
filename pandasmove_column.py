# %%
#######################################
def pandasmove_column(data_frame: pandas.DataFrame, column_name: str, new_index_loc: int):
    """Takes a given DataFrame, column name, and desired index location and moves the referenced column to the desired location.

    References:
        https://sparkbyexamples.com/pandas/pandas-change-position-of-a-column/\n

    Args:
        data_frame (pandas.DataFrame): Reference an existing DataFrame.
        column_name (str): Reference a valid column name.
        new_index_loc (int): Specify the desired index location.
    """
    # import pandas
    if new_index_loc < 0:
        row_num, col_num = data_frame.shape
        new_index_loc = col_num + new_index_loc
    else:
        thecolumn = data_frame.pop(column_name)
        data_frame.insert(new_index_loc, thecolumn.name, thecolumn)

