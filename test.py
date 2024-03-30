# AIzaSyDAUPdeY4N0iENhkiTCoWY8-6tlju4Jdpg#print("halo")
"""At the command line, only need to run once to install the package via pip:
$ pip install google-generativeai"""
import google.generativeai as genai

genai.configure(api_key="AIzaSyDAUPdeY4N0iENhkiTCoWY8-6tlju4Jdpg")

# Set up the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]
model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

convo = model.start_chat(history=[
    {
        "role": "user",
        "parts": ["halo"]
    },
    {
        "role": "model",
        "parts": ["Halo juga! Apa yang bisa saya bantu hari ini?"]
    },
])

# Input message from user
user_input = input("Masukkan pertnyaan: ")
convo.send_message(user_input)

# Print the model's response
print(convo.last.text)