import requests
import pyttsx3
import re
from PIL import Image
from io import BytesIO
from translate import Translator
import speech_recognition as sr


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def translate_to_russian(word):
    translator= Translator(to_lang="ru")
    translation = translator.translate(word)
    return translation


def get_dog_image():
    res = requests.get("https://dog.ceo/api/breeds/image/random")
    data = res.json()
    url = data['message']

    if url == '':
        return "mistake"
    
    while True:
        try:
            res = requests.get(url)
            img = Image.open(BytesIO(res.content))
            img.show()
            break

        except:
            continue

    return url

def save_image(url, filename="dog_image.jpg"):
    res = requests.get(url)

    with open(filename, "wb") as file:
        file.write(res.content)


def recognize_breed(url):
    templ = r'[a-z-]*'
    matches = re.findall(templ, url)
    word = translate_to_russian(matches[12])
    
    return word


def get_resolution(url):
    res = requests.get(url)
    img = Image.open(BytesIO(res.content))
    resolution = img.size

    return resolution


def main():
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone(device_index=2) as source:
            speak("Слушаю, мой господин")
            print("Говорите:")
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language="ru-RU").lower()
            print("Вы сказали: " + str(command))
            if ("показать" in command) or ("следующая" in command):
                url = get_dog_image()
                if url == 'mistake':
                    speak("Простите, ошибка в запросе")
                    continue
                else:
                    speak("Пожалуйста, вот случайное изображение собаки.")

            elif "сохранить" in command:
                save_image(url)
                speak("Изображение собаки сохранено как файл.")

            elif "назвать породу" in command:
                breed = recognize_breed(url)
                speak(f"Порода собаки: {breed}.")

            elif "разрешение" in command:
                resolution = get_resolution(url)
                speak(f"Разрешение изображения: {resolution[0]} на {resolution[1]} пикселей.")
            
            elif "стоп" in command:
                speak("До свидания")
                break

        except sr.UnknownValueError:
            speak("Извините, не удалось распознать команду. Пожалуйста, повторите.")
        except sr.RequestError as e:
            print(f"Ошибка запроса к сервису распознавания речи; {e}")


main()