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

	# DO: load target chats
	# DO: load their conversations

	# DO: generate_msg(conversation: list[str]) -> str
	msg = generate()
	ic(msg)

	# DO: send the response _from your name_ // for starters do with a bot, but keep in mind that that's much easier
	print(f"DBG: to send: {msg}")


if __name__ == "__main__":
	main()
