# %%
#######################################
def pandasread_csv_addheader(csv_file: str, addheader: list):
    """Returns a pandas dataframe from the given .csv file.  Assumes there is no header in the .csv and requires a header to be given as an argument to the 'addheader'.

    Example:
        >>> myheader = ['NAME','AGE','JOB','DEPARTMENT','PAY']\n
        >>> pandasread_csv_addheader('test.csv', addheader=myheader)\n
            NAME  AGE         JOB          DEPARTMENT  PAY\n
        0    bob   21     janitor   sanitization team    2\n
        1  alice   22   secretary          admin team    3\n
        2  chuck   23     plumber   construction team    4\n

    Reference:
        https://stackoverflow.com/questions/36828348/pandas-read-csv-reading-a-csv-file-with-a-missing-header-element

    Args:
        csv_file (str): Reference an existing .csv file.
        addheader (list): Reference the header you want to use for the columns.

    Returns:
        pandas.core.frame.DataFrame: Returns a pandas dataframe.
    """
    import pandas
    df = pandas.read_csv(csv_file, header=None, names=addheader)
    return df

