import os
from read_text import read_text_from_pages
import table_text_to_df

def extract_and_save_tables(pdf_path):

    # Define page ranges for each table
    table_pages = {
        "4-24": (2, 8),
        "4-25": (8, 11),  
        "4-26": (11, 11)   
    }
    
    for table_name, (start_page, end_page) in table_pages.items():
        text = read_text_from_pages(pdf_path, start_page, end_page)
        df = table_text_to_df.table_text_to_df(text)
        csv_path = os.path.join("Rapido/data/", f"{table_name}.csv")
        df.to_csv(csv_path, index=False)
        print(f"Saved {csv_path}")

# Path to the PDF file
pdf_path = 'Rapido/data/MAN_32-40_Troubleshooting_Guide.pdf'
extract_and_save_tables(pdf_path)
