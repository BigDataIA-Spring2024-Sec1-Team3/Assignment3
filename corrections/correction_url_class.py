import pandas as pd
import numpy as np
from utils.model_url_class import URLClass
import re
import csv

def correct_topic_value(error_raised, topic_name):
    if error_raised=="Topic cannot be None or Empty":
        return 
    if error_raised=="Topic name cannot start with a number or special character.":
        pattern = r'^[\d\W_]+'
        # Use re.sub to replace the matched pattern with an empty string
        stripped_topic_name = re.sub(pattern, '', topic_name)
        return stripped_topic_name
    if error_raised=="Invalid topic. Refresher reading is for test.":
        return
       
def validate_data(file_path, model):
    temp= []
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        # Assuming the delimiter is a comma, adjust if necessary
        reader = csv.DictReader(csvfile, delimiter='\t')
        for _, row in enumerate(reader, start=1):
            attempts=0
            while attempts<5:
                try:
                    # passing the row to pydantic validation model
                    model_instance = model(**row)
                    # print(model_instance.model_dump()["year"])
                    
                    temp.append( model_instance.model_dump())
                    break
                # if row couldn't bypass validation, we will try to correct the data based on the error raised
                except Exception as e:
                    for error in e.errors():
                        column_name = error['loc'][0]
                        error_raised = error['msg']
                        if column_name=="topic_name":
                            modified_value=correct_topic_value(error_raised, row[column_name])
                            if not modified_value:
                                break
                        if column_name=="year":
                            row[column_name] = None
                        if column_name=="level":
                            row[column_name] = row[column_name].strip()
                        if column_name=="summary_page_link":
                            break
                        if column_name=="pdf_file_link":
                            row[column_name] = None 
                    attempts+=1
    return temp
                                       
                
        
def clean_csv_generate():
    file_path = 'data\input\csv-input-files\scraped_data.csv'
    list_dict = validate_data(file_path, URLClass)
    df_clean = pd.DataFrame(list_dict)

    clean_csv_location = 'data\output\clean_url_class.csv'
    df_clean.to_csv(clean_csv_location, header=True, index=False, sep="\t", float_format='%d')

if __name__ == '__main__':
    clean_csv_generate()


