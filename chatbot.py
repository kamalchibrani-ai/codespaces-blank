import openai
import gradio as gr
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')


def generate_text(prompt):
    response = openai.Completion.create(
        engine="davinci", # Choose the ChatGPT 3.5 model
        prompt=prompt,
        max_tokens=1024, # Maximum length of the response
        n=1, # Generate a single response
        stop=None, # Stop generating when this token is encountered
        temperature=0.7 # Controls the randomness of the response
    )
    return response.choices[0].text.strip()

chatbot_interface = gr.Interface(
    fn=generate_text,
    inputs=gr.inputs.Textbox(lines=7, placeholder="Enter your message here..."),
    outputs="text"
)
chatbot_interface.launch()
