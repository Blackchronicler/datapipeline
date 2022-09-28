import unittest
from main import calc_propotion


class TestQueryData(unittest.TestCase):

    def test_get_proportion(self):
        langs_bytes = [('Java', 33677705), ('Jupyter Notebook', 27919419), ('Python', 5164443), ('C++', 4186372),
                       ('Starlark', 1409831), ('JavaScript', 991790), ('C', 250514), ('CSS', 98860), ('Shell', 85534),
                       ('Ruby', 78218), ('CMake', 70457), ('Rust', 68368), ('Thrift', 39026), ('Kotlin', 25953),
                       ('Lex', 14469), ('Batchfile', 9238), ('Makefile', 9170), ('Smalltalk', 5432),
                       ('PowerShell', 3000), ('HTML', 2613), ('Dockerfile', 2559), ('Gnuplot', 1261)]
        proportion = calc_propotion.get_proportion(langs_bytes=langs_bytes, lang="Java", total_bytes=74114232)
        self.assertEqual(454.4026712710185, proportion)

    def test_get_total_proportion(self):
        total = calc_propotion.get_total_proportion(454.4026712710185, 454.4026712710185)
        self.assertEqual(908.805342542037, total)
