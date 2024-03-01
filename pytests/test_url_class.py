import pytest
from model_url_class import URLClass
from pydantic import ValidationError

# Success tests with realistic test values
@pytest.mark.parametrize(
    "input_data, test_id",
    [
        ({
            "topic_name": "Equity Valuation",
            "year": 2021,
            "level": "II",
            "introduction": "This is an introduction.",
            "learning_outcome": "The outcome is learning.",
            "summary": "This is a summary.",
            "summary_page_link": "https://www.cfainstitute.org/en/membership/professional-development/refresher-readings",
            "pdf_file_Link": "https://www.cfainstitute.org/-/media/documents/protected/refresher-reading/document.pdf"
        }, 'pass_test_cases'),
    ],
)
def test_url_class_happy_path(input_data, test_id):
    # Act
    url_class_instance = URLClass(**input_data)

    # Assert
    assert url_class_instance.topic_name == input_data["topic_name"]
    assert url_class_instance.year == input_data["year"]
    assert url_class_instance.level == input_data["level"]
    assert url_class_instance.introduction == input_data["introduction"]
    assert url_class_instance.learning_outcome == input_data["learning_outcome"]
    assert url_class_instance.summary == input_data["summary"]
    assert url_class_instance.summary_page_link == input_data["summary_page_link"]
    assert url_class_instance.pdf_file_Link == input_data["pdf_file_Link"]

# Edge cases
@pytest.mark.parametrize(
    "input_data, test_id",
    [
        ({
            "topic_name": "2Equity Valuation",  # starts with a number
        }, 'edge_case_topic_name_1'),
        # Add more test cases as needed
    ],
)
def test_url_class_edge_cases(input_data, test_id):
    # Act & Assert
    with pytest.raises(ValidationError):
        URLClass(**input_data)

# Error cases
@pytest.mark.parametrize(
    "input_data, expected_exception, test_id",
    [
        ({
            "topic_name": "2Equity Valuation",  # starts with a number
        }, ValueError, 'error_case_topic_name_1'),
        ({
            "year": 3000,  # future year
        }, ValueError, 'error_case_year_1'),
        ({
            "level": "IV",  # invalid level
        }, ValueError, 'error_case_level_1'),
        ({
            "introduction": "This is an incomplete sentence",  # incomplete sentence
        }, ValueError, 'error_case_introduction_1'),
        ({
            "summary_page_link": "http://invalid-link.com",  # invalid URL
        }, ValueError, 'error_case_summary_page_link_1'),
        ({
            "pdf_file_Link": "http://invalid-link.com/document.doc",  # invalid PDF URL
        }, ValueError, 'error_case_pdf_file_Link_1'),
        # Add more test cases as needed
    ],
)
def test_url_class_error_cases(input_data, expected_exception, test_id):
    # Act & Assert
    with pytest.raises(expected_exception):
        URLClass(**input_data)
