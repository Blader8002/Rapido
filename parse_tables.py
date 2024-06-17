import re

def parse_tables(text):
    tables = {}
    table_patterns = {
        "4-24": r"Table 4-24:.*?(\n\s*\n)",
        "4-25": r"Table 4-25:.*?(\n\s*\n)",
        "4-26": r"Table 4-26:.*?(\n\s*\n)"
    }
    
    for table_name, pattern in table_patterns.items():
        match = re.search(pattern, text, re.DOTALL)
        if match:
            table_text = match.group(0)
            tables[table_name] = table_text
            
    return tables
