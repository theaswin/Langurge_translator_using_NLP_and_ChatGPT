from django.shortcuts import render
from httpx import request
import pytesseract
from pytesseract import Output
import cv2
import re
import pytesseract
import cv2
import re
from pytesseract import run_and_get_output
import openai
openai.api_key = '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'
# Create your views here.





def home(request):

    # path = request.POST.get('path')
    
    path = '/home/user/Desktop/Langurge_translator/web/app/This world is so beautiful.png'
    img = cv2.imread(path)
    datas = pytesseract.image_to_string(img)
    pattern = '[a-zA-Z]+'
    word = re.findall(pattern,datas)
    out = " ".join(word)
    ###################
    

    

    source = request.POST.get('s1')
    tar = request.POST.get('s2')

    source_language = source
    target_language = tar


    text = out

    # Set the model and parameters
    model_engine = "text-davinci-002"
    temperature = 0.7
    max_tokens = 60

    # Generate the translation using the OpenAI API
    response = openai.Completion.create(
        engine=model_engine,
        prompt=f"Translate the following text from {source_language} to {target_language}: {text}",
        temperature=temperature,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the translation from the response
    translation = response.choices[0].text.strip()

    # Print the translation
    # print(translation)

    contents = {
        'translation' : translation,
    }


    return render(request,'home.html',contents)