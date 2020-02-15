from nose.tools import assert_equal


def sum_two(num1, num2):
    return num1 + num2

class test_solution(object):
    def test(self, sol):
        assert_equal(sol(2, 2), 4)
        assert_equal(sol(4, 4), 8)
        print('all test cases passed')

t=test_solution()
t.test(sum_two)
