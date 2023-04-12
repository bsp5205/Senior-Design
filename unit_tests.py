import unittest
import mood
import main as m
import os
import javalang
import utilities as util

class TestMetrics(unittest.TestCase):

    def test_CC_cyclomatic(self):
        path = "TestAssignmentFiles/cyclomatic.java"
        self.assertEqual(m.calculate_McGabe_cyclomatic_complexity(create_tree(path)), [(3, 8), (4, 9), (5, 13)])

    def test_CC_DNA(self):
        path = "TestAssignmentFiles/DNA.java"
        self.assertEqual(m.calculate_McGabe_cyclomatic_complexity(create_tree(path)), [(5, 41), (9, 26)])

    def test_CC_DNA1(self):
        path = "TestAssignmentFiles/DNA1.java"
        self.assertEqual(m.calculate_McGabe_cyclomatic_complexity(create_tree(path)), [(2, 20)])

    def test_CC_DNA2(self):
        path = "TestAssignmentFiles/DNA2.java"
        self.assertEqual(m.calculate_McGabe_cyclomatic_complexity(create_tree(path)), [(2, 17)])

    def test_CC_DNA3(self):
        path = "TestAssignmentFiles/DNA3.java"
        self.assertEqual(m.calculate_McGabe_cyclomatic_complexity(create_tree(path)), [(1, 4), (1, 4), (16, 41), (3, 7), (2, 8), (2, 8)])

    def test_SLOC_cyclomatic(self):
        path = "TestAssignmentFiles/cyclomatic.java"
        self.assertEqual(m.calculate_SLOC(create_tree(path)), 32)

    def test_SLOC_DNA(self):
        path = "TestAssignmentFiles/DNA.java"
        self.assertEqual(m.calculate_SLOC(create_tree(path)), 69)

    def test_SLOC_DNA1(self):
        path = "TestAssignmentFiles/DNA1.java"
        self.assertEqual(m.calculate_SLOC(create_tree(path)), 22)

    def test_SLOC_DNA2(self):
        path = "TestAssignmentFiles/DNA2.java"
        self.assertEqual(m.calculate_SLOC(create_tree(path)), 19)

    def test_SLOC_DNA3(self):
        path = "TestAssignmentFiles/DNA3.java"
        self.assertEqual(m.calculate_SLOC(create_tree(path)), 76)

    def test_CP_cyclomatic(self):
        path = "TestAssignmentFiles/cyclomatic.java"
        concat_line, comment_count = util.read_file(path, 0)
        self.assertEqual(m.calculate_comment_percentage(create_tree(path), comment_count), 0.0)

    def test_CP_DNA(self):
        path = "TestAssignmentFiles/DNA.java"
        concat_line, comment_count = util.read_file(path, 0)
        self.assertEqual(m.calculate_comment_percentage(create_tree(path), comment_count), 33.33)

    def test_CP_DNA1(self):
        path = "TestAssignmentFiles/DNA1.java"
        concat_line, comment_count = util.read_file(path, 0)
        self.assertEqual(m.calculate_comment_percentage(create_tree(path), comment_count), 31.82)

    def test_CP_DNA2(self):
        path = "TestAssignmentFiles/DNA2.java"
        concat_line, comment_count = util.read_file(path, 0)
        self.assertEqual(m.calculate_comment_percentage(create_tree(path), comment_count), 36.84)

    def test_CP_DNA3(self):
        path = "TestAssignmentFiles/DNA3.java"
        concat_line, comment_count = util.read_file(path, 0)
        self.assertEqual(m.calculate_comment_percentage(create_tree(path), comment_count), 56.58)



def create_tree(path):
    concat_line, comment_count = util.read_file(path, 0)
    tree = javalang.parse.parse(concat_line)
    return tree

if __name__ == "__main__":
    unittest.main()