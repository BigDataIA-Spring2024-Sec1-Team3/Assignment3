import unittest
from utils.model_pdf_metadata import PDFMetadataClass
 
class TestPDFMetadataClassValidation(unittest.TestCase):    
# Pass test cases
    def test_valid_data(self):
        valid_data = {
            'text' : "test topic 1",
            'para' : 2021,
            'bboxes' : [[{'page': '1', 'x': '84.00', 'y': '681.59', 'h': '136.31', 'w': '9.24'}]],
            'pages' : "('1', '1')",
            'section_title' : "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            'section_number' : 0.1,
            'paper_title' : "amework and Macro Consideration",
            'file_path' : "data/input/2024-l3-topics-combined-2.pdf"
        }
        self.assertTrue(PDFMetadataClass(**valid_data))
        
    def test_valid_para(self):
        valid_data = {
            'text' : "test topic 1",
            'para' : 1,
            'bboxes' : [[{'page': '1', 'x': '84.00', 'y': '681.59', 'h': '136.31', 'w': '9.24'}]],
            'pages' : "('1', '1')",
            'section_title' : "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            'section_number' : 0.1,
            'paper_title' : "amework and Macro Consideration",
            'file_path' : "data/input/2024-l3-topics-combined-2.pdf"
            }
        self.assertTrue(PDFMetadataClass(**valid_data))
        
    def test_valid_bboxes(self):
        valid_data = {
            'text' : "test topic 1",
            'para' : 1,
            'bboxes' : [[{'page': '1', 'x': '84.00', 'y': '681.59', 'h': '136.31', 'w': '9.24'}]],
            'pages' : "('1', '1')",
            'section_title' : "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            'section_number' : 0.1,
            'paper_title' : "amework and Macro Consideration",
            'file_path' : "data/input/2024-l3-topics-combined-2.pdf"
            }
        self.assertTrue(PDFMetadataClass(**valid_data))
        
    def test_invalid_para(self):
        # Invalid topic 
        invalid_para = {
            'text' : "test topic 1",
            'para' : "test",
            'bboxes' : [[{'page': '1', 'x': '84.00', 'y': '681.59', 'h': '136.31', 'w': '9.24'}]],
            'pages' : "('1', '1')",
            'section_title' : "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            'section_number' : 0.1,
            'paper_title' : "amework and Macro Consideration",
            'file_path' : "data/input/2024-l3-topics-combined-2.pdf"
            }
        with self.assertRaises(ValueError):
            PDFMetadataClass(**invalid_para)

    def test_invalid_section_number(self):
        # empty topic
        invalid_section_number = {
            'text' : "test topic 1",
            'para' : 2,
            'bboxes' : [[{'page': '1', 'x': '84.00', 'y': '681.59', 'h': '136.31', 'w': '9.24'}]],
            'pages' : "('1', '1')",
            'section_title' : "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            'section_number' : "test",
            'paper_title' : "amework and Macro Consideration",
            'file_path' : "./data/input/2024-l3-topics-combined-2.pdf"
            }
        with self.assertRaises(ValueError):
            PDFMetadataClass(**invalid_section_number)

    def test_invalid_level(self):
        # Invalid level
        invalid_level = {
            'text' : "test topic 1",
            'para' : 2021,
            'bboxes' : [[{'page': '1', 'x': '84.00', 'y': '681.59', 'h': '136.31', 'w': '9.24'}]],
            'pages' : "('1', '1')",
            'section_title' : "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            'section_number' : 0.1,
            'paper_title' : "amework and Macro Consideration",
            'file_path' : "./data/input/2024-l3-topics-combined-2.pdf"
        }
        with self.assertRaises(ValueError):
            PDFMetadataClass(**invalid_level)

    def test_missing_section(self):
        # Missing section
        missing_section = {
            'text' : "test topic 1",
            'para' : 2021,
            'bboxes' : [[{'page': '1', 'x': '84.00', 'y': '681.59', 'h': '136.31', 'w': '9.24'}]],
            'pages' : "('1', '1')",
            'section_title' : "",
            'section_number' : 0.1,
            'paper_title' : "amework and Macro Consideration",
            'file_path' : "./data/input/2024-l3-topics-combined-2.pdf"
        }
        with self.assertRaises(ValueError):
            PDFMetadataClass(**missing_section)


    def test_missing_pages(self):
        # Missing pages
        missing_topic_name = {
            'text' : "test topic 1",
            'para' : 2,
            'bboxes' : [[{'page': '1', 'x': '84.00', 'y': '681.59', 'h': '136.31', 'w': '9.24'}]],
            'pages' : None,
            'section_title' : "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            'section_number' : 0.1,
            'paper_title' : "amework and Macro Consideration",
            'file_path' : "./data/input/2024-l3-topics-combined-2.pdf"
        }
        with self.assertRaises(ValueError):
            PDFMetadataClass(**missing_topic_name)

    def test_paper_title(self):
        # test paper title
        paper_title = {
            'text' : "test topic 1",
            'para' : 1,
            'bboxes' : [[{'page': '1', 'x': '84.00', 'y': '681.59', 'h': '136.31', 'w': '9.24'}]],
            'pages' : "('1', '1')",
            'section_title' : "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            'section_number' : 0.1,
            'paper_title' : None,
            'file_path' : "./data/input/2024-l3-topics-combined-2.pdf"
        }
        with self.assertRaises(ValueError):
            PDFMetadataClass(**paper_title)

if __name__ == '__main__':
    unittest.main()