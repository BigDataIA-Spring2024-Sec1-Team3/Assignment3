import pandas as pd
from pydantic import BaseModel, HttpUrl, Field, validator, constr, ValidationError, field_validator
import re
from typing import Optional
from datetime import datetime

class URLClass(BaseModel):
    topic_name: Optional[str]=Field(default=None)
    year: Optional[int]=Field(default=None)
    level: Optional[str]=Field(default=None)
    introduction: Optional[str]=Field(default=None)
    learning_outcome: Optional[str]=Field(default=None)
    summary: Optional[str]=Field(default=None)
    summary_page_link: Optional[str]=Field(default=None)
    pdf_file_link: Optional[str]=Field(default=None)
    
    # Topic validation
    @field_validator("topic_name")
    def validate_topic_name(cls, topic):
        # if topic is empty, raise error
        if topic in [None, '', 'NaN']:
            raise ValueError("Topic cannot be None or Empty")
        
        # If topic name starts with number of special character, it will be invalid and raise error
        pattern = r'[a-zA-Z]+'
        # Use re.match to check if the pattern matches the start of the string
        match = re.match(pattern, topic)
        if not match:
            raise ValueError("Topic name cannot start with a number or special character.")

        # check if it is test refresher reading
        test_topic = topic.upper().find("TEST RR")
        
        # print("Topic: ",topic,"Test topic:",test_topic)
        if test_topic != -1:    # if test topic found, it returns index
            raise ValueError("Invalid topic. Refresher reading is for test.")

        return topic
    
    # Year validation
    @field_validator('year')
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
    @field_validator('level')
    def cfa_level_validation(cls, level):
        #Skip validation for None or empty strings
        if level in [None, '', 'Nan']:
            return None
        
        # if CFA level is not I, II or III, it is invalid
        if level not in ['I','II','III']:
            raise ValueError('Invalid CFA level')
        
        return level
    
    # summary page link validation
    @field_validator('summary_page_link')
    def summary_page_must_start_with_valid_url(cls, summary_page_url):
        # if summary website url is empty, raise error
        if summary_page_url in [None, '', 'NaN']:
            raise ValueError("summary website url cannot be None or Empty")
        
        # website url should start with https://
        if not summary_page_url.startswith("https://www.cfainstitute.org/membership/professional-development/refresher-readings"):
            raise ValueError('URL must start with a specific URL prefix')
        
        # Check for spaces in url
        if " " in summary_page_url:
            raise ValueError("URL cannot contain spaces.")
        
        return summary_page_url
    
    # pdf link validation
    @field_validator('pdf_file_link')
    def pdf_link_start_end_check(cls, pdf_link_url):
        #Skip validation for None or empty strings
        if pdf_link_url in [None, '', 'Nan']:
            return None
        
        # Check for both leading and trailing spaces
        if pdf_link_url.strip() != pdf_link_url:
            raise ValueError("URL must not contain leading or trailing spaces.")
        
        #pdf url should end with .pdf
        if not pdf_link_url.startswith("https://www.cfainstitute.org/-/media/documents/protected/refresher-reading") or not pdf_link_url.endswith(".pdf"):
            raise ValueError("PDF must start with a specific URL prefix and end with the .pdf extension")
        
        return pdf_link_url