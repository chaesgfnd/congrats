from typing import Any, Self, Union, Optional, List, Tuple, Callable, TypeVar, Generic  # noqa: F401

try:
	from icecream import ic  # noqa: F401
except ImportError:  # Graceful fallback if IceCream isn't installed.
	ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa


def generate():
	s = "happy new year, unless you were naughty. Naughty naughty"
	return s


def main():
	print("INFO: Starting...")
	msg = generate()
	ic(msg)


if __name__ == "__main__":
	main()
