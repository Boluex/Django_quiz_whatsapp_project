# Create your views here.
from bs4 import BeautifulSoup
import random
from django.shortcuts import render
from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import openai
from quiz_proj.settings import OPENAI_SECRET_KEY

from.models import *
import time
import uuid
from users.models import profile
import re
import lxml
# from fpdfs import FPDF
from.models import *
import requests
from users.models import profile,image_data

# from.models import *
# from django.view
# Create your views here.
homework='solve x+y=2,who is the current president of Nigeria,What is science,How tall is the eiffel tower,when was the first world war'
notes='i help in:\n -jamb training and questions \n -Assignments\n-Adverts\n-Reports '
hint="Hint: If you don't understand you can just type the question e.g Solve this question x+y=2 and 2x + y=4"
secondary_stuff='Waec'
url_page='https://0c24-212-100-79-174.eu.ngrok.io'


# The ai code function
openai.api_key = OPENAI_SECRET_KEY
start_sequence = "\nAI:"
restart_sequence = "\nHuman:"

def generate_token(word):
    val=random.randint(100,900)
    token=random.sample(word,12)
    final_token=str(token )+ str(val)
    api=''.join(final_token)
    return api

def whatsapp_ai(match,word):
    if match == None:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=word,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )
        return response.choices[0].text
    else:
        return None
@csrf_exempt
def home_view(request):
    if request.method=='POST':
         user_msg=request.POST.get('Body','').lower()
         bot_resp=MessagingResponse()
         msg=bot_resp.message()
         bot_list_1=['adrian']
         text_list=['summarize','explain','what ','where ','who ','how','when','where ']
         for resp in bot_list_1: 
            if user_msg in resp:
               msg.body(f"Hi there,i'm an educational bot.You can call me adrian\n\n{notes}\nWhat are you interested in?")
         if 'assignment' in user_msg:
            msg.body('Ask your question like: adrian:where is the eiffel tower located at?')
         elif 'adrian:' in user_msg:
            q=user_msg
            pattern=re.compile(r'(what is your name(\W?)|tell me about yourself(\W?)|who made you(\W?)|what can you do(\W?)|how are you(\W?)|who are you(\W?)|are you a robot(\W?))')
            match=pattern.search(q)
            val=whatsapp_ai(match,q)
            msg.body(val)
         
            
         return HttpResponse(str(bot_resp))
    return HttpResponse('saved')

