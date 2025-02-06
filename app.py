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
    if not message.strip():
        return history, gr.update(placeholder="⚠ Escribe un mensaje antes de enviar", interactive=True)
    
    if history is None:
        history = []
    
    messages = history + [
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
        max_new_tokens=max_new_tokens,
        eos_token_id=terminators,
        do_sample=True,
        temperature=temperature + 0.1,
        top_p=0.9
    )

    response = outputs[0]["generated_text"][len(prompt):]
    history.append((message, response))
    
    return history, gr.update(value="", placeholder="💬 Escribe tu mensaje...")

with gr.Blocks(css=".input-container { display: flex; align-items: center; } .send-btn { border: none; background: transparent; cursor: pointer; }") as demo:
    gr.Markdown("# 🤖 Chatbot Smarttie")

    chatbot = gr.Chatbot(height=400, label="Historial de Conversación")

    with gr.Row():
        with gr.Column(scale=12, min_width=200):
            with gr.Row(elem_classes="input-container"):
                user_input = gr.Textbox(
                    placeholder="💬 Escribe tu mensaje...",
                    container=True,
                    show_label=False,
                    interactive=True,
                    scale=10
                )
                send_btn = gr.Button("➡", elem_classes="send-btn", size="sm", variant="primary", scale=1)

    with gr.Row():
        system_prompt = gr.Textbox(
            label="Indicación del Sistema",
            interactive=True
        )

    with gr.Row():
        max_tokens = gr.Slider(500, 4000, value=1000, label="Tokens máximos", step=50)
        temperature = gr.Slider(0.0, 1.0, value=0.7, label="Temperatura", step=0.05)

    with gr.Row():
        clear_btn = gr.Button("🗑 Limpiar Chat", variant="secondary")

    user_input.submit(
        fn=chat_function,
        inputs=[user_input, system_prompt, chatbot, max_tokens, temperature],
        outputs=[chatbot, user_input],
        queue=False
    )

    send_btn.click(
        fn=chat_function,
        inputs=[user_input, system_prompt, chatbot, max_tokens, temperature],
        outputs=[chatbot, user_input],
        queue=False
    )

    clear_btn.click(lambda: [], inputs=[], outputs=[chatbot])

demo.launch(share=True)

