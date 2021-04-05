#!/usr/bin/env python

import pytest

"""
Test 1656: design_an_ordered_stream
"""


@pytest.fixture(scope="session")
def init_variables_1656():
    from src.array_problems.design_an_ordered_stream import OrderedStream

    ordered_stream = OrderedStream(5)

    def _init_variables_1656():
        return ordered_stream

    yield _init_variables_1656


class TestClass1656:
    def test_solution_0(self, init_variables_1656):
        assert not init_variables_1656().insert(3, "ccccc")

    def test_solution_1(self, init_variables_1656):
        assert init_variables_1656().insert(1, "aaaaa") == ["aaaaa"]

    def test_solution_2(self, init_variables_1656):
        assert init_variables_1656().insert(2, "bbbbb") == ["bbbbb", "ccccc"]

    def test_solution_3(self, init_variables_1656):
        assert not init_variables_1656().insert(5, "eeeee")

    def test_solution_4(self, init_variables_1656):
        assert init_variables_1656().insert(4, "ddddd") == ["ddddd", "eeeee"]


"""
Test 1646: get_maximum_in_generated_array
"""


@pytest.fixture(scope="session")
def init_variables_1646():
    from src.array_problems.get_maximum_in_generated_array import Solution

    solution = Solution()

    def _init_variables_1646():
        return solution

    yield _init_variables_1646


class TestClass1646:
    def test_solution_0(self, init_variables_1646):
        assert init_variables_1646().get_maximum_generated(7) == 3

    def test_solution_1(self, init_variables_1646):
        assert init_variables_1646().get_maximum_generated(2) == 1

    def test_solution_2(self, init_variables_1646):
        assert init_variables_1646().get_maximum_generated(3) == 2


"""
Test 1672: richest_costumer_wealth
"""


@pytest.fixture(scope="session")
def init_variables_1672():
    from src.array_problems.richest_costumer_wealth import Solution

    solution = Solution()

    def _init_variables_1672():
        return solution

    yield _init_variables_1672


class TestClass1672:
    def test_solution_0(self, init_variables_1672):
        assert init_variables_1672().maximum_wealth([[1, 2, 3], [3, 2, 1]]) == 6

    def test_solution_1(self, init_variables_1672):
        assert init_variables_1672().maximum_wealth([[1, 5], [7, 3], [3, 5]]) == 10

    def test_solution_2(self, init_variables_1672):
        assert (
            init_variables_1672().maximum_wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]])
            == 17
        )


"""
Test 1674: minimum_moves_to_make_array_complementary
"""


@pytest.fixture(scope="session")
def init_variables_1674():
    from src.array_problems.minimum_moves_to_make_array_complementary import Solution

    solution = Solution()

    def _init_variables_1674():
        return solution

    yield _init_variables_1674


class TestClass1674:
    def test_solution_0(self, init_variables_1674):
        assert init_variables_1674().min_moves([1, 2, 4, 3], 4) == 1

    def test_solution_1(self, init_variables_1674):
        assert init_variables_1674().min_moves([1, 2, 2, 1], 2) == 2

    def test_solution_2(self, init_variables_1674):
        assert init_variables_1674().min_moves([1, 2, 1, 2], 2) == 0


"""
Test 1695. Maximum Erasure Value
"""


@pytest.fixture(scope="session")
def init_variables_1695():
    from src.array_problems.maximum_array_erase_value import Solution

    solution = Solution()

    def _init_variables_1695():
        return solution

    yield _init_variables_1695


class TestClass1695:
    def test_solution_0(self, init_variables_1695):
        assert init_variables_1695().maximum_unique_subarray([4, 2, 4, 5, 6]) == 17

    def test_solution_1(self, init_variables_1695):
        assert (
            init_variables_1695().maximum_unique_subarray([5, 2, 1, 2, 5, 2, 1, 2, 5])
            == 8
        )


"""
Test 1744. Can You Eat Your Favorite Candy on Your Favorite Day?
"""


@pytest.fixture(scope="session")
def init_variables_1744():
    from src.array_problems.can_you_eat_your_favorite_candy_on_your_favorite_day import Solution

    solution = Solution()

    def _init_variables_1744():
        return solution

    yield _init_variables_1744


class TestClass1744:
    def test_solution_0(self, init_variables_1744):
        assert init_variables_1744().can_eat(
            [7, 4, 5, 3, 8], [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]
        ) == [True, False, True]


"""
Test 1742. Maximum Number of Balls in a Box
"""


@pytest.fixture(scope="session")
def init_variables_1742():
    from src.array_problems.maximum_number_of_balls_in_a_box import Solution

    solution = Solution()

    def _init_variables_1742():
        return solution

    yield _init_variables_1742


class TestClass1742:
    def test_solution_0(self, init_variables_1742):
        assert init_variables_1742().count_balls(lowLimit=1, highLimit=10) == 2

    def test_solution_1(self, init_variables_1742):
        assert init_variables_1742().count_balls(lowLimit=5, highLimit=15) == 2

    def test_solution_2(self, init_variables_1742):
        assert init_variables_1742().count_balls(lowLimit=19, highLimit=28) == 2


"""
Test 1769. Minimum Number of Operations to Move All Balls to Each Box
"""


@pytest.fixture(scope="session")
def init_variables_1769():
    from src.array_problems.minimum_number_of_operations_to_move_all_balls_to_each_box import Solution

    solution = Solution()

    def _init_variables_1769():
        return solution

    yield _init_variables_1769


class TestClass1769:
    def test_solution_0(self, init_variables_1769):
        assert init_variables_1769().min_operations(boxes="110") == [1, 1, 3]

    def test_solution_1(self, init_variables_1769):
        assert init_variables_1769().min_operations(boxes="001011") == [
            11,
            8,
            5,
            4,
            3,
            4,
        ]


"""
Test 1800. Maximum Ascending Subarray Sum
"""


@pytest.fixture(scope="session")
def init_variables_1800():
    from src.array_problems.maximum_ascending_subarray_sum import Solution

    solution = Solution()

    def _init_variables_1800():
        return solution

    yield _init_variables_1800


class TestClass1800:
    def test_solution_0(self, init_variables_1800):
        assert (
            init_variables_1800().max_ascending_sum(nums=[10, 20, 30, 5, 10, 50]) == 65
        )

    def test_solution_1(self, init_variables_1800):
        assert init_variables_1800().max_ascending_sum(nums=[10, 20, 30, 40, 50]) == 150

    def test_solution_2(self, init_variables_1800):
        assert (
            init_variables_1800().max_ascending_sum(nums=[12, 17, 15, 13, 10, 11, 12])
            == 33
        )

    def test_solution_3(self, init_variables_1800):
        assert init_variables_1800().max_ascending_sum(nums=[100, 10, 1]) == 100
