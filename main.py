import openai
openai.api_type = "azure"
openai.api_base = "https://gentech-workbench.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "XXYY"

response = openai.ChatCompletion.create(
    engine="gentech-gpt4-research", # The deployment name you chose when you deployed the ChatGPT or GPT-4 model.
    messages=[
        {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
        {"role": "user", "content": "What's the difference between garbanzo beans and chickpeas?"},
    ]
)

print(response)

print(response['choices'][0]['message']['content'])