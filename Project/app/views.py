from django.shortcuts import render
import openai
import os
openai.api_key = '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'


# Create your views here.

def home(request):

    # Inputing the Source langurge and Target langurge
    Source = input("enter source langure")
    Target = input("Enter target")

    source_language = Source
    target_language = Target

    # Inputing the Text to be converted
    text = input("Enter text ")

    # Assigning the parameters
    model_engine = "text-davinci-002"
    temperature = 0.7
    max_tokens = 60

    # Giving prompt to chatGPT and getting response
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
    print(translation)
    return render(request,'home.html')
    
    
    








