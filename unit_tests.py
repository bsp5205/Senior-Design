import unittest
import mood
import main as m
import os
import javalang
import utilities as util

class TestMetrics(unittest.TestCase):

    def test_CC_cyclomatic(self):
        path = "DNA_Holder/cyclomatic.java"
        self.assertEqual(m.calculate_McGabe_cyclomatic_complexity(create_tree(path)), [(3, 8), (4, 9), (5, 13)])

    def test_CC_DNA(self):
        path = "DNA_Holder/DNA.java"
        self.assertEqual(m.calculate_McGabe_cyclomatic_complexity(create_tree(path)), [(5, 41), (9, 26)])

    def test_CC_DNA1(self):
        path = "DNA_Holder/DNA1.java"
        self.assertEqual(m.calculate_McGabe_cyclomatic_complexity(create_tree(path)), [(2, 20)])

    def test_CC_DNA2(self):
        path = "DNA_Holder/DNA2.java"
        self.assertEqual(m.calculate_McGabe_cyclomatic_complexity(create_tree(path)), [(2, 17)])

    def test_CC_DNA3(self):
        path = "DNA_Holder/DNA3.java"
        self.assertEqual(m.calculate_McGabe_cyclomatic_complexity(create_tree(path)), [(1, 4), (1, 4), (16, 41), (3, 7), (2, 8), (2, 8)])

    def test_SLOC_cyclomatic(self):
        path = "DNA_Holder/cyclomatic.java"
        self.assertEqual(m.calculate_SLOC(create_tree(path)), 32)

    def test_SLOC_DNA(self):
        path = "DNA_Holder/DNA.java"
        self.assertEqual(m.calculate_SLOC(create_tree(path)), 69)

    def test_SLOC_DNA1(self):
        path = "DNA_Holder/DNA1.java"
        self.assertEqual(m.calculate_SLOC(create_tree(path)), 22)

    def test_SLOC_DNA2(self):
        path = "DNA_Holder/DNA2.java"
        self.assertEqual(m.calculate_SLOC(create_tree(path)), 19)

    def test_SLOC_DNA3(self):
        path = "DNA_Holder/DNA3.java"
        self.assertEqual(m.calculate_SLOC(create_tree(path)), 76)

    def test_CP_cyclomatic(self):
        path = "DNA_Holder/cyclomatic.java"
        concat_line, comment_count = util.read_file(path, 0)
        self.assertEqual(m.calculate_comment_percentage(create_tree(path), comment_count), 0.0)

    def test_CP_DNA(self):
        path = "DNA_Holder/DNA.java"
        concat_line, comment_count = util.read_file(path, 0)
        self.assertEqual(m.calculate_comment_percentage(create_tree(path), comment_count), 33.33)

    def test_CP_DNA1(self):
        path = "DNA_Holder/DNA1.java"
        concat_line, comment_count = util.read_file(path, 0)
        self.assertEqual(m.calculate_comment_percentage(create_tree(path), comment_count), 31.82)

    def test_CP_DNA2(self):
        path = "DNA_Holder/DNA2.java"
        concat_line, comment_count = util.read_file(path, 0)
        self.assertEqual(m.calculate_comment_percentage(create_tree(path), comment_count), 36.84)

    def test_CP_DNA3(self):
        path = "DNA_Holder/DNA3.java"
        concat_line, comment_count = util.read_file(path, 0)
        self.assertEqual(m.calculate_comment_percentage(create_tree(path), comment_count), 56.58)

    def test_WMC_cyclomatic(self):
        path = "DNA_Holder/cyclomatic.java"
        self.assertEqual(m.calculate_weighted_method_per_class(create_tree(path)), 12)
    def test_WMC_DNA(self):
        path = "DNA_Holder/DNA.java"
        self.assertEqual(m.calculate_weighted_method_per_class(create_tree(path)), 14)

    def test_WMC_DNA1(self):
        path = "DNA_Holder/DNA1.java"
        self.assertEqual(m.calculate_weighted_method_per_class(create_tree(path)), 2)

    def test_WMC_DNA2(self):
        path = "DNA_Holder/DNA2.java"
        self.assertEqual(m.calculate_weighted_method_per_class(create_tree(path)), 2)

    def test_WMC_DNA3(self):
        path = "DNA_Holder/DNA3.java"
        self.assertEqual(m.calculate_weighted_method_per_class(create_tree(path)), 25)

    def test_DIT_cyclomatic(self):
        path = "DNA_Holder/cyclomatic.java"
        self.assertEqual(m.calculate_depth_of_inheritance(create_tree(path)), 0)
    def test_DIT_DNA(self):
        path = "DNA_Holder/DNA.java"
        self.assertEqual(m.calculate_depth_of_inheritance(create_tree(path)), 0)

    def test_DIT_DNA1(self):
        path = "DNA_Holder/DNA1.java"
        self.assertEqual(m.calculate_depth_of_inheritance(create_tree(path)), 1)

    def test_DIT_DNA2(self):
        path = "DNA_Holder/DNA2.java"
        self.assertEqual(m.calculate_depth_of_inheritance(create_tree(path)), 1)

    def test_DIT_DNA3(self):
        path = "DNA_Holder/DNA3.java"
        self.assertEqual(m.calculate_depth_of_inheritance(create_tree(path)), 0)

    def test_AHF_cyclomatic(self):
        path = "DNA_Holder/cyclomatic.java"
        self.assertEqual(mood.calculate_attribute_hiding_factor(create_tree(path)), 0.0)
    def test_AHF_DNA(self):
        path = "DNA_Holder/DNA.java"
        self.assertEqual(mood.calculate_attribute_hiding_factor(create_tree(path)), 0.0)

    def test_AHF_DNA2(self):
        path = "DNA_Holder/DNA2.java"
        self.assertEqual(mood.calculate_attribute_hiding_factor(create_tree(path)), 0.3333333333333333)

    def test_MHF_cyclomatic(self):
        path = "DNA_Holder/cyclomatic.java"
        self.assertEqual(mood.calculate_method_hiding_factor(create_tree(path)), 0.0)
    def test_MHF_DNA(self):
        path = "DNA_Holder/DNA.java"
        self.assertEqual(mood.calculate_method_hiding_factor(create_tree(path)), 0.0)

    def test_MHF_DNA2(self):
        path = "DNA_Holder/DNA2.java"
        self.assertEqual(mood.calculate_method_hiding_factor(create_tree(path)), 0.0)

    def test_MIF_cyclomatic(self):
        path = "DNA_Holder/cyclomatic.java"
        self.assertEqual(mood.calculate_method_inheritance_factor(create_tree(path)), 0.25)
    def test_MIF_DNA(self):
        path = "DNA_Holder/DNA.java"
        self.assertEqual(mood.calculate_method_inheritance_factor(create_tree(path)), 0.8666666666666667)

    def test_MIF_DNA2(self):
        path = "DNA_Holder/DNA2.java"
        self.assertEqual(mood.calculate_method_inheritance_factor(create_tree(path)), 0.8333333333333334)

    def test_AIF_cyclomatic(self):
        path = "DNA_Holder/cyclomatic.java"
        self.assertEqual(mood.calculate_attribute_inheritance_factor(create_tree(path)), 0.0)
    def test_AIF_DNA(self):
        path = "DNA_Holder/DNA.java"
        self.assertEqual(mood.calculate_attribute_inheritance_factor(create_tree(path)), 1.0)

    def test_AIF_DNA2(self):
        path = "DNA_Holder/DNA2.java"
        self.assertEqual(mood.calculate_attribute_inheritance_factor(create_tree(path)), 0.25)

    def test_POF_cyclomatic(self):
        path = "DNA_Holder/cyclomatic.java"
        self.assertEqual(mood.calculate_polymorphism_factor(create_tree(path)), 0.0)
    def test_POF_DNA(self):
        path = "DNA_Holder/DNA.java"
        self.assertEqual(mood.calculate_polymorphism_factor(create_tree(path)), 0.0)

    def test_POF_DNA2(self):
        path = "DNA_Holder/DNA2.java"
        self.assertEqual(mood.calculate_polymorphism_factor(create_tree(path)), 0.0)

    def test_COF_cyclomatic(self):
        path = "DNA_Holder/cyclomatic.java"
        self.assertEqual(mood.calculate_coupling_factor(create_tree(path)), 0.0)
    def test_COF_DNA(self):
        path = "DNA_Holder/DNA.java"
        self.assertEqual(mood.calculate_coupling_factor(create_tree(path)), 0.0)

    def test_COF_DNA2(self):
        path = "DNA_Holder/DNA2.java"
        self.assertEqual(mood.calculate_coupling_factor(create_tree(path)), 0.0)


def create_tree(path):
    concat_line, comment_count = util.read_file(path, 0)
    tree = javalang.parse.parse(concat_line)
    return tree


if __name__ == "__main__":
    unittest.main()