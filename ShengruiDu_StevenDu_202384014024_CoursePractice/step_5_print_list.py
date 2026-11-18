# Course practice: NE2301 ShengruiDu StevenDu 202384014024.
"""Step 5 - print the list of five numbers."""
from step_4_list_of_five_numbers import make_list


def print_numbers(numbers: list[int]) -> None:
    """Print the list as a whole, then one numbered element per line."""
    print("The list of 5 numbers is:", numbers)
    print("Elements:")
    for index, number in enumerate(numbers, start=1):
        print(f"  {index}. {number}")


if __name__ == "__main__":
    print_numbers(make_list())
