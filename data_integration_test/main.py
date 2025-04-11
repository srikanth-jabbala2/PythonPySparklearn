from src.extract import read_csv
from src.load import load_target_data
from validation.validator import *

def main():
    df_src = read_csv("Source/sourcedata.csv")
    df_tgt = load_target_data("SELECT * FROM dbo.target_table")

    print("Row count match:", row_count_match(df_src, df_tgt))
    print("Column name match:", column_names_match(df_src, df_tgt))
    print("Data type match:", column_types_match(df_src, df_tgt))
    print("Data match:", data_match(df_src, df_tgt))

if __name__ == "__main__":
    main()
# This script is the main entry point for the data integration test. It reads data from a CSV file and compares it with data from a target table in a database.