# Course practice: NE2301 ShengruiDu StevenDu 202384014024.
"""Step 6 - sort the list of five numbers and print it."""
from step_4_list_of_five_numbers import make_list


def sort_numbers(numbers: list[int]) -> list[int]:
    """Return a new list holding the same numbers in ascending order."""
    return sorted(numbers)


def sort_in_place(numbers: list[int]) -> None:
    """Sort the list itself in ascending order with list.sort()."""
    numbers.sort()


if __name__ == "__main__":
    numbers = make_list()
    print("Original list :", numbers)
    print("Sorted (sorted):", sort_numbers(numbers))
    sort_in_place(numbers)
    print("Sorted in place:", numbers)
