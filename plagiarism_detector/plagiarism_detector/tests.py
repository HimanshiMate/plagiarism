from django.test import TestCase
from .text_detection import detect_text_plagiarism

class TextDetectionTests(TestCase):
    def test_plagiarism_detection(self):
        text1 = "This is a test sentence."
        text2 = "This is a test sentence."
        result = detect_text_plagiarism(text1, text2)
        self.assertAlmostEqual(result, 1.0, places=1)

    def test_no_plagiarism_detection(self):
        text1 = "This is a test sentence."
        text2 = "This is a completely different sentence."
        result = detect_text_plagiarism(text1, text2)
        self.assertLess(result, 0.5)
