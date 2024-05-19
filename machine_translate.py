import gradio as gr

from utils import format_as_chat
from call_api import generate_output


def translate(sentence,history,target_language):
    prompt = f" Translate this sentence into {target_language}: '{sentence}. Please output only the translated sentence in {target_language}!"
    chat_format = format_as_chat(prompt, history)
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


# res = translate("Awesome, Now I can focus on my career without repetition.",'Chinese',[])
# print(f"Translated result: {res}")

with gr.Blocks() as demo:
    system_prompt = gr.Textbox(value="German", label = "Target Language")

    gr.ChatInterface(
        translate,
        additional_inputs=[system_prompt],
        examples=[
        ["Today is Friday!", "German"], ["Let's have fun.","Chinese"], ["See you tomorrow.","Arabic"]],
        description="Enter an English sentence, choose a target language, I will translate it into the target language for you.",
        title="Llama 3 8B Instruct, Machine Translation from English into any other language."
    )

demo.launch(share=True)
