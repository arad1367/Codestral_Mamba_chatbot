import gradio as gr
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

def chat_with_mistral(api_key, user_input):
    try:
        client = MistralClient(api_key=api_key)
        model = "codestral-mamba-latest"
        system_message = "Your name is G-Advisor. You are a marketing advisor in Germany. You will only answer questions related to marketing in Germany."
        messages = [
            ChatMessage(role="system", content=system_message),
            ChatMessage(role="user", content=user_input)
        ]
        chat_response = client.chat(model=model, messages=messages)
        return chat_response.choices[0].message.content
    except Exception as e:
        return "API key is not valid. Please try again."

with gr.Blocks(theme='gstaff/whiteboard') as demo:
    gr.Markdown("""
    # Hi, This is G-Advisor, your market advisor in Germany.
                I'm based on Mistral mamba model.
    """)
    api_key = gr.Textbox(label="Enter Your Mistral API Key", type="password")
    user_input = gr.Textbox(label="Enter Your Message")
    output = gr.Markdown(label="Chatbot Response")
    btn = gr.Button("Submit")
    btn.click(fn=chat_with_mistral, inputs=[api_key, user_input], outputs=output)

    examples = [
        "What are the top marketing trends in Germany this year?",
        "How can I improve my SEO strategy for my German website?",
        "What are the most effective marketing channels for B2B marketing in Germany?",
        "How can I target my marketing efforts to reach a specific demographic in Germany?"
    ]
    gr.Examples(examples=examples, inputs=user_input)

    footer = """
    <div style="text-align: center; margin-top: 20px;">
        <a href="https://www.linkedin.com/in/pejman-ebrahimi-4a60151a7/" target="_blank">LinkedIn</a> |
        <a href="https://github.com/arad1367" target="_blank">GitHub</a> |
        <a href="https://arad1367.pythonanywhere.com/" target="_blank">Live demo of my PhD defense</a>
        <br>
        Made with 💖 by Pejman Ebrahimi
    </div>
    """
    gr.HTML(footer)

demo.launch()
