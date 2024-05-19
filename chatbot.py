import gradio as gr

from utils import format_as_chat
from call_api import generate_output

def echo(message, history):
    chat_format = format_as_chat(message, history)
    # print(chat_format)
    payload = {
        "inputs": chat_format,
        "parameters": {
            "do_sample": False,
            "max_new_tokens": 400
        }
    }
    # print(payload)
    response = generate_output(payload)
    output = response['generated_text']
    # print(response)
    parts = output.split('assistant\n\n')
    return parts[-1].strip()

# res = echo("Howdy!",[])
# print(res)

demo = gr.ChatInterface(fn=echo, examples=["Today is Friday!", "Let's have fun.", "See you tomorrow."], title="Llama 3 8B Instruct")

demo.launch()
