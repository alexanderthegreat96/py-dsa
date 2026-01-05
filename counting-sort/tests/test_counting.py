import unittest
from array import array
from counting import counting_sort as sort_function


class TestCounting(unittest.TestCase):
    def test_signed_int_array(self):
        test_data = array(
            "i",
            [
                70,
                90,
                63,
                18,
                52,
                83,
                74,
                85,
                96,
                63,
                8,
                82,
                99,
                5,
                33,
                97,
                44,
                57,
                2,
                61,
                44,
            ],
        )
        result = array(
            "i",
            [
                2,
                5,
                8,
                18,
                33,
                44,
                44,
                52,
                57,
                61,
                63,
                63,
                70,
                74,
                82,
                83,
                85,
                90,
                96,
                97,
                99,
            ],
        )
        sort_function(test_data, min(test_data), max(test_data))
        self.assertEqual(test_data, result)

    def test_reverse_array(self):
        """Test sorting an array that's already sorted in reverse order."""
        test_data = array("i", [7, 6, 5, 4, 3, 2, 1])
        result = array("i", [1, 2, 3, 4, 5, 6, 7])
        sort_function(test_data, min(test_data), max(test_data))
        self.assertEqual(test_data, result)

    def test_sorted_array(self):
        test_data = array("i", range(1000, 0, -1))
        result = array("i", range(1, 1001))
        sort_function(test_data, min(test_data), max(test_data))
        self.assertEqual(test_data, result)

    def test_numbers_list(self):
        test_data = [77, 54, 51, 75, 42, 66, 81, 49]
        result = [42, 49, 51, 54, 66, 75, 77, 81]
        sort_function(test_data, min(test_data), max(test_data))
        self.assertEqual(test_data, result)

        test_data = [4725, 4586, 1330, 8792, 1594, 5729]
        result = [1330, 1594, 4586, 4725, 5729, 8792]
        sort_function(test_data, min(test_data), max(test_data))
        self.assertEqual(test_data, result)

    def test_reverse_list(self):
        test_data = list(range(7000, 0, -1))
        result = list(range(1, 7001))
        sort_function(test_data, min(test_data), max(test_data))
        self.assertEqual(test_data, result)

    def test_sorted_list(self):
        test_data = list(range(1, 1000))
        result = list(range(1, 1000))
        sort_function(test_data, min(test_data), max(test_data))
        self.assertEqual(test_data, result)

    def test_empty_array(self):
        test_data = array("i")
        result = array("i")
        sort_function(test_data, 0, 0)
        self.assertEqual(test_data, result)

    def test_empty_list(self):
        test_data = []
        result = []
        sort_function(test_data, 0, 0)
        self.assertEqual(test_data, result)

    def test_long_array(self):
        test_data = array("l", [20, 35, 15, 7, 55, 1, 22])
        result = array("l", [1, 7, 15, 20, 22, 35, 55])
        sort_function(test_data, min(test_data), max(test_data))
        self.assertEqual(test_data, result)

    def test_negative_long_array(self):
        test_data = array(
            "l",
            [
                55,
                43,
                21,
                15,
                10,
                1,
                11,
                41,
                32,
                34,
                41,
                46,
                46,
                50,
                58,
                66,
                75,
                79,
                87,
                92,
            ],
        )
        result = array(
            "l",
            [
                1,
                10,
                11,
                15,
                21,
                32,
                34,
                41,
                41,
                43,
                46,
                46,
                50,
                55,
                58,
                66,
                75,
                79,
                87,
                92,
            ],
        )
        sort_function(test_data, min(test_data), max(test_data))
        self.assertEqual(test_data, result)

    def test_float_array(self):
        test_data = array(
            "f",
            [
                22.611,
                39.861,
                28.622,
                34.486,
                37.547,
                23.979,
                42.834,
                53.765,
                72.946,
                38.882,
                24.268,
                73.459,
                53.261,
                47.42,
                78.628,
                25.842,
                34.07,
                51.227,
                61.251,
                23.765,
            ],
        )

        with self.assertRaises(TypeError):
            sort_function(test_data, min(test_data), max(test_data))

    def test_string_list(self):
        test_data = [
            "Earth",
            "Mars",
            "Jupiter",
            "Saturn",
            "Mercury",
            "Venus",
            "Uranus",
            "Neptune",
            "Pluto",
        ]
        with self.assertRaises(TypeError):
            sort_function(test_data, min(test_data), max(test_data))

    def test_long_reverse_sorted_list(self):
        test_data = list(range(9999, 0, -1))
        result = list(range(1, 10000))
        sort_function(test_data, min(test_data), max(test_data))
        self.assertEqual(test_data, result)

    def test_constant_char_list(self):
        test_data = list("A" * 10000)
        with self.assertRaises(TypeError):
            sort_function(test_data, min(test_data), max(test_data))

    def test_constant_int_list(self):
        test_data = list([12] * 10000)
        result = list([12] * 10000)
        sort_function(test_data, min(test_data), max(test_data))
        self.assertEqual(test_data, result)

    def test_single_element_list(self):
        test_data = [12]
        result = [12]
        sort_function(test_data, min(test_data), max(test_data))
        self.assertEqual(test_data, result)

    def test_zzz_known_bad_case(self):
        test_data = [1, 3, 2, 4, 3, 2, 1]
        result = [1, 1, 2, 2, 3, 3, 4]
        sort_function(test_data, min(test_data), max(test_data))
        self.assertEqual(test_data, result)
