#Task 1

#Pick your solution to one of the exercises in this module. Design tests for this solution and write tests using unittest library. 

import unittest

def calculate_wage(rate: float, hour: float) -> float:
    if hour <= 40:
        return hour * rate
    else:
        return 40 * rate + (hour - 40) * 1.5 * rate

class TestCalculateWage(unittest.TestCase):

    def test_regular_hours(self):
        self.assertEqual(calculate_wage(10.0, 35.0), 350.0)

if __name__ == '__main__':
    unittest.main()
