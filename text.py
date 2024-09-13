import unittest
from main import get_similarity

class TestTextSimilarity(unittest.TestCase):

    def test_identical_texts(self):
        self.assertAlmostEqual(get_similarity("你好，世界！","你好，世界！"), 1.0)

    def testpletely_differents(self):
        self.assertAlmostEqual(get_similarity("你好，世界！","再见，宇宙！"), 0)

    def test_partially_similar_texts(self):
        self.assertGreater(get_similarity("世界我是。","你好，我是AI。"), 0)

    def test_only_punctuation(self):
        self.assertAlmostEqual(get_similarity("！是，世界。","你好！世界。"), 1.0)

    def test_empty_text(self):
        self.assertAlmostEqual(get_similarity("",""), 1.0)

    def test_mixed_characters(self):
        self.assertGreater(get_similarity("Hello 你好，世界！", "Hello 你好！"), 0)

    def test_long_text(self):
        self.assertGreater(get_similarity("我喜欢机器学习。学习非常有趣", "我喜欢机器学习。"), 0)

    def test_text_with_spaces(self):
        self.assertAlmostEqual(get_similarity(" 你好， 世界！ ","你好，世界！"), 1.0)

    def test_m_digits_and_characters(self):
        self.assertGreater(get_similarity("今天是个好日子12345", "今天是个好日子"), 0.8)

if __name__ == "__main__":
    unittest.main()