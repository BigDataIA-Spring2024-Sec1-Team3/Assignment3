import unittest
from utils.model_pdf_content import PDFContentClass
import nltk
nltk.download('punkt')


class TestPDFContentClassValidation(unittest.TestCase):    
# Pass test cases
    def test_valid_topic(self):
        valid_data = {
            "title": "Title",
            "topic_name": "Balance sheet",
            "year": 2022,
            "level": "1",
            "learning_outcome": "Complete Learning Outcome."
        }
        self.assertTrue(PDFContentClass(**valid_data))
        
    def test_valid_level(self):
        # Test valid level
        valid_data = {
            "title": "Economics",
            "topic_name": "Currency Exchange Rates: Understanding Equilibrium Value",
            "year": 2024,
            "level": "2",
            "learning_outcome": "Complete Learning Outcome."
            }
        self.assertTrue(PDFContentClass(**valid_data))
        
    def test_valid_year(self):
        # Invalid year
        valid_data = {
            "title": "Economics",
            "topic_name": "Currency Exchange Rates: Understanding Equilibrium Value",
            "year": 2001,
            "level": "2",
            "learning_outcome": "Complete Learning Outcome."
            }
        self.assertTrue(PDFContentClass(**valid_data))
        
    def test_invalid_topic(self):
        # Invalid topic 
        invalid_topic = {
            "title": "Economics",
            "topic_name": "$Invalid Topic",
            "year": 2021,
            "level": "1",
            "learning_outcome": "Complete Learning Outcome."
            }
        with self.assertRaises(ValueError):
            PDFContentClass(**invalid_topic)

    def test_empty_topic(self):
        # empty topic
        empty_topic = {
            "title": None,
            "topic_name": None,
            "year": None,
            "level": "",
            "learning_outcome": ""
            }
        with self.assertRaises(ValueError):
            PDFContentClass(**empty_topic)

    def test_invalid_level(self):
        # Invalid level
        invalid_level = {
            "title": "Derivatives",
            "topic_name": "Pricing and Valuation of Forward Commitments",
            "year": 2023,
            "level": "4", 
            "learning_outcome": "Complete Learning Outcome."
        }
        with self.assertRaises(ValueError):
            PDFContentClass(**invalid_level)

    def test_missing_title(self):
        # Missing title
        missing_title = {
            "topic_name": "Pricing and Valuation of Forward Commitments",
            "level": "1",
            "year": 2023,
            "learning_outcome": "Complete Learning Outcome."
        }
        with self.assertRaises(ValueError):
            PDFContentClass(**missing_title)


    def test_missing_learning_outcome(self):
        # Missing topic_name
        missing_topic_name = {
            "title": "Derivatives",
            "year": 2023,
            "level": "1",
            "learning_outcome": "Complete Learning Outcome."
        }
        with self.assertRaises(ValueError):
            PDFContentClass(**missing_topic_name)

    def test_empty_title(self):
        # Empty title
        empty_title = {
            "title": "",  # Empty title
            "topic_name": "Pricing and Valuation of Forward Commitments",
            "year": 2023,
            "level": "2",
            "learning_outcome": "Complete Learning Outcome."
        }
        with self.assertRaises(ValueError):
            PDFContentClass(**empty_title)

    def test_invalid_year_type(self):
        # Invalid year type (string)
        invalid_year_type = {
            "title": "Title",
            "topic_name": "Topic",
            "year": "2020",  # Year should be an integer
            "level": "1",
            "learning_outcome": "Learning Outcome."
        }
        with self.assertRaises(TypeError):
            PDFContentClass.year_must_not_be_from_future("2020")


if __name__ == '__main__':
    unittest.main()

