import unittest
from AnnoyingHackJsonConverter import convert_to_json


class ClassNotADict:
    prop_number:int
    prop_string:str
    prop_boolean:bool
    def __init__(self, num:int, string:str, boolean:bool) -> None:
        self.prop_number = num
        self.prop_string = string
        self.prop_boolean = boolean
        
        

class TestAnnoyingHackJsonConverter(unittest.TestCase):
    def test_convert_dict(self):
        test_obj = {
            "prop_number": 1,
            "prop_string": "two",
            "prop_boolean": True
        }
        expected = """{
    "prop_number": 1,
    "prop_string": "two",
    "prop_boolean": true
}"""
        actual = convert_to_json(test_obj)
        self.assertEqual(actual, expected)
    def test_convert_class(self):
        test_obj = ClassNotADict(1, "two", True)
        expected = """{
    "prop_number": 1,
    "prop_string": "two",
    "prop_boolean": true
}"""
        actual = convert_to_json(test_obj)
        self.assertEqual(actual, expected)
    def test_convert_class_no_indent(self):
        test_obj = ClassNotADict(1, "two", True)
        expected = """{"prop_number": 1, "prop_string": "two", "prop_boolean": true}"""
        actual = convert_to_json(test_obj, None)
        self.assertEqual(actual, expected)
