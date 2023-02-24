import openai
import pytesseract
import cv2
import re
from pytesseract import Output
openai.api_key = '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'


source = input("enter source langure: ")
tar = input("Enter target: ")

source_language = source
target_language = tar


text = input("enter text")

print(type(text))
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
print(translation)
