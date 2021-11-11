# %%
#######################################
def pandasget_dataframe_shape(data_frame: pandas.DataFrame):
    row_num, col_num = data_frame.shape
    print('The DataFrame contains...')
    print(f'\trows:  {row_num}')
    print(f'\tcols:  {col_num}')
    return data_frame.shape

