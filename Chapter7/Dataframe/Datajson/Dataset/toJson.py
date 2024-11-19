import pandas as p
import matplotlib as plt
# File path to the JSON file
file_path_json = '/Users/nyfong/coding/Python/Samsung_/Chapter7/Dataframe/Datajson/Dataset/universities_ranking.json'

# Read the JSON file into a DataFrame
df = p.read_json(file_path_json, orient='records')

# Display the first few rows
print(df.head(20))
