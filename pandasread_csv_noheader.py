# %%
#######################################
def pandasread_csv_noheader(csv_file: str):
    """Returns a pandas dataframe from the given .csv file.  Assumes there is no header in the .csv.

    Example:
        >>> pandasread_csv_noheader('test.csv')\n
               0   1           2                   3  4\n
        0    bob  21     janitor   sanitization team  2\n
        1  alice  22   secretary          admin team  3\n
        2  chuck  23     plumber   construction team  4\n

    Reference:
        https://www.tutorialspoint.com/python-read-csv-file-with-pandas-without-header

    Args:
        csv_file (str): Reference a given .csv file.

    Returns:
        pandas.core.frame.DataFrame: Returns a pandas dataframe
    """
    import pandas as pd
    df = pd.read_csv(csv_file, header=None)
    return df

