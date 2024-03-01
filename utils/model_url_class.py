import pandas as pd
from pydantic import BaseModel, validator, constr
from typing import Optional
from datetime import datetime
import nltk

file_path = '../data/input/csv-input-files/scraped_data.csv'
try:
    # Attempt to read the CSV with a specified delimiter (e.g., tab)
    data = pd.read_csv(file_path, delimiter='\t')
    print(data.head())
except Exception as e:
    print("Error reading the CSV file:", e)
    
class URLClass(BaseModel):
    topic_name: [str]
    year: Optional[int]
    level: Optional[str]
    introduction: Optional[str]
    learning_outcome: Optional[str]
    summary: Optional[str]
    summary_page_link: [constr(strict=True)]        # enforcing stricter URL validation
    pdf_file_Link: Optional[constr(strict=True)]    # enforcing stricter URL validation

    # Topic validation
    @validator("topic_name")
    def validate_topic_name(cls, topic):
        # If topic name starts with number of special character, it will be invalid and raise error
        if not topic[0].isalpha():
            raise ValueError("Topic name cannot start with a number or special character.")

        # check if it is test refresher reading
        test_topic = topic.find("TEST RR")
        if test_topic != -1:    # if test topic found, it returns index
            raise ValueError("Invalid topic. Refresher reading is for test.")

        return topic
    
    # Year validation
    @validator('year')
    def year_must_not_be_from_future(cls, year):
        #Skip validation for None or empty strings
        if year in [None, '', 'NaN']:
            return None

        # check if the year is future year
        current_year = datetime.now().year
        if not (year <= current_year):
            raise ValueError('Year field cannot have future year')
        return year

    # level validation
    @validator('level')
    def cfa_level_validation(cls, level):
        #Skip validation for None or empty strings
        if level in [None, '', 'Nan']:
            return None
        
        # if CFA level is not I, II or III, it is invalid
        if level not in ['I','II','III']:
            raise ValueError('Invalid CFA level')
        
        return level

    # Introduction, Learning Outcome, Summary validation
    @validator("introduction", "learning_outcome", "summary")
    def sentence_completeness_check(cls, paragraph):
        #Skip validation for None or empty strings
        if paragraph in [None, '', 'Nan']:
            return None
        
        # If the sentence is not complete in paragraph
        sentences = nltk.sent_tokenize(paragraph)
        if not all(sentence.endswith(".") or sentence.endswith(";") or sentence.endswith(":") for sentence in sentences):
            raise ValueError("Introduction/Learning Outcome/Summary should consist of complete sentences.")
        return paragraph
    
    # summary page link validation
    @validator('summary_page_link')
    def summary_page_must_start_with_valid_url(cls, summary_page_url):
        # website url should start with https://
        if not summary_page_url.startswith("https://www.cfainstitute.org/en/membership/professional-development/refresher-readings"):
            raise ValueError('URL must start with a specific URL prefix')
        
        # Check for both leading and trailing spaces
        if summary_page_url.strip() != summary_page_url:
            raise ValueError("URL must not contain leading or trailing spaces.")
        
        return summary_page_url
    
    # pdf link validation
    @validator('pdf_page_link')
    def pdf_link_start_end_check(cls, pdf_link_url):
        #Skip validation for None or empty strings
        if pdf_link_url in [None, '', 'Nan']:
            return None
        
        # Check for both leading and trailing spaces
        if pdf_link_url.strip() != pdf_link_url:
            raise ValueError("URL must not contain leading or trailing spaces.")
        
        #pdf url should end with .pdf
        if not pdf_link_url.startswith("https://www.cfainstitute.org/-/media/documents/protected/refresher-reading") and not pdf_link_url.endswith(".pdf"):
            raise ValueError("PDF must start with a specific URL prefix and end with the .pdf extension")
        
        return pdf_link_url