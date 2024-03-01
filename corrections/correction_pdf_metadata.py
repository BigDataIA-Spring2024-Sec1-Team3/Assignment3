import pandas as pd
import numpy as np
from utils.model_pdf_metadata import PDFMetadataClass
import re
import csv
import roman
from pydantic import ValidationError

def validate_data(file_path, model):
    temp= []
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        # Assuming the delimiter is a comma, adjust if necessary
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                attempts=0
                while attempts<5:
                    try:
                        # passing the row to pydantic validation model
                        model_instance = model(**row)
                        
                        temp.append(model_instance.model_dump())
                        break
                    # if row couldn't bypass validation, we will try to correct the data based on the error raised
                    except Exception as e:
                        for error in e.errors():
                            column_name = error['loc'][0]
                            error_raised = error['msg']
                            if column_name=="text":
                                row[column_name] = None
                            if column_name=="para":
                                row[column_name] = None
                            if column_name=="bboxes":
                                row[column_name] = None
                            if column_name=="pages":
                                row[column_name] = None
                            if column_name=="section_title":
                                row[column_name] = None
                            if column_name=="section_number":
                                row[column_name] = None
                            if column_name=="paper_title":
                                row[column_name] = None
                            if column_name=="file_path":
                                row[column_name] = None
                        attempts+=1
            except KeyError as e:
                print(f"Error processing row: {e}")
            except ValidationError as e:
                print(f"Validation error: {e}")

    return temp

def clean_csv_generate():
    file_path = 'data/input/csv-input-files/pdf_metadata.csv'
    list_dict = validate_data(file_path, PDFMetadataClass)
    df_clean = pd.DataFrame(list_dict)
    clean_csv_location = 'data/output/clean_pdf_metadata.csv'
    df_clean.to_csv(clean_csv_location, header=True, index=False, sep="|", float_format='%d')
    print("Clean CSV file generated successfully.")
if __name__ == '__main__':
    clean_csv_generate()