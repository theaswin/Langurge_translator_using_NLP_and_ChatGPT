import openai
import os

# Set up OpenAI API credentials
# openai.api_key = os.environ["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"]
openai.api_key = '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'

# Set the text to be translated


# Set the source and target languages
source = input("enter source langure")
tar = input("Enter target")

source_language = source
target_language = tar


text = input("Enter text ")


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
