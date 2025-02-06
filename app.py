from dotenv import load_dotenv
import transformers 
import torch
import gradio as gr

load_dotenv()

model_id = "meta-llama/Llama-3.2-1B-Instruct"
pipeline = transformers.pipeline(
    "text-generation",
    model = model_id,
    model_kwargs = {"torch_dtype": torch.bfloat16},
    device = "cuda",
)

def chat_function(message, system_prompt, history, max_new_tokens, temperature):
    messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": message}
    ]
    prompt = pipeline.tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    terminators = [
        pipeline.tokenizer.eos_token_id,
        pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]
    outputs = pipeline(
        prompt,
        max_new_tokens = max_new_tokens,
        eos_token_id = terminators,
        do_sample = True,
        temperature = temperature + 0.1,
        top_p = 0.9
    )
    return outputs[0]["generated_text"][len(prompt):]

with gr.Blocks() as demo:

    gr.Markdown("# 🤖 Chatbot Smarttie")

    gr.ChatInterface(
        chat_function,
        chatbot=gr.Chatbot(height=400),
        textbox=gr.Textbox(placeholder="Ingresa el mensaje aquí", container=False, scale=7, autofocus=True),
        additional_inputs=[
            gr.Textbox("", label = "Indicación del Sistema"),
            gr.Slider(500, 4000, label= "Tokens máximos"),
            gr.Slider(0,1, label="Temperatura")
        ]    
    )

demo.launch(share=True)

