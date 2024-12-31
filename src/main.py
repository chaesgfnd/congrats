from typing import Any, Self, Union, Optional, List, Tuple, Callable, TypeVar, Generic  # noqa: F401
from telethon import TelegramClient
import asyncio

try:
	from icecream import ic  # noqa: F401
except ImportError:  # Graceful fallback if IceCream isn't installed.
	ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa


def generate():
	s = "happy new year, unless you were naughty. Naughty naughty"
	return s


async def run(client: TelegramClient):
	print("INFO: Starting...")

	# DO: load target chats
	# DO: load their conversations

	# DO: generate_msg(conversation: list[str]) -> str
	msg = generate()
	print(f"{msg=}")

	# DO: send the response _from your name_ // for starters do with a bot, but keep in mind that that's much easier
	me = await client.get_me()
	ic(me)

	# await client.send_message("valeratrades", "you stink")


async def async_foo():
	print("async_foo started")
	await asyncio.sleep(5)
	print("async_foo done")


# async def main():
# asyncio.ensure_future(async_foo())
# print("Do some actions 1")
# await asyncio.sleep(5)
# print("Do some actions 2")


def main():
	api_id = 22372417
	api_hash = "f671f3b5120eb6dff1f6c05a097c05f2"
	phone = "+33638539715"
	username = "chaesgfnd"
	client = TelegramClient(username, api_id, api_hash)
	with client:
		client.loop.run_until_complete(client.send_message("@valeratrades", "Hello, myself!"))

	# code_req = await client.send_code_request(phone=phone)
	## await client.start(phone)
	# print("here")
	# channel = await client.get_entity("valeratrades")
	# ic(channel)
	# return
	# code_req = await client.send_code_request(phone=phone)
	# ic(code_req)

	# client.loop.run_until_complete(run(client))


if __name__ == "__main__":
	main()
	# loop = asyncio.get_event_loop()
	# loop.run_until_complete(main())
