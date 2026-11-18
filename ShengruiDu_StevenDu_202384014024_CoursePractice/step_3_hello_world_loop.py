# Course practice: NE2301 ShengruiDu StevenDu 202384014024.
"""Step 3 - print Hello World FIVE TIMES using a loop."""

REPEAT_COUNT = 5


def print_hello_world(repeat_count: int = REPEAT_COUNT) -> None:
    """Print the greeting once per iteration of a simple for loop."""
    for index in range(1, repeat_count + 1):
        print(f"{index}. Hello, World!")


if __name__ == "__main__":
    print_hello_world()
