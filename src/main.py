from typing import Any, Self, Union, Optional, List, Tuple, Callable, TypeVar, Generic  # noqa: F401
from telethon import TelegramClient
from generate import generate
import os

try:
	from icecream import ic  # noqa: F401
except ImportError:  # Graceful fallback if IceCream isn't installed.
	ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa


REPEATS_FILE_PATH = os.path.expanduser("~/.local/share/congrats/repeats.txt")


def run(client: TelegramClient, user: str):
	with client:
		messages = client.loop.run_until_complete(client.get_messages(user, limit=20))

		message_contents: list[str] = []
		for message in messages:
			message_contents.append(message.text)

	msg = generate(message_contents)
	print(f"{user=}\n{msg=}\n#---------------------")

	with client:
		client.loop.run_until_complete(client.send_message(user, msg))
		with open(REPEATS_FILE_PATH, "a") as f:
			f.write(f"{user}\n")


def filter_out_repeats(target_users: list[str]) -> list[str]:
	os.makedirs(os.path.dirname(REPEATS_FILE_PATH), exist_ok=True)
	try:
		with open(REPEATS_FILE_PATH, "r") as f:
			repeats_str = f.read()
	except:
		return target_users

	repeats = repeats_str.split("\n")

	out_users = []
	for user in target_users:
		if not user in repeats:
			out_users.append(user)

	return out_users


def main():
	print("INFO: Starting...")
	api_id = 22372417
	api_hash = "f671f3b5120eb6dff1f6c05a097c05f2"
	phone = "+33638539715"
	username = "chaesgfnd"
	client = TelegramClient(username, api_id, api_hash)

	considered_users = ["Elena_Kletskova", "valeratrades"]
	users = filter_out_repeats(considered_users)
	print(f"INFO: gonna congratulate: {users}")

	# TODO: async it
	# loop = asyncio.get_event_loop()
	for user in users:
		run(client, user)


if __name__ == "__main__":
	main()
