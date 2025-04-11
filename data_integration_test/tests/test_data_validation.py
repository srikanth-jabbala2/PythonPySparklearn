from src.extract import read_csv
from src.load import load_target_data
from validation.validator import row_count_match, column_names_match, column_types_match, data_match

def test_row_count():
    df_src = read_csv('data/source_data.csv')
    df_tgt = load_target_data("select * from dbo.target_table")
    assert row_count_match(df_src, df_tgt), "Row count does not match between source and target."

def test_columns():
    df_src= read_csv('data/source_data.csv')
    df_tgt = load_target_data("select * from dbo.target_table")
    assert column_names_match(df_src, df_tgt), "Column names do not match between source and target."

def test_column_types():
    df_src = read_csv('data/source_data.csv')
    df_tgt = load_target_data("select * from dbo.target_table")
    assert column_types_match(df_src, df_tgt), "Column types do not match between source and target."

def test_data():
    df_src = read_csv('data/source_data.csv')
    df_tgt = load_target_data("select * from dbo.target_table")
    assert data_match(df_src, df_tgt), "Data does not match between source and target."
# The above code is a set of unit tests for validating data integration processes.