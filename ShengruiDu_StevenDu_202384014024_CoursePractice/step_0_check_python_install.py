# Course practice: NE2301 ShengruiDu StevenDu 202384014024.
"""Step 0 - confirm that a Python 3 interpreter is installed and reachable."""
import platform
import sys


def main() -> None:
    """Print the interpreter version and location so the installation can be confirmed."""
    print("Python installation check")
    print("-" * 44)
    print(f"Version       : {platform.python_version()}")
    print(f"Implementation: {platform.python_implementation()}")
    print(f"Executable    : {sys.executable}")
    print(f"Major.Minor   : {sys.version_info.major}.{sys.version_info.minor}")
    print("-" * 44)
    print("Status        : Python is installed and working.")


if __name__ == "__main__":
    main()
