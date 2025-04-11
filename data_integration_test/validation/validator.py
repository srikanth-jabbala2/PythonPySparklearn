def row_count_match(df_source, df_target):
    return len(df_source) == len(df_target)

def column_names_match(df_source, df_target):
    return list(df_source.columns) == list(df_target.columns)

def column_types_match(df_source, df_target):
    return all(df_source.dtypes[col] == df_target.dtypes[col] for col in df_source.columns)

def data_match(df_source, df_target):
    return df_source.equals(df_target)