# 403fa3bb03ba42cb9504d5d04e0abd78
import json
#from gtts import gTTS
import requests
#import os
#from playsound import playsound


def say_text(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
'''def say_text(str):
    language = 'en'
    myobj = gTTS.gTTS(text=str, lang=language, slow=False)
    myobj.save("hello.mp3")
    os.system("start hello.mp3")'''


if __name__ == "__main__":
    '''url = 'https://newsapi.org/v2/everything?q=apple&from=2021-06-08&to=2021-06-08&sortBy=popularity&apiKey=403fa3bb03ba42cb9504d5d04e0abd78'
    response = requests.get(url).text
    news_dict = json.loads(response)
    arts = news_dict['articles']
    say_text("today's news....")
    for i in arts:
        say_text(i['title'])
        print(i['title'])
        say_text("Moving on to the next news......")

    say_text("Thanks for listening...")'''
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

    headers = {
    'x-rapidapi-key': "d919db8a15mshad38dcadb7cf1a0p1593c9jsndc733f74531e",
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers).text
    news_dict = json.loads(response)
    '''news_dict = json.loads(response)
    arts = news_dict['articles']
    say_text("today's news....")'''

    print(news_dict)
