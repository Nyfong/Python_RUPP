import pandas as p

file_path_csv = '/Users/nyfong/coding/Python/Samsung_/Chapter7/Dataframe/Data/titanic/test.csv'
file_path_xls = '/Users/nyfong/coding/Python/Samsung_/Chapter7/Dataframe/Data/titanic/train.xlsx'

try:
    # Read CSV
    df = p.read_csv(file_path_csv)
    print("CSV file loaded successfully!")
    print(df.head())
except Exception as e:
    print(f"Error reading CSV: {e}")

try:
    # Read XLS
    df1 = p.read_excel(file_path_xls)
    print("XLSX file loaded successfully!")
    print(df1.head())
except Exception as e:
    print(f"Error reading XLS: {e}")
