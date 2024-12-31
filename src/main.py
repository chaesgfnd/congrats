from typing import Any, Self, Union, Optional, List, Tuple, Callable, TypeVar, Generic  # noqa: F401
from telethon import TelegramClient
import asyncio

try:
	from icecream import ic  # noqa: F401
except ImportError:  # Graceful fallback if IceCream isn't installed.
	ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa


# TODO: implement
def generate():
	s = "happy new year, unless you were naughty. Naughty naughty"
	return s


def run(client: TelegramClient, user: str):
	msg = generate()
	print(f"{msg=}")

	with client:
		client.loop.run_until_complete(client.send_message(user, "Hello, myself!"))


def main():
	print("INFO: Starting...")
	api_id = 22372417
	api_hash = "f671f3b5120eb6dff1f6c05a097c05f2"
	phone = "+33638539715"
	username = "chaesgfnd"
	client = TelegramClient(username, api_id, api_hash)

	users = ["me", "@valeratrades"]
	# TODO: async it
	# loop = asyncio.get_event_loop()
	for user in users:
		run(client, user)


if __name__ == "__main__":
	main()
