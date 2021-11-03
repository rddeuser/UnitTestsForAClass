"""
Program: students_unit_test
Author: Becca Deuser
Last date modified: 11/02/2021

The purpose of this program is to test the student class
"""

import unittest
from class_definitions.student import Student


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = Student('Geller', 'Monica', 'culinary')

    def tearDown(self):
        del self.student

    def test_object_create_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Geller')
        self.assertEqual(self.student.first_name, 'Monica')
        self.assertEqual(self.student.major, 'culinary')

    def test_object_all_attributes(self):
        test_student = Student('Bing', 'Chandler', 'finance', 3.0)
        assert test_student.last_name == 'Bing'
        assert test_student.first_name == 'Chandler'
        assert test_student.major == 'finance'
        assert test_student.gpa == 3.0

    def test_student_str(self):
        self.assertEqual(str(self.student), 'Geller, Monica has major culinary with gpa: 0.0')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            test_student = Student('1234', 'Chandler', 'finance')

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            test_student = Student('Bing', '1234', 'finance')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            test_student = Student('Bing', 'Chandler', '1234')

    def test_object_not_created_error_gpa_non_numeric(self):
        with self.assertRaises(ValueError):
            test_student = Student('Bing', 'Chandler', 'finance', 'three point two')

    def test_object_not_created_error_gpa_out_of_range(self):
        with self.assertRaises(ValueError):
            test_student = Student('Bing', 'Chandler', 'finance', 6)


if __name__ == '__main__':
    student1 = Student('Greene', 'Rachel', 'fashion design')
    student2 = Student('Geller', 'Ross', 'paleontology', 4.0)
    print(str(student1))
    print(str(student2))
