import pandas as pd
import re

def table_text_to_df(table_text):
    lines = table_text.strip().split('\n')
    data = []

    # Process each line
    for line in lines:
        # Use regular expression to split columns more accurately
        columns = re.split(r'\s{2,}', line.strip())
        data.append(columns)

    # Create DataFrame, handling cases where not all rows have the same number of columns
    max_cols = max(len(row) for row in data)
    df = pd.DataFrame(data, columns=[f'Column{i+1}' for i in range(max_cols)])
    
    return df
