# Course practice: NE2301 ShengruiDu StevenDu 202384014024.
"""Step 4 - make a list of five numbers."""

NUMBERS = [42, 17, 93, 8, 55]


def make_list() -> list[int]:
    """Return the list of five numbers used by the following steps."""
    return list(NUMBERS)


if __name__ == "__main__":
    numbers = make_list()
    print("List of 5 numbers:", numbers)
    print("Length of the list:", len(numbers))
