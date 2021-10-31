# %%
#######################################
def pandasread_csv(csv_file: str):
    """Returns a pandas dataframe from the given .csv file.  Assumes there is no header in the .csv.

    Example:
        >>> pandasread_csv('brandnew.csv')\n
            NAME  AGE         JOB          DEPARTMENT  PAY\n
        0    bob   21     janitor   sanitization team    2\n
        1  alice   22   secretary          admin team    3\n
        2  chuck   23     plumber   construction team    4\n

    Reference:
        https://www.geeksforgeeks.org/python-read-csv-using-pandas-read_csv/

    Args:
        csv_file (str): Reference a given .csv file.

    Returns:
        pandas.core.frame.DataFrame: Returns a pandas dataframe
    """
    import pandas as pd
    df = pd.read_csv(csv_file)
    return df

