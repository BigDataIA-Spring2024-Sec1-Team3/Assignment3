import unittest
from utils.model_url_class import URLClass 

class TestURLClassValidation(unittest.TestCase):    
# Pass test cases
    def test_valid_topic(self):
        # Valid URL and data
        valid_data = {
            "topic_name": "Balance sheet",
            "year": 2022,
            "level": "I",
            "introduction": "Complete Introduction.",
            "learning_outcome": "Complete Learning Outcome.",
            "summary": "Complete Summary.",
            "summary_page_link": "https://www.cfainstitute.org/membership/professional-development/refresher-readings/valid_summary",
            "pdf_file_link": "https://www.cfainstitute.org/-/media/documents/protected/refresher-reading/valid.pdf"
        }
        self.assertTrue(URLClass(**valid_data))
        
    def test_valid_level(self):
        # Valid URL and data
        valid_data = {
            "topic_name": "Finance Market",
            "year": 2022,
            "level": "II",
            "introduction": "Complete Introduction.",
            "learning_outcome": "Complete Learning Outcome.",
            "summary": "Complete Summary.",
            "summary_page_link": "https://www.cfainstitute.org/membership/professional-development/refresher-readings/valid_summary",
            "pdf_file_link": "https://www.cfainstitute.org/-/media/documents/protected/refresher-reading/valid.pdf"
        }
        self.assertTrue(URLClass(**valid_data))
        
    def test_valid_year(self):
        # Valid URL and data
        valid_data = {
            "topic_name": "Finance Market",
            "year": 2001,
            "level": "II",
            "introduction": "Complete Introduction.",
            "learning_outcome": "Complete Learning Outcome.",
            "summary": "Complete Summary.",
            "summary_page_link": "https://www.cfainstitute.org/membership/professional-development/refresher-readings/valid_summary",
            "pdf_file_link": "https://www.cfainstitute.org/-/media/documents/protected/refresher-reading/valid.pdf"
        }
        self.assertTrue(URLClass(**valid_data))
    
    def test_valid_website_url(self):
        # Valid URL and data
        valid_data = {
            "topic_name": "Finance Market",
            "year": 2022,
            "level": "II",
            "introduction": "Complete Introduction.",
            "learning_outcome": "Complete Learning Outcome.",
            "summary": "Complete Summary.",
            "summary_page_link": "https://www.cfainstitute.org/membership/professional-development/refresher-readings/valid-url",
            "pdf_file_link": "https://www.cfainstitute.org/-/media/documents/protected/refresher-reading/valid.pdf"
        }
        self.assertTrue(URLClass(**valid_data))
        
    def test_valid_pdf_url(self):
        # Valid URL and data
        valid_data = {
            "topic_name": "Finance Market",
            "year": 2000,
            "level": "II",
            "introduction": "Complete Introduction.",
            "learning_outcome": "Complete Learning Outcome.",
            "summary": "Complete Summary.",
            "summary_page_link": "https://www.cfainstitute.org/membership/professional-development/refresher-readings/valid_summary",
            "pdf_file_link": "https://www.cfainstitute.org/-/media/documents/protected/refresher-reading/finance.pdf"
        }
        self.assertTrue(URLClass(**valid_data))

# Fail test cases
    def test_invalid_pdf_url(self):
        # Valid URL but invalid data
        invalid_pdf = {
            "topic_name": "Finance data",
            "year": 2022,
            "level": "I",
            "introduction": None,
            "learning_outcome": None,
            "summary": None,
            "summary_page_link": "https://www.cfainstitute.org/membership/professional-development/refresher-readings/finance-data",
            "pdf_file_link": "https://www.cfainstitute.org/-/media/documents/protected/refresher-reading/invalid.csv"
        }
        with self.assertRaises(ValueError):
            URLClass(**invalid_pdf)

    def test_invalid_level(self):
        # Invalid URL but valid data
        invalid_level = {
            "topic_name": "Valid Topic",
            "year": 2023,
            "level": "IV",
            "introduction": "Complete Introduction.",
            "learning_outcome": "Complete Learning Outcome.",
            "summary": "Complete Summary.",
            "summary_page_link": "https://www.cfainstitute.org/membership/professional-development/refresher-readings/valid-summary",
            "pdf_file_link": "https://www.cfainstitute.org/-/media/documents/protected/refresher-reading/valid.pdf"
        }
        with self.assertRaises(ValueError):
            URLClass(**invalid_level)
        
    def test_invalid_topic(self):
        # Invalid URL and data
        invalid_topic = {
            "topic_name": "$Invalid Topic",
            "year": 2021,
            "level": "I",
            "introduction": "Complete Introduction.",
            "learning_outcome": "Complete Learning Outcome.",
            "summary": "Complete Summary.",
            "summary_page_link": "https://www.cfainstitute.org/membership/professional-development/refresher-readings/valid_summary",
            "pdf_file_link": "https://www.cfainstitute.org/-/media/documents/protected/refresher-reading/valid.pdf"
        }
        with self.assertRaises(ValueError):
            URLClass(**invalid_topic)

    def test_empty_topic(self):
        # Invalid URL and empty data
        empty_topic = {
            "topic_name": None,
            "year": None,
            "level": "",
            "introduction": "",
            "learning_outcome": "",
            "summary": "",
            "summary_page_link": "https://www.cfainstitute.org/membership/professional-development/refresher-readings/invalid_summary",
            "pdf_file_link": ""
        }
        with self.assertRaises(ValueError):
            URLClass(**empty_topic)

    def test_invalid_website_url_with_space(self):
        # Valid URL and empty data
        invalid_website_url = {
            "topic_name": "Equity",
            "year": None,
            "level": "",
            "introduction": "",
            "learning_outcome": "",
            "summary": "",
            "summary_page_link": "https://www.cfainstitute.org/membership/professional-development/refresher-readings/invalid url",
            "pdf_file_link": ""
        }
        with self.assertRaises(ValueError):
            URLClass(**invalid_website_url)

if __name__ == '__main__':
    unittest.main()