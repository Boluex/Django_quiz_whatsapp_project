secret_key='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'
import os
import openai
import re
from quiz_proj.settings import OPENAI_SECRET_KEY

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_SECRET_KEY
start_sequence = "\nAI:"
restart_sequence = "\nHuman: "


def whatsapp_bot(match):
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=match,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )
        return response.choices[0].text
