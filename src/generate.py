from __future__ import annotations
from typing import Any, Self, Union, Optional, List, Tuple, Callable, TypeVar, Generic  # noqa: F401
import openai, os, requests, time, json


api_key = os.getenv("OPENAI_KEY")
# second var is cost of 1k tokens
gpt35 = ("gpt-3.5-turbo", 0.002)
gpt4t = ("gpt-4-1106-preview", 0.015)  # price is a guess, and is not to be trusted

api_key = os.getenv("OPENAI_KEY")
openai.api_type = "azure"
openai.api_key = api_key

examples = [
	(
		"""Опять с попкорном? 🐣
Я вот это одобряю🤘
у меня закончился 😔
ужас мама
мама дай денюшек на кино пожалуйста 🙇🙇🙇🙇
Тебе налик нужен?
не знаю
да
Поднимись наверх
Ку-ку, у тебя всё хорошо?
да я иду домой 👍
Придёшь, не разувайся, вынеси мусор, плиз
мне в туалет надо мама
мама можно доесть креветки?
моя родная мама а это ты в ванне? 🙇🙇🙇🙇🙇
моя родная мама а тебе ещё долго 🙇🙇🙇🙇🙇""",
		"моя родная мама поздравляю тебя с наступающим новым годом 💥💥💥😻😻😻💋💋💋🌟🌟🌟💗💗💗желаю тебе всего самого замечательного и ещё лучше, чтобы новый год прошел ещё лучше чем этот и следующий ещё лучше 😽😽😽❤️‍🔥❤️‍🔥❤️‍🔥💌💌💌🫂🫂🫂 люблю тебя очень мама с новым годом с новым счастьем ‼️‼️‼️‼️‼️‼️",
	),
]


def generate(context_messages: list[str]) -> str:
	"""
	Generates a cohesive response based on the previous messages in the conversation
	"""

	context_messages = [msg for msg in context_messages if msg is not None]
	messages_string = "\n".join(context_messages)
	q = messages_string
	s = request(
		question=q,
		instruction="wish happy new year based on the previous messages in the conversation. Try to adapt the persona of the sender, write only what would they would be likely to send, not what is deemed standard or expected. (and don't use any names)",  # HACK: instead of comment not to use names, really should just include the sender of each message + which will be the author of the wish
		examples=examples,
	)

	return s


def request(question: str, instruction: str, examples: List[Tuple[str, str]], model=gpt35, debug=False):
	system_line = {"role": "system", "content": instruction}
	user_line = {"role": "user", "content": question}
	conversation = [system_line]

	for e in examples:
		conversation += [
			{"role": "user", "content": e[0]},
			{"role": "assistant", "content": e[1]},
		]
	conversation += [user_line]

	url = "https://api.openai.com/v1/chat/completions"
	headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

	data = {
		"model": f"{model[0]}",
		"messages": conversation,
		"temperature": 0,
		# "max_tokens": 100,
	}
	start_time = time.time()
	r = requests.post(url, headers=headers, data=json.dumps(data)).json()
	end_time = time.time()

	if debug:
		print(f"{model[0]}:")
		print(f"{conversation[-1]['content']}")
		print(f"{r['choices'][0]['message']['content']}")
		tokens = float(r["usage"]["total_tokens"])
		cost = model[1] * tokens / 1000
		print(f"cost: {cost} in {end_time-start_time}\n")
	return r["choices"][0]["message"]["content"].split(";")[0]


if __name__ == "__main__":
	test_messages = [
		"Опять с попкорном? 🐣",
		"Я вот это одобряю🤘",
		"у меня закончился 😔",
		"ужас мама",
		"мама дай денюшек на кино пожалуйста 🙇🙇🙇🙇",
		"Тебе налик нужен?",
		"не знаю",
		"да",
		"Поднимись наверх",
		"Ку-ку, у тебя всё хорошо?",
		"да я иду домой 👍",
		"Придёшь, не разувайся, вынеси мусор, плиз",
		"мне в туалет надо мама",
		"мама можно доесть креветки?",
		"моя родная мама а это ты в ванне? 🙇🙇🙇🙇🙇",
		"моя родная мама а тебе ещё долго 🙇🙇🙇🙇🙇",
	]
	print(generate(test_messages))
