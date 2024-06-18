from extract_pdf import *
import os 
import csv
import pandas as pd
import re
import PyPDF2

current_dir= os.getcwd()
parent_dir = os.path.dirname(current_dir)

file1 = f"{parent_dir}/UTS-Hackathon/MAN_32-40_IMO_TierIII–Marine_.pdf"
file2 = f"{parent_dir}/UTS-Hackathon/MAN_32-40_Troubleshooting_Guide.pdf"
alertfile = f"{parent_dir}/UTS-Hackathon/ALARMS.xlsx"


                 
def remove_numbers(text):
    return ''.join([char for char in text if not char.isdigit()])

def remove_non_alpha(text):
    return ''.join([char for char in text if char.isalpha() or char.isspace()])



def retrieve_info_to_dataframe(data, text, causes, page_num):
    lines = text.splitlines() 
    
    '''
    for cause in causes:
        new = [line for line in lines if cause.lower() in line.lower()]
        data.extend(new)
    if page_num % 50 == 0 :
        print(data)
    '''

    
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    
    for cause in causes:
         # Filter paragraphs containing the word "bearing" 
        bearing_paragraphs = [p for p in paragraphs if cause.lower() in p.lower()]
        data.extend(bearing_paragraphs)
    
    if page_num % 50 == 0 :
        print(data)
    return data

if __name__ == '__main__':
    alerts = pd.read_excel(alertfile)
    cause = pd.read_excel(f"{current_dir}/BEARING_causes.xlsx")
    print(cause['Description'])
    subsystems = alerts['SUBSYSTEM'].unique()
    data = []
    with open(file1, 'rb') as file:
        for page_num in range(11, number_pages(file)) :
            print(f"Searching page : {page_num}")
            page = read_page(file, page_num)
            data = retrieve_info_to_dataframe(data, page, cause['Description'], page_num)
    print(data)

    #pdf_to_html(file1, "pdf.html")
            


