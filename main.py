import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

# pip install pyaudio
# pip install pydub
# pip install pandas
# pip install gTTS

def textToSpeech(text, filename):
    mytext1 = str(text)
    
    language1 = 'hi'
    language2 = 'en'
    myobj1 = gTTS(text=mytext1, lang=language1, slow=False)
    myobj1.save(filename)   
    for i in range(12, 22):
        if filename == f"{i}_hindi.mp3":
            mytext2 = str(text)
            print(f"{i}_hindi.mp3")
            myobj2 = gTTS(text=mytext2, lang=language2, slow=False)
            myobj2.save(filename)


    


# This function returns pydub audio segment
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')

    # 1 - Generate kripaya dhyan dijiye
    start = 41110
    finish = 44010
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")

    # 2 - is from city

    # 3 - Generate se chalkar
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    # 4 - is via-city

    # 5 - Generate ke raste
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # 6 - is to-city

    # 7 - Generate ko jane wali gaadi sankhya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 8 - Train number and name

    # 9 - Generate kuch hi samay me platform sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")

    # 10 - platform number

    # 11 - Generate par aa rahi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")


def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2 - Generate From city
        textToSpeech(item['from'], '2_hindi.mp3')

        # 4 - Generate via city
        textToSpeech(item['via'], '4_hindi.mp3')

        # 6 - Generate to city
        textToSpeech(item['to'], '6_hindi.mp3')

        # 8 - Generate train number and name
        textToSpeech(item['train_no'] + " " + item['train_name'], '8_hindi.mp3')

        # 10 - Generate  platform number
        textToSpeech(item['platform'], '10_hindi.mp3')

        # For english announcement
         # 12 - Generate From city
        textToSpeech('May I have your attention please. Train number', '12_hindi.mp3')

        # 13 - Generate train number and name
        textToSpeech(item['train_no'] + " " + item['train_name'], '13_hindi.mp3')

        # 14 - Generate From city
        textToSpeech('from', '14_hindi.mp3')
                
        # 15 - Generate From city
        textToSpeech(item['from'], '15_hindi.mp3')

        # 16 - Generate From city
        textToSpeech('to', '16_hindi.mp3')

        # 17 - Generate to city
        textToSpeech(item['to'], '17_hindi.mp3')

        # 18 - Generate to city
        textToSpeech('via', '18_hindi.mp3')

        # 19 - Generate via city
        textToSpeech(item['via'], '19_hindi.mp3')

        # 20 - Generate to city
        textToSpeech('is arriving shortly on platform number', '20_hindi.mp3')

        # 21 - Generate  platform number
        textToSpeech(item['platform'], '21_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1, 22)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")


if __name__ == "__main__":
    print("Generating Skeleton....")
    generateSkeleton()
    print("Now generating announcement...")
    generateAnnouncement("announce_hindi.xlsx")
